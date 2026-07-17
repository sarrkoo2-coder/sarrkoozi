#!/usr/bin/env python3
"""Print a compact learning-progress report from data/progress.csv."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "progress.csv"
WEIGHTS = {
    "knowledge": 0.25,
    "practice": 0.30,
    "artifact": 0.30,
    "explanation": 0.15,
}


def number(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, 0) or 0)
    except ValueError:
        return 0.0


def weekly_score(row: dict[str, str]) -> float:
    return sum(number(row, key) * weight for key, weight in WEIGHTS.items())


def main() -> None:
    if not CSV_PATH.exists():
        raise SystemExit(f"Progress file not found: {CSV_PATH}")

    with CSV_PATH.open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))

    completed = [row for row in rows if row.get("status") == "done"]
    active = [row for row in rows if row.get("status") in {"in-progress", "review", "rework"}]
    total_hours = sum(number(row, "hours") for row in rows)
    scored = [weekly_score(row) for row in rows if any(number(row, k) for k in WEIGHTS)]
    average = sum(scored) / len(scored) if scored else 0.0
    artifacts = sum(1 for row in rows if (row.get("artifact_link") or "").strip())
    readiness = (
        (len(completed) / len(rows) * 45)
        + (average / 100 * 35)
        + (artifacts / len(rows) * 20)
    )

    print("Junior BA learning progress")
    print("-" * 30)
    print(f"Modules completed: {len(completed)}/{len(rows)}")
    print(f"Active modules:    {len(active)}")
    print(f"Study hours:       {total_hours:.1f}")
    print(f"Average score:     {average:.1f}/100")
    print(f"Artifacts linked:  {artifacts}/{len(rows)}")
    print(f"Readiness index:   {readiness:.1f}/100")

    if active:
        print("\nCurrent focus:")
        for row in active:
            print(f"- Week {row['week']}: {row['module']} ({row['status']})")


if __name__ == "__main__":
    main()
