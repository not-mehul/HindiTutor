import React, { useState } from 'react';
import { useApp } from '../context/AppContext';
import {
  Globe,
  User,
  Type,
  Volume2,
  Trash2,
  Check,
  Award,
  Info,
  Download,
  Upload,
  Database,
  Flame,
  Zap,
  Heart,
  Calendar,
  AlertCircle
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
    streak,
    hearts,
    lastActiveDate,
    xp,
    courseBundle,
    exportBackup,
    importBackup,
    resetAllData
  } = useApp();

  const isEn = uiLanguage === 'en';
  const [importMessage, setImportMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);

  const handleExportBackup = () => {
    try {
      const jsonStr = exportBackup();
      const blob = new Blob([jsonStr], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `HindiTutor_Backup_${new Date().toISOString().split('T')[0]}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      sfx.playSuccess();
      setImportMessage({
        type: 'success',
        text: isEn ? 'Progress backup file exported successfully!' : 'Резервная копия прогресса успешно сохранена в файл!'
      });
    } catch {
      sfx.playError();
      setImportMessage({
        type: 'error',
        text: isEn ? 'Failed to export backup.' : 'Ошибка при экспорте резервной копии.'
      });
    }
  };

  const handleImportFile = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const content = event.target?.result as string;
      if (content) {
        const success = importBackup(content);
        if (success) {
          sfx.playSuccess();
          setImportMessage({
            type: 'success',
            text: isEn ? 'Progress successfully restored from backup!' : 'Прогресс успешно восстановлен из резервной копии!'
          });
        } else {
          sfx.playError();
          setImportMessage({
            type: 'error',
            text: isEn ? 'Invalid backup file format.' : 'Неверный или поврежденный формат файла резервной копии.'
          });
        }
      }
    };
    reader.readAsText(file);
    e.target.value = '';
  };

  const handleResetProgress = () => {
    const confirmText = isEn
      ? 'Are you sure you want to reset all lesson progress, XP, streak, and completed days? This cannot be undone.'
      : 'Вы уверены, что хотите сбросить весь прогресс уроков, опыт (XP), ударный режим и отметки? Это действие нельзя отменить.';

    if (window.confirm(confirmText)) {
      resetAllData();
      sfx.playSuccess();
      setImportMessage({
        type: 'success',
        text: isEn
          ? 'All progress has been reset to Day 1 (Streak: 1, XP: 0).'
          : 'Весь прогресс сброшен к Дню 1 (Ударный режим: 1, XP: 0).'
      });
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
            ? 'Customize language audit mode, learner grammatical gender, script display, and local browser cache.'
            : 'Управление языком аудита, грамматическим родом, показом письменности и локальным кэшем браузера.'}
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
              className={`p-4 rounded-2xl border-2 flex items-center justify-between transition-all cursor-pointer ${
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
              className={`p-4 rounded-2xl border-2 flex items-center justify-between transition-all cursor-pointer ${
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
              className={`p-4 rounded-2xl border-2 flex items-center justify-between transition-all cursor-pointer ${
                learnerGender === 'f'
                  ? 'border-pink-500 bg-pink-50/50 shadow-xs'
                  : 'border-gray-200 hover:border-gray-300 bg-white'
              }`}
            >
              <div className="flex items-center gap-3">
                <span className="text-2xl">👩</span>
                <div className="text-left">
                  <div className="font-bold text-gray-900 text-sm">
                    {isEn ? 'Female Speaker (Default)' : 'Женский род (Основной)'}
                  </div>
                  <div className="text-xs text-gray-500">
                    बोलती हूँ (bōltī hū̃) • Речевая норма курса
                  </div>
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
              className={`p-4 rounded-2xl border-2 flex items-center justify-between transition-all cursor-pointer ${
                learnerGender === 'm'
                  ? 'border-pink-500 bg-pink-50/50 shadow-xs'
                  : 'border-gray-200 hover:border-gray-300 bg-white'
              }`}
            >
              <div className="flex items-center gap-3">
                <span className="text-2xl">👨</span>
                <div className="text-left">
                  <div className="font-bold text-gray-900 text-sm">
                    {isEn ? 'Male Speaker' : 'Мужской род'}
                  </div>
                  <div className="text-xs text-gray-500">
                    बोलता हूँ (bōltā hū̃)
                  </div>
                </div>
              </div>
              {learnerGender === 'm' && (
                <div className="w-6 h-6 rounded-full bg-pink-500 text-white flex items-center justify-center">
                  <Check className="w-3.5 h-3.5 stroke-[3]" />
                </div>
              )}
            </button>
          </div>
        </div>

        {/* Display and Audio Options */}
        <div className="bg-white rounded-3xl border-2 border-gray-100 p-6 shadow-xs space-y-4">
          {/* Devanagari Toggle */}
          <div className="flex items-center justify-between p-3 rounded-2xl hover:bg-gray-50 transition-colors">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-2xl bg-amber-50 text-amber-600 flex items-center justify-center">
                <Type className="w-5 h-5" />
              </div>
              <div>
                <div className="font-bold text-gray-900 text-sm">
                  {isEn ? 'Display Devanagari Script' : 'Отображение письма деванагари'}
                </div>
                <div className="text-xs text-gray-500">
                  {isEn
                    ? 'Show native Hindi script alongside Latin ISO and Cyrillic phonetic transliterations.'
                    : 'Показывать оригинальное письмо деванагари рядом с латинской и русской транслитерацией.'}
                </div>
              </div>
            </div>
            <button
              onClick={() => setShowDevanagari(!showDevanagari)}
              className={`w-12 h-7 rounded-full transition-colors p-0.5 cursor-pointer ${
                showDevanagari ? 'bg-emerald-500' : 'bg-gray-200'
              }`}
            >
              <div
                className={`bg-white w-6 h-6 rounded-full shadow-md transform transition-transform ${
                  showDevanagari ? 'translate-x-5' : 'translate-x-0'
                }`}
              />
            </button>
          </div>

          <div className="border-t border-gray-100" />

          {/* Sound Effects Toggle */}
          <div className="flex items-center justify-between p-3 rounded-2xl hover:bg-gray-50 transition-colors">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-2xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
                <Volume2 className="w-5 h-5" />
              </div>
              <div>
                <div className="font-bold text-gray-900 text-sm">
                  {isEn ? 'Sound Effects & UI Chimes' : 'Звуковые эффекты и обратная связь'}
                </div>
                <div className="text-xs text-gray-500">
                  {isEn
                    ? 'Audio chimes for correct answers, errors, and fanfare celebrations.'
                    : 'Звуковые сигналы для правильных ответов, ошибок и завершения уроков.'}
                </div>
              </div>
            </div>
            <button
              onClick={() => setSoundEnabled(!soundEnabled)}
              className={`w-12 h-7 rounded-full transition-colors p-0.5 cursor-pointer ${
                soundEnabled ? 'bg-emerald-500' : 'bg-gray-200'
              }`}
            >
              <div
                className={`bg-white w-6 h-6 rounded-full shadow-md transform transition-transform ${
                  soundEnabled ? 'translate-x-5' : 'translate-x-0'
                }`}
              />
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

        {/* Local Browser Storage & Backup Management */}
        <div className="bg-white rounded-3xl border-2 border-gray-100 p-6 shadow-xs">
          <div className="flex items-center gap-3 mb-4">
            <div className="w-10 h-10 rounded-2xl bg-cyan-50 text-cyan-600 flex items-center justify-center">
              <Database className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-base md:text-lg font-bold text-gray-900">
                {isEn ? 'Local Browser Cache & Data Persistence' : 'Локальное хранилище браузера и кэш'}
              </h2>
              <p className="text-xs text-gray-500">
                {isEn
                  ? 'All progress, streak habits, XP, and settings are cached client-side in your browser localStorage without requiring a server account.'
                  : 'Все результаты, серия дней, опыт и настройки сохраняются непосредственно в кэше вашего браузера (localStorage) без необходимости авторизации.'}
              </p>
            </div>
          </div>

          {/* Cached Data Metrics Grid */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center my-4">
            <div className="p-3 bg-amber-50/60 rounded-2xl border border-amber-200">
              <div className="flex items-center justify-center gap-1 text-amber-700 mb-0.5">
                <Flame className="w-4 h-4 fill-amber-500 text-amber-500" />
                <span className="text-lg font-black">{streak}</span>
              </div>
              <div className="text-[11px] font-bold text-amber-900 uppercase">
                {isEn ? 'Streak (Starts @ 1)' : 'Серия (от 1)'}
              </div>
            </div>

            <div className="p-3 bg-blue-50/60 rounded-2xl border border-blue-200">
              <div className="flex items-center justify-center gap-1 text-blue-700 mb-0.5">
                <Zap className="w-4 h-4 fill-blue-500 text-blue-500" />
                <span className="text-lg font-black">{xp}</span>
              </div>
              <div className="text-[11px] font-bold text-blue-900 uppercase">XP Points</div>
            </div>

            <div className="p-3 bg-rose-50/60 rounded-2xl border border-rose-200">
              <div className="flex items-center justify-center gap-1 text-rose-700 mb-0.5">
                <Heart className="w-4 h-4 fill-rose-500 text-rose-500" />
                <span className="text-lg font-black">{hearts} / 5</span>
              </div>
              <div className="text-[11px] font-bold text-rose-900 uppercase">
                {isEn ? 'Hearts' : 'Жизни'}
              </div>
            </div>

            <div className="p-3 bg-emerald-50/60 rounded-2xl border border-emerald-200">
              <div className="flex items-center justify-center gap-1 text-emerald-700 mb-0.5">
                <Calendar className="w-4 h-4 text-emerald-600" />
                <span className="text-xs font-black truncate">{lastActiveDate || 'Today'}</span>
              </div>
              <div className="text-[11px] font-bold text-emerald-900 uppercase">
                {isEn ? 'Last Active' : 'Активность'}
              </div>
            </div>
          </div>

          {/* Backup Import/Export Buttons */}
          <div className="pt-2 flex flex-col sm:flex-row items-center gap-3">
            <button
              onClick={handleExportBackup}
              className="w-full sm:w-auto px-4 py-2.5 bg-slate-900 hover:bg-slate-800 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition-all flex items-center justify-center gap-2 cursor-pointer"
            >
              <Download className="w-4 h-4" />
              <span>{isEn ? 'Export Progress (JSON)' : 'Экспорт прогресса (JSON)'}</span>
            </button>

            <label className="w-full sm:w-auto px-4 py-2.5 bg-white border-2 border-slate-200 hover:border-slate-300 active:scale-95 text-slate-800 font-bold text-xs rounded-xl shadow-xs transition-all flex items-center justify-center gap-2 cursor-pointer">
              <Upload className="w-4 h-4" />
              <span>{isEn ? 'Import Progress Backup' : 'Восстановить из файла'}</span>
              <input
                type="file"
                accept=".json,application/json"
                onChange={handleImportFile}
                className="hidden"
              />
            </label>
          </div>

          {importMessage && (
            <div
              className={`mt-3 p-3 rounded-xl text-xs font-bold flex items-center gap-2 animate-in fade-in ${
                importMessage.type === 'success'
                  ? 'bg-emerald-50 text-emerald-800 border border-emerald-200'
                  : 'bg-rose-50 text-rose-800 border border-rose-200'
              }`}
            >
              {importMessage.type === 'success' ? (
                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
              ) : (
                <AlertCircle className="w-4 h-4 text-rose-600 shrink-0" />
              )}
              <span>{importMessage.text}</span>
            </div>
          )}
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
                ? 'Clear all completed lesson records, streaks, and accumulated XP from local storage to test fresh from Day 1 (Streak: 1, XP: 0).'
                : 'Сбросить все отметки о пройденных днях, серию и очки опыта для повторного тестирования с чистого листа с Дня 1 (Серия: 1, XP: 0).'}
            </p>
          </div>
          <button
            onClick={handleResetProgress}
            className="px-4 py-2.5 bg-red-600 hover:bg-red-700 active:scale-95 text-white font-bold text-xs rounded-xl shadow-xs transition-all whitespace-nowrap cursor-pointer"
          >
            {isEn ? 'Reset All Progress' : 'Сбросить весь прогресс'}
          </button>
        </div>
      </div>
    </div>
  );
};
