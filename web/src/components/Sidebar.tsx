import React from 'react';
import { Map, Activity, BookOpen, Settings, User } from 'lucide-react';
import { useApp } from '../context/AppContext';

export const Sidebar: React.FC = () => {
  const { activeTab, setActiveTab, uiLanguage, learnerGender, setLearnerGender } = useApp();

  const navItems = [
    {
      id: 'roadmap' as const,
      labelRu: 'Учебный путь',
      labelEn: 'Learning Path',
      icon: Map,
    },
    {
      id: 'phonetics' as const,
      labelRu: 'Фонетический зал',
      labelEn: 'Phonetics Gym',
      icon: Activity,
    },
    {
      id: 'cognates' as const,
      labelRu: 'Индоевропейские корни',
      labelEn: 'PIE Cognates',
      icon: BookOpen,
    },
    {
      id: 'settings' as const,
      labelRu: 'Настройки',
      labelEn: 'Settings',
      icon: Settings,
    },
  ];

  return (
    <aside className="hidden md:flex flex-col w-64 bg-white border-r border-slate-200 min-h-[calc(100vh-61px)] p-4 shrink-0">
      <div className="space-y-1.5 flex-1">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`w-full flex items-center gap-3 px-3.5 py-3 rounded-2xl font-bold text-sm transition-all ${
                isActive
                  ? 'bg-emerald-50 text-emerald-700 border-2 border-emerald-500 shadow-xs'
                  : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900 border-2 border-transparent'
              }`}
            >
              <Icon className={`w-5 h-5 ${isActive ? 'text-emerald-600' : 'text-slate-400'}`} />
              <span>{uiLanguage === 'ru' ? item.labelRu : item.labelEn}</span>
            </button>
          );
        })}
      </div>

      {/* Gender Profile Box */}
      <div className="mt-auto bg-slate-50 border border-slate-200 rounded-2xl p-3.5 text-xs">
        <div className="flex items-center justify-between mb-2">
          <span className="font-bold text-slate-700 flex items-center gap-1.5">
            <User className="w-3.5 h-3.5 text-slate-500" />
            {uiLanguage === 'ru' ? 'Род говорящего' : 'Learner Gender'}
          </span>
          <span className="font-extrabold text-emerald-600">
            {learnerGender === 'f' ? '-tī' : '-tā'}
          </span>
        </div>
        <div className="grid grid-cols-2 gap-1.5 bg-slate-200/70 p-1 rounded-xl">
          <button
            onClick={() => setLearnerGender('f')}
            className={`py-1 rounded-lg font-bold text-center transition-all ${
              learnerGender === 'f'
                ? 'bg-white text-emerald-800 shadow-xs'
                : 'text-slate-600 hover:text-slate-800'
            }`}
          >
            {uiLanguage === 'ru' ? 'Женский' : 'Female'}
          </button>
          <button
            onClick={() => setLearnerGender('m')}
            className={`py-1 rounded-lg font-bold text-center transition-all ${
              learnerGender === 'm'
                ? 'bg-white text-emerald-800 shadow-xs'
                : 'text-slate-600 hover:text-slate-800'
            }`}
          >
            {uiLanguage === 'ru' ? 'Мужской' : 'Male'}
          </button>
        </div>
        <p className="mt-2 text-[10px] text-slate-500 leading-tight">
          {uiLanguage === 'ru'
            ? 'Адаптирует глагольные окончания (Main boltī hū̃ / boltā hū̃)'
            : 'Controls 1st-person verb agreement (-tī hū̃ vs -tā hū̃)'}
        </p>
      </div>
    </aside>
  );
};
