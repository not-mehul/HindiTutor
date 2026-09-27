import React from 'react';
import { useApp } from '../context/AppContext';
import {
  Globe,
  User,
  Type,
  Volume2,
  Trash2,
  Check,
  Award,
  Info
} from 'lucide-react';
import { speakHindi, sfx } from '../utils/audio';

export const SettingsView: React.FC = () => {
  const {
    uiLanguage,
    setUiLanguage,
    learnerGender,
    setLearnerGender,
    showDevanagari,
    setShowDevanagari,
    soundEnabled,
    setSoundEnabled,
    completedDays,
    xp,
    courseBundle
  } = useApp();

  const isEn = uiLanguage === 'en';

  const handleResetProgress = () => {
    const confirmText = isEn
      ? 'Are you sure you want to reset all lesson progress, XP, and completed days? This cannot be undone.'
      : 'Вы уверены, что хотите сбросить весь прогресс уроков, опыт (XP) и отметки? Это действие нельзя отменить.';

    if (window.confirm(confirmText)) {
      localStorage.removeItem('ht_completed');
      localStorage.removeItem('ht_xp');
      localStorage.removeItem('ht_streak');
      window.location.reload();
    }
  };

  const handleTestAudio = () => {
    sfx.playSuccess();
    setTimeout(() => {
      speakHindi('नमस्ते! आप कैसे हैं?');
    }, 400);
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 pb-24 md:pb-12">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-2xl md:text-3xl font-extrabold text-gray-900 mb-2">
          {isEn ? 'Course Settings & Configuration' : 'Настройки курса и параметры обучения'}
        </h1>
        <p className="text-gray-500 text-sm md:text-base">
          {isEn
            ? 'Customize language audit mode, learner grammatical gender, script display, and audio feedback.'
            : 'Управление языком аудита, грамматическим родом говорящего, показом письменности и звуковыми эффектами.'}
        </p>
      </div>

      <div className="space-y-6">
        {/* Language Audit Mode */}
        <div className="bg-white rounded-3xl border-2 border-gray-100 p-6 shadow-xs">
          <div className="flex items-center gap-3 mb-4">
            <div className="w-10 h-10 rounded-2xl bg-indigo-50 text-indigo-600 flex items-center justify-center">
              <Globe className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-base md:text-lg font-bold text-gray-900">
                {isEn ? 'Interface & Content Audit Mode' : 'Язык интерфейса и режим аудита'}
              </h2>
              <p className="text-xs text-gray-500">
                {isEn
                  ? 'Switch between Russian (for native learner immersion) and English (for curriculum audit & content review).'
                  : 'Переключение между русским (для прямого обучения) и английским (для аудита и проверки).'}
              </p>
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <button
              onClick={() => setUiLanguage('ru')}
              className={`p-4 rounded-2xl border-2 flex items-center justify-between transition-all ${
                uiLanguage === 'ru'
                  ? 'border-indigo-600 bg-indigo-50/50 shadow-xs'
                  : 'border-gray-200 hover:border-gray-300 bg-white'
              }`}
            >
              <div className="flex items-center gap-3">
                <span className="text-2xl">🇷🇺</span>
                <div className="text-left">
                  <div className="font-bold text-gray-900 text-sm">Русский (Russian)</div>
                  <div className="text-xs text-gray-500">Основной режим погружения</div>
                </div>
              </div>
              {uiLanguage === 'ru' && (
                <div className="w-6 h-6 rounded-full bg-indigo-600 text-white flex items-center justify-center">
                  <Check className="w-3.5 h-3.5 stroke-[3]" />
                </div>
              )}
            </button>

            <button
              onClick={() => setUiLanguage('en')}
              className={`p-4 rounded-2xl border-2 flex items-center justify-between transition-all ${
                uiLanguage === 'en'
                  ? 'border-indigo-600 bg-indigo-50/50 shadow-xs'
                  : 'border-gray-200 hover:border-gray-300 bg-white'
              }`}
            >
              <div className="flex items-center gap-3">
                <span className="text-2xl">🇬🇧</span>
                <div className="text-left">
                  <div className="font-bold text-gray-900 text-sm">English (English Audit)</div>
                  <div className="text-xs text-gray-500">Instructor & Reviewer audit mode</div>
                </div>
              </div>
              {uiLanguage === 'en' && (
                <div className="w-6 h-6 rounded-full bg-indigo-600 text-white flex items-center justify-center">
                  <Check className="w-3.5 h-3.5 stroke-[3]" />
                </div>
              )}
            </button>
          </div>
        </div>

        {/* Learner Gender Toggle */}
        <div className="bg-white rounded-3xl border-2 border-gray-100 p-6 shadow-xs">
          <div className="flex items-center gap-3 mb-4">
            <div className="w-10 h-10 rounded-2xl bg-pink-50 text-pink-600 flex items-center justify-center">
              <User className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-base md:text-lg font-bold text-gray-900">
                {isEn ? 'Speaker Grammatical Gender' : 'Грамматический род говорящего'}
              </h2>
              <p className="text-xs text-gray-500">
                {isEn
                  ? 'In Hindi, verbs agree with the speaker in gender: female uses -tī hū̃ (-тии хууⁿ), male uses -tā hū̃ (-таа хууⁿ).'
                  : 'В хинди глаголы согласуются с полом говорящего: женский род использует окончание -тии (-tī), мужской -таа (-tā).'}
              </p>
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <button
              onClick={() => setLearnerGender('f')}
              className={`p-4 rounded-2xl border-2 flex items-center justify-between transition-all ${
                learnerGender === 'f'
                  ? 'border-pink-500 bg-pink-50/50 shadow-xs'
                  : 'border-gray-200 hover:border-gray-300 bg-white'
              }`}
            >
              <div className="text-left">
                <div className="font-bold text-gray-900 text-sm flex items-center gap-2">
                  <span>👩</span>
                  <span>{isEn ? 'Female Learner (Default)' : 'Женский род (По умолчанию)'}</span>
                </div>
                <div className="text-xs text-pink-700 font-mono mt-1">
                  mãĩ boltī hū̃ / маиⁿ боолтии хууⁿ (Я говорю)
                </div>
              </div>
              {learnerGender === 'f' && (
                <div className="w-6 h-6 rounded-full bg-pink-500 text-white flex items-center justify-center">
                  <Check className="w-3.5 h-3.5 stroke-[3]" />
                </div>
              )}
            </button>

            <button
              onClick={() => setLearnerGender('m')}
              className={`p-4 rounded-2xl border-2 flex items-center justify-between transition-all ${
                learnerGender === 'm'
                  ? 'border-blue-500 bg-blue-50/50 shadow-xs'
                  : 'border-gray-200 hover:border-gray-300 bg-white'
              }`}
            >
              <div className="text-left">
                <div className="font-bold text-gray-900 text-sm flex items-center gap-2">
                  <span>👨</span>
                  <span>{isEn ? 'Male Learner' : 'Мужской род'}</span>
                </div>
                <div className="text-xs text-blue-700 font-mono mt-1">
                  mãĩ boltā hū̃ / маиⁿ боолтаа хууⁿ (Я говорю)
                </div>
              </div>
              {learnerGender === 'm' && (
                <div className="w-6 h-6 rounded-full bg-blue-500 text-white flex items-center justify-center">
                  <Check className="w-3.5 h-3.5 stroke-[3]" />
                </div>
              )}
            </button>
          </div>
        </div>

        {/* Script & Sound Preferences */}
        <div className="bg-white rounded-3xl border-2 border-gray-100 p-6 shadow-xs space-y-4">
          <h2 className="text-base md:text-lg font-bold text-gray-900 flex items-center gap-2">
            <Type className="w-5 h-5 text-gray-600" />
            <span>{isEn ? 'Display & Audio Preferences' : 'Отображение и звук'}</span>
          </h2>

          {/* Devanagari Switch */}
          <div className="flex items-center justify-between p-3 rounded-2xl hover:bg-gray-50 transition-colors">
            <div>
              <div className="font-bold text-gray-900 text-sm">
                {isEn ? 'Show Devanagari Script (देवनागरी)' : 'Показывать письменность деванагари'}
              </div>
              <div className="text-xs text-gray-500">
                {isEn
                  ? 'Display authentic Hindi script alongside targeted Cyrillic & Latin phonetics'
                  : 'Показывать буквы деванагари рядом с целевой русской фонетикой и латиницей'}
              </div>
            </div>
            <button
              onClick={() => setShowDevanagari(!showDevanagari)}
              className={`w-14 h-8 flex items-center rounded-full p-1 cursor-pointer transition-colors duration-200 ease-in-out ${
                showDevanagari ? 'bg-emerald-500 justify-end' : 'bg-gray-300 justify-start'
              }`}
            >
              <div className="bg-white w-6 h-6 rounded-full shadow-md transform transition-transform" />
            </button>
          </div>

          <div className="border-t border-gray-100" />

          {/* Sound Effects Switch */}
          <div className="flex items-center justify-between p-3 rounded-2xl hover:bg-gray-50 transition-colors">
            <div>
              <div className="font-bold text-gray-900 text-sm">
                {isEn ? 'Tactile Sound Effects' : 'Звуковые эффекты интерфейса'}
              </div>
              <div className="text-xs text-gray-500">
                {isEn
                  ? 'Synthesized celebratory chimes, errors, and button tap clicks'
                  : 'Синтезированные щелчки кнопок, звуки правильного ответа и победные фанфары'}
              </div>
            </div>
            <button
              onClick={() => setSoundEnabled(!soundEnabled)}
              className={`w-14 h-8 flex items-center rounded-full p-1 cursor-pointer transition-colors duration-200 ease-in-out ${
                soundEnabled ? 'bg-emerald-500 justify-end' : 'bg-gray-300 justify-start'
              }`}
            >
              <div className="bg-white w-6 h-6 rounded-full shadow-md transform transition-transform" />
            </button>
          </div>

          <div className="border-t border-gray-100" />

          {/* Audio Test Button */}
          <div className="flex items-center justify-between p-3 rounded-2xl hover:bg-gray-50 transition-colors">
            <div>
              <div className="font-bold text-gray-900 text-sm">
                {isEn ? 'Studio Neural Voice Check (Swara hi-IN)' : 'Проверка студийного голоса (Swara hi-IN)'}
              </div>
              <div className="text-xs text-gray-500">
                {isEn
                  ? 'Plays natural female neural audio (Azure SwaraNeural) with fallback speech synthesis'
                  : 'Воспроизводит чистый женский нейронный голос (Azure SwaraNeural) без роботизированного акцента'}
              </div>
            </div>
            <button
              onClick={handleTestAudio}
              className="px-4 py-2 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 active:scale-95 rounded-xl font-bold text-xs flex items-center gap-1.5 transition-all cursor-pointer"
            >
              <Volume2 className="w-4 h-4" />
              <span>{isEn ? 'Test Sound' : 'Проверить звук'}</span>
            </button>
          </div>
        </div>

        {/* Course Statistics & Manifest Summary */}
        <div className="bg-white rounded-3xl border-2 border-gray-100 p-6 shadow-xs">
          <h2 className="text-base md:text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
            <Award className="w-5 h-5 text-amber-500" />
            <span>{isEn ? 'Curriculum Architecture' : 'Архитектура курса'}</span>
          </h2>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center mb-4">
            <div className="p-3 bg-gray-50 rounded-2xl border border-gray-100">
              <div className="text-2xl font-black text-gray-900">{courseBundle.manifest.totalDays}</div>
              <div className="text-[11px] font-bold text-gray-400 uppercase mt-0.5">{isEn ? 'Total Days' : 'Дней курса'}</div>
            </div>
            <div className="p-3 bg-gray-50 rounded-2xl border border-gray-100">
              <div className="text-2xl font-black text-gray-900">{courseBundle.manifest.totalPhases}</div>
              <div className="text-[11px] font-bold text-gray-400 uppercase mt-0.5">{isEn ? 'Phases' : 'Фазы обучения'}</div>
            </div>
            <div className="p-3 bg-gray-50 rounded-2xl border border-gray-100">
              <div className="text-2xl font-black text-gray-900">{completedDays.length} / 40</div>
              <div className="text-[11px] font-bold text-gray-400 uppercase mt-0.5">{isEn ? 'Completed' : 'Пройдено'}</div>
            </div>
            <div className="p-3 bg-gray-50 rounded-2xl border border-gray-100">
              <div className="text-2xl font-black text-amber-500">{xp}</div>
              <div className="text-[11px] font-bold text-gray-400 uppercase mt-0.5">XP</div>
            </div>
          </div>

          <div className="text-xs text-gray-500 bg-gray-50 rounded-xl p-3.5 space-y-1.5 border border-gray-100">
            <div className="flex items-center gap-2 font-bold text-gray-700">
              <Info className="w-4 h-4 text-emerald-600" />
              <span>{isEn ? 'Daily 20-Minute Protocol' : 'Ежедневный 20-минутный протокол'}</span>
            </div>
            <p>1. 00:00–04:00: {courseBundle.manifest.dailyProtocol.phase1}</p>
            <p>2. 04:00–11:00: {courseBundle.manifest.dailyProtocol.phase2}</p>
            <p>3. 11:00–17:00: {courseBundle.manifest.dailyProtocol.phase3}</p>
            <p>4. 17:00–20:00: {courseBundle.manifest.dailyProtocol.phase4}</p>
          </div>
        </div>

        {/* Danger Zone: Reset Data */}
        <div className="bg-red-50/50 rounded-3xl border border-red-200 p-6 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div>
            <h3 className="font-bold text-red-900 text-base flex items-center gap-2">
              <Trash2 className="w-4 h-4 text-red-600" />
              <span>{isEn ? 'Reset Learner Progress' : 'Сброс прогресса'}</span>
            </h3>
            <p className="text-xs text-red-700 mt-1 max-w-md">
              {isEn
                ? 'Clear all completed lesson records, streaks, and accumulated XP from local storage to test from Day 1.'
                : 'Сбросить все отметки о пройденных днях, серию и очки опыта для повторного тестирования с Дня 1.'}
            </p>
          </div>
          <button
            onClick={handleResetProgress}
            className="px-4 py-2.5 bg-red-600 hover:bg-red-700 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition-all whitespace-nowrap"
          >
            {isEn ? 'Reset All Progress' : 'Сбросить весь прогресс'}
          </button>
        </div>
      </div>
    </div>
  );
};
