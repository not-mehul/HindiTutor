import React, { useState } from 'react';
import {
  Flame,
  Heart,
  Zap,
  Globe,
  User,
  Volume2,
  VolumeX,
  X,
  ShieldAlert
} from 'lucide-react';
import { useApp } from '../context/AppContext';
import { sfx } from '../utils/audio';

export const Navbar: React.FC = () => {
  const {
    uiLanguage,
    setUiLanguage,
    learnerGender,
    setLearnerGender,
    streak,
    hearts,
    xp,
    soundEnabled,
    setSoundEnabled
  } = useApp();

  const [activeStatModal, setActiveStatModal] = useState<'streak' | 'xp' | 'hearts' | null>(null);
  const [showAuditorBanner, setShowAuditorBanner] = useState<boolean>(true);

  const isEn = uiLanguage === 'en';

  return (
    <>
      <header className="sticky top-0 z-40 bg-white border-b border-slate-200 px-4 py-2.5 shadow-xs">
        <div className="max-w-5xl mx-auto flex items-center justify-between">
          {/* Brand */}
          <div className="flex items-center gap-2">
            <span className="text-2xl select-none">🇮🇳</span>
            <div>
              <h1 className="font-extrabold text-slate-800 text-lg leading-tight tracking-tight">
                HindiTutor <span className="text-xs bg-emerald-100 text-emerald-800 font-semibold px-1.5 py-0.5 rounded-full ml-1">40 Days</span>
              </h1>
              <p className="text-[11px] text-slate-500 font-medium">
                {isEn ? 'Spoken Hindi for Russian Speakers (Auditor View)' : 'Разговорный хинди для русскоязычных'}
              </p>
            </div>
          </div>

          {/* Gamification Stats */}
          <div className="flex items-center gap-2 sm:gap-4">
            {/* Streak */}
            <button
              onClick={() => {
                sfx.playTap();
                setActiveStatModal('streak');
              }}
              className="flex items-center gap-1 bg-amber-50 hover:bg-amber-100 text-amber-700 px-2.5 py-1 rounded-xl text-xs font-bold border border-amber-200 cursor-pointer transition-all active:scale-95"
              title="Daily Streak"
            >
              <Flame className="w-4 h-4 text-amber-500 fill-amber-500" />
              <span>{streak}</span>
            </button>

            {/* XP */}
            <button
              onClick={() => {
                sfx.playTap();
                setActiveStatModal('xp');
              }}
              className="flex items-center gap-1 bg-blue-50 hover:bg-blue-100 text-blue-700 px-2.5 py-1 rounded-xl text-xs font-bold border border-blue-200 cursor-pointer transition-all active:scale-95"
              title="XP Points"
            >
              <Zap className="w-4 h-4 text-blue-500 fill-blue-500" />
              <span>{xp}</span>
            </button>

            {/* Hearts */}
            <button
              onClick={() => {
                sfx.playTap();
                setActiveStatModal('hearts');
              }}
              className="flex items-center gap-1 bg-rose-50 hover:bg-rose-100 text-rose-700 px-2.5 py-1 rounded-xl text-xs font-bold border border-rose-200 cursor-pointer transition-all active:scale-95"
              title="Hearts / Lives"
            >
              <Heart className="w-4 h-4 text-rose-500 fill-rose-500" />
              <span>{hearts}</span>
            </button>

            <div className="h-5 w-px bg-slate-200 hidden sm:block" />

            {/* Controls: Language Toggle (EN / RU) */}
            <button
              onClick={() => {
                sfx.playTap();
                setUiLanguage(uiLanguage === 'ru' ? 'en' : 'ru');
              }}
              className={`flex items-center gap-1.5 px-2.5 py-1 rounded-xl text-xs font-bold transition-all border cursor-pointer active:scale-95 ${
                uiLanguage === 'en'
                  ? 'bg-indigo-600 text-white border-indigo-700 shadow-xs'
                  : 'bg-slate-100 text-slate-700 border-slate-300 hover:bg-slate-200'
              }`}
              title={isEn ? 'Switch to Russian learner immersion mode' : 'Включить английский режим аудита'}
            >
              <Globe className="w-3.5 h-3.5" />
              <span>{uiLanguage === 'ru' ? 'RU 🇷🇺' : 'EN 🇬🇧 (Audit)'}</span>
            </button>

            {/* Gender Toggle (Female / Male) */}
            <button
              onClick={() => {
                sfx.playTap();
                setLearnerGender(learnerGender === 'f' ? 'm' : 'f');
              }}
              className="hidden md:flex items-center gap-1.5 px-2.5 py-1 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 border border-slate-300 hover:bg-slate-200 transition-all cursor-pointer active:scale-95"
              title="Toggle target grammatical agreement (feminine -tī / masculine -tā)"
            >
              <User className="w-3.5 h-3.5 text-slate-500" />
              <span>{learnerGender === 'f' ? '👩 Жен. (-tī)' : '👨 Муж. (-tā)'}</span>
            </button>

            {/* Audio toggle */}
            <button
              onClick={() => {
                setSoundEnabled(!soundEnabled);
                if (!soundEnabled) sfx.playTap();
              }}
              className="p-1.5 rounded-lg text-slate-500 hover:bg-slate-100 cursor-pointer"
              title="Toggle Sound Effects"
            >
              {soundEnabled ? <Volume2 className="w-4 h-4 text-emerald-600" /> : <VolumeX className="w-4 h-4 text-slate-400" />}
            </button>
          </div>
        </div>
      </header>

      {/* Auditor Mode Banner (when viewing in English) */}
      {isEn && showAuditorBanner && (
        <div className="bg-indigo-900 text-indigo-100 text-xs px-4 py-2 border-b border-indigo-800 flex items-center justify-between">
          <div className="max-w-5xl mx-auto w-full flex items-center justify-between gap-3">
            <div className="flex items-center gap-2">
              <ShieldAlert className="w-4 h-4 text-indigo-300 shrink-0" />
              <span>
                <strong>Auditor Mode Active:</strong> Prompts, hints, and grammatical explanations are displayed in English for curriculum inspection. The primary course targets Russian native speakers.
              </span>
            </div>
            <button
              onClick={() => setShowAuditorBanner(false)}
              className="text-indigo-300 hover:text-white p-0.5 rounded-md cursor-pointer shrink-0"
              title="Dismiss banner"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      )}

      {/* Gamification Info Modal */}
      {activeStatModal && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white max-w-sm w-full rounded-3xl p-6 shadow-2xl border border-slate-200 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2.5">
                {activeStatModal === 'streak' && (
                  <div className="w-10 h-10 rounded-2xl bg-amber-100 text-amber-600 flex items-center justify-center">
                    <Flame className="w-6 h-6 fill-amber-500 text-amber-500" />
                  </div>
                )}
                {activeStatModal === 'xp' && (
                  <div className="w-10 h-10 rounded-2xl bg-blue-100 text-blue-600 flex items-center justify-center">
                    <Zap className="w-6 h-6 fill-blue-500 text-blue-500" />
                  </div>
                )}
                {activeStatModal === 'hearts' && (
                  <div className="w-10 h-10 rounded-2xl bg-rose-100 text-rose-600 flex items-center justify-center">
                    <Heart className="w-6 h-6 fill-rose-500 text-rose-500" />
                  </div>
                )}
                <div>
                  <h3 className="font-black text-slate-800 text-base">
                    {activeStatModal === 'streak' && (isEn ? `${streak}-Day Streak` : `Ударный режим: ${streak} дня`)}
                    {activeStatModal === 'xp' && (isEn ? `${xp} Total XP` : `Опыт: ${xp} XP`)}
                    {activeStatModal === 'hearts' && (isEn ? `${hearts} Hearts Remaining` : `Энергия: ${hearts} сердец`)}
                  </h3>
                  <span className="text-[11px] font-bold uppercase text-slate-400">
                    {activeStatModal === 'streak' && (isEn ? 'Daily Habit' : 'Ежедневная привычка')}
                    {activeStatModal === 'xp' && (isEn ? 'Learning Progress' : 'Прогресс обучения')}
                    {activeStatModal === 'hearts' && (isEn ? 'Mistake Shield' : 'Запас ошибок')}
                  </span>
                </div>
              </div>
              <button
                onClick={() => setActiveStatModal(null)}
                className="p-1 rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-100 cursor-pointer"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <p className="text-xs text-slate-600 leading-relaxed mb-4">
              {activeStatModal === 'streak' && (
                isEn
                  ? 'Complete at least one 20-minute verbal session each day to keep your streak alive. Daily verbal practice is vital for cementing Hindi syntactic reflexes.'
                  : 'Занимайтесь хотя бы 20 минут в день, чтобы не прерывать серию. Ежедневная речевая практика закрепляет глагольное согласование и синтаксис SOV на уровне рефлексов.'
              )}
              {activeStatModal === 'xp' && (
                isEn
                  ? 'XP is earned by answering exercises correctly (+10 XP), completing full lessons (+50 XP), reviewing cognate flashcards (+5 XP), and passing phonetics calibration tests (+25 XP).'
                  : 'XP начисляется за правильные ответы (+10 XP), завершение уроков (+50 XP), повторение карточек индоевропейских корней (+5 XP) и аудирование в фонетическом зале (+25 XP).'
              )}
              {activeStatModal === 'hearts' && (
                isEn
                  ? 'Hearts protect you during drills. If you make a mistake, 1 heart is lost. When hearts reach 0, you can instantly refill them for free so your learning is never blocked!'
                  : 'Сердца защищают вас при выполнении упражнений. Ошибка отнимает 1 сердце. Если сердца закончатся, вы можете мгновенно восстановить их бесплатно, чтобы продолжить обучение!'
              )}
            </p>

            <button
              onClick={() => setActiveStatModal(null)}
              className="w-full py-2.5 bg-slate-900 hover:bg-black text-white font-extrabold text-xs rounded-xl cursor-pointer transition-all"
            >
              {isEn ? 'Got it' : 'Понятно'}
            </button>
          </div>
        </div>
      )}
    </>
  );
};
