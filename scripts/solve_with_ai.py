#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Solution Generator for LeetCode Problems
Gemini-only (Gemini 3 Flash)
"""

import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import re
import time
from typing import Dict, Optional
from datetime import datetime, timezone
try:
    from google import genai
    _GENAI_IMPORT_ERROR = None
except Exception as _genai_err:
    genai = None
    _GENAI_IMPORT_ERROR = _genai_err

# Fix Windows console encoding
if sys.platform == 'win32':
    import io
    import os
    # Set encoding via environment variable (safer for subprocess)
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    # Only wrap if not already wrapped
    if hasattr(sys.stdout, 'buffer') and not isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'buffer') and not isinstance(sys.stderr, io.TextIOWrapper):
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


class AISolutionGenerator:
    """Generates solutions using Gemini API (default for CI) or OpenAI Codex CLI (local follow-up)"""

    MODEL_NAME = "gemini-3.8-flash"
    FALLBACK_MODEL = "gemini-3-flash-preview"
    CODEX_MODEL = "gpt-6-luna"
    CODEX_REASONING_EFFORT = "low"
    API_VERSION = "v1beta"
    MAX_OUTPUT_TOKENS = 65536
    TEMPERATURE = 1.0
    RATE_LIMIT_SLEEP_SECONDS = 60
    OVERLOADED_SLEEP_SECONDS = 120
    MAX_RETRIES = 6

    # Language batches (Split into smaller groups to avoid token limits/safety issues & improve template adherence)
    LANGUAGE_BATCHES = [
        ["C++", "Java", "Python", "Python3", "C", "C#", "JavaScript"],
        ["TypeScript", "PHP", "Swift", "Kotlin", "Dart", "Go"],
        ["Ruby", "Scala", "Rust", "Racket", "Erlang", "Elixir"]
    ]

    # Map Language Name (from batches) -> JSON Output Key
    LANG_TO_JSON_KEY = {
        "C++": "cpp",
        "C#": "csharp",
        # "Go": "go", # Implicit via lower()
        # "Python": "python",
    }

    # Map JSON Output Key -> Snippet Filename Key (if different)
    JSON_KEY_TO_FILENAME = {
        "go": "golang",
    }

    def _load_dotenv_if_present(self) -> None:
        """Load key=value pairs from project root .env if GEMINI_API_KEY is not in environment."""
        if os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"):
            return
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env_path = os.path.join(root_dir, ".env")
        if not os.path.exists(env_path):
            return
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for raw_line in f:
                    line = raw_line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    if line.startswith("export "):
                        line = line[len("export "):].strip()
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if key and val and key not in os.environ:
                        os.environ[key] = val
        except Exception:
            pass

    def __init__(self, provider: Optional[str] = None, model_name: Optional[str] = None):
        self._load_dotenv_if_present()
        self.provider = (provider or os.getenv("AI_PROVIDER", "gemini")).strip().lower()
        self.codex_reasoning_effort = os.getenv("CODEX_REASONING_EFFORT", self.CODEX_REASONING_EFFORT)

        if self.provider == "codex":
            self.model_name = model_name or os.getenv("CODEX_MODEL", self.CODEX_MODEL)
        else:
            self.model_name = model_name or os.getenv("GEMINI_MODEL", self.MODEL_NAME)
        self.active_model = self.model_name

        # Initialize Gemini client (explicitly use v1beta so preview models work in google-genai >= 3.0)
        self.client = None
        self.import_error = _GENAI_IMPORT_ERROR
        gemini_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if genai and gemini_key:
            try:
                self.client = genai.Client(
                    api_key=gemini_key,
                    http_options={"api_version": self.API_VERSION},
                )
            except TypeError:
                self.client = genai.Client(api_key=gemini_key)

        # Batch delay configuration:
        # - Gemini free tier (5 RPM): default 15s between batches
        # - Codex CLI (ChatGPT subscription): default 1s between batches
        default_delay = "1" if self.provider == "codex" else "15"
        try:
            self.batch_delay = float(os.getenv("BATCH_DELAY_SECONDS", default_delay))
        except ValueError:
            self.batch_delay = float(default_delay)

    def _find_codex_binary(self) -> Optional[str]:
        """Locate the OpenAI Codex CLI executable on the system."""
        env_bin = os.getenv("CODEX_BIN")
        if env_bin and os.path.exists(env_bin):
            return env_bin
        which_bin = shutil.which("codex")
        if which_bin and os.path.exists(which_bin):
            return which_bin
        chatgpt_app_bin = "/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex"
        if os.path.exists(chatgpt_app_bin):
            return chatgpt_app_bin
        ext_candidates = sorted(
            glob.glob(
                os.path.expanduser(
                    "~/.antigravity-ide/extensions/openai.chatgpt-*/bin/*/codex"
                )
            ),
            reverse=True,
        )
        for cand in ext_candidates:
            if os.path.exists(cand):
                return cand
        return None

    def _generate_with_codex(self, prompt: str, batch_index: int) -> str:
        """Execute a single batch prompt non-interactively via `codex exec` using ChatGPT subscription."""
        codex_bin = self._find_codex_binary()
        if not codex_bin:
            raise RuntimeError(
                "Codex CLI binary not found. Install @openai/codex or set CODEX_BIN."
            )

        codex_prompt = (
            prompt
            + "\n\nIMPORTANT: Do NOT run any shell commands or tools. "
            "Respond immediately in a single turn with ONLY the raw JSON object."
        )

        with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False, encoding="utf-8") as tmp_out:
            out_path = tmp_out.name

        try:
            cmd = [
                codex_bin,
                "exec",
                "--ephemeral",
                "--ignore-user-config",
                "--skip-git-repo-check",
                "-C",
                "/tmp",
                "-s",
                "read-only",
                "-m",
                self.model_name,
                "-c",
                f'model_reasoning_effort="{self.codex_reasoning_effort}"',
                "-o",
                out_path,
                "-",
            ]
            proc = subprocess.run(
                cmd,
                input=codex_prompt,
                text=True,
                capture_output=True,
                timeout=300,
            )

            # Extract token usage from codex stdout/stderr if present
            combined_log = (proc.stdout or "") + "\n" + (proc.stderr or "")
            tokens_match = re.search(r"tokens used\s*\n\s*([\d,]+)", combined_log, re.IGNORECASE)
            if tokens_match:
                print(
                    f"[Codex] Batch {batch_index} ({self.model_name}, reasoning={self.codex_reasoning_effort}) "
                    f"Usage: tokens_used: {tokens_match.group(1)}",
                    file=sys.stderr,
                )

            if proc.returncode != 0:
                err_snippet = self._compact_detail(proc.stderr or proc.stdout or f"exit code {proc.returncode}")
                raise RuntimeError(f"codex exec failed (exit {proc.returncode}): {err_snippet}")

            output_text = ""
            if os.path.exists(out_path):
                with open(out_path, "r", encoding="utf-8") as f:
                    output_text = f.read().strip()

            if not output_text:
                output_text = (proc.stdout or "").strip()

            return output_text
        finally:
            if os.path.exists(out_path):
                try:
                    os.remove(out_path)
                except OSError:
                    pass

    def _is_rate_limited(self, error: Exception) -> bool:
        """Best-effort detection of 429/rate-limit errors across SDK versions."""
        status = getattr(error, "status_code", None)
        if status in (429, 503):
            return True
        code = getattr(error, "code", None)
        if code in (429, 503):
            return True
        message = str(error).lower()
        return (
            "429" in message
            or "rate limit" in message
            or "resource_exhausted" in message
            or "503" in message
            or "unavailable" in message
            or "overloaded" in message
        )

    def _is_overloaded(self, error: Exception) -> bool:
        """Detect 503/unavailable overload errors for longer backoff."""
        status = getattr(error, "status_code", None)
        if status == 503:
            return True
        code = getattr(error, "code", None)
        if code == 503:
            return True
        message = str(error).lower()
        return "503" in message or "unavailable" in message or "overloaded" in message

    def _normalize_finish_reason(self, finish_reason) -> Optional[str]:
        if finish_reason is None:
            return None
        if isinstance(finish_reason, int):
            reason_map = {
                1: "STOP",
                2: "MAX_TOKENS",
                3: "SAFETY",
                4: "RECITATION",
                5: "OTHER",
            }
            return reason_map.get(finish_reason, str(finish_reason))
        if hasattr(finish_reason, "name"):
            return str(finish_reason.name)
        if isinstance(finish_reason, str):
            if "FinishReason." in finish_reason:
                return finish_reason.split("FinishReason.")[-1]
            return finish_reason
        return str(finish_reason)

    def _extract_error_detail(self, error: Exception) -> Optional[str]:
        """Best-effort extraction of a concise, human-readable error detail."""
        if error is None:
            return None

        def _stringify(value) -> Optional[str]:
            if isinstance(value, str):
                return value.strip()
            if isinstance(value, dict):
                try:
                    return json.dumps(value, ensure_ascii=False)
                except Exception:
                    return str(value)
            if isinstance(value, (list, tuple)) and value:
                return _stringify(value[0])
            return None

        for attr in ("message", "detail", "details"):
            detail = _stringify(getattr(error, attr, None))
            if detail:
                return self._compact_detail(detail)

        if getattr(error, "args", None):
            for arg in error.args:
                detail = _stringify(arg)
                if detail:
                    return self._compact_detail(detail)

        response = getattr(error, "response", None)
        if response is not None:
            detail = _stringify(getattr(response, "text", None))
            if detail:
                return self._compact_detail(detail)

        return None

    def _compact_detail(self, detail: str, max_len: int = 300) -> str:
        """Normalize whitespace and trim overly long details for logging."""
        compacted = " ".join(detail.split())
        if len(compacted) > max_len:
            return f"{compacted[:max_len - 3]}..."
        return compacted

    def _generate_with_backoff(self, prompt: str, batch_index: int):
        last_error = None
        attempts = 0
        while attempts < self.MAX_RETRIES:
            try:
                return self._generate_content(self.model_name, prompt)
            except Exception as e:
                last_error = e
                if not self._is_rate_limited(e):
                    raise
                overloaded = self._is_overloaded(e)
                reason_label = "503" if overloaded else "429"
                detail = self._extract_error_detail(e)
                if detail:
                    print(f"[Gemini] Batch {batch_index} {reason_label} detail: {detail}", file=sys.stderr)

                # On 429 rate limit / quota exhaustion or 503 overload on primary (gemini-3.8-flash),
                # switch to fallback (gemini-3-flash-preview, "Gemini 3 Flash") immediately.
                if self.FALLBACK_MODEL and self.model_name != self.FALLBACK_MODEL:
                    print(
                        f"[Gemini] Batch {batch_index} {reason_label} on {self.model_name}. "
                        f"Switching to fallback model {self.FALLBACK_MODEL}.",
                        file=sys.stderr,
                    )
                    self.model_name = self.FALLBACK_MODEL
                    self.active_model = self.FALLBACK_MODEL
                    continue

                sleep_seconds = self.OVERLOADED_SLEEP_SECONDS if overloaded else self.RATE_LIMIT_SLEEP_SECONDS
                print(f"[Gemini] Batch {batch_index} {reason_label} on {self.model_name}. Sleeping {sleep_seconds}s then retrying.", file=sys.stderr)
                time.sleep(sleep_seconds)
                attempts += 1
        if last_error:
            raise last_error
        raise RuntimeError("Unknown Gemini generation error")

    def _build_generation_config(self):
        config_kwargs = {
            "temperature": self.TEMPERATURE,
            "max_output_tokens": self.MAX_OUTPUT_TOKENS,
            "response_mime_type": "application/json",
        }
        if hasattr(genai, "types") and hasattr(genai.types, "GenerateContentConfig"):
            return genai.types.GenerateContentConfig(**config_kwargs)
        return config_kwargs

    def _generate_content(self, model_name: str, prompt: str):
        config = self._build_generation_config()
        try:
            return self.client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=config,
            )
        except TypeError:
            # Fallback for older call signatures
            return self.client.models.generate_content(
                model=model_name,
                contents=prompt,
                generation_config=config,
            )

    PROMPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")

    def _get_json_key(self, lang_name: str) -> str:
        """Get JSON output key for a language name."""
        return self.LANG_TO_JSON_KEY.get(lang_name, lang_name.lower())

    def _get_filename_key(self, json_key: str) -> str:
        """Get snippet filename key for a JSON output key."""
        return self.JSON_KEY_TO_FILENAME.get(json_key, json_key)

    def _load_prompt_template(self, template_name: str) -> str:
        """Load prompt template file from scripts/prompts/ directory."""
        template_path = os.path.join(self.PROMPTS_DIR, template_name)
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()

    def create_prompt(
        self,
        problem_data: Dict,
        target_languages: list,
        include_metadata: bool = True,
        reference_solution: Optional[Dict] = None,
    ) -> str:
        """Create a prompt for the AI models for specific languages using external prompt templates."""
        title = problem_data.get('title', '')
        content = problem_data.get('content_prompt') or problem_data.get('content', '')
        difficulty = problem_data.get('difficulty', '')
        hints = problem_data.get('hints', [])
        code_template = problem_data.get('code_template', '')

        # Metadata for locating snippets
        problem_slug = problem_data.get('title_slug', '')
        problem_date = problem_data.get('date', '')

        lang_pairs = []
        for lang in target_languages:
            out_key = self._get_json_key(lang)
            lang_pairs.append((out_key, lang))

        sample_solutions_lines = [
            f'    "{out_key}": "Complete {lang} code"' for out_key, lang in lang_pairs
        ]
        sample_solutions = "\n".join(sample_solutions_lines)

        optional_sections = ""
        if hints:
            optional_sections += "Hints:\n"
            for i, hint in enumerate(hints, 1):
                optional_sections += f"{i}. {hint}\n"
            optional_sections += "\n"

        # For Batch 2+, inject Batch 1's verified approach & reference code so the model
        # translates the established algorithm instead of re-solving from scratch.
        if not include_metadata and reference_solution:
            ref_approach = reference_solution.get("approach", "")
            if isinstance(ref_approach, str) and ref_approach.strip():
                optional_sections += (
                    "VERIFIED ALGORITHM (implement this exact algorithm in the target languages "
                    "without re-solving from scratch):\n"
                    f"{ref_approach.strip()}\n\n"
                )
            ref_sols = reference_solution.get("solutions", {})
            if isinstance(ref_sols, dict):
                for ref_lang in ("python3", "python", "cpp", "java"):
                    ref_code = ref_sols.get(ref_lang, "")
                    if (
                        isinstance(ref_code, str)
                        and ref_code.strip()
                        and "generation failed" not in ref_code.lower()
                        and "failed to parse" not in ref_code.lower()
                    ):
                        optional_sections += (
                            f"REFERENCE IMPLEMENTATION ({ref_lang}):\n"
                            f"```{ref_lang}\n{ref_code.strip()}\n```\n\n"
                        )
                        break

        # Inject specific templates ONLY for requested languages (no duplicate top-level Python template)
        snippets_prompt = ""
        for lang in target_languages:
            out_key = self._get_json_key(lang)
            file_key = self._get_filename_key(out_key)

            snippet = self._load_snippet(problem_slug, file_key, problem_date)
            if not snippet and out_key in ("python", "python3") and code_template:
                snippet = code_template
            if snippet:
                # Add a hint about the template, forcing the Output Key for the code block
                snippets_prompt += f"\nFor {lang}, use this EXACT code template (keep method signature):"
                snippets_prompt += f"\n```{out_key}\n{snippet.strip()}\n```\n"

        if snippets_prompt:
            optional_sections += f"IMPORTANT CODE TEMPLATES:\n{snippets_prompt}\n"

        if difficulty and str(difficulty).upper() == "HARD":
            optional_sections += (
                "SPECIAL RULES FOR HARD PROBLEMS:\n"
                "- The algorithm must be completely optimal strictly focusing on time/space efficiency.\n\n"
            )

        langs_str = ", ".join(target_languages)
        template_file = "solve_with_metadata.txt" if include_metadata else "solve_solutions_only.txt"
        template = self._load_prompt_template(template_file)

        return template.format(
            title=title,
            difficulty=difficulty,
            content=content,
            optional_sections=optional_sections,
            langs_str=langs_str,
            sample_solutions=sample_solutions,
        )

    def _snippet_candidates(self, problem_slug: str, lang_slug: str, problem_date: Optional[str]) -> list:
        """Build possible snippet locations, preferring the new per-date layout."""
        candidates = []
        if problem_date:
            try:
                dt = datetime.strptime(problem_date, "%Y-%m-%d")
                date_dir = os.path.join(
                    "_posts",
                    "_daily",
                    dt.strftime("%Y"),
                    dt.strftime("%m"),
                    dt.strftime("%d"),
                )
                candidates.append(os.path.join(date_dir, f"{lang_slug}.txt"))
            except ValueError:
                # Ignore invalid dates and fall back to legacy layout
                pass
        candidates.append(os.path.join("_posts", "_snippets", problem_slug, f"{lang_slug}.txt"))
        return candidates

    def _load_snippet(self, problem_slug: str, lang_slug: str, problem_date: Optional[str] = None) -> Optional[str]:
        """Load code snippet template for given problem and language."""
        for snippet_path in self._snippet_candidates(problem_slug, lang_slug, problem_date):
            if os.path.exists(snippet_path):
                with open(snippet_path, 'r', encoding='utf-8') as f:
                    return f.read()
        return None

    def _detect_indent_unit(self, code: str) -> int:
        """Detect indentation unit (e.g., 2 or 4 spaces) from code."""
        lines = code.split('\n')
        indents = []
        for line in lines:
            stripped = line.lstrip(' ')
            if not stripped:
                continue
            indent = len(line) - len(stripped)
            if indent > 0:
                indents.append(indent)
        
        if not indents:
            return 4
            
        # Find GCD of all indents
        from math import gcd
        from functools import reduce
        
        # Filter out very large indents (likely continuations)
        valid_indents = [i for i in indents if i <= 12]
        if not valid_indents:
            return 4
            
        common_indent = reduce(gcd, valid_indents)
        return common_indent if common_indent in [2, 4] else 4

    def _find_matching_line(self, template_lines: list, ai_line: str) -> Optional[int]:
        """Find a matching line in template based on content similarity."""
        ai_content = ai_line.strip()
        if not ai_content or len(ai_content) < 5:
            return None
        
        for i, template_line in enumerate(template_lines):
            template_content = template_line.strip()
            if template_content == ai_content:
                return i
            if len(template_content) >= 10 and len(ai_content) >= 10:
                if template_content[:10] == ai_content[:10]:
                    return i
        return None

    def _detect_excess_from_template(self, ai_code: str, template_code: str) -> Optional[int]:
        """Detect excess indentation by comparing AI code with template."""
        ai_lines = ai_code.split('\n')
        template_lines = template_code.split('\n')
        
        excesses = []
        for ai_line in ai_lines[:15]:
            if not ai_line.strip():
                continue
            
            template_idx = self._find_matching_line(template_lines, ai_line)
            if template_idx is not None:
                template_line = template_lines[template_idx]
                template_indent = len(template_line) - len(template_line.lstrip(' '))
                ai_indent = len(ai_line) - len(ai_line.lstrip(' '))
                diff = ai_indent - template_indent
                if diff > 0:
                    excesses.append(diff)
        
        if excesses:
            from collections import Counter
            counter = Counter(excesses)
            most_common_excess = counter.most_common(1)[0][0]
            return most_common_excess if most_common_excess >= 7 else None
        return None

    def _clean_code(self, code: str, problem_slug: str = "", lang_slug: str = "", problem_date: str = "") -> str:
        """Clean code by removing markdown code block markers and normalizing whitespace"""
        if not code:
            return code

        # Remove markdown code block markers (```python, ```cpp, etc.)
        lines = code.split('\n')
        cleaned_lines = []

        for line in lines:
            stripped = line.strip()
            # Skip lines that are just code block markers
            if stripped.startswith('```') and len(stripped) <= 20:
                continue
            cleaned_lines.append(line)

        # Rejoin and clean up
        cleaned = '\n'.join(cleaned_lines)

        # Remove leading/trailing whitespace
        cleaned = cleaned.strip()

        # Remove common leading indentation from all lines
        cleaned = textwrap.dedent(cleaned)

        # Try snippet-based correction if we have both problem_slug and lang_slug
        if problem_slug and lang_slug:
            # Correctly map JSON key to filename key (e.g. go -> golang)
            file_key = self._get_filename_key(lang_slug)
            template = self._load_snippet(problem_slug, file_key, problem_date)
            if template:
                excess = self._detect_excess_from_template(cleaned, template)
                if excess and excess >= 7:
                    lines = cleaned.split('\n')
                    corrected_lines = []
                    for line in lines:
                        if not line.strip():
                            corrected_lines.append(line)
                        else:
                            current_indent = len(line) - len(line.lstrip(' '))
                            new_indent = max(0, current_indent - excess)
                            corrected_lines.append(' ' * new_indent + line.lstrip(' '))
                    return '\n'.join(corrected_lines)

        # Fallback: Dynamic analysis for fixed excess indentation
        lines = cleaned.split('\n')
        non_empty_lines = []
        for line in lines:
            if line.strip():
                non_empty_lines.append(line)
                if len(non_empty_lines) >= 10:
                    break
        
        if len(non_empty_lines) >= 3:
            first_indent = len(non_empty_lines[0]) - len(non_empty_lines[0].lstrip(' '))
            
            diffs_from_first = []
            for line in non_empty_lines[1:]:
                indent = len(line) - len(line.lstrip(' '))
                diff = indent - first_indent
                if diff > 0:
                    diffs_from_first.append(diff)
            
            if diffs_from_first:
                fixed_excess = min(diffs_from_first)
                
                if fixed_excess >= 7:
                    # Determine indent unit from snippet if available, else default to 4
                    indent_unit = 4
                    if problem_slug and lang_slug:
                        template = self._load_snippet(problem_slug, lang_slug, problem_date)
                        if template:
                            indent_unit = self._detect_indent_unit(template)

                    # Calculate actual excess to remove, preserving natural indentation
                    excess_to_remove = fixed_excess
                    
                    # Check if preserving indent_unit leaves a likely bug amount (7-9)
                    if 7 <= (fixed_excess - indent_unit) <= 10:
                        excess_to_remove = fixed_excess - indent_unit
                    # Also check 2 spaces (common in JS/TS/Ruby)
                    elif 7 <= (fixed_excess - 2) <= 10:
                        excess_to_remove = fixed_excess - 2
                    
                    cleaned_lines = []
                    for line in lines:
                        if not line.strip():
                            cleaned_lines.append(line)
                        else:
                            current_indent = len(line) - len(line.lstrip(' '))
                            new_indent = max(0, current_indent - excess_to_remove)
                            cleaned_lines.append(' ' * new_indent + line.lstrip(' '))
                    
                    cleaned = '\n'.join(cleaned_lines)

        return cleaned

    def parse_json_response(self, response_text: str, problem_slug: str = "", problem_date: str = "") -> Dict:
        """Extract and parse JSON from AI response"""
        if not response_text or not isinstance(response_text, str):
            return self._create_error_response("" if response_text is None else str(response_text))
        try:
            # 1. Try to find JSON within markdown code blocks first
            json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
            else:
                # 2. Fallback: Find first '{' and last '}'
                start = response_text.find('{')
                end = response_text.rfind('}') + 1
                if start != -1 and end > start:
                    json_str = response_text[start:end]
                else:
                    # If response_mime_type is json, the whole text might be json
                    try:
                        json.loads(response_text)
                        json_str = response_text
                    except:
                        return self._create_error_response(response_text)

            # 3. Fix common JSON corruption from Gemini
            # A. Fix invalid JSON escapes (e.g. \max in LaTeX -> \\max)
            def fix_escapes(s):
                res = []
                i = 0
                while i < len(s):
                    if s[i] == '\\':
                        if i + 1 < len(s):
                            if s[i+1] in ['\\', '"', '/', 'b', 'f', 'n', 'r', 't', 'u']:
                                res.append(s[i:i+2])
                                i += 2
                            else:
                                res.append('\\\\')
                                res.append(s[i+1])
                                i += 2
                        else:
                            res.append('\\\\')
                            i += 1
                    else:
                        res.append(s[i])
                        i += 1
                return "".join(res)
            
            json_str = fix_escapes(json_str)

            # B. Fix missing closing quotes before next JSON keys if text got truncated
            for key in ["time_complexity", "space_complexity", "solutions"]:
                pattern = r'([^"\{\},\[\]\s])\s*\n\s*"' + key + r'"\s*:'
                json_str = re.sub(pattern, r'\1",\n  "' + key + '":', json_str)

            # Trust the AI response and parse directly
            parsed = None
            try:
                parsed = json.loads(json_str, strict=False)
            except json.JSONDecodeError as e:
                # Fallback: remove extra trailing characters (e.g. extraneous '}' generated by the AI)
                idx = json_str.rfind('}')
                while idx > 0:
                    idx = json_str.rfind('}', 0, idx)
                    if idx <= 0:
                        break
                    try:
                        parsed = json.loads(json_str[:idx+1], strict=False)
                        break
                    except json.JSONDecodeError:
                        pass
                
                if parsed is None:
                    raise e

            # Validate structure
            if 'solutions' in parsed and isinstance(parsed['solutions'], dict):
                for lang, code in parsed['solutions'].items():
                    parsed['solutions'][lang] = self._clean_code(code, problem_slug, lang, problem_date)
                return parsed
            elif 'code' in parsed: # Legacy format support
                return {
                    "approach": parsed.get("approach", "N/A"),
                    "time_complexity": parsed.get("time_complexity", "N/A"),
                    "space_complexity": parsed.get("space_complexity", "N/A"),
                    "solutions": {
                        "python": self._clean_code(parsed.get("code", ""), problem_slug, "python", problem_date)
                    }
                }
            elif 'approach' in parsed: # Support metadata-only responses
                return parsed
            else:
                print(f"[Parse] JSON structure mismatch. Keys found: {list(parsed.keys())}", file=sys.stderr)
                return self._create_error_response(response_text)

        except json.JSONDecodeError as e:
            # Check for common truncation errors
            if "Unterminated string" in str(e) or "Expecting value" in str(e):
                print(f"[Parse] Error: AI response was truncated (likely too large).", file=sys.stderr)
            else:
                print(f"[Parse] JSON decode error: {e}", file=sys.stderr)
            return self._create_error_response(response_text)
        except Exception as e:
            print(f"[Parse] Unexpected error: {e}", file=sys.stderr)
            return self._create_error_response(response_text)

    def _create_error_response(self, response_text: str) -> Dict:
        """Create a fallback response when parsing fails"""
        if response_text is None:
            response_text = ""
        # Log the full response to stderr so failures are visible in console
        if response_text:
            cleaned = response_text.replace("```", "'''").replace("\r", "")
            print(f"[Parse Failure] Raw response:\n{cleaned}", file=sys.stderr)
        
        # Embed the full response in the markdown for easier debugging
        # Escape triple backticks to avoid breaking the markdown code block
        # Use a unique delimiter to avoid conflict
        safe_response = response_text.replace("```", "'''")
        
        return {
            "_parse_error": True,
            "approach": "Failed to parse AI response",
            "time_complexity": "N/A",
            "space_complexity": "N/A",
            "solutions": {
                "python": f"# Failed to parse response\n# Check logs for full output.\n# Full Response:\n'''\n{safe_response}\n'''"
            }
        }

    def _merge_solutions(self, all_solutions: Dict, new_solution: Dict) -> None:
        """Merge a new solution batch into the main solutions dictionary"""
        if not new_solution:
            return

        new_approach = new_solution.get("approach")
        new_time = new_solution.get("time_complexity")
        new_space = new_solution.get("space_complexity")

        if isinstance(new_approach, str) and new_approach.strip():
            existing_approach = all_solutions.get("approach", "")
            if not existing_approach or len(new_approach) > len(existing_approach):
                all_solutions["approach"] = new_approach
                if isinstance(new_time, str) and new_time.strip():
                    all_solutions["time_complexity"] = new_time
                if isinstance(new_space, str) and new_space.strip():
                    all_solutions["space_complexity"] = new_space

        if isinstance(new_time, str) and new_time.strip() and not all_solutions.get("time_complexity"):
            all_solutions["time_complexity"] = new_time
        if isinstance(new_space, str) and new_space.strip() and not all_solutions.get("space_complexity"):
            all_solutions["space_complexity"] = new_space

        # Merge solutions
        if "solutions" in new_solution:
            if "solutions" not in all_solutions:
                all_solutions["solutions"] = {}
            all_solutions["solutions"].update(new_solution["solutions"])

    def _get_batches_for_difficulty(self, difficulty: str) -> list:
        """Determine language batches dynamically by problem difficulty."""
        diff_upper = difficulty.upper() if difficulty else ""
        if diff_upper == "HARD":
            # 5 requests
            return [
                ["C++", "Java", "Python"],
                ["Python3", "C", "C#", "JavaScript"],
                ["TypeScript", "PHP", "Swift", "Kotlin"],
                ["Dart", "Go", "Ruby", "Scala"],
                ["Rust", "Racket", "Erlang", "Elixir"],
            ]
        if diff_upper == "MEDIUM":
            # 4 requests (chunks of ~5)
            return [
                ["C++", "Java", "Python", "Python3", "C"],
                ["C#", "JavaScript", "TypeScript", "PHP", "Swift"],
                ["Kotlin", "Dart", "Go", "Ruby", "Scala"],
                ["Rust", "Racket", "Erlang", "Elixir"],
            ]
        # 3 requests (EASY or unknown)
        return self.LANGUAGE_BATCHES

    def _is_valid_code(self, code: object) -> bool:
        """Return True if a language solution string is non-empty and not an error placeholder."""
        if not isinstance(code, str) or not code.strip():
            return False
        lowered = code.lower()
        return "generation failed" not in lowered and "failed to parse response" not in lowered

    def _seed_existing_solution(self, problem_data: Dict, final_solution: Dict) -> None:
        """Seed final_solution with valid metadata and language solutions from an existing post if present."""
        existing = problem_data.get("existing_ai_solution")
        if not isinstance(existing, dict):
            return
        approach = existing.get("approach", "")
        if isinstance(approach, str) and approach.strip() and not approach.lower().startswith("failed to parse"):
            final_solution["approach"] = approach
            if existing.get("time_complexity"):
                final_solution["time_complexity"] = existing["time_complexity"]
            if existing.get("space_complexity"):
                final_solution["space_complexity"] = existing["space_complexity"]

        existing_sols = existing.get("solutions", {})
        if isinstance(existing_sols, dict):
            for lang_key, code in existing_sols.items():
                if self._is_valid_code(code):
                    final_solution.setdefault("solutions", {})[lang_key] = code

    def _is_batch_already_solved(self, final_solution: Dict, batch: list) -> bool:
        """Check if every language in the batch already has a valid solution in final_solution."""
        if not final_solution.get("approach"):
            return False
        sols = final_solution.get("solutions", {})
        for lang in batch:
            key = self._get_json_key(lang)
            if not self._is_valid_code(sols.get(key)):
                return False
        return True

    def solve_with_codex(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using OpenAI Codex CLI (`codex exec`) with ChatGPT subscription."""
        codex_bin = self._find_codex_binary()
        if not codex_bin:
            print("Codex CLI binary not found. Install @openai/codex or set CODEX_BIN.", file=sys.stderr)
            return None

        problem_slug = problem_data.get("title_slug", "")
        problem_date = problem_data.get("date", "")
        difficulty = problem_data.get("difficulty", "")
        final_solution: Dict = {"solutions": {}}
        self._seed_existing_solution(problem_data, final_solution)
        total_elapsed_time = 0.0

        batches = self._get_batches_for_difficulty(difficulty)
        only_missing = bool(problem_data.get("only_missing"))

        for i, batch in enumerate(batches):
            if only_missing and self._is_batch_already_solved(final_solution, batch):
                print(f"  - Batch {i+1}/{len(batches)}: {', '.join(batch)} [already solved, skipping]", file=sys.stderr)
                continue

            print(f"  - Batch {i+1}/{len(batches)}: {', '.join(batch)}", file=sys.stderr)
            try:
                include_metadata = (i == 0 and not final_solution.get("approach")) or not final_solution.get("approach")
                prompt = self.create_prompt(
                    problem_data,
                    batch,
                    include_metadata=include_metadata,
                    reference_solution=final_solution if not include_metadata else None,
                )
                start_time = time.time()
                response_text = self._generate_with_codex(prompt, i + 1)
                end_time = time.time()
                total_elapsed_time += (end_time - start_time)

                batch_result = self.parse_json_response(response_text, problem_slug, problem_date)
                if batch_result and batch_result.get("_parse_error"):
                    self._fill_failed_batch(final_solution, batch, "Parsing failed")
                elif batch_result and "solutions" in batch_result:
                    batch_result.pop("_parse_error", None)
                    self._merge_solutions(final_solution, batch_result)
                else:
                    self._fill_failed_batch(final_solution, batch, "Parsing failed")
            except Exception as e:
                print(f"Error with Codex Batch {i+1}: {e}", file=sys.stderr)
                self._fill_failed_batch(final_solution, batch, f"Error: {str(e)}")

            if i < len(batches) - 1:
                time.sleep(self.batch_delay)

        final_solution["elapsed_time"] = total_elapsed_time
        return final_solution

    def solve_with_gemini(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using Gemini (Batched)"""
        if self.import_error:
            print("Gemini SDK import failed. Install dependencies with: pip install -r scripts/requirements.txt", file=sys.stderr)
            print(f"Import error: {self.import_error}", file=sys.stderr)
            return None
        if not self.client:
            print("Gemini API key not found. Set GEMINI_API_KEY or GOOGLE_API_KEY.", file=sys.stderr)
            return None

        problem_slug = problem_data.get('title_slug', '')
        problem_date = problem_data.get('date', '')
        difficulty = problem_data.get('difficulty', '')
        final_solution = {"solutions": {}}
        self._seed_existing_solution(problem_data, final_solution)
        total_elapsed_time = 0.0
        
        batches = self._get_batches_for_difficulty(difficulty)
        only_missing = bool(problem_data.get("only_missing"))
        
        for i, batch in enumerate(batches):
            if only_missing and self._is_batch_already_solved(final_solution, batch):
                print(f"  - Batch {i+1}/{len(batches)}: {', '.join(batch)} [already solved, skipping]", file=sys.stderr)
                continue

            print(f"  - Batch {i+1}/{len(batches)}: {', '.join(batch)}", file=sys.stderr)
            try:
                include_metadata = (i == 0 and not final_solution.get("approach")) or not final_solution.get("approach")
                prompt = self.create_prompt(
                    problem_data,
                    batch,
                    include_metadata=include_metadata,
                    reference_solution=final_solution if not include_metadata else None,
                )
                start_time = time.time()
                response = self._generate_with_backoff(prompt, i + 1)
                end_time = time.time()
                batch_time = end_time - start_time
                total_elapsed_time += batch_time
                
                # Log usage metadata if available (including thoughts_token_count for thinking models)
                if hasattr(response, 'usage_metadata'):
                    usage = response.usage_metadata
                    thoughts_tokens = getattr(usage, 'thoughts_token_count', 0) or 0
                    print(
                        f"[Gemini] Batch {i+1} Usage: prompt_token_count: {usage.prompt_token_count}, "
                        f"thoughts_token_count: {thoughts_tokens}, "
                        f"candidates_token_count: {usage.candidates_token_count}, "
                        f"total_token_count: {usage.total_token_count}",
                        file=sys.stderr,
                    )

                # Check for blocked/empty response or finish reason
                # Safely access candidate
                if not getattr(response, "candidates", None):
                     print(f"[Gemini] Batch {i+1} Failed: No candidates returned.", file=sys.stderr)
                     if hasattr(response, 'prompt_feedback'):
                         print(f"[Gemini] Prompt Feedback: {response.prompt_feedback}", file=sys.stderr)
                     self._fill_failed_batch(final_solution, batch, "No candidates returned")
                     continue

                candidate = response.candidates[0]
                finish_reason = getattr(candidate, "finish_reason", None)
                reason_str = self._normalize_finish_reason(finish_reason)
                if reason_str not in (None, "STOP"):
                    print(f"[Gemini] Batch {i+1} stopped. Reason: {reason_str}", file=sys.stderr)

                    if reason_str == "SAFETY":
                        print(f"[Gemini] Safety Ratings: {candidate.safety_ratings}", file=sys.stderr)

                # If it's safety/recitation or empty content, we might not have text parts
                if not getattr(candidate, "content", None) or not getattr(candidate.content, "parts", None):
                    reason = reason_str or "No content"
                    self._fill_failed_batch(final_solution, batch, f"Generation failed: {reason}")
                    continue

                # Store raw response safely
                try:
                    response_text = getattr(response, "text", None)
                    if not isinstance(response_text, str):
                        response_text = "" if response_text is None else str(response_text)
                    batch_result = self.parse_json_response(response_text, problem_slug, problem_date)
                    if batch_result and batch_result.get("_parse_error"):
                        self._fill_failed_batch(final_solution, batch, "Parsing failed")
                    elif batch_result and "solutions" in batch_result:
                        batch_result.pop("_parse_error", None)
                        self._merge_solutions(final_solution, batch_result)
                    else:
                        self._fill_failed_batch(final_solution, batch, "Parsing failed")
                except ValueError as ve:
                    # response.text raises ValueError if there are no valid parts
                    print(f"[Gemini] Batch {i+1} Error accessing text: {ve}", file=sys.stderr)
                    self._fill_failed_batch(final_solution, batch, f"Error accessing text: {str(ve)}")

            except Exception as e:
                print(f"Error with Gemini Batch {i+1}: {e}", file=sys.stderr)
                self._fill_failed_batch(final_solution, batch, f"Error: {str(e)}")

            if i < len(batches) - 1:
                time.sleep(self.batch_delay)

        final_solution["elapsed_time"] = total_elapsed_time
        return final_solution

    def _fill_failed_batch(self, final_solution: Dict, batch: list, error_msg: str) -> None:
        """Fill failed languages with error placeholders (without overwriting already-valid solutions)."""
        if "solutions" not in final_solution:
            final_solution["solutions"] = {}
        
        for lang in batch:
            key = lang.lower().replace("c++", "cpp").replace("c#", "csharp")
            if not self._is_valid_code(final_solution["solutions"].get(key)):
                final_solution["solutions"][key] = f"// Generation failed for {lang}\n// Reason: {error_msg}"

    def generate_solution(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using the configured provider ('gemini' or 'codex')."""
        print(f"Generating solution with {self.model_name} (provider={self.provider})...", file=sys.stderr)
        if self.provider == "codex":
            return self.solve_with_codex(problem_data)
        return self.solve_with_gemini(problem_data)


def main():
    """Main function"""
    if len(sys.argv) > 1:
        # Read from file if provided
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            problem_data = json.load(f)
    else:
        # Read from stdin
        problem_data = json.load(sys.stdin)

    generator = AISolutionGenerator()
    solution = generator.generate_solution(problem_data)

    if solution:
        # Add solution to problem data with timestamp
        problem_data['ai_solution'] = {
            'model': generator.model_name,
            'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            **solution
        }
    else:
        print("Failed to generate solution", file=sys.stderr)

    # Output enhanced problem data as JSON
    print(json.dumps(problem_data, indent=2, ensure_ascii=False))

    return 0 if solution else 1


if __name__ == "__main__":
    sys.exit(main())
