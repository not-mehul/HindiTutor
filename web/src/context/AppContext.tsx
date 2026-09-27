import React, { createContext, useContext, useState } from 'react';
import type { UiLanguage, GenderType, DayLesson } from '../data/types';
import { HINDI_COURSE_BUNDLE } from '../data/courseBundle';

interface AppContextType {
  // Localization & Settings
  uiLanguage: UiLanguage;
  setUiLanguage: (lang: UiLanguage) => void;
  learnerGender: GenderType;
  setLearnerGender: (gender: GenderType) => void;
  showDevanagari: boolean;
  setShowDevanagari: (show: boolean) => void;
  soundEnabled: boolean;
  setSoundEnabled: (enabled: boolean) => void;

  // Gamification & Progress
  completedDays: number[];
  markDayCompleted: (day: number) => void;
  streak: number;
  setStreak: (streak: number) => void;
  hearts: number;
  xp: number;
  decrementHearts: () => void;
  resetHearts: () => void;
  addXp: (amount: number) => void;

  // Navigation
  activeTab: 'roadmap' | 'lesson' | 'phonetics' | 'cognates' | 'settings';
  setActiveTab: (tab: 'roadmap' | 'lesson' | 'phonetics' | 'cognates' | 'settings') => void;
  selectedDay: DayLesson | null;
  startLesson: (dayNumber: number) => void;
  closeLesson: () => void;

  // Bundle data
  courseBundle: typeof HINDI_COURSE_BUNDLE;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export const AppProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  // UI Language: 'ru' for student immersion, 'en' for instructor audit
  const [uiLanguage, setUiLanguageState] = useState<UiLanguage>(() => {
    return (localStorage.getItem('ht_ui_lang') as UiLanguage) || 'ru';
  });

  const setUiLanguage = (lang: UiLanguage) => {
    setUiLanguageState(lang);
    localStorage.setItem('ht_ui_lang', lang);
  };

  // Learner Gender default is female ('f') based on course curriculum design
  const [learnerGender, setLearnerGenderState] = useState<GenderType>(() => {
    return (localStorage.getItem('ht_gender') as GenderType) || 'f';
  });

  const setLearnerGender = (gender: GenderType) => {
    setLearnerGenderState(gender);
    localStorage.setItem('ht_gender', gender);
  };

  const [showDevanagari, setShowDevanagariState] = useState<boolean>(() => {
    return localStorage.getItem('ht_devanagari') !== 'false';
  });

  const setShowDevanagari = (show: boolean) => {
    setShowDevanagariState(show);
    localStorage.setItem('ht_devanagari', String(show));
  };

  const [soundEnabled, setSoundEnabledState] = useState<boolean>(true);
  const setSoundEnabled = (enabled: boolean) => {
    setSoundEnabledState(enabled);
  };

  // Gamification progress
  const [completedDays, setCompletedDays] = useState<number[]>(() => {
    try {
      const stored = localStorage.getItem('ht_completed');
      return stored ? JSON.parse(stored) : [];
    } catch {
      return [];
    }
  });

  const [streak, setStreakState] = useState<number>(() => {
    return parseInt(localStorage.getItem('ht_streak') || '3', 10);
  });

  const setStreak = (val: number) => {
    setStreakState(val);
    localStorage.setItem('ht_streak', String(val));
  };

  const [hearts, setHearts] = useState<number>(5);
  const [xp, setXp] = useState<number>(() => {
    return parseInt(localStorage.getItem('ht_xp') || '120', 10);
  });

  // Navigation
  const [activeTab, setActiveTab] = useState<'roadmap' | 'lesson' | 'phonetics' | 'cognates' | 'settings'>('roadmap');
  const [selectedDayNumber, setSelectedDayNumber] = useState<number | null>(null);

  const selectedDay = selectedDayNumber
    ? ((HINDI_COURSE_BUNDLE.days.find(d => d.day === selectedDayNumber) as unknown) as DayLesson) || null
    : null;

  const markDayCompleted = (day: number) => {
    if (!completedDays.includes(day)) {
      const updated = [...completedDays, day];
      setCompletedDays(updated);
      localStorage.setItem('ht_completed', JSON.stringify(updated));
    }
    const newXp = xp + 50;
    setXp(newXp);
    localStorage.setItem('ht_xp', String(newXp));
  };

  const addXp = (amount: number) => {
    const updated = xp + amount;
    setXp(updated);
    localStorage.setItem('ht_xp', String(updated));
  };

  const decrementHearts = () => {
    setHearts(prev => Math.max(0, prev - 1));
  };

  const resetHearts = () => {
    setHearts(5);
  };

  const startLesson = (dayNumber: number) => {
    setSelectedDayNumber(dayNumber);
    setActiveTab('lesson');
    resetHearts();
  };

  const closeLesson = () => {
    setSelectedDayNumber(null);
    setActiveTab('roadmap');
  };

  return (
    <AppContext.Provider
      value={{
        uiLanguage,
        setUiLanguage,
        learnerGender,
        setLearnerGender,
        showDevanagari,
        setShowDevanagari,
        soundEnabled,
        setSoundEnabled,
        completedDays,
        markDayCompleted,
        streak,
        setStreak,
        hearts,
        xp,
        decrementHearts,
        resetHearts,
        addXp,
        activeTab,
        setActiveTab,
        selectedDay,
        startLesson,
        closeLesson,
        courseBundle: HINDI_COURSE_BUNDLE,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useApp = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp must be used within an AppProvider');
  }
  return context;
};
