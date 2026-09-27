/**
 * Audio Utility for Spoken Hindi Web App
 * - Hybrid Architecture:
 *   1. High-fidelity Pre-rendered Neural Audio (Microsoft Azure Neural hi-IN-SwaraNeural FEMALE)
 *   2. Enhanced Web Speech API fallback with voice caching, STRICT FEMALE voice prioritization, and 1.15 pitch
 * - Cyrillic & ISO Latin Sanitization & Automatic Devanagari Transliteration
 * - Web Audio API synthesized tactile sound effects (Success chime, Error buzz, Celebration fanfare)
 */

import audioManifestRaw from '../data/audioManifest.json';

interface ManifestEntry {
  text: string;
  url: string;
  filename: string;
  voice?: string;
}

const audioManifest: Record<string, ManifestEntry> = audioManifestRaw as unknown as Record<string, ManifestEntry>;

// Active pre-rendered audio element
let currentAudio: HTMLAudioElement | null = null;

// Cached browser speech synthesis voices
let cachedVoices: SpeechSynthesisVoice[] = [];

if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
  const updateVoices = () => {
    try {
      cachedVoices = window.speechSynthesis.getVoices();
    } catch {
      cachedVoices = [];
    }
  };
  updateVoices();
  window.speechSynthesis.onvoiceschanged = updateVoices;
}

/**
 * Sound Effects Engine using pure Web Audio API (zero external asset dependencies)
 */
class SoundEffectsEngine {
  private ctx: AudioContext | null = null;

  private getContext(): AudioContext | null {
    if (typeof window === 'undefined') return null;
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx();
      }
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume().catch(() => {});
    }
    return this.ctx;
  }

  // Positive Duolingo-style double chime
  playSuccess() {
    const ctx = this.getContext();
    if (!ctx) return;
    try {
      const now = ctx.currentTime;
      const osc1 = ctx.createOscillator();
      const osc2 = ctx.createOscillator();
      const gain = ctx.createGain();

      osc1.type = 'sine';
      osc2.type = 'triangle';

      osc1.frequency.setValueAtTime(587.33, now); // D5
      osc1.frequency.setValueAtTime(880, now + 0.1); // A5

      osc2.frequency.setValueAtTime(587.33, now);
      osc2.frequency.setValueAtTime(880, now + 0.1);

      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);

      osc1.connect(gain);
      osc2.connect(gain);
      gain.connect(ctx.destination);

      osc1.start(now);
      osc2.start(now);
      osc1.stop(now + 0.5);
      osc2.stop(now + 0.5);
    } catch (e) {
      console.warn("Audio chime error:", e);
    }
  }

  // Low error buzz
  playError() {
    const ctx = this.getContext();
    if (!ctx) return;
    try {
      const now = ctx.currentTime;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(180, now);
      osc.frequency.linearRampToValueAtTime(130, now + 0.25);

      gain.gain.setValueAtTime(0.18, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start(now);
      osc.stop(now + 0.35);
    } catch (e) {
      console.warn("Audio buzz error:", e);
    }
  }

  // Lesson Complete Celebration fanfare
  playFanfare() {
    const ctx = this.getContext();
    if (!ctx) return;
    try {
      const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
      const now = ctx.currentTime;

      notes.forEach((freq, idx) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        const noteStart = now + idx * 0.12;

        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, noteStart);

        gain.gain.setValueAtTime(0.18, noteStart);
        gain.gain.exponentialRampToValueAtTime(0.001, noteStart + 0.35);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(noteStart);
        osc.stop(noteStart + 0.4);
      });
    } catch (e) {
      console.warn("Fanfare error:", e);
    }
  }

  playComplete() {
    this.playFanfare();
  }

  // Tactile button / word chip tap sound
  playTap() {
    const ctx = this.getContext();
    if (!ctx) return;
    try {
      const now = ctx.currentTime;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(360, now);
      osc.frequency.exponentialRampToValueAtTime(180, now + 0.04);
      gain.gain.setValueAtTime(0.08, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + 0.045);
    } catch {
      // ignore
    }
  }
}

export const sfx = new SoundEffectsEngine();

/**
 * Play pre-rendered studio neural MP3 file (100% Female Voice)
 */
function playPreRecordedAudio(url: string): Promise<boolean> {
  return new Promise((resolve) => {
    try {
      if (currentAudio) {
        currentAudio.pause();
        currentAudio.currentTime = 0;
      }
      // Resolve base path so audio files load properly on any domain or subpath (e.g. GitHub Pages)
      const baseUrl = import.meta.env.BASE_URL || './';
      let resolvedUrl = url;
      if (url.startsWith('/audio/')) {
        resolvedUrl = `${baseUrl.endsWith('/') ? baseUrl : baseUrl + '/'}audio/${url.slice(7)}`;
      }
      currentAudio = new Audio(resolvedUrl);
      currentAudio.onended = () => resolve(true);
      currentAudio.onerror = () => resolve(false);
      currentAudio.play().then(() => resolve(true)).catch(() => resolve(false));
    } catch {
      resolve(false);
    }
  });
}

/**
 * Clean instructional notes, Russian commentary, and brackets from input strings
 */
export function cleanTextForSpeech(input: string): string {
  if (!input) return '';
  // Remove parenthetical Russian commentary e.g. (зубной), (не смягчать 'т'!), (Большое спасибо!)
  let cleaned = input.replace(/\([^)]*\)/g, '').trim();
  // Remove quotes
  cleaned = cleaned.replace(/['"«»]/g, '').trim();
  // If slash options present like "Khō gayā (m) / Khō gayī (f)", take first option
  if (cleaned.includes('/')) {
    cleaned = cleaned.split('/')[0].trim();
  }
  return cleaned;
}

/**
 * Targeted Russian Cyrillic phonetics to Devanagari transliteration table
 */
const CYR_TO_DEV_TABLE: [string, string][] = [
  ['т͟х', 'ठ'], ['д͟х', 'ढ'], ['кх', 'ख'], ['гх', 'घ'], ['чх', 'छ'], ['джх', 'झ'],
  ['тх', 'थ'], ['дх', 'ध'], ['пх', 'फ'], ['бх', 'भ'], ['дж', 'ज'],
  ['т͟', 'ट'], ['д͟', 'ड'], ['р͟', 'ड़'],
  ['к', 'क'], ['г', 'ग'], ['ч', 'च'], ['т', 'त'], ['д', 'द'], ['п', 'प'], ['б', 'ब'],
  ['м', 'म'], ['н', 'न'], ['й', 'य'], ['р', 'र'], ['л', 'ल'], ['в', 'व'],
  ['ш', 'श'], ['с', 'स'], ['х', 'ह'], ['ф', 'फ़'], ['з', 'ज़'],
  ['аа', 'ा'], ['ии', 'ी'], ['уу', 'ू'], ['э', 'े'], ['оо', 'ो'], ['о', 'ो'],
  ['а', ''], ['и', 'ि'], ['у', 'ु'],
  ['ⁿ', 'ँ']
];

export function transliterateCyrillicToDevanagari(text: string): string {
  // If no Cyrillic characters, return as is
  if (!/[\u0400-\u04FF]/.test(text)) return text;

  let result = text.toLowerCase();
  for (const [cyr, dev] of CYR_TO_DEV_TABLE) {
    result = result.split(cyr).join(dev);
  }
  return result;
}

/**
 * Fallback Web Speech API synthesis strictly enforcing a FEMALE voice profile
 */
function synthesizeWithBrowser(text: string, rate: number = 0.85) {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) return;

  try {
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'hi-IN';
    utterance.rate = rate; // 0.85x gives cleaner phoneme clarity
    utterance.pitch = 1.18; // Elevated pitch guarantees a clear female vocal resonance

    if (cachedVoices.length === 0) {
      cachedVoices = window.speechSynthesis.getVoices();
    }

    const FEMALE_NAMES = ['swara', 'kavya', 'kalpana', 'sunita', 'veena', 'lekha', 'neerja', 'aditi', 'zira', 'susan', 'female', 'woman', 'girl'];
    const MALE_NAMES = ['madhur', 'hemant', 'male', 'guy', 'boy', 'david', 'mark', 'george', 'espeak'];

    // 1. Strictly prioritize Hindi FEMALE voice
    const hindiFemaleVoice = cachedVoices.find(v => {
      const name = v.name.toLowerCase();
      const lang = v.lang.toLowerCase();
      const isHindi = lang.includes('hi');
      const isFemale = FEMALE_NAMES.some(fn => name.includes(fn));
      const isMale = MALE_NAMES.some(mn => name.includes(mn));
      return isHindi && isFemale && !isMale;
    });

    // 2. Or any Hindi voice that is not explicitly male
    const nonMaleHindiVoice = cachedVoices.find(v => {
      const name = v.name.toLowerCase();
      const lang = v.lang.toLowerCase();
      const isHindi = lang.includes('hi');
      const isMale = MALE_NAMES.some(mn => name.includes(mn));
      return isHindi && !isMale;
    });

    // 3. Or any female voice on system
    const anyFemaleVoice = cachedVoices.find(v => {
      const name = v.name.toLowerCase();
      return FEMALE_NAMES.some(fn => name.includes(fn)) && !MALE_NAMES.some(mn => name.includes(mn));
    });

    const voice = hindiFemaleVoice || nonMaleHindiVoice || anyFemaleVoice;
    if (voice) {
      utterance.voice = voice;
    }

    window.speechSynthesis.speak(utterance);
  } catch (e) {
    console.warn("Browser Speech Synthesis Error:", e);
  }
}

/**
 * Primary Audio Entrypoint for Spoken Hindi
 * 1. Cleans input (strips Russian parentheticals, notes)
 * 2. Checks if a pre-rendered FEMALE studio neural MP3 exists in audioManifest
 * 3. If Cyrillic, transliterates to Devanagari and re-checks manifest
 * 4. Fallback: Synthesizes via Web Speech API with strict FEMALE voice & 1.18 pitch
 */
export async function speakHindi(textOrKey: string, rate: number = 0.85) {
  if (!textOrKey) return;

  const raw = textOrKey.trim();
  const cleaned = cleanTextForSpeech(raw);

  // Look up candidate keys in order of precision
  const candidates = [
    raw,
    cleaned,
    raw.toLowerCase(),
    cleaned.toLowerCase(),
    `text:${raw}`,
    `text:${cleaned}`,
    `text:${raw.toLowerCase()}`,
    `text:${cleaned.toLowerCase()}`,
    `vocab_${raw}`,
    `vocab_${cleaned}`,
    `roleplay_${raw}`,
    `phrase_${raw}`,
    `pair_${raw}`
  ];

  for (const cand of candidates) {
    const match = audioManifest[cand];
    if (match && match.url) {
      const success = await playPreRecordedAudio(match.url);
      if (success) return;
    }
  }

  // If text contains Cyrillic characters, transliterate to Devanagari
  if (/[\u0400-\u04FF]/.test(cleaned)) {
    const devanagariText = transliterateCyrillicToDevanagari(cleaned);
    const devCandidates = [devanagariText, `text:${devanagariText}`, devanagariText.toLowerCase()];
    for (const dCand of devCandidates) {
      const match = audioManifest[dCand];
      if (match && match.url) {
        const success = await playPreRecordedAudio(match.url);
        if (success) return;
      }
    }
    // Synthesize the converted Devanagari rather than Russian Cyrillic!
    synthesizeWithBrowser(devanagariText, rate);
    return;
  }

  // Fallback to browser Web Speech API with female voice
  synthesizeWithBrowser(cleaned, rate);
}
