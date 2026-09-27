import React from 'react';
import { Map, Activity, BookOpen, Settings } from 'lucide-react';
import { useApp } from '../context/AppContext';

export const BottomNav: React.FC = () => {
  const { activeTab, setActiveTab, uiLanguage } = useApp();

  const navItems = [
    {
      id: 'roadmap' as const,
      labelRu: 'Путь',
      labelEn: 'Path',
      icon: Map,
    },
    {
      id: 'phonetics' as const,
      labelRu: 'Фонетика',
      labelEn: 'Phonetics',
      icon: Activity,
    },
    {
      id: 'cognates' as const,
      labelRu: 'Корни',
      labelEn: 'Cognates',
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
    <nav className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-white border-t border-slate-200 px-3 py-1.5 flex items-center justify-around shadow-lg">
      {navItems.map((item) => {
        const Icon = item.icon;
        const isActive = activeTab === item.id;
        return (
          <button
            key={item.id}
            onClick={() => setActiveTab(item.id)}
            className={`flex flex-col items-center gap-1 py-1 px-3 rounded-xl transition-all ${
              isActive
                ? 'text-emerald-600 font-extrabold'
                : 'text-slate-500 font-medium hover:text-slate-800'
            }`}
          >
            <Icon className={`w-5 h-5 ${isActive ? 'stroke-[2.5px]' : 'stroke-2'}`} />
            <span className="text-[11px] leading-none">
              {uiLanguage === 'ru' ? item.labelRu : item.labelEn}
            </span>
          </button>
        );
      })}
    </nav>
  );
};
