#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Solution Generator for LeetCode Problems
Supports Gemini (default) and Groq providers
"""

import json
import os
import sys
import textwrap
import re
import time
from typing import Dict, Optional
from datetime import datetime, timezone
import requests
from google import generativeai as genai

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
    """Generates solutions using AI providers"""

    # Model configurations
    MODEL_CONFIGS = {
        'gemini-2.5-flash': {
            'provider': 'gemini',
            'api_key_env': 'GEMINI_API_KEY'
        },
        'llama-3.3-70b-versatile': {
            'provider': 'groq',
            'api_key_env': 'GROQ_API_KEY'
        },
        'qwen-2.5-32b': {
            'provider': 'groq',
            'api_key_env': 'GROQ_API_KEY'
        },
        'groq/compound': {
            'provider': 'groq',
            'api_key_env': 'GROQ_API_KEY'
        }
    }

    # Language batches for generation (Split into smaller groups to avoid token limits/safety issues)
    LANGUAGE_BATCHES = [
        ["C++", "Java", "Python", "Python3", "C", "C#", "JavaScript", "TypeScript", "PHP", "Swift", "Kotlin", "Dart", "Go", "Ruby", "Scala", "Rust", "Racket", "Erlang", "Elixir"]
    ]

    def __init__(self):
        # Get model name from environment (default: gemini-2.5-flash)
        self.model_name = os.getenv('AI_MODEL', 'gemini-2.5-flash')

        # Get model config
        model_config = self.MODEL_CONFIGS.get(self.model_name)
        if not model_config:
            print(f"Error: Unknown model '{self.model_name}'. Supported models: {', '.join(self.MODEL_CONFIGS.keys())}", file=sys.stderr)
            sys.exit(1)

        self.provider = model_config['provider']

        # Initialize API clients based on available keys
        self.gemini_model = None
        self.groq_api_key = None

        # Gemini setup
        if self.provider == 'gemini':
            gemini_key = os.getenv('GEMINI_API_KEY')
            if gemini_key:
                genai.configure(api_key=gemini_key)
                self.gemini_model = genai.GenerativeModel(self.model_name)

        # Groq setup
        if self.provider == 'groq':
            self.groq_api_key = os.getenv('GROQ_API_KEY')

    
    def _extract_detail_message(self, response) -> Optional[str]:
        """Extract a human-readable error/detail message from an HTTP response."""
        if not response or not getattr(response, "text", ""):
            return None
        try:
            data = response.json()
        except ValueError:
            return None

        def _from_obj(obj):
            if isinstance(obj, str):
                return obj
            if isinstance(obj, dict):
                for key in ("detail", "message", "error"):
                    val = obj.get(key)
                    if isinstance(val, str):
                        return val
                    if isinstance(val, dict):
                        inner = _from_obj(val)
                        if inner:
                            return inner
            if isinstance(obj, list):
                for item in obj:
                    inner = _from_obj(item)
                    if inner:
                        return inner
            return None

        return _from_obj(data)

    def create_prompt(self, problem_data: Dict, target_languages: list) -> str:
        """Create a prompt for the AI models for specific languages"""
        title = problem_data.get('title', '')
        content = problem_data.get('content', '')
        difficulty = problem_data.get('difficulty', '')
        hints = problem_data.get('hints', [])
        code_template = problem_data.get('code_template', '')

        lang_pairs = []
        for lang in target_languages:
            key = lang.lower().replace("c++", "cpp").replace("c#", "csharp")
            lang_pairs.append((key, lang))
        sample_solutions_lines = [
            f'    "{key}": "Complete {lang} code"' for key, lang in lang_pairs
        ]
        sample_solutions = "\n".join(sample_solutions_lines)

        prompt = f"""You are an expert programmer solving LeetCode problems in multiple languages.

Problem: {title}
Difficulty: {difficulty}

Problem Description:
{content}

"""

        if hints:
            prompt += "Hints:\n"
            for i, hint in enumerate(hints, 1):
                prompt += f"{i}. {hint}\n"
            prompt += "\n"

        if code_template:
            prompt += f"Code Template (Python):\n```python\n{code_template}\n```\n\n"

        langs_str = ", ".join(target_languages)
        prompt += f"""Please provide solutions ONLY for these languages (match this list exactly): {langs_str}

OUTPUT RULES (CRITICAL):
- Return a single valid JSON object that matches the schema below.
- Do not include markdown, code fences, or any text outside the JSON object.
- Prefer ASCII characters; use Unicode only when necessary (e.g., in comments or string literals).
- Each code string must contain code only (technical comments allowed, but no explanatory narration).
- Use actual line breaks in code strings (they will be automatically escaped to \\n when serialized to JSON).
- CRITICAL: ALL backslashes in code MUST be escaped as \\\\ (double backslash). This is MANDATORY.
  - Example: "int* ptr;" should be "int* ptr;" (no escaping needed for forward context)
  - Example: Use "newline" for line breaks, NOT backslash-space continuation "\\    // comment"
  - Only valid JSON escape sequences allowed: \\", \\\\, \\/, \\b, \\f, \\n, \\r, \\t, \\uXXXX
  - NEVER use backslash followed by space or other invalid characters (e.g., "\\    " is INVALID)
- Properly escape special characters: use \\" for quotes inside strings.
- Avoid HTML entities (like \\u003c); use actual characters instead.

APPROACH REQUIREMENTS:
- Provide a DETAILED explanation of your approach (maximum 3 paragraphs)
- Explain the problem-solving strategy step by step
- Describe the algorithm logic clearly
- Include examples or edge cases if helpful
- Make the explanation thorough and educational

CODE FORMATTING REQUIREMENTS (CRITICAL):
- Each code solution MUST include proper line breaks and indentation
- DO NOT write code in a single line - use multiple lines with proper formatting
- Follow standard formatting conventions for each language
- Properly indent nested blocks (loops, conditionals, functions)
- Add blank lines between logical sections for readability

COMPLEXITY ANALYSIS:
- Provide detailed time and space complexity with explanations
- Explain why the complexity is what it is
- Be thorough and educational in your analysis

Format your response as JSON:
{{
  "approach": "Detailed explanation here (up to 3 paragraphs)",
  "time_complexity": "O(...) with detailed explanation",
  "space_complexity": "O(...) with detailed explanation",
  "solutions": {{
{sample_solutions}
  }}
}}

Important: Each code solution must be complete and runnable. Include class/function definitions, imports, and follow language conventions for each specific language.

Provide ONLY the JSON response, no additional text."""

        return prompt

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
            template = self._load_snippet(problem_slug, lang_slug, problem_date)
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

            # Trust the AI response and parse directly
            parsed = json.loads(json_str, strict=False)

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
        # Log full response for debugging as requested
        # print(f"[Parse Failure] Full Response:\n{response_text}", file=sys.stderr) # User requested to suppress full log for known errors
        
        # Embed the full response in the markdown for easier debugging
        # Escape triple backticks to avoid breaking the markdown code block
        # Use a unique delimiter to avoid conflict
        safe_response = response_text.replace("```", "'''")
        
        return {
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

        # Merge metadata (approach, complexity) - take the first valid one or longest
        if not all_solutions.get("approach") or (new_solution.get("approach") and len(new_solution["approach"]) > len(all_solutions["approach"])):
            all_solutions["approach"] = new_solution.get("approach", "N/A")
            all_solutions["time_complexity"] = new_solution.get("time_complexity", "N/A")
            all_solutions["space_complexity"] = new_solution.get("space_complexity", "N/A")

        # Merge solutions
        if "solutions" in new_solution:
            if "solutions" not in all_solutions:
                all_solutions["solutions"] = {}
            all_solutions["solutions"].update(new_solution["solutions"])

    def solve_with_gemini(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using Gemini (Batched)"""
        if not self.gemini_model:
            print("Gemini API key not found", file=sys.stderr)
            return None

        problem_slug = problem_data.get('title_slug', '')
        problem_date = problem_data.get('date', '')
        final_solution = {"solutions": {}}
        total_elapsed_time = 0.0
        
        # Safety settings to block fewer responses
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]

        for i, batch in enumerate(self.LANGUAGE_BATCHES):
            print(f"  - Batch {i+1}/{len(self.LANGUAGE_BATCHES)}: {', '.join(batch)}", file=sys.stderr)
            try:
                prompt = self.create_prompt(problem_data, batch)
                # Configure generation parameters for maximum output and JSON enforcement
                generation_config = genai.types.GenerationConfig(
                    max_output_tokens=65536,
                    temperature=0.2,
                    response_mime_type="application/json"
                )
                
                start_time = time.time()
                response = self.gemini_model.generate_content(
                    prompt,
                    generation_config=generation_config,
                    safety_settings=safety_settings
                )
                end_time = time.time()
                batch_time = end_time - start_time
                total_elapsed_time += batch_time
                
                # Log usage metadata if available
                if hasattr(response, 'usage_metadata'):
                    usage = response.usage_metadata
                    print(f"[Gemini] Batch {i+1} Usage: prompt_token_count: {usage.prompt_token_count}, candidates_token_count: {usage.candidates_token_count}, total_token_count: {usage.total_token_count}", file=sys.stderr)

                # Check for blocked/empty response or finish reason
                # Safely access candidate
                if not response.candidates:
                     print(f"[Gemini] Batch {i+1} Failed: No candidates returned.", file=sys.stderr)
                     if hasattr(response, 'prompt_feedback'):
                         print(f"[Gemini] Prompt Feedback: {response.prompt_feedback}", file=sys.stderr)
                     self._fill_failed_batch(final_solution, batch, "No candidates returned")
                     continue

                candidate = response.candidates[0]
                if candidate.finish_reason != 1: # 1 is STOP (success)
                    reason_map = {
                        1: "STOP",
                        2: "MAX_TOKENS",
                        3: "SAFETY",
                        4: "RECITATION",
                        5: "OTHER"
                    }
                    reason_str = reason_map.get(candidate.finish_reason, f"UNKNOWN({candidate.finish_reason})")
                    print(f"[Gemini] Batch {i+1} stopped. Reason: {reason_str}", file=sys.stderr)
                    
                    if candidate.finish_reason == 3:
                        print(f"[Gemini] Safety Ratings: {candidate.safety_ratings}", file=sys.stderr)
                    
                    # If it's safety or recitation, we might not have text parts
                    if not candidate.content.parts:
                        # Handle empty response for this batch
                        self._fill_failed_batch(final_solution, batch, f"Generation failed: {reason_str}")
                        continue

                # Store raw response safely
                try:
                    response_text = response.text
                    batch_result = self.parse_json_response(response_text, problem_slug, problem_date)
                    if batch_result and "solutions" in batch_result:
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

        final_solution["elapsed_time"] = total_elapsed_time
        return final_solution

    def solve_with_groq(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using Groq (Batched)"""
        if not self.groq_api_key:
            print("Groq API key not found", file=sys.stderr)
            return None

        problem_slug = problem_data.get('title_slug', '')
        problem_date = problem_data.get('date', '')
        final_solution = {"solutions": {}}
        total_elapsed_time = 0.0

        for i, batch in enumerate(self.LANGUAGE_BATCHES):
            print(f"  - Batch {i+1}/{len(self.LANGUAGE_BATCHES)}: {', '.join(batch)}", file=sys.stderr)
            try:
                prompt = self.create_prompt(problem_data, batch)

                # Call Groq API (OpenAI-compatible endpoint)
                start_time = time.time()
                response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.groq_api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": self.model_name,
                        "messages": [
                            {"role": "system", "content": "You are an expert programmer solving LeetCode problems. Always format code with proper line breaks and indentation."},
                            {"role": "user", "content": prompt}
                        ],
                        "temperature": 0.2,
                        "max_completion_tokens": 32768  # Increased to prevent truncation
                    },
                    timeout=60
                )
                end_time = time.time()
                batch_time = end_time - start_time
                total_elapsed_time += batch_time
                
                if not response.ok:
                    detail_msg = self._extract_detail_message(response)
                    if response.status_code == 429:
                        print(f"[Groq] Batch {i+1} Error: Rate limit exceeded (429).", file=sys.stderr)
                        if detail_msg:
                            print(f"[Groq] Detail: {detail_msg}", file=sys.stderr)
                    else:
                        print(f"[Groq] Batch {i+1} HTTP {response.status_code} Error.", file=sys.stderr)
                        if detail_msg:
                            print(f"[Groq] Detail: {detail_msg}", file=sys.stderr)
                        else:
                            print(f"[Groq] Full Body:\n{response.text}", file=sys.stderr)

                    error_reason = f"HTTP Error {response.status_code}"
                    if detail_msg:
                        error_reason = f"{error_reason} - {detail_msg}"
                    self._fill_failed_batch(final_solution, batch, error_reason)
                    continue

                data = response.json()
                if 'usage' in data:
                    print(f"[Groq] Batch {i+1} Usage: {data['usage']}", file=sys.stderr)
                
                content = data['choices'][0]['message']['content']
                # print(f"[Groq] Batch {i+1} Raw Content:\n{content}", file=sys.stderr)
                batch_result = self.parse_json_response(content, problem_slug, problem_date)
                
                if batch_result and "solutions" in batch_result:
                    self._merge_solutions(final_solution, batch_result)
                else:
                    self._fill_failed_batch(final_solution, batch, "Parsing failed")

            except Exception as e:
                print(f"Error with Groq Batch {i+1}: {e}", file=sys.stderr)
                self._fill_failed_batch(final_solution, batch, f"Error: {str(e)}")
            
            # Add delay to prevent rate limiting (429)
            if i < len(self.LANGUAGE_BATCHES) - 1:
                time.sleep(5)

        final_solution["elapsed_time"] = total_elapsed_time
        return final_solution
    def _fill_failed_batch(self, final_solution: Dict, batch: list, error_msg: str) -> None:
        """Fill failed languages with error placeholders"""
        if "solutions" not in final_solution:
            final_solution["solutions"] = {}
        
        for lang in batch:
            key = lang.lower().replace("c++", "cpp").replace("c#", "csharp")
            final_solution["solutions"][key] = f"// Generation failed for {lang}\n// Reason: {error_msg}"

    def generate_solution(self, problem_data: Dict) -> Optional[Dict]:
        """Generate solution using the configured model"""
        print(f"Generating solution with {self.model_name}...", file=sys.stderr)

        if self.provider == 'groq':
            return self.solve_with_groq(problem_data)
        elif self.provider == 'gemini':
            return self.solve_with_gemini(problem_data)
        else:
            print(f"Unknown provider: {self.provider}, falling back to Gemini", file=sys.stderr)
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
