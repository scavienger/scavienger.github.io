#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unified post generator / regenerator.

Features:
  - Fetch LeetCode Daily Challenges via GraphQL dailyCodingChallengeV2 and cache date->(link,titleSlug)
  - Generate or overwrite posts for a date or date range
  - Gemini-only AI solutions (gemini-3.8-flash primary, fallback to gemini-3-flash-preview on 429 rate limit)
  - If post exists, overwrite AI solution sections; if missing, create new post
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import requests
from bs4 import BeautifulSoup
import yaml

# Reuse existing components
from solve_with_ai import AISolutionGenerator
from generate_post import PostGenerator

# Constants
DEFAULT_MODEL = "gemini-3.8-flash"
CACHE_PATH = os.path.join("data", "daily_challenges.json")
DAILY_POSTS_DIR = os.path.join("_posts", "_daily")


def ensure_cache_dir():
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)


def ensure_posts_dirs():
    os.makedirs(DAILY_POSTS_DIR, exist_ok=True)


def fetch_daily_challenges_v2(year: int, month: int) -> Dict[str, Dict[str, str]]:
    """
    Fetch daily challenges for a given year/month via GraphQL dailyCodingChallengeV2.
    """
    graphql_url = "https://leetcode.com/graphql"
    query = """
    query dailyChallenges($year: Int!, $month: Int!) {
      dailyCodingChallengeV2(year: $year, month: $month) {
        challenges {
          date
          link
          question { titleSlug }
        }
      }
    }
    """
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }
    variables = {"year": year, "month": month}
    resp = requests.post(graphql_url, json={"query": query, "variables": variables}, headers=headers, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        raise RuntimeError(f"GraphQL errors: {data['errors']}")
    root = data.get("data", {}).get("dailyCodingChallengeV2", {}) or {}
    challenges = root.get("challenges", []) or []

    out = {}
    for ch in challenges:
        date = ch.get("date")
        link = ch.get("link")
        slug = ch.get("question", {}).get("titleSlug")
        if date and link and slug:
            out[date] = {"link": link, "titleSlug": slug}
    return out


def load_cache() -> Dict[str, Dict[str, str]]:
    if not os.path.exists(CACHE_PATH):
        return {}
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_cache(cache: Dict[str, Dict[str, str]]):
    ensure_cache_dir()
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def update_cache_if_needed(target_dates: List[str]) -> Dict[str, Dict[str, str]]:
    """
    Load cache and refresh from network if any target date is missing.
    """
    cache = load_cache()
    missing = [d for d in target_dates if d not in cache]
    if not missing:
        return cache

    print(f"Cache missing dates: {', '.join(missing)}. Fetching daily challenges via GraphQL...", file=sys.stderr)

    months = set((int(d[:4]), int(d[5:7])) for d in missing)
    fetched_any = False
    for year, month in months:
        try:
            daily_map = fetch_daily_challenges_v2(year, month)
            if daily_map:
                cache.update(daily_map)
                fetched_any = True
        except Exception as e:
            print(f"Warning: failed to fetch challenges for {year}-{month:02d}: {e}", file=sys.stderr)

    if not fetched_any:
        print("Warning: fetched challenge list is empty; keeping existing cache.", file=sys.stderr)
        return cache

    save_cache(cache)
    return cache


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d")


def build_post_path(posts_dir: str, date_str: str, slug: str) -> str:
    """Build the new nested path for a post without the date prefix in filename."""
    dt = parse_date(date_str)
    year = dt.strftime("%Y")
    month = dt.strftime("%m")
    day = dt.strftime("%d")
    return os.path.join(posts_dir, year, month, day, f"{slug}.md")


def build_date_list(start_date: str, end_date: Optional[str]) -> List[str]:
    if not end_date:
        return [start_date]
    start_dt = parse_date(start_date)
    end_dt = parse_date(end_date)
    if end_dt < start_dt:
        raise ValueError("end_date must be >= start_date")
    dates = []
    cur = start_dt
    while cur <= end_dt:
        dates.append(cur.strftime("%Y-%m-%d"))
        cur += timedelta(days=1)
    return dates


def normalize_prompt_content(html_content: str) -> str:
    """Convert HTML content into compact plain text for AI prompts."""
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator="\n")
    lines = []
    last_blank = False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line:
            lines.append(line)
            last_blank = False
        elif not last_blank:
            lines.append("")
            last_blank = True
    return "\n".join(lines).strip()


def fetch_problem_by_slug(slug: str, snippet_dir: Optional[str] = None) -> Optional[Dict]:
    """
    Fetch problem details via LeetCode GraphQL by titleSlug.
    """
    graphql_url = "https://leetcode.com/graphql"
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            content
            difficulty
            exampleTestcases
            topicTags { name slug }
            codeSnippets { lang langSlug code }
            hints
        }
    }
    """
    payload = {"query": query, "variables": {"titleSlug": slug}}
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    resp = requests.post(graphql_url, json=payload, headers=headers, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
        return None
    question = data.get("data", {}).get("question")
    if not question:
        return None

    python_code = ""
    for snippet in question.get("codeSnippets", []):
        if snippet.get("langSlug") in ["python3", "python"]:
            python_code = snippet.get("code", "")
            break

    target_snippet_dir = snippet_dir or os.path.join("_posts", "_snippets", slug)
    if target_snippet_dir:
        os.makedirs(target_snippet_dir, exist_ok=True)
        for snippet in question.get("codeSnippets", []):
            lang_slug = snippet.get("langSlug", "")
            code = snippet.get("code", "")
            if lang_slug and code:
                snippet_file = os.path.join(target_snippet_dir, f"{lang_slug}.txt")
                with open(snippet_file, "w", encoding="utf-8") as f:
                    f.write(code)

    return {
        "title": question.get("title", "Unknown Title"),
        "title_slug": question.get("titleSlug", slug),
        "question_id": question.get("questionFrontendId", ""),
        "difficulty": question.get("difficulty", "Unknown"),
        "content": question.get("content", ""),
        "content_prompt": normalize_prompt_content(question.get("content", "")),
        "images": [],
        "topics": [tag.get("name") for tag in question.get("topicTags", [])],
        "hints": question.get("hints", []),
        "code_template": python_code,
    }


def generate_ai_solutions(
    problem_data: Dict,
    provider: Optional[str] = None,
    model_name: Optional[str] = None,
) -> List[Dict]:
    generator = AISolutionGenerator(provider=provider, model_name=model_name)
    sol = generator.generate_solution(problem_data)
    # Consider it a failure if generator returned nothing, or if it returned an error placeholder.
    approach_text = (sol or {}).get("approach", "")
    solutions = (sol or {}).get("solutions", {}) if sol else {}
    has_solutions = bool(sol and solutions)
    def _is_placeholder_solution(code: object) -> bool:
        if not isinstance(code, str):
            return False
        lowered = code.lower()
        return "generation failed" in lowered or "failed to parse response" in lowered
    has_real_solution = any(not _is_placeholder_solution(code) for code in solutions.values())
    looks_like_error = isinstance(approach_text, str) and approach_text.lower().startswith("failed to parse ai response")

    if sol and has_solutions and has_real_solution and not looks_like_error:
        sol["model"] = generator.model_name or DEFAULT_MODEL
        sol["generated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")
        elapsed = sol.get("elapsed_time", 0.0)
        print(f"✅ Generated with {sol['model']} -> {elapsed:.2f}s", file=sys.stderr)
        return [sol]

    reason = "missing result" if not sol else "parse/validation error"
    print(f"❌ Failed to generate with {generator.model_name or DEFAULT_MODEL} ({reason})", file=sys.stderr)
    return []


def find_post_file(date_str: str, posts_dir: str, slug: str) -> Optional[str]:
    """Locate an existing post, preferring the new nested path and falling back to legacy flat names."""
    expected_path = build_post_path(posts_dir, date_str, slug)
    if os.path.exists(expected_path):
        return expected_path

    if not os.path.exists(posts_dir):
        return None

    prefix = f"{date_str}-"
    for fname in os.listdir(posts_dir):
        if fname.startswith(prefix) and fname.endswith(".md"):
            return os.path.join(posts_dir, fname)
    return None


def load_existing_post(filepath: str) -> Dict:
    """Return a dict with keys 'ai_solutions' (list) and other front-matter if present."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return {}
    parts = re.split(r"^---\s*$", content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return {}
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except Exception:
        meta = {}
    return meta if isinstance(meta, dict) else {}


def build_question_data(problem: Dict, date_str: str, link: str, slug: str) -> Dict:
    """Create the dictionary that will be fed to PostGenerator."""
    return {
        "title": problem["title"],
        "slug": slug,
        "title_slug": problem.get("title_slug", slug),
        "date": date_str,
        "difficulty": problem["difficulty"],
        "content": problem["content"],
        "images": problem["images"],
        "topics": problem["topics"],
        "hints": problem["hints"],
        "code_template": problem["code_template"],
        "link": link,
        "question_id": problem.get("question_id", ""),
        "ai_solutions": [],   # will be filled later
    }

def process_date(
    date_str: str,
    link: str,
    slug: str,
    posts_dir: str,
    provider: Optional[str] = None,
    model_name: Optional[str] = None,
    only_missing: bool = False,
) -> bool:
    print(f"\n=== Processing {date_str} ({slug}) [{os.path.basename(posts_dir)}] ===", file=sys.stderr)
    post_path = build_post_path(posts_dir, date_str, slug)
    snippet_dir = os.path.dirname(post_path)

    problem = fetch_problem_by_slug(slug, snippet_dir=snippet_dir)
    if not problem:
        print(f"!! Failed to fetch problem for {slug}", file=sys.stderr)
        return False

    problem["date"] = date_str
    problem["slug"] = slug
    problem["only_missing"] = only_missing

    # Load any existing post to preserve solutions
    existing_post_path = find_post_file(date_str, posts_dir, slug)
    existing_meta = load_existing_post(existing_post_path) if existing_post_path else {}
    existing_solutions = existing_meta.get("ai_solutions", [])
    if existing_solutions and isinstance(existing_solutions[0], dict):
        problem["existing_ai_solution"] = existing_solutions[0]

    qdata = build_question_data(problem, date_str, f"https://leetcode.com{link}", slug)
    new_solutions = generate_ai_solutions(problem, provider=provider, model_name=model_name)
    qdata["ai_solutions"] = new_solutions if new_solutions else existing_solutions

    generator = PostGenerator(posts_dir)
    ensure_posts_dirs()
    filepath = generator.generate_post(qdata)
    if filepath:
        print(f"[ok] Wrote post: {filepath}", file=sys.stderr)
        return True
    print(f"!! Failed to write post for {date_str}", file=sys.stderr)
    return False


def scan_missing_posts(
    posts_dir: str = DAILY_POSTS_DIR,
    since_date: str = "2025-11-01",
    until_date: Optional[str] = None,
) -> List[Dict[str, str]]:
    """Scan daily posts directory for dates missing a post file or missing AI solutions entirely."""
    import glob

    start_dt = parse_date(since_date)
    end_dt = parse_date(until_date) if until_date else datetime.now()
    cache = load_cache()

    missing_items: List[Dict[str, str]] = []
    cur = start_dt
    while cur <= end_dt:
        d_str = cur.strftime("%Y-%m-%d")
        day_dir = os.path.join(posts_dir, cur.strftime("%Y"), cur.strftime("%m"), cur.strftime("%d"))
        md_files = sorted(glob.glob(os.path.join(day_dir, "*.md")))
        if not md_files:
            slug = (cache.get(d_str) or {}).get("titleSlug", "unknown")
            missing_items.append({
                "date": d_str,
                "status": "NO_POST_FILE",
                "difficulty": "Unknown",
                "slug": slug,
            })
        else:
            for p in md_files:
                with open(p, "r", encoding="utf-8") as f:
                    text = f.read()
                meta = load_existing_post(p)
                diff = str(meta.get("difficulty", "Unknown"))
                ai_sols = meta.get("ai_solutions", [])
                slug = os.path.splitext(os.path.basename(p))[0]
                if not ai_sols or "TODO: Add solution approach here." in text:
                    missing_items.append({
                        "date": d_str,
                        "status": "NO_AI_SOLUTION",
                        "difficulty": diff,
                        "slug": slug,
                    })
                elif isinstance(ai_sols[0], dict):
                    sols = ai_sols[0].get("solutions", {}) or {}
                    if sols and all("generation failed" in str(v).lower() for v in sols.values()):
                        missing_items.append({
                            "date": d_str,
                            "status": "ALL_LANGS_FAILED",
                            "difficulty": diff,
                            "slug": slug,
                        })
        cur += timedelta(days=1)

    # Sort newest first
    missing_items.sort(key=lambda x: x["date"], reverse=True)
    return missing_items


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate LeetCode daily challenge posts.")
    parser.add_argument("start_date", nargs="?", help="YYYY-MM-DD")
    parser.add_argument("end_date", nargs="?", help="YYYY-MM-DD (optional)")
    parser.add_argument(
        "--list-missing",
        action="store_true",
        help="List dates missing a post file or missing AI solutions entirely (newest first).",
    )
    parser.add_argument(
        "--provider",
        choices=["gemini", "codex"],
        default=os.getenv("AI_PROVIDER", "gemini"),
        help="AI provider to use: 'gemini' (default for GitHub Actions) or 'codex' (ChatGPT subscription CLI for local follow-up).",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Override model name (e.g. 'gpt-6-luna' or 'gpt-6.1-sol' for codex; 'gemini-3.8-flash' for gemini).",
    )
    parser.add_argument(
        "--only-missing",
        action="store_true",
        help="Skip batches whose languages already have valid solutions in the existing post.",
    )
    args = parser.parse_args()

    if args.list_missing:
        items = scan_missing_posts(DAILY_POSTS_DIR)
        print(f"Found {len(items)} completely missing/unsolved dates (newest first):")
        for item in items:
            print(f"  {item['date']}  [{item['difficulty']:<7}]  {item['status']:<16}  {item['slug']}")
        return 0

    if not args.start_date:
        parser.error("start_date is required unless --list-missing is specified.")

    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    end_date = args.end_date if args.end_date and date_pattern.match(args.end_date) else None

    try:
        dates = build_date_list(args.start_date, end_date)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    active_model = args.model or (
        AISolutionGenerator.CODEX_MODEL if args.provider == "codex" else DEFAULT_MODEL
    )
    print(f"Dates: {', '.join(dates)}", file=sys.stderr)
    print(f"Provider: {args.provider} | Model: {active_model}", file=sys.stderr)

    cache = update_cache_if_needed(dates)

    overall_success = True
    for i, d in enumerate(dates):
        info = cache.get(d)

        if info:
            extra_kwargs = {}
            if args.provider != "gemini":
                extra_kwargs["provider"] = args.provider
            if args.model is not None:
                extra_kwargs["model_name"] = args.model
            if args.only_missing:
                extra_kwargs["only_missing"] = True
            ok = process_date(
                d,
                info["link"],
                info["titleSlug"],
                DAILY_POSTS_DIR,
                **extra_kwargs,
            )
            overall_success = overall_success and ok
        else:
            print(f"ℹ️ No daily challenge for {d} in cache. Skipping.", file=sys.stderr)

        # Wait between dates (except after last)
        if i < len(dates) - 1:
            inter_date_wait = 2 if args.provider == "codex" else 60
            print(f"Waiting {inter_date_wait} seconds before next date...", file=sys.stderr)
            time.sleep(inter_date_wait)

    return 0 if overall_success else 1

if __name__ == "__main__":
    sys.exit(main())
