#!/usr/bin/env python3
"""
scripts/generate_all_audio.py
Exhaustive Pure Devanagari Neural Audio Generator for HindiTutor (Voice: hi-IN-SwaraNeural)
Synthesizes 100% authentic native Hindi speech by converting all course inputs into canonical
Devanagari script before synthesis, eliminating any English/Hinglish phonetic degradation.
"""

import asyncio
import glob
import hashlib
import json
import re
import sys
import shutil
from pathlib import Path

# Add project root to sys.path so we can import scripts.devanagari_master
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.devanagari_master import iso_to_devanagari

VOICE_FEMALE = "hi-IN-SwaraNeural"

OUTPUT_DIR = PROJECT_ROOT / "web" / "public" / "audio"
DIST_AUDIO_DIR = PROJECT_ROOT / "web" / "dist" / "audio"
MANIFEST_FILE = PROJECT_ROOT / "web" / "src" / "data" / "audioManifest.json"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
DIST_AUDIO_DIR.mkdir(parents=True, exist_ok=True)

try:
    import edge_tts
except ImportError:
    print("Error: edge-tts is not installed. Please run: pip install edge-tts")
    sys.exit(1)

def has_cyrillic(text: str) -> bool:
    return bool(re.search(r'[\u0400-\u04FF]', text))

def has_devanagari(text: str) -> bool:
    return bool(re.search(r'[\u0900-\u097F]', text))

def clean_text_for_speech(text: str) -> str:
    if not text:
        return ""
    # Strip parentheticals e.g. (m), (f), (зубной)
    cleaned = re.sub(r'[\(\[\{][^\)\]\}]*[\)\]\}]', '', text)
    # Strip quotes and brackets
    cleaned = re.sub(r'["\'«»\[\]]', '', cleaned)
    # If slash options present e.g. "Khō gayā / Khō gayī", take first option
    if '/' in cleaned:
        cleaned = cleaned.split('/')[0]
    # Strip trailing/leading punctuation
    cleaned = re.sub(r'^[!?.,:;—\-_]+|[!?.,:;—\-_]+$', '', cleaned)
    return cleaned.strip()

def sanitize_filename(prefix: str, text: str) -> str:
    h = hashlib.md5(text.strip().encode('utf-8')).hexdigest()[:10]
    clean_prefix = re.sub(r'[^a-zA-Z0-9]', '_', prefix)[:10].strip('_')
    return f"{clean_prefix}_{h}"

async def synthesize_item(sem: asyncio.Semaphore, text: str, filename: str):
    output_path = OUTPUT_DIR / f"{filename}.mp3"
    dist_path = DIST_AUDIO_DIR / f"{filename}.mp3"

    # Reuse if already synthesized and valid
    if output_path.exists() and output_path.stat().st_size > 500:
        if not dist_path.exists():
            shutil.copy2(output_path, dist_path)
        return f"/audio/{filename}.mp3"

    async with sem:
        try:
            # Azure SwaraNeural with -4% rate for natural, articulate diction
            communicate = edge_tts.Communicate(text, VOICE_FEMALE, rate="-4%")
            await communicate.save(str(output_path))
            shutil.copy2(output_path, dist_path)
            print(f"  ✓ Synthesized [Devanagari]: '{text[:30]}' -> {filename}.mp3")
            return f"/audio/{filename}.mp3"
        except Exception as e:
            print(f"  ✗ Failed '{text[:30]}': {e}")
            return None

async def main():
    print("=" * 70)
    print("Exhaustive Pure Devanagari Audio Generator (Azure hi-IN-SwaraNeural FEMALE)")
    print("=" * 70)

    # dev_speech_text -> set of lookup keys
    speech_registry = {}

    def register(text_to_speak: str, *keys):
        if not text_to_speak:
            return
        clean_speech = clean_text_for_speech(text_to_speak)
        if not clean_speech:
            return

        # 1. Obtain pure Devanagari text for speech synthesis
        if has_devanagari(clean_speech):
            dev_speech = clean_speech
        else:
            dev_speech = iso_to_devanagari(clean_speech)

        if not dev_speech or not dev_speech.strip():
            dev_speech = clean_speech

        if dev_speech not in speech_registry:
            speech_registry[dev_speech] = set()

        # 2. Register all conceivable lookup keys
        all_raw_keys = list(keys) + [clean_speech, dev_speech]
        for k in all_raw_keys:
            if not k:
                continue
            k_str = str(k).strip()
            if not k_str:
                continue

            k_clean = clean_text_for_speech(k_str)
            k_no_punct = re.sub(r'[!?.,:;—\-_"\'«»\[\]]', '', k_str).strip()
            k_clean_no_punct = re.sub(r'[!?.,:;—\-_"\'«»\[\]]', '', k_clean).strip()

            variants = {
                k_str,
                k_clean,
                k_no_punct,
                k_clean_no_punct,
                k_str.lower(),
                k_clean.lower(),
                k_no_punct.lower(),
                k_clean_no_punct.lower(),
                f"text:{k_str}",
                f"text:{k_clean}",
                f"text:{k_no_punct}",
                f"text:{k_str.lower()}",
                f"text:{k_clean.lower()}",
                f"text:{k_no_punct.lower()}"
            }
            speech_registry[dev_speech].update(variants)

    # 1. Crawl all 40 Days
    days_files = sorted(glob.glob(str(PROJECT_ROOT / "content" / "days" / "day_*.json")))
    print(f"Crawling {len(days_files)} curriculum day files...")

    for df in days_files:
        with open(df, "r", encoding="utf-8") as f:
            data = json.load(f)
            day_num = data.get("day", 1)

            # A. Vocabulary
            for v in data.get("vocabulary", []):
                vid = v.get("id", "")
                dev = v.get("devanagari", "").strip()
                iso = v.get("transliterationIso", "").strip()
                cyr = v.get("phoneticCyrillic", "").strip()

                target_speech = dev if dev else iso
                register(target_speech, dev, iso, cyr, vid, f"vocab_{vid}", f"vocab_{iso}", f"vocab_{dev}")

                # Register each individual word in multi-word vocabulary
                for word in iso.split():
                    clean_w = clean_text_for_speech(word)
                    if len(clean_w) > 1 and not has_cyrillic(clean_w):
                        register(clean_w, clean_w, f"chip_{clean_w}")

            # B. Exercises
            for e_idx, ex in enumerate(data.get("exercises", [])):
                # Word Chips
                for chip in ex.get("wordChips", []):
                    register(chip, chip, f"chip_{chip}")
                # Options
                for opt in ex.get("options", []):
                    clean_opt = clean_text_for_speech(opt)
                    if clean_opt and not has_cyrillic(clean_opt):
                        register(clean_opt, opt, clean_opt)
                # Correct Answer
                ans = ex.get("correctAnswer")
                if isinstance(ans, list):
                    joined_ans = " ".join(ans)
                    register(joined_ans, joined_ans)
                    for a in ans:
                        register(a, a, f"chip_{a}")
                elif isinstance(ans, str):
                    clean_ans = clean_text_for_speech(ans)
                    if clean_ans and not has_cyrillic(clean_ans):
                        register(clean_ans, ans, clean_ans)
                # Targets
                iso_t = ex.get("transliterationIsoTarget")
                dev_t = ex.get("devanagariTarget")
                cyr_t = ex.get("phoneticCyrillicTarget")
                target_ex = dev_t if dev_t else iso_t
                if target_ex:
                    register(target_ex, iso_t, dev_t, cyr_t)

            # C. Simulation Roleplay turns
            turns = data.get("simulationRoleplay", {}).get("turns", [])
            for t_idx, turn in enumerate(turns):
                s_iso = turn.get("speechIso", "").strip()
                s_dev = turn.get("speechDevanagari", "").strip()
                s_cyr = turn.get("speechCyrillic", "").strip()
                t_key = f"roleplay_d{day_num}_t{t_idx}"

                target_turn = s_dev if s_dev else s_iso
                register(target_turn, t_key, s_iso, s_dev, s_cyr)

                # Acceptable response chips
                for resp in turn.get("acceptableResponsesIso", []):
                    register(resp, resp, f"resp_{resp}")
                for resp_dev in turn.get("acceptableResponsesDevanagari", []):
                    register(resp_dev, resp_dev)

            # D. Phonetic Focus Drills
            drills = data.get("phoneticFocus", {}).get("drills", [])
            for dr in drills:
                cp = dr.get("contrastPair", "").strip()
                if "vs" in cp:
                    parts = cp.split("vs")
                    for p in parts:
                        clean_p = clean_text_for_speech(p)
                        if clean_p and not has_cyrillic(clean_p):
                            register(clean_p, clean_p, p.strip())
                else:
                    clean_p = clean_text_for_speech(cp)
                    if clean_p and not has_cyrillic(clean_p):
                        register(clean_p, clean_p, cp.strip())

    # 2. Cognates Index
    cog_file = PROJECT_ROOT / "content" / "cognates_index.json"
    if cog_file.exists():
        with open(cog_file, "r", encoding="utf-8") as f:
            cog_data = json.load(f)
            for c in cog_data.get("cognates", []):
                dev = c.get("hindiDevanagari", "")
                iso = c.get("hindiWordIso", "")
                cyr = c.get("hindiPhoneticCyrillic", "")

                for p in re.split(r'[/,]', dev):
                    p_clean = clean_text_for_speech(p)
                    if p_clean and not has_cyrillic(p_clean):
                        register(p_clean, p.strip(), p_clean)

                for p in re.split(r'[/,]', iso):
                    p_clean = clean_text_for_speech(p)
                    if p_clean and not has_cyrillic(p_clean):
                        register(p_clean, p.strip(), p_clean)

                target_c = dev if dev else iso
                register(target_c, dev, iso, cyr)

    # 3. Phonetics Gym Consonants & Minimal Pairs
    phonetics_gym = {
        "त": "त", "थ": "थ", "द": "द", "ध": "ध",
        "ट": "ट", "ठ": "ठ", "ड": "ड", "ढ": "ढ", "ड़": "ड़",
        "ख": "ख", "घ": "घ", "छ": "छ", "झ": "झ", "फ": "फ", "भ": "भ",
        "क": "क", "ग": "ग", "च": "च", "ज": "ज", "प": "प", "ब": "ब",
        "म": "म", "न": "न", "र": "र", "ल": "ल", "व": "व", "श": "श", "स": "स", "ह": "ह",
        "ta": "त", "tha": "थ", "da": "द", "dha": "ध",
        "ṭa": "ट", "ṭha": "ठ", "ḍa": "ड", "ḍha": "ढ", "ṛa": "ड़",
        "kha": "ख", "gha": "घ", "cha": "छ", "jha": "झ", "pha": "फ", "bha": "भ",
        "ताल": "ताल", "टाल": "टाल", "tāl": "ताल", "ṭāl": "टाल",
        "सात": "सात", "साथ": "साथ", "sāt": "सात", "sāth": "साथ",
        "कम": "कम", "काम": "काम", "kam": "कम", "kām": "काम",
        "फल": "फल", "पल": "पल", "phal": "फल", "pal": "पल",
        "भाई": "भाई", "बाई": "बाई", "bhāī": "भाई", "bāī": "बाई"
    }
    for k, val in phonetics_gym.items():
        register(val, k, val, f"pair_{k}", f"phoneme_{k}")

    # 4. Settings & Check Phrases
    test_phrases = [
        "नमस्ते! आप कैसे हैं?",
        "नमस्ते",
        "आप कैसे हैं?",
        "मैं ठीक हूँ",
        "धन्यवाद",
        "शुक्रिया",
        "हाँ-जी",
        "नहीं-जी",
        "बहुत अच्छा"
    ]
    for tp in test_phrases:
        register(tp, tp, f"phrase_{tp}")

    print(f"Total unique Devanagari speech targets: {len(speech_registry)}")

    # Concurrency semaphore
    sem = asyncio.Semaphore(10)
    manifest_entries = {}

    tasks = []
    text_list = list(speech_registry.keys())

    for text in text_list:
        fname = sanitize_filename("fem", text)
        tasks.append((text, fname, synthesize_item(sem, text, fname)))

    print(f"Starting neural speech synthesis for {len(tasks)} items...")
    results = await asyncio.gather(*(t[2] for t in tasks))

    success_count = 0
    for idx, (text, fname, _) in enumerate(tasks):
        url = results[idx]
        if url:
            success_count += 1
            entry = {
                "text": text,
                "url": url,
                "filename": f"{fname}.mp3",
                "voice": "female"
            }
            # Associate entry with all registered keys
            for key in speech_registry[text]:
                manifest_entries[key] = entry

    # Save manifest
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest_entries, f, ensure_ascii=False, indent=2)

    print("=" * 70)
    print(f"✓ Total synthesized/verified Devanagari audio files: {success_count}")
    print(f"✓ Total lookup manifest keys indexed: {len(manifest_entries)}")
    print(f"✓ Manifest saved to: {MANIFEST_FILE}")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(main())
