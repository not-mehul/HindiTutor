/**
 * TypeScript Data Models for 40-Day Spoken Hindi Course for Russian Speakers
 * Supporting dual UI localization (Russian & English Audit Mode)
 */

export type GenderType = "m" | "f" | "both" | "n/a";
export type UiLanguage = "ru" | "en";

export interface PieCognate {
  pieRoot?: string;
  russianCognate?: string;
  hindiRoot?: string;
  notes?: string;
  notesEn?: string;
}

export interface VocabularyItem {
  id: string;
  devanagari: string;
  transliterationIso: string;
  phoneticCyrillic: string;
  translationRu: string;
  translationEn: string;
  partOfSpeech: "noun" | "pronoun" | "verb" | "adjective" | "postposition" | "interjection" | "adverb" | "particle";
  gender?: GenderType;
  audioHint?: string;
  pieCognate?: PieCognate;
}

export interface PhoneticDrill {
  prompt: string;
  contrastPair: string;
  instructionsRu: string;
  instructionsEn?: string;
}

export interface PhoneticFocus {
  targetSound: string;
  targetSoundEn?: string;
  articulatoryMechanism: string;
  articulatoryMechanismEn?: string;
  russianInterferenceWarning: string;
  russianInterferenceWarningEn?: string;
  drills: readonly PhoneticDrill[] | PhoneticDrill[];
}

export interface ContrastiveBridge {
  grammarConcept: string;
  grammarConceptEn?: string;
  russianParallel: string;
  russianParallelEn?: string;
  syntacticFormula: string;
  explanationRu: string;
  explanationEn?: string;
  pieCognateConnection?: {
    root: string;
    russian: string;
    hindi: string;
    meaning: string;
    meaningEn?: string;
  };
}

export type ExerciseType =
  | "phonetic_discrimination"
  | "word_reorder_sov"
  | "fill_in_blank"
  | "substitution_drill"
  | "listen_and_repeat"
  | "rapid_oral_challenge"
  | "dialogue_roleplay";

export interface Exercise {
  id: string;
  type: ExerciseType;
  instructionRu: string;
  instructionEn?: string;
  prompt: string;
  options?: readonly string[] | string[];
  correctAnswer: string | string[];
  wordChips?: readonly string[] | string[];
  phoneticCyrillicTarget?: string;
  transliterationIsoTarget?: string;
  audioKey?: string;
  explanationRu?: string;
  explanationEn?: string;
}

export interface RoleplayTurn {
  speaker: string;
  speechRu: string;
  speechEn?: string;
  speechIso: string;
  speechCyrillic: string;
  speechDevanagari?: string;
  learnerHintRu?: string;
  learnerHintEn?: string;
  acceptableResponsesIso?: readonly string[] | string[];
}

export interface SimulationRoleplay {
  scenarioTitleRu: string;
  scenarioTitleEn?: string;
  setting: string;
  partnerRoleRu: string;
  partnerRoleEn?: string;
  learnerRoleRu: string;
  learnerRoleEn?: string;
  turns: readonly RoleplayTurn[] | RoleplayTurn[];
}

export interface CulturalPragmatics {
  titleRu: string;
  titleEn?: string;
  pointsRu: readonly string[] | string[];
  pointsEn?: readonly string[] | string[];
}

export interface CognitiveTimeAllocation {
  phase1WarmupMinutes: string;
  phase2StructuralCoreMinutes: string;
  phase3ShadowingDrillsMinutes: string;
  phase4SimulationMinutes: string;
}

export interface DayLesson {
  day: number;
  phase: number;
  title: {
    en: string;
    ru: string;
  };
  theme: string;
  themeEn?: string;
  estimatedMinutes: number;
  cognitiveTimeAllocation?: CognitiveTimeAllocation;
  learningObjectives: {
    en: readonly string[] | string[];
    ru: readonly string[] | string[];
  };
  phoneticFocus: PhoneticFocus;
  contrastiveBridge: ContrastiveBridge;
  vocabulary: readonly VocabularyItem[] | VocabularyItem[];
  exercises: readonly Exercise[] | Exercise[];
  simulationRoleplay: SimulationRoleplay;
  culturalPragmatics: CulturalPragmatics;
}

export interface PhaseManifest {
  phaseNumber: number;
  titleRu: string;
  titleEn: string;
  daysRange: readonly [number, number] | [number, number];
  theme: string;
  themeEn?: string;
  summaryRu: string;
  summaryEn?: string;
}

export interface CourseManifest {
  courseId: string;
  version: string;
  titleRu: string;
  titleEn: string;
  author: string;
  sourceLanguage: "ru";
  targetLanguage: "hi";
  totalDays: 40;
  totalPhases: 5;
  dailyProtocol: {
    phase1: string;
    phase2: string;
    phase3: string;
    phase4: string;
  };
  phases: readonly PhaseManifest[] | PhaseManifest[];
  totalVocabularyCount?: number;
}

export interface PhonemeCategory {
  categoryRu: string;
  categoryEn?: string;
  devanagari: readonly string[];
  iso: readonly string[];
  cyrillicPhonetic: readonly string[];
  articulatoryMechanism: string;
  articulatoryMechanismEn?: string;
  russianContrastRu?: string;
  russianContrastEn?: string;
  russianInterferenceWarning?: string;
  russianInterferenceWarningEn?: string;
  tactileDrill?: string;
  tactileDrillEn?: string;
  minimalPairs?: readonly { pair: string; meaningRu: string; meaningEn?: string }[];
}

export interface PhoneticsGuide {
  titleRu: string;
  titleEn: string;
  corePrinciples: readonly {
    nameRu: string;
    nameEn?: string;
    descriptionRu: string;
    descriptionEn?: string;
  }[];
  phonemeCategories: readonly PhonemeCategory[];
}

export interface CognateItem {
  pieRoot: string;
  russianWord: string;
  hindiWordIso: string;
  hindiPhoneticCyrillic: string;
  hindiDevanagari?: string;
  semanticFieldRu?: string;
  semanticFieldEn?: string;
  notesRu?: string;
  notesEn?: string;
}

export interface CognatesIndex {
  titleRu: string;
  titleEn: string;
  descriptionRu: string;
  cognates: readonly CognateItem[];
}
