import React from 'react';
import { AppProvider, useApp } from './context/AppContext';
import { Navbar } from './components/Navbar';
import { Sidebar } from './components/Sidebar';
import { BottomNav } from './components/BottomNav';
import { RoadmapView } from './components/RoadmapView';
import { LessonRunner } from './components/LessonRunner';
import { PhoneticsGym } from './components/PhoneticsGym';
import { CognatesExplorer } from './components/CognatesExplorer';
import { SettingsView } from './components/SettingsView';

const MainLayout: React.FC = () => {
  const { activeTab, selectedDay } = useApp();

  // If a lesson is actively running, render LessonRunner in focused full-view mode
  if (activeTab === 'lesson' && selectedDay) {
    return <LessonRunner />;
  }

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col text-slate-800">
      {/* Sticky Top Navigation */}
      <Navbar />

      {/* Main Body with Desktop Sidebar + Content Area */}
      <div className="flex-1 flex max-w-7xl w-full mx-auto">
        <Sidebar />

        <main className="flex-1 min-w-0">
          {activeTab === 'roadmap' && <RoadmapView />}
          {activeTab === 'phonetics' && <PhoneticsGym />}
          {activeTab === 'cognates' && <CognatesExplorer />}
          {activeTab === 'settings' && <SettingsView />}
        </main>
      </div>

      {/* Mobile Sticky Bottom Navigation */}
      <BottomNav />
    </div>
  );
};

export default function App() {
  return (
    <AppProvider>
      <MainLayout />
    </AppProvider>
  );
}
