import React, { useState, useEffect } from 'react';
import {
  X,
  Volume2,
  CheckCircle2,
  XCircle,
  ArrowRight,
  Sparkles,
  AlertCircle,
  Clock,
  Trophy,
  Heart,
  RotateCcw,
  Send,
  Mic,
  MicOff
} from 'lucide-react';
import confetti from 'canvas-confetti';
import { useApp } from '../context/AppContext';
import { sfx, speakHindi } from '../utils/audio';
import type { Exercise } from '../data/types';

export const LessonRunner: React.FC = () => {
  const {
    selectedDay,
    closeLesson,
    markDayCompleted,
    hearts,
    decrementHearts,
    resetHearts,
    uiLanguage,
    soundEnabled,
  } = useApp();

  if (!selectedDay) return null;

  // Stages: 'warmup' -> 'theory' -> 'exercise' (indices 0..3) -> 'roleplay' -> 'completed'
  type StageType = 'warmup' | 'theory' | 'exercise' | 'roleplay' | 'completed';
  const [stage, setStage] = useState<StageType>('warmup');
  const [exerciseIndex, setExerciseIndex] = useState<number>(0);

  // Exercise interaction state
  const currentExercise: Exercise | undefined = selectedDay.exercises[exerciseIndex];
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [selectedChips, setSelectedChips] = useState<string[]>([]);
  const [remainingChips, setRemainingChips] = useState<string[]>([]);
  const [feedback, setFeedback] = useState<'idle' | 'correct' | 'incorrect'>('idle');

  // Rapid Oral Countdown
  const [rapidTimer, setRapidTimer] = useState<number>(3);
  const [rapidActive, setRapidActive] = useState<boolean>(false);

  // Speech Recognition & Oral Repetition State
  const [isListening, setIsListening] = useState<boolean>(false);
  const [speechTranscript, setSpeechTranscript] = useState<string>('');
  const [speechError, setSpeechError] = useState<string | null>(null);
  const [speechSupported, setSpeechSupported] = useState<boolean>(true);

  // Interactive Turn-by-Turn Roleplay State
  const roleplayTurns = selectedDay.simulationRoleplay.turns;
  const [roleplayStep, setRoleplayStep] = useState<number>(0);
  const [learnerChosenResponse, setLearnerChosenResponse] = useState<string | null>(null);

  // Out of hearts modal
  const [showHeartRefillModal, setShowHeartRefillModal] = useState<boolean>(false);

  // Initialize chips for word_reorder
  useEffect(() => {
    if (currentExercise && currentExercise.type === 'word_reorder_sov') {
      const chips = [...(currentExercise.wordChips || [])];
      chips.sort(() => Math.random() - 0.5);
      setRemainingChips(chips);
      setSelectedChips([]);
    } else {
      setSelectedChips([]);
      setRemainingChips([]);
    }
    setSelectedOption(null);
    setFeedback('idle');

    if (currentExercise && currentExercise.type === 'rapid_oral_challenge') {
      setRapidTimer(3);
      setRapidActive(true);
    } else {
      setRapidActive(false);
    }
  }, [currentExercise, stage]);

  // Detect speech recognition support
  useEffect(() => {
    if (typeof window !== 'undefined') {
      const hasSpeech = !!((window as any).SpeechRecognition || (window as any).webkitSpeechRecognition);
      setSpeechSupported(hasSpeech);
    }
  }, []);

  // Reset speech state when exercise changes
  useEffect(() => {
    setIsListening(false);
    setSpeechTranscript('');
    setSpeechError(null);
  }, [exerciseIndex, stage]);

  // Countdown timer for rapid oral challenge
  useEffect(() => {
    let interval: ReturnType<typeof setInterval>;
    if (rapidActive && rapidTimer > 0 && feedback === 'idle') {
      interval = setInterval(() => {
        setRapidTimer((prev) => prev - 1);
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [rapidActive, rapidTimer, feedback]);

  // Check heart depletion
  useEffect(() => {
    if (hearts <= 0) {
      setShowHeartRefillModal(true);
    }
  }, [hearts]);

  // Auto-speak partner dialogue when roleplay step advances
  useEffect(() => {
    if (stage === 'roleplay' && roleplayTurns[roleplayStep]) {
      const turn = roleplayTurns[roleplayStep];
      const isPartner = !turn.speaker.toLowerCase().includes('вы') && !turn.speaker.toLowerCase().includes('learner');
      if (isPartner) {
        speakHindi(turn.speechIso || turn.speechCyrillic);
      }
      setLearnerChosenResponse(null);
    }
  }, [stage, roleplayStep, roleplayTurns]);

  // Total progression steps
  const totalSteps = 2 + selectedDay.exercises.length + 1; // warmup + theory + exercises + roleplay
  let currentStepNum = 1;
  if (stage === 'warmup') currentStepNum = 1;
  else if (stage === 'theory') currentStepNum = 2;
  else if (stage === 'exercise') currentStepNum = 3 + exerciseIndex;
  else if (stage === 'roleplay') currentStepNum = totalSteps;
  else if (stage === 'completed') currentStepNum = totalSteps;

  const progressPercent = Math.round((currentStepNum / totalSteps) * 100);

  // Chip selection handlers
  const handleSelectChip = (chip: string, idx: number) => {
    if (soundEnabled) sfx.playTap();
    speakHindi(chip);
    setSelectedChips((prev) => [...prev, chip]);
    setRemainingChips((prev) => prev.filter((_, i) => i !== idx));
  };

  const handleDeselectChip = (chip: string, idx: number) => {
    if (soundEnabled) sfx.playTap();
    setRemainingChips((prev) => [...prev, chip]);
    setSelectedChips((prev) => prev.filter((_, i) => i !== idx));
  };

  // Microphone Speech Recognition Handler
  const handleToggleMic = () => {
    const SpeechRecognitionClass =
      (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;

    if (!SpeechRecognitionClass) {
      setSpeechSupported(false);
      return;
    }

    if (isListening) {
      setIsListening(false);
      return;
    }

    try {
      const recognition = new SpeechRecognitionClass();
      recognition.lang = 'hi-IN';
      recognition.interimResults = false;
      recognition.maxAlternatives = 3;

      recognition.onstart = () => {
        setIsListening(true);
        setSpeechError(null);
      };

      recognition.onresult = (event: any) => {
        const transcript = event.results[0]?.[0]?.transcript || '';
        setSpeechTranscript(transcript);
        setIsListening(false);
        if (soundEnabled) sfx.playSuccess();
        setFeedback('correct');
      };

      recognition.onerror = (event: any) => {
        setIsListening(false);
        if (event.error === 'not-allowed') {
          setSpeechError(
            uiLanguage === 'ru'
              ? 'Доступ к микрофону заблокирован в настройках браузера'
              : 'Microphone access denied in browser settings'
          );
        } else if (event.error === 'no-speech') {
          setSpeechError(
            uiLanguage === 'ru'
              ? 'Звук не распознан. Попробуйте еще раз или подтвердите кнопкой ниже'
              : 'No speech heard. Try again or tap confirm below'
          );
        } else {
          setSpeechError(event.error);
        }
      };

      recognition.onend = () => {
        setIsListening(false);
      };

      recognition.start();
    } catch (err: any) {
      setIsListening(false);
      setSpeechError(err?.message || 'Error initializing microphone');
    }
  };

  // Oral Repetition Manual Confirmation Handler
  const handleOralRepetitionConfirmed = () => {
    if (soundEnabled) sfx.playSuccess();
    setFeedback('correct');
  };

  // Check Answer Handler
  const handleCheckAnswer = () => {
    if (!currentExercise || feedback !== 'idle') return;

    let isCorrect = false;

    if (currentExercise.type === 'word_reorder_sov') {
      const targetAns = currentExercise.correctAnswer;
      if (Array.isArray(targetAns)) {
        isCorrect = selectedChips.join(' ') === targetAns.join(' ');
      } else {
        isCorrect = selectedChips.join(' ') === targetAns;
      }
    } else if (currentExercise.type === 'listen_and_repeat') {
      isCorrect = true;
    } else {
      isCorrect = selectedOption === currentExercise.correctAnswer;
    }

    if (isCorrect) {
      setFeedback('correct');
      if (soundEnabled) sfx.playSuccess();
    } else {
      setFeedback('incorrect');
      if (soundEnabled) sfx.playError();
      decrementHearts();
    }
  };

  // Move to next step
  const handleNextStep = () => {
    if (stage === 'warmup') {
      setStage('theory');
    } else if (stage === 'theory') {
      setStage('exercise');
      setExerciseIndex(0);
    } else if (stage === 'exercise') {
      if (exerciseIndex + 1 < selectedDay.exercises.length) {
        setExerciseIndex((prev) => prev + 1);
        setFeedback('idle');
      } else {
        setStage('roleplay');
        setRoleplayStep(0);
        setFeedback('idle');
      }
    } else if (stage === 'roleplay') {
      // Advance roleplay step or complete lesson
      if (roleplayStep + 1 < roleplayTurns.length) {
        setRoleplayStep((prev) => prev + 1);
      } else {
        markDayCompleted(selectedDay.day);
        setStage('completed');
        if (soundEnabled) sfx.playFanfare();
        confetti({
          particleCount: 100,
          spread: 80,
          origin: { y: 0.6 },
        });
      }
    }
  };

  // Learner chooses a response in roleplay
  const handleRoleplayResponse = (response: string) => {
    if (soundEnabled) sfx.playTap();
    setLearnerChosenResponse(response);
    speakHindi(response);
    setTimeout(() => {
      if (roleplayStep + 1 < roleplayTurns.length) {
        setRoleplayStep((prev) => prev + 1);
      } else {
        markDayCompleted(selectedDay.day);
        setStage('completed');
        if (soundEnabled) sfx.playFanfare();
        confetti({
          particleCount: 100,
          spread: 80,
          origin: { y: 0.6 },
        });
      }
    }, 1200);
  };

  // Keyboard navigation shortcuts
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Ignore if user typing in an input
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;

      if (e.key === 'Enter') {
        if (stage === 'exercise' && feedback === 'idle') {
          handleCheckAnswer();
        } else if (stage !== 'completed') {
          handleNextStep();
        }
      } else if (stage === 'exercise' && feedback === 'idle') {
        if (currentExercise && currentExercise.type !== 'word_reorder_sov' && currentExercise.options) {
          const num = parseInt(e.key, 10);
          if (num >= 1 && num <= currentExercise.options.length) {
            setSelectedOption(currentExercise.options[num - 1]);
            if (soundEnabled) sfx.playTap();
          }
        } else if (e.key === 'Backspace' && selectedChips.length > 0) {
          const lastIdx = selectedChips.length - 1;
          handleDeselectChip(selectedChips[lastIdx], lastIdx);
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [stage, feedback, selectedOption, selectedChips, currentExercise, roleplayStep]);

  // Helper to extract clean Hindi speech from exercise
  const getExerciseSpeechText = (ex: Exercise): string => {
    if (ex.transliterationIsoTarget) return ex.transliterationIsoTarget;
    if (ex.phoneticCyrillicTarget) return ex.phoneticCyrillicTarget;
    if (typeof ex.correctAnswer === 'string' && !/[\u0400-\u04FF]/.test(ex.correctAnswer)) {
      return ex.correctAnswer;
    }
    if (Array.isArray(ex.correctAnswer)) {
      return ex.correctAnswer.join(' ');
    }
    const quoted = ex.prompt.match(/['"«]([a-zA-Zāīūēōṛñṃṭḍṭhḍhṇśṣ\s]+)['"»]/);
    if (quoted && quoted[1]) return quoted[1];
    if (!/[\u0400-\u04FF]/.test(ex.prompt)) return ex.prompt;
    return '';
  };

  return (
    <div className="fixed inset-0 z-50 bg-white flex flex-col justify-between overflow-y-auto">
      {/* Top Header Bar */}
      <div className="max-w-2xl w-full mx-auto px-4 py-4 flex items-center justify-between gap-4 border-b border-slate-100">
        <button
          onClick={closeLesson}
          className="p-2 rounded-xl text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition-all cursor-pointer"
          title="Exit lesson"
        >
          <X className="w-6 h-6" />
        </button>

        {/* Progress bar */}
        <div className="flex-1 h-3.5 bg-slate-100 rounded-full overflow-hidden border border-slate-200">
          <div
            className="h-full bg-emerald-500 rounded-full transition-all duration-300 shadow-xs"
            style={{ width: `${progressPercent}%` }}
          />
        </div>

        {/* Hearts count */}
        <div className="flex items-center gap-1 font-extrabold text-rose-500 text-sm">
          <Heart className="w-5 h-5 fill-rose-500" />
          <span>{hearts}</span>
        </div>
      </div>

      {/* Main Content Area */}
      <main className="max-w-xl w-full mx-auto px-4 py-6 flex-1 flex flex-col justify-center">
        {/* STAGE 1: PHONETICS WARMUP (00:00 - 04:00) */}
        {stage === 'warmup' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-300">
            <div className="flex items-center gap-2 text-xs font-bold text-emerald-700 bg-emerald-50 px-3 py-1.5 rounded-full w-fit mb-3 border border-emerald-200">
              <Clock className="w-3.5 h-3.5" />
              <span>{uiLanguage === 'ru' ? 'Фаза 1 (00:00–04:00): Фонетическая калибровка' : 'Phase 1 (00:00–04:00): Phonetic Warmup'}</span>
            </div>

            <h2 className="text-2xl font-black text-slate-900 leading-tight">
              {selectedDay.phoneticFocus.targetSound}
            </h2>

            <div className="mt-4 bg-emerald-50/70 border border-emerald-200 rounded-2xl p-4">
              <h4 className="font-extrabold text-xs text-emerald-900 uppercase tracking-wider mb-1">
                {uiLanguage === 'ru' ? '👅 Артикуляционная механика:' : '👅 Articulatory Mechanism:'}
              </h4>
              <p className="text-sm text-emerald-950 leading-relaxed font-medium">
                {selectedDay.phoneticFocus.articulatoryMechanism}
              </p>
            </div>

            <div className="mt-3 bg-amber-50 border border-amber-200 rounded-2xl p-4">
              <h4 className="font-extrabold text-xs text-amber-900 uppercase tracking-wider mb-1 flex items-center gap-1.5">
                <AlertCircle className="w-4 h-4 text-amber-600" />
                {uiLanguage === 'ru' ? 'Предостережение от русской интерференции:' : 'Russian Interference Warning:'}
              </h4>
              <p className="text-xs text-amber-950 leading-relaxed">
                {selectedDay.phoneticFocus.russianInterferenceWarning}
              </p>
            </div>

            {/* Drills Box with clean, separate buttons */}
            <div className="mt-4 space-y-2.5">
              <span className="text-xs font-black text-slate-700 uppercase tracking-wider">
                {uiLanguage === 'ru' ? 'Практические звуковые пары:' : 'Auditory Practice Pairs:'}
              </span>
              {selectedDay.phoneticFocus.drills.map((drill, idx) => {
                const parts = drill.contrastPair.split('vs');
                const p1 = parts[0].replace(/\([^)]*\)/g, '').trim();
                const p2 = parts[1] ? parts[1].replace(/\([^)]*\)/g, '').trim() : '';

                return (
                  <div key={idx} className="bg-white border border-slate-200 rounded-2xl p-3 flex items-center justify-between gap-3 shadow-xs">
                    <div>
                      <div className="text-sm font-extrabold text-slate-900">
                        {drill.contrastPair}
                      </div>
                      <div className="text-xs text-slate-500 mt-0.5">
                        {drill.instructionsRu}
                      </div>
                    </div>
                    <div className="flex items-center gap-1.5 shrink-0">
                      <button
                        onClick={() => speakHindi(p1)}
                        className="px-2.5 py-1.5 rounded-xl bg-emerald-100 text-emerald-800 hover:bg-emerald-200 active:scale-95 transition-all text-xs font-bold flex items-center gap-1 cursor-pointer"
                        title={`Normal speed: ${p1}`}
                      >
                        <Volume2 className="w-4 h-4" />
                        <span>{p1}</span>
                      </button>
                      <button
                        onClick={() => speakHindi(p1, 0.65)}
                        className="p-1.5 rounded-xl bg-slate-100 text-slate-600 hover:bg-slate-200 active:scale-95 transition-all text-[11px] font-bold cursor-pointer"
                        title={`Slow speed (0.65x): ${p1}`}
                      >
                        🐢
                      </button>
                      {p2 && (
                        <>
                          <button
                            onClick={() => speakHindi(p2)}
                            className="px-2.5 py-1.5 rounded-xl bg-amber-100 text-amber-900 hover:bg-amber-200 active:scale-95 transition-all text-xs font-bold flex items-center gap-1 cursor-pointer"
                            title={`Normal speed: ${p2}`}
                          >
                            <Volume2 className="w-4 h-4" />
                            <span>{p2}</span>
                          </button>
                          <button
                            onClick={() => speakHindi(p2, 0.65)}
                            className="p-1.5 rounded-xl bg-slate-100 text-slate-600 hover:bg-slate-200 active:scale-95 transition-all text-[11px] font-bold cursor-pointer"
                            title={`Slow speed (0.65x): ${p2}`}
                          >
                            🐢
                          </button>
                        </>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* STAGE 2: STRUCTURAL CORE THEORY (04:00 - 11:00) */}
        {stage === 'theory' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-300 space-y-6">
            <div className="flex items-center gap-2 text-xs font-bold text-blue-700 bg-blue-50 px-3 py-1.5 rounded-full w-fit border border-blue-200">
              <Clock className="w-3.5 h-3.5" />
              <span>{uiLanguage === 'ru' ? 'Фаза 2 (04:00–11:00): Сопоставительный якорь' : 'Phase 2 (04:00–11:00): Contrastive Bridge'}</span>
            </div>

            <div>
              <h2 className="text-2xl font-black text-slate-900 mb-2">
                {selectedDay.contrastiveBridge.grammarConcept}
              </h2>
              <div className="bg-blue-50 border border-blue-200 rounded-2xl p-4 my-4">
                <span className="text-xs font-black text-blue-700 uppercase tracking-wider block mb-1">
                  {uiLanguage === 'ru' ? 'Русская грамматическая параллель:' : 'Russian Grammatical Parallel:'}
                </span>
                <p className="text-sm font-extrabold text-blue-950">
                  {selectedDay.contrastiveBridge.russianParallel}
                </p>
              </div>
              <p className="text-sm text-slate-700 leading-relaxed mt-4">
                {uiLanguage === 'ru'
                  ? selectedDay.contrastiveBridge.explanationRu
                  : (selectedDay.contrastiveBridge.explanationEn || selectedDay.contrastiveBridge.explanationRu)}
              </p>
            </div>

            {/* Syntactic Formula Box */}
            <div className="bg-slate-900 text-white rounded-2xl p-4 font-mono text-center text-sm md:text-base font-bold tracking-wide shadow-inner">
              <span className="text-xs text-slate-400 block font-sans uppercase mb-1">
                {uiLanguage === 'ru' ? 'Синтаксическая формула:' : 'Syntactic Formula:'}
              </span>
              {selectedDay.contrastiveBridge.syntacticFormula}
            </div>

            {/* PIE Cognate anchor if present */}
            {selectedDay.contrastiveBridge.pieCognateConnection && (
              <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-4 flex items-center gap-3">
                <Sparkles className="w-6 h-6 text-emerald-600 shrink-0" />
                <div className="text-xs text-emerald-950">
                  <span className="font-bold">Праиндоевропейский корень: </span>
                  <span className="font-mono font-bold text-emerald-800">{selectedDay.contrastiveBridge.pieCognateConnection.root}</span>
                  {' '}— русское <i>{selectedDay.contrastiveBridge.pieCognateConnection.russian}</i> и хинди <b>{selectedDay.contrastiveBridge.pieCognateConnection.hindi}</b> ({selectedDay.contrastiveBridge.pieCognateConnection.meaning}).
                </div>
              </div>
            )}
          </div>
        )}

        {/* STAGE 3: INTERACTIVE DRILLS (11:00 - 17:00) */}
        {stage === 'exercise' && currentExercise && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-300">
            {/* Exercise Header */}
            <div className="flex items-center justify-between pb-3 border-b border-slate-100">
              <span className="text-xs font-extrabold bg-amber-100 text-amber-800 px-3 py-1 rounded-full uppercase tracking-wider">
                {uiLanguage === 'ru' ? 'Упражнение' : 'Exercise'} {exerciseIndex + 1} / {selectedDay.exercises.length}
              </span>
              <span className="text-xs text-slate-400 font-medium">
                {uiLanguage === 'ru' ? 'Фаза 3 (11:00–17:00)' : 'Phase 3 (11:00–17:00)'}
              </span>
            </div>

            {/* Instruction */}
            <h3 className="text-lg font-black text-slate-900 mt-4">
              {uiLanguage === 'ru'
                ? currentExercise.instructionRu
                : (currentExercise.instructionEn || currentExercise.instructionRu)}
            </h3>

            {/* Prompt Box with dual audio buttons */}
            <div className="mt-4 bg-slate-50 border-2 border-slate-200 rounded-3xl p-5 text-center flex items-center justify-center gap-3">
              <p className="text-lg font-black text-slate-900">
                {currentExercise.prompt}
              </p>
              {(() => {
                const targetSpeech = getExerciseSpeechText(currentExercise);
                if (targetSpeech) {
                  return (
                    <div className="flex items-center gap-1.5 shrink-0">
                      <button
                        onClick={() => speakHindi(targetSpeech)}
                        className="p-2 rounded-xl bg-white border border-slate-200 text-emerald-600 hover:bg-emerald-50 active:scale-95 transition-all shadow-xs cursor-pointer"
                        title="Normal speed"
                      >
                        <Volume2 className="w-5 h-5" />
                      </button>
                      <button
                        onClick={() => speakHindi(targetSpeech, 0.65)}
                        className="p-2 rounded-xl bg-white border border-slate-200 text-slate-600 hover:bg-slate-100 active:scale-95 transition-all shadow-xs text-xs cursor-pointer"
                        title="Slow speed (0.65x)"
                      >
                        🐢
                      </button>
                    </div>
                  );
                }
                return null;
              })()}
            </div>

            {/* TYPE 1: WORD REORDER SOV (Tactile Chips with Audio) */}
            {currentExercise.type === 'word_reorder_sov' && (
              <div className="mt-6 space-y-4">
                {/* Target Selected Slot Line */}
                <div className="min-h-[64px] border-b-2 border-slate-300 p-2 flex flex-wrap items-center gap-2">
                  {selectedChips.length === 0 ? (
                    <span className="text-xs text-slate-400 italic">
                      {uiLanguage === 'ru' ? 'Нажимайте слова в строгом порядке SOV...' : 'Tap words in strict Hindi SOV order...'}
                    </span>
                  ) : (
                    selectedChips.map((chip, idx) => (
                      <button
                        key={idx}
                        onClick={() => handleDeselectChip(chip, idx)}
                        className="btn-duo-green px-4 py-2.5 rounded-2xl text-white font-extrabold text-sm shadow-md cursor-pointer animate-in zoom-in-95 duration-150"
                      >
                        {chip}
                      </button>
                    ))
                  )}
                </div>

                {/* Remaining Chips to Select */}
                <div className="flex flex-wrap justify-center gap-2.5 pt-4">
                  {remainingChips.map((chip, idx) => (
                    <button
                      key={idx}
                      onClick={() => handleSelectChip(chip, idx)}
                      className="btn-duo-slate px-4 py-2.5 rounded-2xl text-slate-800 font-extrabold text-sm border border-slate-200 shadow-md cursor-pointer"
                    >
                      {chip}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* TYPE 2: MULTIPLE CHOICE OPTIONS (Keyboard 1..4 enabled) */}
            {currentExercise.type !== 'word_reorder_sov' && currentExercise.options && (
              <div className="mt-6 space-y-3">
                {currentExercise.options.map((option, idx) => {
                  const isSelected = selectedOption === option;
                  return (
                    <button
                      key={idx}
                      onClick={() => {
                        setSelectedOption(option);
                        if (soundEnabled) sfx.playTap();
                        speakHindi(option);
                      }}
                      className={`w-full p-4 rounded-2xl border-2 text-left font-bold text-sm flex items-center justify-between transition-all cursor-pointer ${
                        isSelected
                          ? 'border-emerald-500 bg-emerald-50 text-emerald-900 shadow-md'
                          : 'border-slate-200 bg-white hover:border-slate-300 text-slate-800'
                      }`}
                    >
                      <div className="flex items-center gap-3">
                        <span className="w-6 h-6 rounded-lg bg-slate-100 text-slate-500 text-xs font-black flex items-center justify-center">
                          {idx + 1}
                        </span>
                        <span>{option}</span>
                      </div>
                      <Volume2 className="w-4 h-4 text-slate-400 hover:text-emerald-600 transition-colors" />
                    </button>
                  );
                })}
              </div>
            )}

            {/* TYPE 3: LISTEN AND REPEAT / ORAL SHADOWING (Microphone + Dual Audio + Self-Verification) */}
            {currentExercise.type === 'listen_and_repeat' && (
              <div className="mt-6 space-y-4">
                {/* Target Hindi Pronunciation Display Card */}
                <div className="bg-gradient-to-br from-emerald-50 to-teal-50/50 border-2 border-emerald-200 rounded-3xl p-6 text-center shadow-xs">
                  <span className="text-[11px] font-black uppercase tracking-wider text-emerald-700 bg-white/80 px-3 py-1 rounded-full border border-emerald-200 inline-block mb-3">
                    {uiLanguage === 'ru' ? '🎯 Целевое произношение (Шейдоуинг)' : '🎯 Target Oral Pronunciation'}
                  </span>

                  <div className="text-2xl sm:text-3xl font-black text-slate-900 tracking-wide">
                    {currentExercise.transliterationIsoTarget || currentExercise.correctAnswer}
                  </div>

                  {currentExercise.phoneticCyrillicTarget && (
                    <div className="text-sm font-semibold text-emerald-800 mt-2 font-mono">
                      [{currentExercise.phoneticCyrillicTarget}]
                    </div>
                  )}

                  {/* Dual Audio Playback inside the Card */}
                  <div className="flex items-center justify-center gap-3 mt-4 pt-3 border-t border-emerald-200/60">
                    <button
                      onClick={() => speakHindi(currentExercise.transliterationIsoTarget || (currentExercise.correctAnswer as string))}
                      className="px-4 py-2.5 rounded-2xl bg-emerald-600 text-white hover:bg-emerald-700 active:scale-95 font-bold text-xs flex items-center gap-2 shadow-xs transition-all cursor-pointer"
                    >
                      <Volume2 className="w-4 h-4" />
                      <span>{uiLanguage === 'ru' ? 'Слушать (1.0x)' : 'Listen (1.0x)'}</span>
                    </button>
                    <button
                      onClick={() => speakHindi(currentExercise.transliterationIsoTarget || (currentExercise.correctAnswer as string), 0.65)}
                      className="px-3.5 py-2.5 rounded-2xl bg-white border border-emerald-200 text-slate-700 hover:bg-emerald-50 active:scale-95 font-bold text-xs flex items-center gap-1.5 shadow-xs transition-all cursor-pointer"
                    >
                      <span>🐢</span>
                      <span>{uiLanguage === 'ru' ? 'Медленно (0.65x)' : 'Slow (0.65x)'}</span>
                    </button>
                  </div>
                </div>

                {/* Interactive Microphone & Oral Repetition Box */}
                <div className="bg-white border-2 border-slate-200 rounded-3xl p-5 shadow-xs text-center space-y-3">
                  <div className="text-xs font-bold text-slate-600">
                    {uiLanguage === 'ru'
                      ? 'Произнесите фразу вслух в микрофон или выполните устное повторение:'
                      : 'Speak the phrase out loud into the microphone or practice oral repetition:'}
                  </div>

                  {/* Microphone Button */}
                  <div className="flex justify-center">
                    <button
                      onClick={handleToggleMic}
                      className={`relative px-6 py-3.5 rounded-2xl font-extrabold text-sm flex items-center gap-2.5 transition-all cursor-pointer shadow-md ${
                        isListening
                          ? 'bg-rose-500 text-white animate-pulse ring-4 ring-rose-200'
                          : 'bg-slate-900 text-white hover:bg-slate-800 active:scale-95'
                      }`}
                    >
                      {isListening ? (
                        <>
                          <MicOff className="w-5 h-5 animate-pulse" />
                          <span>{uiLanguage === 'ru' ? 'Слушаю... Говорите!' : 'Listening... Speak now!'}</span>
                        </>
                      ) : (
                        <>
                          <Mic className="w-5 h-5 text-emerald-400" />
                          <span>{uiLanguage === 'ru' ? '🎙️ Произнести в микрофон' : '🎙️ Speak with Microphone'}</span>
                        </>
                      )}
                    </button>
                  </div>

                  {/* Feedback on recognized speech */}
                  {speechTranscript && (
                    <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-3 text-xs font-bold text-emerald-800 animate-in fade-in">
                      <span>{uiLanguage === 'ru' ? 'Распознано: ' : 'Recognized: '}</span>
                      <span className="font-extrabold">"{speechTranscript}"</span>
                      <span className="ml-1 text-emerald-600 font-black">✓</span>
                    </div>
                  )}

                  {/* Speech recognition error / fallback note */}
                  {speechError && (
                    <div className="bg-amber-50 border border-amber-200 rounded-2xl p-2.5 text-xs text-amber-800 animate-in fade-in">
                      <span>{speechError}</span>
                    </div>
                  )}

                  {!speechSupported && (
                    <div className="text-[11px] text-slate-400 italic">
                      {uiLanguage === 'ru'
                        ? 'Браузерная проверка речи недоступна в этом браузере. Используйте подтверждение ниже:'
                        : 'Web speech recognition unavailable in this browser. Use confirmation below:'}
                    </div>
                  )}

                  {/* Manual Confirmation Alternative Button */}
                  <div className="pt-2 border-t border-slate-100 flex justify-center">
                    <button
                      onClick={handleOralRepetitionConfirmed}
                      className="px-5 py-2.5 rounded-2xl bg-emerald-50 border border-emerald-300 text-emerald-800 hover:bg-emerald-100 active:scale-95 font-extrabold text-xs flex items-center gap-2 cursor-pointer transition-all shadow-xs"
                    >
                      <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                      <span>{uiLanguage === 'ru' ? '✅ Я повторил(а) вслух' : '✅ I repeated out loud'}</span>
                    </button>
                  </div>
                </div>
              </div>
            )}
          </div>
        )}

        {/* STAGE 4: INTERACTIVE TURN-BY-TURN ROLEPLAY SIMULATOR (17:00 - 20:00) */}
        {stage === 'roleplay' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-300 space-y-4">
            {/* Header */}
            <div className="flex items-center justify-between pb-3 border-b border-slate-100">
              <span className="text-xs font-extrabold bg-purple-100 text-purple-800 px-3 py-1 rounded-full uppercase tracking-wider">
                {uiLanguage === 'ru' ? 'Фаза 4: Ситуативная ролевая игра' : 'Phase 4: Roleplay Simulator'}
              </span>
              <span className="text-xs text-slate-400 font-medium">
                {uiLanguage === 'ru' ? 'Реплика' : 'Turn'} {roleplayStep + 1} / {roleplayTurns.length}
              </span>
            </div>

            <div>
              <h2 className="text-xl font-black text-slate-900">
                {selectedDay.simulationRoleplay.scenarioTitleRu}
              </h2>
              <p className="text-xs text-slate-500 mt-0.5">
                {selectedDay.simulationRoleplay.setting}
              </p>
            </div>

            {/* Chat Thread revealing up to roleplayStep */}
            <div className="space-y-3 max-h-[380px] overflow-y-auto p-2 border border-slate-200 rounded-3xl bg-slate-50/50">
              {roleplayTurns.slice(0, roleplayStep + 1).map((turn, idx) => {
                const isLearner = turn.speaker.toLowerCase().includes('вы') || turn.speaker.toLowerCase().includes('learner');
                const isCurrentTurn = idx === roleplayStep;

                return (
                  <div
                    key={idx}
                    className={`flex flex-col ${isLearner ? 'items-end' : 'items-start'} animate-in fade-in slide-in-from-bottom-2 duration-200`}
                  >
                    <span className="text-[10px] font-extrabold uppercase text-slate-400 mb-1 px-1">
                      {turn.speaker}
                    </span>
                    <div
                      className={`max-w-[88%] rounded-3xl p-3.5 text-xs font-medium shadow-xs transition-all ${
                        isCurrentTurn ? 'ring-2 ring-emerald-400 ring-offset-1' : ''
                      } ${
                        isLearner
                          ? 'bg-emerald-600 text-white rounded-br-xs'
                          : 'bg-white text-slate-800 rounded-bl-xs border border-slate-200'
                      }`}
                    >
                      <div className="flex items-center justify-between gap-3">
                        <span className="font-bold text-sm leading-snug">
                          {turn.speechIso}
                        </span>
                        <div className="flex items-center gap-1 shrink-0">
                          <button
                            onClick={() => speakHindi(turn.speechIso || turn.speechCyrillic)}
                            className={`p-1 rounded-full cursor-pointer ${isLearner ? 'hover:bg-emerald-700' : 'hover:bg-slate-100'}`}
                            title="Listen"
                          >
                            <Volume2 className="w-4 h-4" />
                          </button>
                        </div>
                      </div>
                      <div className={`text-[11px] mt-0.5 ${isLearner ? 'text-emerald-100' : 'text-slate-500'}`}>
                        [{turn.speechCyrillic}]
                      </div>
                      <div className={`mt-1.5 text-[11px] pt-1.5 border-t ${
                        isLearner ? 'border-emerald-500/50 text-emerald-100' : 'border-slate-100 text-slate-600'
                      }`}>
                        {turn.speechRu}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* If current turn is learner, show response chips */}
            {(() => {
              const currentTurn = roleplayTurns[roleplayStep];
              if (!currentTurn) return null;
              const isLearner = currentTurn.speaker.toLowerCase().includes('вы') || currentTurn.speaker.toLowerCase().includes('learner');

              if (isLearner) {
                return (
                  <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-4 animate-in fade-in">
                    <span className="text-xs font-black text-emerald-800 uppercase tracking-wider block mb-1">
                      {uiLanguage === 'ru' ? '🎯 Ваша реплика (выберите ответ):' : '🎯 Your response (choose option):'}
                    </span>
                    {currentTurn.learnerHintRu && (
                      <p className="text-xs text-emerald-950 mb-3 italic">
                        Подсказка: {currentTurn.learnerHintRu}
                      </p>
                    )}
                    <div className="flex flex-wrap gap-2">
                      {(currentTurn.acceptableResponsesIso || [currentTurn.speechIso]).map((resp, rIdx) => (
                        <button
                          key={rIdx}
                          onClick={() => handleRoleplayResponse(resp)}
                          className={`btn-duo-green px-4 py-2.5 rounded-2xl text-white font-extrabold text-xs shadow-md cursor-pointer flex items-center gap-1.5 transition-all ${
                            learnerChosenResponse === resp ? 'ring-3 ring-emerald-300 scale-105' : ''
                          }`}
                        >
                          <Send className="w-3.5 h-3.5" />
                          <span>{resp}</span>
                        </button>
                      ))}
                    </div>
                  </div>
                );
              }
              return null;
            })()}
          </div>
        )}

        {/* STAGE 5: LESSON COMPLETE CELEBRATION */}
        {stage === 'completed' && (
          <div className="text-center animate-in zoom-in-95 duration-300 py-8">
            <div className="w-24 h-24 mx-auto bg-amber-100 rounded-full flex items-center justify-center shadow-lg border-4 border-amber-200 animate-bounce">
              <Trophy className="w-12 h-12 text-amber-600" />
            </div>

            <h2 className="text-2xl font-black text-slate-900 mt-6">
              {uiLanguage === 'ru' ? 'Урок успешно завершен!' : 'Lesson Completed!'}
            </h2>
            <p className="text-sm text-slate-600 mt-2 max-w-sm mx-auto">
              {uiLanguage === 'ru'
                ? `Вы освоили материал Дня ${selectedDay.day}: ${selectedDay.title.ru}.`
                : `You have mastered Day ${selectedDay.day}: ${selectedDay.title.en}.`}
            </p>

            {/* Rewards Badge */}
            <div className="mt-6 flex items-center justify-center gap-4">
              <div className="bg-blue-50 border border-blue-200 px-4 py-2.5 rounded-2xl text-center">
                <span className="text-xs text-blue-600 font-bold block">XP Points</span>
                <span className="text-lg font-black text-blue-800">+50 XP</span>
              </div>
              <div className="bg-amber-50 border border-amber-200 px-4 py-2.5 rounded-2xl text-center">
                <span className="text-xs text-amber-600 font-bold block">Status</span>
                <span className="text-lg font-black text-amber-800">100% Verified</span>
              </div>
            </div>

            <div className="mt-8">
              <button
                onClick={closeLesson}
                className="w-full btn-duo-green py-4 rounded-2xl text-white font-black text-base shadow-md cursor-pointer"
              >
                {uiLanguage === 'ru' ? 'Вернуться к пути' : 'Continue Learning'}
              </button>
            </div>
          </div>
        )}
      </main>

      {/* Out of Hearts Modal */}
      {showHeartRefillModal && (
        <div className="fixed inset-0 z-60 bg-black/50 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl p-6 max-w-sm w-full text-center shadow-2xl animate-in zoom-in-95">
            <div className="w-16 h-16 bg-rose-100 rounded-full flex items-center justify-center mx-auto mb-4 text-rose-500">
              <Heart className="w-8 h-8 fill-rose-500" />
            </div>
            <h3 className="text-xl font-extrabold text-slate-900 mb-2">
              {uiLanguage === 'ru' ? 'Закончились жизни!' : 'Out of Hearts!'}
            </h3>
            <p className="text-xs text-slate-600 mb-6 leading-relaxed">
              {uiLanguage === 'ru'
                ? 'Ошибки — естественная часть языкового обучения. Восполните запас жизней и продолжайте тренировку.'
                : 'Mistakes are how we learn! Refill your hearts to continue practicing without limits.'}
            </p>
            <button
              onClick={() => {
                resetHearts();
                setShowHeartRefillModal(false);
                if (soundEnabled) sfx.playSuccess();
              }}
              className="w-full btn-duo-green py-3.5 rounded-2xl text-white font-extrabold text-sm shadow-md cursor-pointer flex items-center justify-center gap-2"
            >
              <RotateCcw className="w-4 h-4" />
              <span>{uiLanguage === 'ru' ? 'Восполнить 5 жизней (+5 ❤️)' : 'Refill 5 Hearts (+5 ❤️)'}</span>
            </button>
          </div>
        </div>
      )}

      {/* Sticky Bottom Action Drawer */}
      {stage !== 'completed' && (
        <footer className={`border-t p-4 transition-colors ${
          feedback === 'correct'
            ? 'bg-emerald-100 border-emerald-300'
            : feedback === 'incorrect'
            ? 'bg-rose-100 border-rose-300'
            : 'bg-white border-slate-200'
        }`}>
          <div className="max-w-xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
            {/* Feedback Message */}
            {feedback === 'correct' && (
              <div className="flex items-center gap-2 text-emerald-800 font-extrabold text-sm animate-in fade-in">
                <CheckCircle2 className="w-6 h-6 text-emerald-600 shrink-0" />
                <div>
                  <span>
                    {currentExercise?.type === 'listen_and_repeat'
                      ? (uiLanguage === 'ru' ? 'Превосходно! Устное повторение выполнено.' : 'Excellent! Oral repetition completed.')
                      : (uiLanguage === 'ru' ? 'Превосходно! Правильно.' : 'Excellent! Correct.')}
                  </span>
                  {currentExercise?.explanationRu && (
                    <p className="text-xs font-normal text-emerald-950 mt-0.5">
                      {uiLanguage === 'ru' ? currentExercise.explanationRu : (currentExercise.explanationEn || currentExercise.explanationRu)}
                    </p>
                  )}
                </div>
              </div>
            )}

            {feedback === 'incorrect' && (
              <div className="flex items-center gap-2 text-rose-800 font-extrabold text-sm animate-in fade-in">
                <XCircle className="w-6 h-6 text-rose-600 shrink-0" />
                <div>
                  <span>{uiLanguage === 'ru' ? 'Ошибка!' : 'Incorrect!'}</span>
                  <p className="text-xs font-normal text-rose-950 mt-0.5">
                    {uiLanguage === 'ru' ? currentExercise?.explanationRu : (currentExercise?.explanationEn || currentExercise?.explanationRu)}
                  </p>
                </div>
              </div>
            )}

            {feedback === 'idle' && (
              <div className="text-xs text-slate-500 font-medium hidden sm:block">
                {stage === 'warmup' && (uiLanguage === 'ru' ? 'Прослушайте звуки и перейдите к теории (Enter)' : 'Listen to phonetics, then proceed (Enter)')}
                {stage === 'theory' && (uiLanguage === 'ru' ? 'Изучите правило и перейдите к практике (Enter)' : 'Review the bridge, then practice (Enter)')}
                {stage === 'exercise' && currentExercise?.type === 'listen_and_repeat' && (uiLanguage === 'ru' ? 'Повторите вслух или используйте микрофон (Enter)' : 'Repeat aloud or use mic (Enter)')}
                {stage === 'exercise' && currentExercise?.type !== 'listen_and_repeat' && (uiLanguage === 'ru' ? 'Выберите ответ (1–4) или соберите фразу (Enter)' : 'Select answer (1–4) or chips (Enter)')}
                {stage === 'roleplay' && (uiLanguage === 'ru' ? 'Участвуйте в диалоге и завершите день' : 'Engage in dialogue to complete lesson')}
              </div>
            )}

            {/* Action Button */}
            <div className="w-full sm:w-auto">
              {stage === 'exercise' && feedback === 'idle' ? (
                <button
                  onClick={handleCheckAnswer}
                  disabled={
                    (currentExercise?.type === 'word_reorder_sov' && selectedChips.length === 0) ||
                    (currentExercise?.type !== 'word_reorder_sov' && currentExercise?.type !== 'listen_and_repeat' && !selectedOption)
                  }
                  className="w-full sm:w-auto btn-duo-green py-3 px-8 rounded-2xl text-white font-black text-sm disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer shadow-md"
                >
                  {currentExercise?.type === 'listen_and_repeat'
                    ? (uiLanguage === 'ru' ? 'Я повторил(а) вслух' : 'I repeated out loud')
                    : (uiLanguage === 'ru' ? 'Проверить' : 'Check')}
                </button>
              ) : (
                <button
                  onClick={handleNextStep}
                  className="w-full sm:w-auto btn-duo-green py-3 px-8 rounded-2xl text-white font-black text-sm flex items-center justify-center gap-2 cursor-pointer shadow-md"
                >
                  <span>{uiLanguage === 'ru' ? 'Продолжить' : 'Continue'}</span>
                  <ArrowRight className="w-4 h-4 stroke-[3px]" />
                </button>
              )}
            </div>
          </div>
        </footer>
      )}
    </div>
  );
};
