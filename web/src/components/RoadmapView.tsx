import React, { useState } from 'react';
import {
  Check,
  Lock,
  Play,
  Star,
  Volume2,
  X,
  ChevronRight,
  Award,
  Clock
} from 'lucide-react';
import { useApp } from '../context/AppContext';
import type { DayLesson } from '../data/types';
import { speakHindi, sfx } from '../utils/audio';

export const RoadmapView: React.FC = () => {
  const {
    courseBundle,
    completedDays,
    startLesson,
    uiLanguage,
    showDevanagari,
  } = useApp();

  const [previewDay, setPreviewDay] = useState<DayLesson | null>(null);

  // Group days by Phase (1 to 5)
  const phases = courseBundle.manifest.phases;

  // Curvature offsets for Duolingo serpentine path: left, center, right, center...
  const getOffsetClass = (index: number) => {
    const pattern = [0, 40, 70, 40, 0, -40, -70, -40];
    const offset = pattern[index % pattern.length];
    if (offset === 70) return 'translate-x-12 sm:translate-x-16';
    if (offset === 40) return 'translate-x-6 sm:translate-x-8';
    if (offset === -40) return '-translate-x-6 sm:-translate-x-8';
    if (offset === -70) return '-translate-x-12 sm:-translate-x-16';
    return 'translate-x-0';
  };

  const getPhaseColor = (phaseNum: number) => {
    switch (phaseNum) {
      case 1:
        return {
          bg: 'bg-emerald-500',
          border: 'border-emerald-600',
          ring: 'ring-emerald-400',
          banner: 'from-emerald-600 to-teal-600',
          pillActive: 'bg-emerald-600 text-white'
        };
      case 2:
        return {
          bg: 'bg-blue-500',
          border: 'border-blue-600',
          ring: 'ring-blue-400',
          banner: 'from-blue-600 to-indigo-600',
          pillActive: 'bg-blue-600 text-white'
        };
      case 3:
        return {
          bg: 'bg-amber-500',
          border: 'border-amber-600',
          ring: 'ring-amber-400',
          banner: 'from-amber-600 to-orange-600',
          pillActive: 'bg-amber-600 text-white'
        };
      case 4:
        return {
          bg: 'bg-rose-500',
          border: 'border-rose-600',
          ring: 'ring-rose-400',
          banner: 'from-rose-600 to-pink-600',
          pillActive: 'bg-rose-600 text-white'
        };
      case 5:
        return {
          bg: 'bg-purple-500',
          border: 'border-purple-600',
          ring: 'ring-purple-400',
          banner: 'from-purple-600 to-violet-600',
          pillActive: 'bg-purple-600 text-white'
        };
      default:
        return {
          bg: 'bg-emerald-500',
          border: 'border-emerald-600',
          ring: 'ring-emerald-400',
          banner: 'from-emerald-600 to-teal-600',
          pillActive: 'bg-emerald-600 text-white'
        };
    }
  };

  const scrollToPhase = (phaseNum: number) => {
    sfx.playTap();
    const elem = document.getElementById(`phase-${phaseNum}`);
    if (elem) {
      elem.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  return (
    <div className="flex-1 pb-24 md:pb-12 max-w-xl mx-auto px-4 pt-4">
      {/* Sticky Phase Jump Navigation Bar */}
      <div className="sticky top-[53px] z-30 bg-slate-50/95 backdrop-blur-md py-2.5 mb-6 border-b border-slate-200/80 -mx-4 px-4 shadow-xs">
        <div className="flex items-center gap-1.5 overflow-x-auto scrollbar-none pb-0.5">
          <span className="text-[11px] font-extrabold uppercase tracking-wider text-slate-400 shrink-0 mr-1 hidden sm:inline">
            {uiLanguage === 'ru' ? 'Фазы:' : 'Phases:'}
          </span>
          {phases.map(phase => {
            const [startDay, endDay] = phase.daysRange;
            const phaseDays = courseBundle.days.filter(d => d.day >= startDay && d.day <= endDay);
            const countCompleted = phaseDays.filter(d => completedDays.includes(d.day)).length;
            const isFull = countCompleted === phaseDays.length && phaseDays.length > 0;

            return (
              <button
                key={phase.phaseNumber}
                onClick={() => scrollToPhase(phase.phaseNumber)}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all shrink-0 cursor-pointer ${
                  isFull
                    ? 'bg-amber-100 text-amber-900 border border-amber-300'
                    : 'bg-white border border-slate-200 text-slate-700 hover:bg-slate-100 active:scale-95'
                }`}
              >
                <span>{uiLanguage === 'ru' ? `Фаза ${phase.phaseNumber}` : `Phase ${phase.phaseNumber}`}</span>
                <span className={`text-[10px] px-1.5 py-0.2 rounded-md font-mono ${
                  isFull ? 'bg-amber-200 text-amber-950' : 'bg-slate-100 text-slate-600'
                }`}>
                  {countCompleted}/{phaseDays.length}
                </span>
                {isFull && <Check className="w-3 h-3 text-amber-700 stroke-[3]" />}
              </button>
            );
          })}
        </div>
      </div>

      {/* Overview Intro Banner */}
      <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-xs mb-8 text-center sm:text-left flex flex-col sm:flex-row items-center gap-4">
        <div className="w-14 h-14 rounded-2xl bg-emerald-100 flex items-center justify-center shrink-0">
          <Award className="w-8 h-8 text-emerald-700" />
        </div>
        <div className="flex-1">
          <h2 className="text-base font-extrabold text-slate-800">
            {uiLanguage === 'ru' ? '40-дневный разговорный маршрут' : '40-Day Conversational Roadmap'}
          </h2>
          <p className="text-xs text-slate-600 mt-1">
            {uiLanguage === 'ru'
              ? '20 минут в день: от нуля до уверенной устной речи в путешествии по Индии.'
              : '20 minutes a day: zero knowledge to confident verbal fluency for travel in India.'}
          </p>
          <div className="mt-2.5 flex items-center gap-2">
            <div className="flex-1 h-2 bg-slate-100 rounded-full overflow-hidden border border-slate-200">
              <div
                className="h-full bg-emerald-500 transition-all duration-500"
                style={{ width: `${(completedDays.length / 40) * 100}%` }}
              />
            </div>
            <span className="text-xs font-bold text-slate-700">{completedDays.length}/40</span>
          </div>
        </div>
      </div>

      {/* 5 Phases Flow */}
      {phases.map((phase) => {
        const colors = getPhaseColor(phase.phaseNumber);
        const [startDay, endDay] = phase.daysRange;
        const phaseDays = courseBundle.days.filter(
          (d) => d.day >= startDay && d.day <= endDay
        );
        const phaseCompleted = phaseDays.filter((d) => completedDays.includes(d.day)).length;

        return (
          <section key={phase.phaseNumber} id={`phase-${phase.phaseNumber}`} className="mb-12 scroll-mt-24">
            {/* Phase Header Banner */}
            <div className={`bg-gradient-to-r ${colors.banner} text-white rounded-3xl p-5 shadow-sm mb-8`}>
              <div className="flex items-center justify-between text-xs font-bold uppercase tracking-wider text-white/80">
                <span>
                  {uiLanguage === 'ru' ? `Фаза ${phase.phaseNumber}` : `Phase ${phase.phaseNumber}`}
                </span>
                <span>
                  {uiLanguage === 'ru'
                    ? `Дни ${startDay}–${endDay}`
                    : `Days ${startDay}–${endDay}`}
                </span>
              </div>
              <h3 className="text-lg font-black text-white mt-1 leading-snug">
                {uiLanguage === 'ru' ? phase.titleRu : phase.titleEn}
              </h3>
              <p className="text-xs text-white/90 mt-1 leading-relaxed">
                {uiLanguage === 'ru' ? phase.theme : ((phase as unknown as { themeEn?: string }).themeEn || phase.theme)}
              </p>
              <div className="mt-3 flex items-center justify-between text-xs font-bold text-white/90">
                <span>
                  {uiLanguage === 'ru' ? 'Пройдено уроков:' : 'Completed lessons:'} {phaseCompleted}/{phaseDays.length}
                </span>
                <span className="bg-white/20 px-2 py-0.5 rounded-full text-[11px]">
                  {Math.round((phaseCompleted / phaseDays.length) * 100)}%
                </span>
              </div>
            </div>

            {/* Serpentine Node Pathway */}
            <div className="flex flex-col items-center gap-6 py-2 relative">
              {phaseDays.map((day, idx) => {
                const isCompleted = completedDays.includes(day.day);
                const isCurrent = !isCompleted && (day.day === 1 || completedDays.includes(day.day - 1));
                const offsetClass = getOffsetClass(idx);

                return (
                  <div
                    key={day.day}
                    className={`flex flex-col items-center transition-transform duration-200 ${offsetClass}`}
                  >
                    {/* Floating Day Node Button */}
                    <button
                      onClick={() => {
                        sfx.playTap();
                        setPreviewDay((day as unknown) as DayLesson);
                      }}
                      className={`relative w-20 h-20 rounded-full flex flex-col items-center justify-center font-black transition-all cursor-pointer select-none ${
                        isCompleted
                          ? 'bg-amber-400 border-b-6 border-amber-600 text-amber-950 active:translate-y-1 active:border-b-2 shadow-md'
                          : isCurrent
                          ? `${colors.bg} border-b-6 ${colors.border} text-white ring-4 ${colors.ring} ring-offset-2 animate-pulse active:translate-y-1 active:border-b-2 shadow-lg`
                          : 'bg-slate-200 border-b-6 border-slate-300 text-slate-500 hover:bg-slate-300 active:translate-y-1'
                      }`}
                    >
                      {/* Top icon indicator */}
                      {isCompleted ? (
                        <Check className="w-7 h-7 stroke-[3px]" />
                      ) : isCurrent ? (
                        <Play className="w-7 h-7 fill-white stroke-none ml-1" />
                      ) : (
                        <Lock className="w-5 h-5 text-slate-400 mb-0.5" />
                      )}

                      <span className="text-xs tracking-tight leading-none mt-0.5">
                        {uiLanguage === 'ru' ? `День ${day.day}` : `Day ${day.day}`}
                      </span>

                      {/* Floating Star Badge for Completed */}
                      {isCompleted && (
                        <div className="absolute -top-1.5 -right-1.5 bg-amber-500 text-white rounded-full p-1 shadow-xs border-2 border-white">
                          <Star className="w-3.5 h-3.5 fill-white" />
                        </div>
                      )}
                    </button>

                    {/* Small Subtitle Label */}
                    <span className="mt-2 text-xs font-bold text-slate-700 text-center max-w-[150px] leading-tight line-clamp-1">
                      {uiLanguage === 'ru' ? day.title.ru : day.title.en}
                    </span>
                  </div>
                );
              })}
            </div>
          </section>
        );
      })}

      {/* Enriched Lesson Preview Modal */}
      {previewDay && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white w-full max-w-lg rounded-3xl p-6 shadow-2xl border border-slate-200 animate-in fade-in zoom-in-95 duration-150 max-h-[90vh] overflow-y-auto">
            {/* Modal Header */}
            <div className="flex items-start justify-between">
              <div>
                <span className="text-xs font-bold uppercase tracking-wider text-emerald-600 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200">
                  {uiLanguage === 'ru'
                    ? `Фаза ${previewDay.phase} • День ${previewDay.day}`
                    : `Phase ${previewDay.phase} • Day ${previewDay.day}`}
                </span>
                <h3 className="text-xl font-black text-slate-800 mt-2 leading-snug">
                  {uiLanguage === 'ru' ? previewDay.title.ru : previewDay.title.en}
                </h3>
                <p className="text-xs text-slate-500 font-medium mt-0.5">
                  {previewDay.theme}
                </p>
              </div>
              <button
                onClick={() => setPreviewDay(null)}
                className="p-1 rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-100 cursor-pointer"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Daily 20-Minute Protocol Grid */}
            <div className="mt-4 bg-emerald-50/60 border border-emerald-200/80 rounded-2xl p-3.5">
              <div className="flex items-center gap-2 mb-2 text-xs font-extrabold text-emerald-900">
                <Clock className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                <span>{uiLanguage === 'ru' ? '20-минутный распорядок урока:' : '20-Minute Lesson Architecture:'}</span>
              </div>
              <div className="grid grid-cols-2 gap-2 text-[11px] font-medium text-emerald-950">
                <div className="bg-white/80 p-2 rounded-xl border border-emerald-100">
                  <span className="font-bold block text-emerald-800">⏱️ 0–4 мин</span>
                  <span>{uiLanguage === 'ru' ? 'Разминка и активная лексика' : 'Warm-up & Key Vocabulary'}</span>
                </div>
                <div className="bg-white/80 p-2 rounded-xl border border-emerald-100">
                  <span className="font-bold block text-emerald-800">🧠 4–11 мин</span>
                  <span>{uiLanguage === 'ru' ? 'Формула SOV и контрастив' : 'SOV Formula & Contrastive Core'}</span>
                </div>
                <div className="bg-white/80 p-2 rounded-xl border border-emerald-100">
                  <span className="font-bold block text-emerald-800">🎯 11–17 мин</span>
                  <span>{uiLanguage === 'ru' ? 'Устные упражнения и тренажер' : 'Verbal Drills & Word Builder'}</span>
                </div>
                <div className="bg-white/80 p-2 rounded-xl border border-emerald-100">
                  <span className="font-bold block text-emerald-800">🎭 17–20 мин</span>
                  <span>{uiLanguage === 'ru' ? 'Диалог-симуляция в Индии' : 'Interactive Travel Roleplay'}</span>
                </div>
              </div>
            </div>

            {/* Cognitive Bridge Preview */}
            <div className="mt-3.5 bg-slate-50 border border-slate-200 rounded-2xl p-3.5 text-xs">
              <span className="font-extrabold text-slate-700 block mb-1">
                {uiLanguage === 'ru' ? '🧠 Сопоставительный якорь:' : '🧠 Contrastive Linguistic Bridge:'}
              </span>
              <p className="text-slate-600">
                {previewDay.contrastiveBridge.russianParallel}
              </p>
              <div className="mt-2 text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded-lg font-mono font-semibold text-[11px] border border-emerald-200">
                {previewDay.contrastiveBridge.syntacticFormula}
              </div>
            </div>

            {/* Vocabulary Preview Chips with Dual Audio */}
            <div className="mt-4">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-extrabold text-slate-700">
                  {uiLanguage === 'ru' ? 'Словарь занятия (нажмите для озвучки):' : 'Key Vocabulary (click to listen):'}
                </span>
                <span className="text-[11px] text-slate-400 font-semibold">
                  {previewDay.vocabulary.length} {uiLanguage === 'ru' ? 'слов' : 'words'}
                </span>
              </div>
              <div className="flex flex-wrap gap-1.5 max-h-36 overflow-y-auto pr-1">
                {previewDay.vocabulary.map((v) => {
                  const targetAudio = v.devanagari || v.transliterationIso;
                  return (
                    <div
                      key={v.id}
                      className="flex items-center gap-1.5 bg-white border border-slate-200 hover:border-emerald-400 px-2.5 py-1.5 rounded-xl text-xs font-medium text-slate-700 transition-all text-left shadow-xs"
                    >
                      <button
                        onClick={() => speakHindi(targetAudio, 1.0)}
                        className="p-1 rounded-lg hover:bg-emerald-100 text-emerald-600 transition-colors cursor-pointer"
                        title={uiLanguage === 'ru' ? 'Послушать (1.0x)' : 'Listen (1.0x)'}
                      >
                        <Volume2 className="w-3.5 h-3.5" />
                      </button>
                      <button
                        onClick={() => speakHindi(targetAudio, 0.65)}
                        className="p-1 rounded-lg hover:bg-emerald-100 text-emerald-600 transition-colors cursor-pointer text-[10px]"
                        title={uiLanguage === 'ru' ? 'Медленно (0.65x)' : 'Slow (0.65x)'}
                      >
                        🐢
                      </button>
                      <div>
                        <div className="font-bold text-slate-900">
                          {v.transliterationIso} <span className="font-normal text-slate-500">[{v.phoneticCyrillic}]</span>
                          {showDevanagari && <span className="ml-1 text-[11px] text-slate-400">{v.devanagari}</span>}
                        </div>
                        <div className="text-[10px] text-slate-500">
                          {uiLanguage === 'ru' ? v.translationRu : v.translationEn}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Action Buttons */}
            <div className="mt-6 flex items-center gap-3">
              <button
                onClick={() => {
                  sfx.playSuccess();
                  const dayToStart = previewDay.day;
                  setPreviewDay(null);
                  startLesson(dayToStart);
                }}
                className="flex-1 btn-duo-green py-3.5 rounded-2xl text-white font-black text-sm flex items-center justify-center gap-2 cursor-pointer shadow-md active:scale-95 transition-all"
              >
                <span>
                  {completedDays.includes(previewDay.day)
                    ? (uiLanguage === 'ru' ? 'Пройти повторно (+10 XP)' : 'Review Lesson (+10 XP)')
                    : (uiLanguage === 'ru' ? 'Начать урок (20 мин)' : 'Start Lesson (20 min)')}
                </span>
                <ChevronRight className="w-4 h-4 stroke-[3px]" />
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
