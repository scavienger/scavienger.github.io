import sys
from pathlib import Path
from typing import List, Dict

import pytest

# Ensure project root and scripts directory are importable
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SCRIPTS_DIR = ROOT / "scripts"
if SCRIPTS_DIR.is_dir() and str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import scripts.generate_posts as gp


def _run_main(monkeypatch, argv: List[str], daily_map: Dict[str, Dict]):
    """Run generate_posts.main with network/AI calls mocked out."""
    calls = []

    def fake_update_cache(target_dates):
        return daily_map

    def fake_process_date(date_str, link, slug, posts_dir):
        calls.append(
            {
                "date": date_str,
                "link": link,
                "slug": slug,
                "posts_dir": posts_dir,
            }
        )
        return True

    monkeypatch.setattr(gp, "update_cache_if_needed", fake_update_cache)
    monkeypatch.setattr(gp, "process_date", fake_process_date)
    monkeypatch.setattr(gp.time, "sleep", lambda s: None)
    monkeypatch.setattr(sys, "argv", ["generate_posts.py"] + argv)

    code = gp.main()
    return code, calls


def test_single_date_all_default_models(monkeypatch):
    daily = {"2025-11-01": {"link": "/problems/foo/", "titleSlug": "foo"}}
    code, calls = _run_main(monkeypatch, ["2025-11-01"], daily)

    assert code == 0
    assert len(calls) == 1
    assert calls[0]["date"] == "2025-11-01"
    assert calls[0]["posts_dir"] == gp.DAILY_POSTS_DIR


def test_date_range_all_default_models(monkeypatch):
    daily = {
        "2025-11-01": {"link": "/problems/foo/", "titleSlug": "foo"},
        "2025-11-02": {"link": "/problems/bar/", "titleSlug": "bar"},
    }
    code, calls = _run_main(monkeypatch, ["2025-11-01", "2025-11-02"], daily)

    assert code == 0
    assert len(calls) == 2
    assert [c["date"] for c in calls] == ["2025-11-01", "2025-11-02"]
