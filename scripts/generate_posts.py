#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unified post generator / regenerator.

Features:
  - Fetch LeetCode Daily Challenges via problemset __NEXT_DATA__ and cache date->(link,titleSlug)
  - Generate or overwrite posts for a date or date range
  - Multiple AI models (defaults: gemini-2.5-flash, llama-3.3-70b-versatile, groq/compound); validates model names
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
SUPPORTED_MODELS = ['gemini-2.5-flash', 'llama-3.3-70b-versatile', 'groq/compound']
DEFAULT_MODELS = ['gemini-2.5-flash', 'llama-3.3-70b-versatile']
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


def validate_models(models: List[str]) -> List[str]:
    if not models:
        return DEFAULT_MODELS
    invalid = [m for m in models if m not in SUPPORTED_MODELS]
    if invalid:
        raise ValueError(f"Invalid model(s): {', '.join(invalid)}. Supported: {', '.join(SUPPORTED_MODELS)}")
    return models


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
        "images": [],
        "topics": [tag.get("name") for tag in question.get("topicTags", [])],
        "hints": question.get("hints", []),
        "code_template": python_code,
    }


def generate_ai_solutions(problem_data: Dict, model_names: List[str]) -> List[Dict]:
    solutions = []
    for model in model_names:
        os.environ["AI_MODEL"] = model
        generator = AISolutionGenerator()
        sol = generator.generate_solution(problem_data)
        if sol:
            sol["model"] = model
            sol["generated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")
            solutions.append(sol)
            elapsed = sol.get("elapsed_time", 0.0)
            print(f"✅ Generated with {model} -> {elapsed:.2f}s", file=sys.stderr)
        else:
            # Use ❌ to clearly indicate failure in logs
            print(f"❌ Failed to generate with {model}", file=sys.stderr)
    return solutions


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
    """Return a dict with keys 'ai_solutions' (list) and other front‑matter if present."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return {}
    parts = content.split("---")
    # parts[1] is the YAML front‑matter
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except Exception:
        meta = {}
    return meta


def merge_solutions(existing: List[Dict], new: List[Dict]) -> List[Dict]:
    """Replace or add solutions by model name."""
    existing_by_model = {s.get("model"): s for s in existing or []}
    for sol in new:
        existing_by_model[sol.get("model")] = sol
    return list(existing_by_model.values())

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

def process_date(date_str: str, link: str, slug: str, model_names: List[str], posts_dir: str, update_models: Optional[List[str]] = None) -> bool:
    print(f"\n=== Processing {date_str} ({slug}) [{os.path.basename(posts_dir)}] ===", file=sys.stderr)
    post_path = build_post_path(posts_dir, date_str, slug)
    snippet_dir = os.path.dirname(post_path)

    problem = fetch_problem_by_slug(slug, snippet_dir=snippet_dir)
    if not problem:
        print(f"!! Failed to fetch problem for {slug}", file=sys.stderr)
        return False

    problem["date"] = date_str
    problem["slug"] = slug

    # Load any existing post to preserve solutions
    existing_post_path = find_post_file(date_str, posts_dir, slug)
    existing_meta = load_existing_post(existing_post_path) if existing_post_path else {}
    existing_solutions = existing_meta.get("ai_solutions", [])

    # Determine which models we actually need to generate
    if update_models:
        needed_models = [m for m in update_models if m in model_names]
    else:
        # generate only missing models
        needed_models = [m for m in model_names if not any(s.get("model") == m for s in existing_solutions)]

    if not needed_models:
        print(f"?? All requested models already present for {date_str}. Skipping generation.", file=sys.stderr)
        # Still write post to ensure any other fields are up-to-date
        qdata = build_question_data(problem, date_str, f"https://leetcode.com{link}", slug)
        qdata["ai_solutions"] = existing_solutions
        generator = PostGenerator(posts_dir)
        ensure_posts_dirs()
        generator.generate_post(qdata)
        return True

    qdata = build_question_data(problem, date_str, f"https://leetcode.com{link}", slug)
    # Generate only needed models
    new_solutions = generate_ai_solutions(problem, needed_models)
    # Merge with existing solutions (replace same model)
    merged = merge_solutions(existing_solutions, new_solutions)
    qdata["ai_solutions"] = merged

    generator = PostGenerator(posts_dir)
    ensure_posts_dirs()
    filepath = generator.generate_post(qdata)
    if filepath:
        print(f"[ok] Wrote post: {filepath}", file=sys.stderr)
        return True
    print(f"!! Failed to write post for {date_str}", file=sys.stderr)
    return False


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate LeetCode daily challenge posts.")
    parser.add_argument("start_date", help="YYYY-MM-DD")
    parser.add_argument("end_date", nargs="?", help="YYYY-MM-DD (optional)")
    parser.add_argument("models", nargs="*", help="Model names to use (default: all supported)")
    parser.add_argument("--update-models", dest="update_models", default="", help="Comma‑separated list of models to re‑generate for existing posts")
    args = parser.parse_args()

    # Determine if the second positional argument is actually an end_date or a model name.
    # If it does not match the YYYY-MM-DD pattern, treat it as part of the models list.
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    end_date = args.end_date if args.end_date and date_pattern.match(args.end_date) else None
    models_list = []
    if args.end_date and not date_pattern.match(args.end_date):
        # args.end_date is actually a model name; prepend it to models list
        models_list.append(args.end_date)
    models_list.extend(args.models)

    try:
        dates = build_date_list(args.start_date, end_date)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    try:
        models = validate_models(models_list)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    update_models = [m.strip() for m in args.update_models.split(',') if m.strip()] if args.update_models else None

    print(f"Dates: {', '.join(dates)}", file=sys.stderr)
    print(f"Models: {', '.join(models)}", file=sys.stderr)
    if update_models:
        print(f"Update‑only models: {', '.join(update_models)}", file=sys.stderr)

    cache = update_cache_if_needed(dates)

    overall_success = True
    for i, d in enumerate(dates):
        info = cache.get(d)

        if info:
            ok = process_date(d, info["link"], info["titleSlug"], models, DAILY_POSTS_DIR, update_models)
            overall_success = overall_success and ok
        else:
            print(f"ℹ️ No daily challenge for {d} in cache. Skipping.", file=sys.stderr)

        # Wait between dates (except after last)
        if i < len(dates) - 1:
            print("Waiting 60 seconds before next date...", file=sys.stderr)
            time.sleep(60)

    return 0 if overall_success else 1

if __name__ == "__main__":
    sys.exit(main())
