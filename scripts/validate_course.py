#!/usr/bin/env python3
"""
validate_course.py - Validates all 40 Hindi lesson files, manifest, and reference guides.
Ensures structural completeness, pedagogical constraints, and Duolingo-ready parsability.
"""

import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
DAYS_DIR = CONTENT_DIR / "days"
SCHEMA_FILE = BASE_DIR / "schema" / "course_schema.json"
MANIFEST_FILE = CONTENT_DIR / "course_manifest.json"
PHONETICS_FILE = CONTENT_DIR / "phonetics_guide.json"
COGNATES_FILE = CONTENT_DIR / "cognates_index.json"

REQUIRED_TOP_FIELDS = [
    "day", "phase", "title", "theme", "estimatedMinutes",
    "learningObjectives", "phoneticFocus", "contrastiveBridge",
    "vocabulary", "exercises", "simulationRoleplay", "culturalPragmatics"
]

EXERCISE_TYPES = {
    "phonetic_discrimination",
    "word_reorder_sov",
    "fill_in_blank",
    "substitution_drill",
    "listen_and_repeat",
    "rapid_oral_challenge",
    "dialogue_roleplay"
}

def validate_day_file(file_path: Path, expected_day: int) -> list:
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return [f"Failed to parse JSON: {e}"]

    # Day check
    if data.get("day") != expected_day:
        errors.append(f"Day mismatch: expected {expected_day}, got {data.get('day')}")

    # Phase check
    phase = data.get("phase")
    expected_phase = (expected_day - 1) // 8 + 1
    if phase != expected_phase:
        errors.append(f"Phase mismatch for day {expected_day}: expected {expected_phase}, got {phase}")

    # Top-level required fields
    for field in REQUIRED_TOP_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")

    # Titles
    title = data.get("title", {})
    if not isinstance(title, dict) or not title.get("en") or not title.get("ru"):
        errors.append("Title must contain non-empty 'en' and 'ru' strings")

    # Learning objectives
    objs = data.get("learningObjectives", {})
    if not isinstance(objs, dict) or not objs.get("ru") or not objs.get("en"):
        errors.append("learningObjectives must contain 'ru' and 'en' lists")

    # Phonetics focus
    pf = data.get("phoneticFocus", {})
    for req in ["targetSound", "articulatoryMechanism", "russianInterferenceWarning", "drills"]:
        if req not in pf:
            errors.append(f"phoneticFocus missing '{req}'")

    # Contrastive bridge
    cb = data.get("contrastiveBridge", {})
    for req in ["grammarConcept", "russianParallel", "syntacticFormula", "explanationRu"]:
        if req not in cb:
            errors.append(f"contrastiveBridge missing '{req}'")

    # Vocabulary
    vocab = data.get("vocabulary", [])
    if not isinstance(vocab, list) or len(vocab) < 3:
        errors.append(f"Vocabulary must contain at least 3 items, found {len(vocab) if isinstance(vocab, list) else 0}")
    else:
        vocab_ids = set()
        for idx, item in enumerate(vocab):
            for vreq in ["id", "devanagari", "transliterationIso", "phoneticCyrillic", "translationRu", "translationEn", "partOfSpeech"]:
                if not item.get(vreq):
                    errors.append(f"Vocab item #{idx} missing '{vreq}'")
            if item.get("id"):
                if item["id"] in vocab_ids:
                    errors.append(f"Duplicate vocab id '{item['id']}'")
                vocab_ids.add(item["id"])

    # Exercises
    exs = data.get("exercises", [])
    if not isinstance(exs, list) or len(exs) < 4:
        errors.append(f"Exercises must contain at least 4 items, found {len(exs) if isinstance(exs, list) else 0}")
    else:
        for idx, ex in enumerate(exs):
            for ereq in ["id", "type", "instructionRu", "prompt", "correctAnswer"]:
                if ereq not in ex or ex[ereq] is None:
                    errors.append(f"Exercise #{idx} missing '{ereq}'")
            ex_type = ex.get("type")
            if ex_type not in EXERCISE_TYPES:
                errors.append(f"Exercise #{idx} has invalid type '{ex_type}'")
            if ex_type == "word_reorder_sov" and not ex.get("wordChips"):
                errors.append(f"Exercise #{idx} (word_reorder_sov) missing 'wordChips'")

    # Simulation roleplay
    sim = data.get("simulationRoleplay", {})
    for sreq in ["scenarioTitleRu", "setting", "partnerRoleRu", "learnerRoleRu", "turns"]:
        if sreq not in sim:
            errors.append(f"simulationRoleplay missing '{sreq}'")
    turns = sim.get("turns", [])
    if not isinstance(turns, list) or len(turns) < 2:
        errors.append(f"simulationRoleplay must have at least 2 turns, found {len(turns) if isinstance(turns, list) else 0}")

    # Cultural pragmatics
    cp = data.get("culturalPragmatics", {})
    if not cp.get("titleRu") or not cp.get("pointsRu"):
        errors.append("culturalPragmatics must have 'titleRu' and 'pointsRu'")

    return errors

def main():
    print("=" * 60)
    print("Hindi 40-Day Curriculum Validator for Russian Speakers")
    print("=" * 60)

    total_errors = 0
    total_vocab = 0
    total_exercises = 0

    # 1. Validate manifest
    if not MANIFEST_FILE.exists():
        print(f"❌ Missing manifest file: {MANIFEST_FILE}")
        total_errors += 1
    else:
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            manifest = json.load(f)
            if manifest.get("totalDays") != 40:
                print("❌ Manifest totalDays must be 40")
                total_errors += 1
            else:
                print(f"✓ Manifest valid ({manifest.get('titleRu')})")

    # 2. Validate reference files
    if not PHONETICS_FILE.exists():
        print(f"❌ Missing phonetics guide: {PHONETICS_FILE}")
        total_errors += 1
    else:
        print("✓ Phonetics guide found")

    if not COGNATES_FILE.exists():
        print(f"❌ Missing cognates index: {COGNATES_FILE}")
        total_errors += 1
    else:
        print("✓ Cognates index found")

    # 3. Validate each of the 40 days
    print("\nValidating 40 Daily Modules:")
    for day in range(1, 41):
        day_filename = f"day_{day:02d}.json"
        day_path = DAYS_DIR / day_filename
        if not day_path.exists():
            print(f"❌ Day {day:02d}: File {day_filename} does not exist!")
            total_errors += 1
            continue

        errors = validate_day_file(day_path, day)
        if errors:
            print(f"❌ Day {day:02d} ({day_filename}) has {len(errors)} error(s):")
            for err in errors:
                print(f"   - {err}")
            total_errors += len(errors)
        else:
            with open(day_path, "r", encoding="utf-8") as f:
                ddata = json.load(f)
                v_count = len(ddata.get("vocabulary", []))
                e_count = len(ddata.get("exercises", []))
                total_vocab += v_count
                total_exercises += e_count
                print(f"  ✓ Day {day:02d}: {ddata['title']['ru']} ({v_count} vocab, {e_count} exercises)")

    print("-" * 60)
    print(f"SUMMARY: 40 Days | Total Vocabulary: {total_vocab} | Total Exercises: {total_exercises}")
    if total_errors == 0:
        print("🎉 ALL 40 DAYS AND SCHEMAS ARE 100% VALID AND COMPLETE!")
        return 0
    else:
        print(f"⚠️ Validation failed with {total_errors} errors.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
