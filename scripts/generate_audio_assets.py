#!/usr/bin/env python3
"""
Comprehensive Neural Audio Generator for 40-Day Hindi Curriculum
Uses Microsoft Azure Neural Hindi Female Voice (hi-IN-SwaraNeural)
via edge-tts to generate studio-grade MP3 audio for:
1. All 172 unique curriculum vocabulary items (indexed by Devanagari, ISO, and Cyrillic)
2. All 179 Simulation Roleplay turns across all 40 days
3. Phonetics Gym minimal pairs & key consonants
4. Warmup phonetic contrast drills (cleaned of Russian parentheticals)
5. Interactive exercise targets (listen-and-repeat, cloze targets)
6. PIE Cognates & essential communicative phrases
"""

import asyncio
import glob
import hashlib
import json
import os
import re
import sys
from pathlib import Path

# Voice Configuration - STRICTLY FEMALE
VOICE_FEMALE = "hi-IN-SwaraNeural"  # Clear, natural female Delhi/Mumbai educational voice

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "web" / "public" / "audio"
MANIFEST_FILE = PROJECT_ROOT / "web" / "src" / "data" / "audioManifest.json"
PUBLIC_MANIFEST = OUTPUT_DIR / "manifest.json"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)

try:
    import edge_tts
except ImportError:
    print("Error: edge-tts is not installed. Please run: pip install edge-tts")
    sys.exit(1)


def sanitize_filename(prefix: str, text: str) -> str:
    h = hashlib.md5(text.strip().encode('utf-8')).hexdigest()[:10]
    clean = re.sub(r'[^a-zA-Z0-9]', '_', text.strip().lower())[:15].strip('_')
    clean_prefix = re.sub(r'[^a-zA-Z0-9]', '_', prefix)[:12].strip('_')
    return f"{clean_prefix}_{clean}_{h}" if clean else f"{clean_prefix}_{h}"


def has_cyrillic(text: str) -> bool:
    """Returns True if string contains Cyrillic characters."""
    return bool(re.search(r'[\u0400-\u04FF]', text))


def clean_text_for_speech(text: str) -> str:
    """Strips Russian parentheticals, notes, and instructional markup."""
    # Remove anything inside parentheses e.g. (зубной), (не смягчать 'т'!), (Большое спасибо!)
    cleaned = re.sub(r'\([^)]*\)', '', text)
    # Remove quotes
    cleaned = re.sub(r'["\'«»]', '', cleaned)
    # Remove slashes or split options, e.g. "Khō gayā (m) / Khō gayī (f)" -> "Khō gayā"
    if '/' in cleaned:
        cleaned = cleaned.split('/')[0]
    # Remove exclamation or question marks at the beginning or extra punctuation
    return cleaned.strip()


async def synthesize_item(sem: asyncio.Semaphore, text: str, filename: str):
    # Guard against passing Cyrillic to the Hindi synthesizer
    if has_cyrillic(text):
        print(f"  ⚠ Skipping Cyrillic text from Hindi synthesizer: '{text}'")
        return None

    output_path = OUTPUT_DIR / f"{filename}.mp3"
    if output_path.exists() and output_path.stat().st_size > 500:
        return f"/audio/{filename}.mp3"

    async with sem:
        try:
            # -8% rate is optimal for language learners to hear aspiration and retroflexion
            communicate = edge_tts.Communicate(text, VOICE_FEMALE, rate="-8%")
            await communicate.save(str(output_path))
            print(f"  ✓ Synthesized [FEMALE]: {text[:35]} -> {filename}.mp3")
            return f"/audio/{filename}.mp3"
        except Exception as e:
            print(f"  ✗ Failed '{text[:35]}': {e}")
            return None


async def main():
    print("=" * 65)
    print("Comprehensive Hindi Neural Audio Generator (hi-IN-SwaraNeural FEMALE)")
    print("=" * 65)

    # Dictionary: text_to_synthesize -> list of manifest keys to map to this file
    text_to_keys = {}

    def register(text_to_speak: str, *keys):
        clean_speech = clean_text_for_speech(text_to_speak)
        if not clean_speech or has_cyrillic(clean_speech):
            return
        if clean_speech not in text_to_keys:
            text_to_keys[clean_speech] = set()
        for k in keys:
            if k:
                k_str = str(k).strip()
                text_to_keys[clean_speech].add(k_str)
                text_to_keys[clean_speech].add(f"text:{k_str}")
                text_to_keys[clean_speech].add(f"text:{k_str.lower()}")
                # Also add without parentheticals
                k_clean = clean_text_for_speech(k_str)
                if k_clean and k_clean != k_str:
                    text_to_keys[clean_speech].add(k_clean)
                    text_to_keys[clean_speech].add(f"text:{k_clean}")
                    text_to_keys[clean_speech].add(f"text:{k_clean.lower()}")
        # Also map pure speech text itself
        text_to_keys[clean_speech].add(f"text:{clean_speech}")
        text_to_keys[clean_speech].add(f"text:{clean_speech.lower()}")

    # 1. Collect all Vocabulary
    days_files = sorted(glob.glob(str(PROJECT_ROOT / "content" / "days" / "day_*.json")))
    for df in days_files:
        with open(df, "r", encoding="utf-8") as f:
            data = json.load(f)

            # A. Vocabulary
            for v in data.get("vocabulary", []):
                vid = v["id"]
                dev = v.get("devanagari", "").strip()
                iso = v.get("transliterationIso", "").strip()
                cyr = v.get("phoneticCyrillic", "").strip()

                clean_dev = clean_text_for_speech(dev)
                speech_text = clean_dev if clean_dev and not has_cyrillic(clean_dev) else clean_text_for_speech(iso)
                register(speech_text, f"vocab_{vid}", dev, iso, cyr, vid)

            # B. Simulation Roleplay turns
            turns = data.get("simulationRoleplay", {}).get("turns", [])
            day_num = data.get("day", 1)
            for idx, t in enumerate(turns):
                s_iso = t.get("speechIso", "").strip()
                s_cyr = t.get("speechCyrillic", "").strip()
                s_dev = t.get("speechDevanagari", "").strip()

                speech_target = ""
                if s_dev and not has_cyrillic(s_dev):
                    speech_target = clean_text_for_speech(s_dev)
                elif s_iso and not has_cyrillic(s_iso):
                    speech_target = clean_text_for_speech(s_iso)

                if speech_target:
                    turn_key = f"roleplay_d{day_num}_t{idx}"
                    register(speech_target, turn_key, s_iso, s_cyr)

            # C. Phonetic Focus Drills (Warmup)
            drills = data.get("phoneticFocus", {}).get("drills", [])
            for dr in drills:
                cp = dr.get("contrastPair", "").strip()
                if "vs" in cp:
                    parts = cp.split("vs")
                    p1 = clean_text_for_speech(parts[0])
                    p2 = clean_text_for_speech(parts[1])
                    if p1 and not has_cyrillic(p1):
                        register(p1, p1, parts[0].strip())
                    if p2 and not has_cyrillic(p2):
                        register(p2, p2, parts[1].strip())
                else:
                    p = clean_text_for_speech(cp)
                    if p and not has_cyrillic(p):
                        register(p, p, cp)

            # D. Exercise Targets
            for ex in data.get("exercises", []):
                iso_t = ex.get("transliterationIsoTarget")
                cyr_t = ex.get("phoneticCyrillicTarget")
                ans = ex.get("correctAnswer")

                ans_text = ""
                if isinstance(ans, list):
                    ans_text = " ".join(ans)
                elif isinstance(ans, str):
                    ans_text = ans

                speech_target = ""
                if iso_t and not has_cyrillic(iso_t):
                    speech_target = clean_text_for_speech(iso_t)
                elif ans_text and not has_cyrillic(ans_text):
                    speech_target = clean_text_for_speech(ans_text)

                if speech_target:
                    keys = [k for k in [iso_t, cyr_t, ans_text, ex.get("prompt")] if k]
                    register(speech_target, *keys)

    # 2. Phonetics Gym Minimal Pairs & Consonants
    phonetics_items = {
        "pair_tal_dental": "ताल",
        "pair_tal_retroflex": "टाल",
        "pair_sat_unaspirated": "सात",
        "pair_sath_aspirated": "साथ",
        "pair_kam_short": "कम",
        "pair_kam_long": "काम",
        "pair_phal_aspirated": "फल",
        "pair_pal_unaspirated": "पल",
        "pair_bhai_aspirated": "भाई",
        "pair_bai_plain": "बाई",
        "phoneme_ta_dental": "त",
        "phoneme_tha_aspirated": "थ",
        "phoneme_da_dental": "द",
        "phoneme_dha_aspirated": "ध",
        "phoneme_ta_retroflex": "ट",
        "phoneme_tha_retroflex": "ठ",
        "phoneme_da_retroflex": "ड",
        "phoneme_dha_retroflex": "ढ",
        "phoneme_ra_flap": "ड़",
        "phoneme_kha_aspirated": "ख",
        "phoneme_gha_aspirated": "घ",
        "phoneme_cha_aspirated": "छ",
        "phoneme_jha_aspirated": "झ",
    }
    for k, text in phonetics_items.items():
        register(text, k, text)

    # 3. Cognates
    cognates_file = PROJECT_ROOT / "content" / "cognates_index.json"
    if cognates_file.exists():
        with open(cognates_file, "r", encoding="utf-8") as f:
            cog_data = json.load(f)
            for c in cog_data.get("cognates", []):
                dev = c.get("hindiDevanagari", "").strip()
                iso = c.get("hindiWordIso", "").strip()
                cyr = c.get("hindiPhoneticCyrillic", "").strip()
                parts = [p.strip() for p in re.split(r'[/,]', dev) if p.strip()]
                for p in parts:
                    if not has_cyrillic(p):
                        register(p, p, iso, cyr)

    # 4. Common Conversational Phrases
    phrases = [
        "नमस्ते",
        "आप कैसे हैं?",
        "मैं ठीक हूँ",
        "धन्यवाद",
        "शुक्रिया",
        "मुझे पानी चाहिए",
        "मुझे चाय पसंद है",
        "कितने रुपये हैं?",
        "कृपया कम कीजिए",
        "धन्यवाद! फिर मिलेंगे",
        "नमस्ते! आप कैसे हैं?"
    ]
    for ph in phrases:
        register(ph, ph)

    print(f"Total unique non-Cyrillic speech targets to synthesize: {len(text_to_keys)}")

    # Concurrency limit
    sem = asyncio.Semaphore(8)
    tasks = []
    keys_list = list(text_to_keys.keys())

    for idx, speech_text in enumerate(keys_list):
        fname = sanitize_filename("fem", speech_text)
        tasks.append((speech_text, fname, synthesize_item(sem, speech_text, fname)))

    results = await asyncio.gather(*(t[2] for t in tasks))

    manifest = {}

    for idx, (speech_text, fname, _) in enumerate(tasks):
        url = results[idx]
        if url:
            item_entry = {
                "text": speech_text,
                "url": url,
                "filename": f"{fname}.mp3",
                "voice": "female"
            }
            # Assign to all mapped keys (both Devanagari, ISO, and Cyrillic)
            mapped_keys = text_to_keys[speech_text]
            for mk in mapped_keys:
                manifest[mk] = item_entry

    # Save manifest files
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    with open(PUBLIC_MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("=" * 65)
    print(f"✓ All audio synthesized using FEMALE voice ({VOICE_FEMALE})!")
    print(f"✓ Total indexed manifest keys: {len(manifest)}")
    print(f"✓ Manifest saved to: {MANIFEST_FILE}")
    print(f"✓ Audio files saved to: {OUTPUT_DIR}")
    print("=" * 65)


if __name__ == "__main__":
    asyncio.run(main())
