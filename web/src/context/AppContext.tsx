import React, { createContext, useContext, useState, useEffect } from 'react';
import type { UiLanguage, GenderType, DayLesson } from '../data/types';
import { HINDI_COURSE_BUNDLE } from '../data/courseBundle';

export interface AppBackupData {
  app: string;
  version: string;
  exportedAt: string;
  data: {
    completedDays: number[];
    completedDates: Record<number, string>;
    streak: number;
    lastActiveDate: string | null;
    xp: number;
    hearts: number;
    uiLanguage: UiLanguage;
    learnerGender: GenderType;
    showDevanagari: boolean;
    soundEnabled: boolean;
  };
}

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
  completedDates: Record<number, string>;
  markDayCompleted: (day: number) => void;
  streak: number;
  setStreak: (streak: number) => void;
  lastActiveDate: string | null;
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

  // Backup & Storage Management
  exportBackup: () => string;
  importBackup: (backupJson: string) => boolean;
  resetAllData: () => void;

  // Bundle data
  courseBundle: typeof HINDI_COURSE_BUNDLE;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

// Helper to get formatted local date string (YYYY-MM-DD)
const getTodayDateString = (): string => {
  const d = new Date();
  const year = d.getFullYear();
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
};

// Helper to calculate difference in calendar days between two YYYY-MM-DD strings
const getCalendarDayDifference = (earlierDateStr: string, laterDateStr: string): number => {
  try {
    const [y1, m1, d1] = earlierDateStr.split('-').map(Number);
    const [y2, m2, d2] = laterDateStr.split('-').map(Number);
    const date1 = new Date(y1, m1 - 1, d1);
    const date2 = new Date(y2, m2 - 1, d2);
    const diffTime = date2.getTime() - date1.getTime();
    return Math.round(diffTime / (1000 * 60 * 60 * 24));
  } catch {
    return 0;
  }
};

export const AppProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  // 1. UI Language: 'ru' for student immersion, 'en' for instructor audit
  const [uiLanguage, setUiLanguageState] = useState<UiLanguage>(() => {
    try {
      const stored = localStorage.getItem('ht_ui_lang');
      return (stored === 'en' || stored === 'ru') ? stored : 'ru';
    } catch {
      return 'ru';
    }
  });

  const setUiLanguage = (lang: UiLanguage) => {
    setUiLanguageState(lang);
    try { localStorage.setItem('ht_ui_lang', lang); } catch {}
  };

  // 2. Learner Gender default is female ('f') based on course curriculum design
  const [learnerGender, setLearnerGenderState] = useState<GenderType>(() => {
    try {
      const stored = localStorage.getItem('ht_gender');
      return (stored === 'f' || stored === 'm' || stored === 'both') ? stored : 'f';
    } catch {
      return 'f';
    }
  });

  const setLearnerGender = (gender: GenderType) => {
    setLearnerGenderState(gender);
    try { localStorage.setItem('ht_gender', gender); } catch {}
  };

  // 3. Devanagari script display toggle
  const [showDevanagari, setShowDevanagariState] = useState<boolean>(() => {
    try {
      return localStorage.getItem('ht_devanagari') !== 'false';
    } catch {
      return true;
    }
  });

  const setShowDevanagari = (show: boolean) => {
    setShowDevanagariState(show);
    try { localStorage.setItem('ht_devanagari', String(show)); } catch {}
  };

  // 4. Sound effects toggle
  const [soundEnabled, setSoundEnabledState] = useState<boolean>(() => {
    try {
      return localStorage.getItem('ht_sound') !== 'false';
    } catch {
      return true;
    }
  });

  const setSoundEnabled = (enabled: boolean) => {
    setSoundEnabledState(enabled);
    try { localStorage.setItem('ht_sound', String(enabled)); } catch {}
  };

  // 5. Completed Days array
  const [completedDays, setCompletedDays] = useState<number[]>(() => {
    try {
      const stored = localStorage.getItem('ht_completed');
      if (stored) {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed)) return parsed;
      }
      return [];
    } catch {
      return [];
    }
  });

  // 6. Completed Dates timestamp map: { [day: number]: string }
  const [completedDates, setCompletedDates] = useState<Record<number, string>>(() => {
    try {
      const stored = localStorage.getItem('ht_completed_dates');
      return stored ? JSON.parse(stored) : {};
    } catch {
      return {};
    }
  });

  // 7. Last Active Date (YYYY-MM-DD)
  const [lastActiveDate, setLastActiveDate] = useState<string | null>(() => {
    try {
      return localStorage.getItem('ht_last_active_date') || null;
    } catch {
      return null;
    }
  });

  // 8. Daily Streak: starts from 1 instead of 3
  const [streak, setStreakState] = useState<number>(() => {
    try {
      const stored = localStorage.getItem('ht_streak');
      const storedLastDate = localStorage.getItem('ht_last_active_date');
      const storedCompleted = localStorage.getItem('ht_completed');

      // If user had previous hardcoded '3' without activity, normalize to 1
      if (stored === '3' && !storedLastDate && (!storedCompleted || storedCompleted === '[]')) {
        localStorage.setItem('ht_streak', '1');
        return 1;
      }

      if (stored) {
        const parsed = parseInt(stored, 10);
        return isNaN(parsed) || parsed < 1 ? 1 : parsed;
      }

      // Default start streak is 1
      localStorage.setItem('ht_streak', '1');
      return 1;
    } catch {
      return 1;
    }
  });

  const setStreak = (val: number) => {
    const safeVal = Math.max(1, val);
    setStreakState(safeVal);
    try { localStorage.setItem('ht_streak', String(safeVal)); } catch {}
  };

  // 9. Check streak continuity on mount
  useEffect(() => {
    const today = getTodayDateString();
    if (!lastActiveDate) {
      setLastActiveDate(today);
      try { localStorage.setItem('ht_last_active_date', today); } catch {}
    } else {
      const dayDiff = getCalendarDayDifference(lastActiveDate, today);
      if (dayDiff > 1) {
        // Missed more than 1 day: reset streak to 1
        setStreakState(1);
        try { localStorage.setItem('ht_streak', '1'); } catch {}
      }
    }
  }, [lastActiveDate]);

  // 10. Hearts (0..5)
  const [hearts, setHeartsState] = useState<number>(() => {
    try {
      const stored = localStorage.getItem('ht_hearts');
      if (stored !== null) {
        const parsed = parseInt(stored, 10);
        return isNaN(parsed) ? 5 : Math.max(0, Math.min(5, parsed));
      }
      return 5;
    } catch {
      return 5;
    }
  });

  const decrementHearts = () => {
    setHeartsState(prev => {
      const next = Math.max(0, prev - 1);
      try { localStorage.setItem('ht_hearts', String(next)); } catch {}
      return next;
    });
  };

  const resetHearts = () => {
    setHeartsState(5);
    try { localStorage.setItem('ht_hearts', '5'); } catch {}
  };

  // 11. XP Points: start from 0 instead of 120
  const [xp, setXp] = useState<number>(() => {
    try {
      const stored = localStorage.getItem('ht_xp');
      if (stored !== null) {
        const parsed = parseInt(stored, 10);
        return isNaN(parsed) ? 0 : parsed;
      }
      // If completed days exist, award 50 XP per day
      const storedCompleted = localStorage.getItem('ht_completed');
      if (storedCompleted) {
        const parsedDays = JSON.parse(storedCompleted);
        if (Array.isArray(parsedDays) && parsedDays.length > 0) {
          return parsedDays.length * 50;
        }
      }
      return 0;
    } catch {
      return 0;
    }
  });

  const addXp = (amount: number) => {
    const updated = xp + amount;
    setXp(updated);
    try { localStorage.setItem('ht_xp', String(updated)); } catch {}
  };

  // 12. Active navigation tab
  const [activeTab, setActiveTabState] = useState<'roadmap' | 'lesson' | 'phonetics' | 'cognates' | 'settings'>(() => {
    try {
      const stored = localStorage.getItem('ht_active_tab');
      if (stored && ['roadmap', 'lesson', 'phonetics', 'cognates', 'settings'].includes(stored)) {
        return stored as any;
      }
      return 'roadmap';
    } catch {
      return 'roadmap';
    }
  });

  const setActiveTab = (tab: 'roadmap' | 'lesson' | 'phonetics' | 'cognates' | 'settings') => {
    setActiveTabState(tab);
    try { localStorage.setItem('ht_active_tab', tab); } catch {}
  };

  // 13. Selected day for lesson
  const [selectedDayNumber, setSelectedDayNumber] = useState<number | null>(() => {
    try {
      const stored = localStorage.getItem('ht_selected_day');
      return stored ? parseInt(stored, 10) : null;
    } catch {
      return null;
    }
  });

  const selectedDay = selectedDayNumber
    ? ((HINDI_COURSE_BUNDLE.days.find(d => d.day === selectedDayNumber) as unknown) as DayLesson) || null
    : null;

  // Mark Day Completed & advance streak
  const markDayCompleted = (day: number) => {
    const today = getTodayDateString();
    const storedLastDate = localStorage.getItem('ht_last_active_date');

    // 1. Update completed days list
    let updatedCompleted = completedDays;
    if (!completedDays.includes(day)) {
      updatedCompleted = [...completedDays, day].sort((a, b) => a - b);
      setCompletedDays(updatedCompleted);
      try { localStorage.setItem('ht_completed', JSON.stringify(updatedCompleted)); } catch {}
    }

    // 2. Save completed timestamp
    const updatedDates = {
      ...completedDates,
      [day]: new Date().toISOString()
    };
    setCompletedDates(updatedDates);
    try { localStorage.setItem('ht_completed_dates', JSON.stringify(updatedDates)); } catch {}

    // 3. Advance streak if consecutive day
    let nextStreak = streak;
    if (storedLastDate) {
      const dayDiff = getCalendarDayDifference(storedLastDate, today);
      if (dayDiff === 1) {
        // Consecutive calendar day: increment streak
        nextStreak = streak + 1;
      } else if (dayDiff === 0) {
        // Same day practice: preserve current streak (minimum 1)
        nextStreak = Math.max(1, streak);
      } else {
        // Missed days: restart streak at 1
        nextStreak = 1;
      }
    } else {
      nextStreak = 1;
    }

    setStreakState(nextStreak);
    setLastActiveDate(today);
    try {
      localStorage.setItem('ht_streak', String(nextStreak));
      localStorage.setItem('ht_last_active_date', today);
    } catch {}

    // 4. Award XP (+50 XP for completed session)
    const newXp = xp + 50;
    setXp(newXp);
    try { localStorage.setItem('ht_xp', String(newXp)); } catch {}
  };

  const startLesson = (dayNumber: number) => {
    setSelectedDayNumber(dayNumber);
    setActiveTabState('lesson');
    resetHearts();
    try {
      localStorage.setItem('ht_selected_day', String(dayNumber));
      localStorage.setItem('ht_active_tab', 'lesson');
    } catch {}
  };

  const closeLesson = () => {
    setSelectedDayNumber(null);
    setActiveTabState('roadmap');
    try {
      localStorage.removeItem('ht_selected_day');
      localStorage.removeItem('ht_lesson_progress');
      localStorage.setItem('ht_active_tab', 'roadmap');
    } catch {}
  };

  // 14. Export Backup JSON
  const exportBackup = (): string => {
    const backup: AppBackupData = {
      app: 'HindiTutor',
      version: '1.0',
      exportedAt: new Date().toISOString(),
      data: {
        completedDays,
        completedDates,
        streak,
        lastActiveDate: localStorage.getItem('ht_last_active_date') || getTodayDateString(),
        xp,
        hearts,
        uiLanguage,
        learnerGender,
        showDevanagari,
        soundEnabled,
      }
    };
    return JSON.stringify(backup, null, 2);
  };

  // 15. Import Backup JSON
  const importBackup = (backupJson: string): boolean => {
    try {
      const parsed = JSON.parse(backupJson);
      const data = parsed.data || parsed;

      if (Array.isArray(data.completedDays)) {
        setCompletedDays(data.completedDays);
        localStorage.setItem('ht_completed', JSON.stringify(data.completedDays));
      }
      if (data.completedDates && typeof data.completedDates === 'object') {
        setCompletedDates(data.completedDates);
        localStorage.setItem('ht_completed_dates', JSON.stringify(data.completedDates));
      }
      if (typeof data.streak === 'number') {
        const s = Math.max(1, data.streak);
        setStreakState(s);
        localStorage.setItem('ht_streak', String(s));
      }
      if (typeof data.lastActiveDate === 'string') {
        setLastActiveDate(data.lastActiveDate);
        localStorage.setItem('ht_last_active_date', data.lastActiveDate);
      }
      if (typeof data.xp === 'number') {
        setXp(data.xp);
        localStorage.setItem('ht_xp', String(data.xp));
      }
      if (typeof data.hearts === 'number') {
        const h = Math.max(0, Math.min(5, data.hearts));
        setHeartsState(h);
        localStorage.setItem('ht_hearts', String(h));
      }
      if (data.uiLanguage === 'ru' || data.uiLanguage === 'en') {
        setUiLanguageState(data.uiLanguage);
        localStorage.setItem('ht_ui_lang', data.uiLanguage);
      }
      if (data.learnerGender === 'f' || data.learnerGender === 'm' || data.learnerGender === 'both') {
        setLearnerGenderState(data.learnerGender);
        localStorage.setItem('ht_gender', data.learnerGender);
      }
      if (typeof data.showDevanagari === 'boolean') {
        setShowDevanagariState(data.showDevanagari);
        localStorage.setItem('ht_devanagari', String(data.showDevanagari));
      }
      if (typeof data.soundEnabled === 'boolean') {
        setSoundEnabledState(data.soundEnabled);
        localStorage.setItem('ht_sound', String(data.soundEnabled));
      }
      return true;
    } catch (err) {
      console.error('Failed to import backup JSON:', err);
      return false;
    }
  };

  // 16. Reset all user data cleanly
  const resetAllData = () => {
    const keysToRemove = [
      'ht_completed',
      'ht_completed_dates',
      'ht_xp',
      'ht_streak',
      'ht_last_active_date',
      'ht_hearts',
      'ht_lesson_progress',
      'ht_selected_day',
      'ht_active_tab',
    ];

    keysToRemove.forEach(k => {
      try { localStorage.removeItem(k); } catch {}
    });

    setCompletedDays([]);
    setCompletedDates({});
    setStreakState(1);
    setLastActiveDate(getTodayDateString());
    setXp(0);
    setHeartsState(5);
    setSelectedDayNumber(null);
    setActiveTabState('roadmap');
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
        completedDates,
        markDayCompleted,
        streak,
        setStreak,
        lastActiveDate,
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
        exportBackup,
        importBackup,
        resetAllData,
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
