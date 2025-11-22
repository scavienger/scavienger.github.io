#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unified post generator / regenerator.

Features:
  - Fetch LeetCode Daily Challenges via problemset __NEXT_DATA__ and cache date->(link,titleSlug)
  - Generate or overwrite posts for a date or date range
  - Multiple AI models (defaults: gemini-2.5-flash, llama-3.3-70b-versatile); validates model names
  - If post exists, overwrite AI solution sections; if missing, create new post

Usage:
  python scripts/generate_posts.py <start_date> [end_date] [models...]
    - date format: YYYY-MM-DD
    - if end_date omitted: single date
    - if models omitted: all supported models
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import requests
from bs4 import BeautifulSoup

# Reuse existing components
from solve_with_ai import AISolutionGenerator
from generate_post import PostGenerator

# Constants
SUPPORTED_MODELS = ['gemini-2.5-flash', 'llama-3.3-70b-versatile', 'qwen-2.5-32b', 'groq/compound']
DEFAULT_MODELS = ['gemini-2.5-flash', 'llama-3.3-70b-versatile']
CACHE_PATH = os.path.join("data", "daily_challenges.json")
WEEKLY_CACHE_PATH = os.path.join("data", "weekly_challenges.json")
DAILY_POSTS_DIR = os.path.join("_posts", "_daily")
WEEKLY_POSTS_DIR = os.path.join("_posts", "_weekly")


def ensure_cache_dir():
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    os.makedirs(os.path.dirname(WEEKLY_CACHE_PATH), exist_ok=True)


def ensure_posts_dirs():
    os.makedirs(DAILY_POSTS_DIR, exist_ok=True)
    os.makedirs(WEEKLY_POSTS_DIR, exist_ok=True)


def fetch_daily_challenges_v2(year: int, month: int) -> Dict[str, Dict[str, Dict[str, str]]]:
    """
    Fetch daily/weekly challenges for a given year/month via GraphQL dailyCodingChallengeV2.
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
        weeklyChallenges {
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
    weekly = root.get("weeklyChallenges", []) or []

    def to_map(items):
        out = {}
        for ch in items:
            date = ch.get("date")
            link = ch.get("link")
            slug = ch.get("question", {}).get("titleSlug")
            if date and link and slug:
                out[date] = {"link": link, "titleSlug": slug}
        return out

    return {"daily": to_map(challenges), "weekly": to_map(weekly)}


def load_cache() -> Dict[str, Dict[str, str]]:
    if not os.path.exists(CACHE_PATH):
        return {}
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_weekly_cache() -> Dict[str, Dict[str, str]]:
    if not os.path.exists(WEEKLY_CACHE_PATH):
        return {}
    with open(WEEKLY_CACHE_PATH, "r", encoding="utf-8") as f:
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
    weekly_cache = load_weekly_cache()
    missing = [d for d in target_dates if d not in cache]
    if not missing:
        return cache

    print(f"Cache missing dates: {', '.join(missing)}. Fetching daily challenges via GraphQL...", file=sys.stderr)

    # determine months to fetch
    months = set((int(d[:4]), int(d[5:7])) for d in missing)
    fetched_any = False
    for year, month in months:
        try:
            fetched = fetch_daily_challenges_v2(year, month)
            daily_map = fetched.get("daily", {})
            weekly_map = fetched.get("weekly", {})
            if daily_map:
                cache.update(daily_map)
                fetched_any = True
            if weekly_map:
                weekly_cache.update(weekly_map)
        except Exception as e:
            print(f"Warning: failed to fetch challenges for {year}-{month:02d}: {e}", file=sys.stderr)

    if not fetched_any:
        print("Warning: fetched challenge list is empty; keeping existing cache.", file=sys.stderr)
        return cache

    save_cache(cache)
    # Save weekly cache even if unchanged to ensure file exists
    ensure_cache_dir()
    with open(WEEKLY_CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(weekly_cache, f, ensure_ascii=False, indent=2)
    return cache


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d")


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


def fetch_problem_by_slug(slug: str) -> Optional[Dict]:
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

    # Extract Python template if present
    python_code = ""
    for snippet in question.get("codeSnippets", []):
        if snippet.get("langSlug") in ["python3", "python"]:
            python_code = snippet.get("code", "")
            break

    # Images are not explicitly included; leave empty
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
            print(f"⚠️ Failed to generate with {model}", file=sys.stderr)
    return solutions


def find_post_file(date_str: str, posts_dir: str) -> Optional[str]:
    prefix = f"{date_str}-"
    if not os.path.exists(posts_dir):
        return None
    for fname in os.listdir(posts_dir):
        if fname.startswith(prefix) and fname.endswith(".md"):
            return os.path.join(posts_dir, fname)
    return None


def build_question_data(problem: Dict, date_str: str, link: str) -> Dict:
    return {
        "title": problem["title"],
        "date": date_str,
        "difficulty": problem["difficulty"],
        "content": problem["content"],
        "images": problem["images"],
        "topics": problem["topics"],
        "hints": problem["hints"],
        "code_template": problem["code_template"],
        "link": link,
        "question_id": problem.get("question_id", ""),
        "ai_solutions": [],
    }


def process_date(date_str: str, link: str, slug: str, model_names: List[str], posts_dir: str) -> bool:
    print(f"\n=== Processing {date_str} ({slug}) [{os.path.basename(posts_dir)}] ===", file=sys.stderr)
    problem = fetch_problem_by_slug(slug)
    if not problem:
        print(f"⚠️ Failed to fetch problem for {slug}", file=sys.stderr)
        return False

    qdata = build_question_data(problem, date_str, f"https://leetcode.com{link}")
    ai_solutions = generate_ai_solutions(problem, model_names)
    qdata["ai_solutions"] = ai_solutions

    generator = PostGenerator(posts_dir)
    ensure_posts_dirs()
    filepath = generator.generate_post(qdata)
    if filepath:
        print(f"✅ Wrote post: {filepath}", file=sys.stderr)
        return True
    print(f"⚠️ Failed to write post for {date_str}", file=sys.stderr)
    return False


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    # Parse args
    start_date = sys.argv[1]
    end_date = None
    models_start_index = 2

    if len(sys.argv) >= 3 and re.match(r"^\d{4}-\d{2}-\d{2}$", sys.argv[2]):
        end_date = sys.argv[2]
        models_start_index = 3

    try:
        dates = build_date_list(start_date, end_date)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    try:
        models = validate_models(sys.argv[models_start_index:])
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print(f"Dates: {', '.join(dates)}", file=sys.stderr)
    print(f"Models: {', '.join(models)}", file=sys.stderr)

    # Ensure cache and load challenges
    cache = update_cache_if_needed(dates)
    weekly_cache = load_weekly_cache()

    # Track overall success
    overall_success = True
    for d in dates:
        info = cache.get(d)
        weekly_info = weekly_cache.get(d)

        # Daily
        if info:
            ok = process_date(d, info["link"], info["titleSlug"], models, DAILY_POSTS_DIR)
            overall_success = overall_success and ok
        else:
            print(f"ℹ️ No daily challenge for {d} in cache. Skipping daily.", file=sys.stderr)

        # Weekly (optional)
        if weekly_info:
            ok_w = process_date(d, weekly_info["link"], weekly_info["titleSlug"], models, WEEKLY_POSTS_DIR)
            overall_success = overall_success and ok_w
        else:
            print(f"ℹ️ No weekly challenge for {d} in cache. Skipping weekly.", file=sys.stderr)

    return 0 if overall_success else 1


if __name__ == "__main__":
    sys.exit(main())
