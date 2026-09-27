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
  drills: PhoneticDrill[];
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
  options?: string[];
  correctAnswer: string | string[];
  wordChips?: string[];
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
  acceptableResponsesIso?: string[];
}

export interface SimulationRoleplay {
  scenarioTitleRu: string;
  scenarioTitleEn?: string;
  setting: string;
  partnerRoleRu: string;
  partnerRoleEn?: string;
  learnerRoleRu: string;
  learnerRoleEn?: string;
  turns: RoleplayTurn[];
}

export interface CulturalPragmatics {
  titleRu: string;
  titleEn?: string;
  pointsRu: string[];
  pointsEn?: string[];
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
    en: string[];
    ru: string[];
  };
  phoneticFocus: PhoneticFocus;
  contrastiveBridge: ContrastiveBridge;
  vocabulary: VocabularyItem[];
  exercises: Exercise[];
  simulationRoleplay: SimulationRoleplay;
  culturalPragmatics: CulturalPragmatics;
}

export interface PhaseManifest {
  phaseNumber: number;
  titleRu: string;
  titleEn: string;
  daysRange: [number, number];
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
  phases: PhaseManifest[];
  totalVocabularyCount?: number;
}
