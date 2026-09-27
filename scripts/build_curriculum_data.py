#!/usr/bin/env python3
"""
build_curriculum_data.py - Compiles all 40 individual Day JSON modules
from Phase 1 to Phase 5 into content/days/day_01.json ... day_40.json.
"""

import json
import sys
from pathlib import Path

# Add scripts directory to sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from data_phase1 import DAYS_PHASE_1
from data_phase2 import DAYS_PHASE_2
from data_phase3 import DAYS_PHASE_3
from data_phase4 import DAYS_PHASE_4
from data_phase5 import DAYS_PHASE_5

BASE_DIR = SCRIPT_DIR.parent
DAYS_DIR = BASE_DIR / "content" / "days"
DAYS_DIR.mkdir(parents=True, exist_ok=True)

def main():
    all_days = (
        DAYS_PHASE_1 +
        DAYS_PHASE_2 +
        DAYS_PHASE_3 +
        DAYS_PHASE_4 +
        DAYS_PHASE_5
    )

    if len(all_days) != 40:
        print(f"Error: Expected 40 days, got {len(all_days)}")
        sys.exit(1)

    print(f"Compiling {len(all_days)} daily lessons into {DAYS_DIR}...")

    total_vocab = 0
    total_exercises = 0

    for day_data in all_days:
        day_num = day_data["day"]
        filename = f"day_{day_num:02d}.json"
        target_path = DAYS_DIR / filename

        # Compute stats
        v_count = len(day_data.get("vocabulary", []))
        e_count = len(day_data.get("exercises", []))
        total_vocab += v_count
        total_exercises += e_count

        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(day_data, f, ensure_ascii=False, indent=2)

        print(f"  ✓ Written {filename} (Phase {day_data['phase']}) - {day_data['title']['ru']}")

    print("=" * 60)
    print(f"Successfully generated all 40 day files!")
    print(f"Total Vocabulary items: {total_vocab}")
    print(f"Total Duolingo-style Exercises: {total_exercises}")
    print("=" * 60)

if __name__ == "__main__":
    main()
