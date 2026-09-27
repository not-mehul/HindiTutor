import React, { useState } from 'react';
import { useApp } from '../context/AppContext';
import {
  Volume2,
  Sparkles,
  AlertTriangle,
  HelpCircle,
  CheckCircle2,
  XCircle,
  Headphones,
  RotateCcw,
  Zap,
  ArrowRight
} from 'lucide-react';
import { speakHindi, sfx } from '../utils/audio';
import type { PhonemeCategory } from '../data/types';

export const PhoneticsGym: React.FC = () => {
  const { uiLanguage, showDevanagari, courseBundle, addXp, soundEnabled } = useApp();
  const guide = courseBundle.phoneticsGuide;
  const isEn = uiLanguage === 'en';

  const [activeTab, setActiveTab] = useState<'soundboard' | 'quiz'>('soundboard');
  const [activeCategoryIndex, setActiveCategoryIndex] = useState<number>(0);

  // Curated minimal pairs for interactive testing & quiz
  const interactiveMinimalPairs = [
    {
      id: 'pair-1',
      type: isEn ? 'Dental vs Retroflex' : 'Зубной vs Ретрофлексный',
      word1: { dev: 'ताल', iso: 'tāl', cyr: 'таал', meaningRu: 'ритм', meaningEn: 'musical rhythm' },
      word2: { dev: 'टाल', iso: 'ṭāl', cyr: 'т͟аал', meaningRu: 'откладывать / переносить', meaningEn: 'to postpone / evade' },
      tipRu: 'Сравните: "таал" язык плотно у зубов, "т͟аал" язык загнут глубоко к нёбу.',
      tipEn: 'Compare: "tāl" tongue presses flat against upper teeth, "ṭāl" tongue tip curls back to hard palate.'
    },
    {
      id: 'pair-2',
      type: isEn ? 'Unaspirated vs Aspirated' : 'Непридыхательный vs Придыхательный',
      word1: { dev: 'सात', iso: 'sāt', cyr: 'саат', meaningRu: 'семь (7)', meaningEn: 'seven (7)' },
      word2: { dev: 'साथ', iso: 'sāth', cyr: 'саатх', meaningRu: 'вместе / с', meaningEn: 'together / with' },
      tipRu: 'Тест с бумажкой: на "саат" лист неподвижен, на "саатх" отклоняется от резкого выдоха.',
      tipEn: 'Paper test: on "sāt" the paper strip does not move, on "sāth" it sharply flutters from chest breath.'
    },
    {
      id: 'pair-3',
      type: isEn ? 'Short vs Long Vowel (No Reduction)' : 'Краткий vs Долгий гласный (Без редукции)',
      word1: { dev: 'कम', iso: 'kam', cyr: 'кам', meaningRu: 'мало / меньше', meaningEn: 'less / little' },
      word2: { dev: 'काम', iso: 'kām', cyr: 'каам', meaningRu: 'работа / дело', meaningEn: 'work / chore' },
      tipRu: 'В русском "о/а" сокращаются. В хинди "каам" ровно в 2 раза дольше "кам".',
      tipEn: 'In Russian, unstressed vowels reduce. In Hindi, "kām" is held exactly twice as long as "kam".'
    },
    {
      id: 'pair-4',
      type: isEn ? 'Unvoiced Aspirated vs Voiced Aspirated' : 'Глухой vs Звонкий придыхательный',
      word1: { dev: 'फल', iso: 'phal', cyr: 'пхал', meaningRu: 'фрукт', meaningEn: 'fruit' },
      word2: { dev: 'पल', iso: 'pal', cyr: 'пал', meaningRu: 'миг / мгновение', meaningEn: 'moment / instant' },
      tipRu: 'Не путайте "phal" с русским "ф" (фа). Губы смыкаются полностью, затем мощный взрыв [п]+[х].',
      tipEn: 'Do not confuse "phal" with "f". Lips close completely into [p], followed by an explosive burst of breath.'
    },
    {
      id: 'pair-5',
      type: isEn ? 'Voiced Stop vs Voiced Aspirated' : 'Звонкий vs Звонкий придыхательный',
      word1: { dev: 'भाई', iso: 'bhāī', cyr: 'бхааии', meaningRu: 'брат', meaningEn: 'brother' },
      word2: { dev: 'बाई', iso: 'bāī', cyr: 'бааии', meaningRu: 'леди / женщина (вежл.)', meaningEn: 'lady / woman' },
      tipRu: 'В "bhāī" голосовые связки вибрируют одновременно с легочным выдохом.',
      tipEn: 'In "bhāī", vocal cords vibrate simultaneously with a deep pulmonary breath release.'
    }
  ];

  const activeCategory: PhonemeCategory =
    ((guide.phonemeCategories[activeCategoryIndex] as unknown) as PhonemeCategory) ||
    ((guide.phonemeCategories[0] as unknown) as PhonemeCategory);

  // Quiz State
  const [quizPairIdx, setQuizPairIdx] = useState<number>(0);
  const [quizSecretChoice, setQuizSecretChoice] = useState<'word1' | 'word2'>('word1');
  const [quizSelectedChoice, setQuizSelectedChoice] = useState<'word1' | 'word2' | null>(null);
  const [quizScore, setQuizScore] = useState<number>(0);
  const [quizCompleted, setQuizCompleted] = useState<boolean>(false);

  const startQuizRound = (index: number) => {
    const randomChoice: 'word1' | 'word2' = Math.random() > 0.5 ? 'word1' : 'word2';
    setQuizPairIdx(index);
    setQuizSecretChoice(randomChoice);
    setQuizSelectedChoice(null);

    // Play secret word
    const currentPair = interactiveMinimalPairs[index];
    const target = randomChoice === 'word1' ? currentPair.word1.dev : currentPair.word2.dev;
    setTimeout(() => {
      speakHindi(target);
    }, 200);
  };

  const handleStartQuiz = () => {
    setActiveTab('quiz');
    setQuizScore(0);
    setQuizCompleted(false);
    startQuizRound(0);
  };

  const handleQuizAnswer = (choice: 'word1' | 'word2') => {
    if (quizSelectedChoice) return;
    setQuizSelectedChoice(choice);
    const isCorrect = choice === quizSecretChoice;
    if (isCorrect) {
      if (soundEnabled) sfx.playSuccess();
      setQuizScore((prev) => prev + 1);
    } else {
      if (soundEnabled) sfx.playError();
    }
  };

  const handleNextQuizQuestion = () => {
    if (quizPairIdx + 1 < interactiveMinimalPairs.length) {
      startQuizRound(quizPairIdx + 1);
    } else {
      setQuizCompleted(true);
      addXp(25);
      if (soundEnabled) sfx.playFanfare();
    }
  };

  const currentQuizPair = interactiveMinimalPairs[quizPairIdx];
  const targetSecretDev = quizSecretChoice === 'word1' ? currentQuizPair.word1.dev : currentQuizPair.word2.dev;

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 pb-24 md:pb-12">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-amber-500 to-orange-500 rounded-3xl p-6 md:p-8 text-white shadow-lg mb-8">
        <div className="flex items-center gap-3 mb-2">
          <span className="p-2.5 bg-white/20 rounded-2xl backdrop-blur-md">
            <Sparkles className="w-6 h-6 text-yellow-200" />
          </span>
          <span className="text-xs uppercase tracking-wider font-extrabold bg-black/20 px-3 py-1 rounded-full">
            {isEn ? 'Sound Lab & Articulatory Gym' : 'Звуковая лаборатория и артикуляционный зал'}
          </span>
        </div>
        <h1 className="text-2xl md:text-3xl font-extrabold mb-2">
          {isEn ? guide.titleEn : guide.titleRu}
        </h1>
        <p className="text-amber-100 text-sm md:text-base max-w-3xl leading-relaxed">
          {isEn
            ? 'Designed specifically for Russian native speakers to calibrate retroflex curl, 4-way stop aspiration, and overcome automatic Russian vowel reduction (anti-akan’ye).'
            : 'Создан специально для носителей русского языка: тренируйте загибание кончика языка, 4-частные взрывные согласные и преодолевайте русское аканье для кристальной разборчивости речи.'}
        </p>

        {/* Tab Switcher: Soundboard vs Ear Calibration Quiz */}
        <div className="mt-6 flex flex-wrap gap-2">
          <button
            onClick={() => setActiveTab('soundboard')}
            className={`px-4 py-2 rounded-xl text-xs md:text-sm font-extrabold transition-all cursor-pointer ${
              activeTab === 'soundboard'
                ? 'bg-white text-amber-700 shadow-md scale-102'
                : 'bg-white/20 hover:bg-white/30 text-white'
            }`}
          >
            🔊 {isEn ? 'Phoneme Soundboard' : 'Звуковая таблица'}
          </button>
          <button
            onClick={handleStartQuiz}
            className={`px-4 py-2 rounded-xl text-xs md:text-sm font-extrabold transition-all cursor-pointer flex items-center gap-1.5 ${
              activeTab === 'quiz'
                ? 'bg-white text-amber-700 shadow-md scale-102'
                : 'bg-white/20 hover:bg-white/30 text-white'
            }`}
          >
            <Headphones className="w-4 h-4" />
            <span>{isEn ? 'Blind Ear Calibration Quiz' : 'Тренажер слуха (Слепой тест)'}</span>
          </button>
        </div>
      </div>

      {/* QUIZ MODE */}
      {activeTab === 'quiz' && (
        <div className="bg-white rounded-3xl border-2 border-amber-200 p-6 md:p-8 shadow-sm mb-12 animate-in fade-in duration-200">
          {!quizCompleted ? (
            <div className="max-w-xl mx-auto space-y-6">
              <div className="flex items-center justify-between pb-4 border-b border-slate-100">
                <span className="text-xs font-black uppercase tracking-wider text-amber-700 bg-amber-50 px-3 py-1 rounded-full">
                  {isEn ? 'Ear Calibration Test' : 'Калибровка слуха'} {quizPairIdx + 1} / {interactiveMinimalPairs.length}
                </span>
                <span className="text-xs font-extrabold text-slate-500">
                  {isEn ? 'Score:' : 'Счет:'} {quizScore}
                </span>
              </div>

              <div className="text-center">
                <h3 className="text-xl font-black text-slate-900 mb-1">
                  {isEn ? 'Which word do you hear?' : 'Какое слово вы слышите?'}
                </h3>
                <p className="text-xs text-slate-500">
                  {currentQuizPair.type}
                </p>

                {/* Big Mystery Speaker Button */}
                <div className="my-6 flex items-center justify-center gap-3">
                  <button
                    onClick={() => speakHindi(targetSecretDev)}
                    className="w-20 h-20 rounded-full bg-amber-500 hover:bg-amber-600 active:scale-95 text-white flex items-center justify-center shadow-lg transition-all cursor-pointer"
                    title="Play sound"
                  >
                    <Volume2 className="w-9 h-9" />
                  </button>
                  <button
                    onClick={() => speakHindi(targetSecretDev, 0.65)}
                    className="w-12 h-12 rounded-full bg-slate-100 hover:bg-slate-200 active:scale-95 text-slate-700 flex items-center justify-center shadow-xs transition-all cursor-pointer text-sm font-bold"
                    title="Slow speed (0.65x)"
                  >
                    🐢
                  </button>
                </div>
                <span className="text-xs text-slate-400">
                  {isEn ? 'Tap to listen again' : 'Нажмите, чтобы прослушать еще раз'}
                </span>
              </div>

              {/* The Two Choice Buttons */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                {/* Option 1 */}
                <button
                  onClick={() => handleQuizAnswer('word1')}
                  disabled={quizSelectedChoice !== null}
                  className={`p-4 rounded-2xl border-2 text-left font-bold transition-all cursor-pointer ${
                    quizSelectedChoice === null
                      ? 'border-slate-200 bg-slate-50/50 hover:border-amber-400 hover:bg-amber-50/20 active:scale-98'
                      : quizSecretChoice === 'word1'
                      ? 'border-emerald-500 bg-emerald-50 text-emerald-950 shadow-sm'
                      : quizSelectedChoice === 'word1'
                      ? 'border-rose-400 bg-rose-50 text-rose-950'
                      : 'border-slate-200 bg-white opacity-40'
                  }`}
                >
                  <div className="text-lg font-black">{currentQuizPair.word1.dev}</div>
                  <div className="text-sm font-bold text-slate-700">[{currentQuizPair.word1.cyr}] ({currentQuizPair.word1.iso})</div>
                  <div className="text-xs text-slate-500 mt-1">
                    {isEn ? currentQuizPair.word1.meaningEn : currentQuizPair.word1.meaningRu}
                  </div>
                </button>

                {/* Option 2 */}
                <button
                  onClick={() => handleQuizAnswer('word2')}
                  disabled={quizSelectedChoice !== null}
                  className={`p-4 rounded-2xl border-2 text-left font-bold transition-all cursor-pointer ${
                    quizSelectedChoice === null
                      ? 'border-slate-200 bg-slate-50/50 hover:border-amber-400 hover:bg-amber-50/20 active:scale-98'
                      : quizSecretChoice === 'word2'
                      ? 'border-emerald-500 bg-emerald-50 text-emerald-950 shadow-sm'
                      : quizSelectedChoice === 'word2'
                      ? 'border-rose-400 bg-rose-50 text-rose-950'
                      : 'border-slate-200 bg-white opacity-40'
                  }`}
                >
                  <div className="text-lg font-black">{currentQuizPair.word2.dev}</div>
                  <div className="text-sm font-bold text-slate-700">[{currentQuizPair.word2.cyr}] ({currentQuizPair.word2.iso})</div>
                  <div className="text-xs text-slate-500 mt-1">
                    {isEn ? currentQuizPair.word2.meaningEn : currentQuizPair.word2.meaningRu}
                  </div>
                </button>
              </div>

              {/* Feedback and Continue */}
              {quizSelectedChoice !== null && (
                <div className="p-4 rounded-2xl border bg-slate-50 space-y-3 animate-in fade-in">
                  <div className="flex items-center gap-2 font-black text-sm">
                    {quizSelectedChoice === quizSecretChoice ? (
                      <>
                        <CheckCircle2 className="w-5 h-5 text-emerald-600" />
                        <span className="text-emerald-800">
                          {isEn ? 'Correct! Sharp ear!' : 'Отлично! Слух калиброван верно.'}
                        </span>
                      </>
                    ) : (
                      <>
                        <XCircle className="w-5 h-5 text-rose-600" />
                        <span className="text-rose-800">
                          {isEn ? 'Not quite!' : 'Не совсем!'}
                        </span>
                      </>
                    )}
                  </div>
                  <p className="text-xs text-slate-600 leading-relaxed">
                    {isEn ? currentQuizPair.tipEn : currentQuizPair.tipRu}
                  </p>
                  <button
                    onClick={handleNextQuizQuestion}
                    className="w-full btn-duo-green py-3 rounded-xl text-white font-extrabold text-xs shadow-md cursor-pointer flex items-center justify-center gap-1.5"
                  >
                    <span>{isEn ? 'Next Pair' : 'Следующая пара'}</span>
                    <ArrowRight className="w-4 h-4" />
                  </button>
                </div>
              )}
            </div>
          ) : (
            <div className="text-center py-8 space-y-4 max-w-sm mx-auto">
              <div className="w-16 h-16 bg-amber-100 text-amber-700 rounded-full flex items-center justify-center mx-auto">
                <Sparkles className="w-8 h-8" />
              </div>
              <h3 className="text-2xl font-black text-slate-900">
                {isEn ? 'Ear Calibration Complete!' : 'Калибровка слуха завершена!'}
              </h3>
              <p className="text-sm text-slate-600">
                {isEn ? `You scored ${quizScore} out of ${interactiveMinimalPairs.length}.` : `Ваш результат: ${quizScore} из ${interactiveMinimalPairs.length}.`}
              </p>
              <div className="bg-amber-50 border border-amber-200 py-2.5 px-4 rounded-xl font-bold text-amber-800 text-sm flex items-center justify-center gap-1.5">
                <Zap className="w-4 h-4 text-amber-600 fill-amber-600" />
                <span>+25 XP</span>
              </div>
              <div className="pt-2 flex gap-2">
                <button
                  onClick={handleStartQuiz}
                  className="flex-1 py-3 px-4 rounded-xl border-2 border-slate-200 font-extrabold text-xs hover:bg-slate-50 cursor-pointer flex items-center justify-center gap-1"
                >
                  <RotateCcw className="w-4 h-4" />
                  <span>{isEn ? 'Try Again' : 'Пройти снова'}</span>
                </button>
                <button
                  onClick={() => setActiveTab('soundboard')}
                  className="flex-1 btn-duo-green py-3 px-4 rounded-xl text-white font-extrabold text-xs shadow-md cursor-pointer"
                >
                  {isEn ? 'Back to Soundboard' : 'К таблице звуков'}
                </button>
              </div>
            </div>
          )}
        </div>
      )}

      {/* SOUNDBOARD MODE */}
      {activeTab === 'soundboard' && (
        <>
          {/* Core Principles Carousel/Grid */}
          <div className="mb-10">
            <h2 className="text-xl font-bold text-gray-900 mb-4 flex items-center gap-2">
              <span>🎯</span>
              <span>{isEn ? '5 Core Contrastive Principles (RU ↔ HI)' : '5 ключевых принципов артикуляции'}</span>
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {guide.corePrinciples.map((principle, idx) => (
                <div key={idx} className="bg-white p-5 rounded-2xl border border-gray-100 shadow-xs hover:shadow-md transition-shadow">
                  <div className="w-8 h-8 rounded-full bg-amber-100 text-amber-700 font-bold flex items-center justify-center text-sm mb-3">
                    {idx + 1}
                  </div>
                  <h3 className="font-bold text-gray-900 text-base mb-2">
                    {principle.nameRu}
                  </h3>
                  <p className="text-gray-600 text-xs md:text-sm leading-relaxed">
                    {principle.descriptionRu}
                  </p>
                </div>
              ))}
            </div>
          </div>

          {/* Interactive Category Soundboard */}
          <div className="mb-12 bg-white rounded-3xl border border-gray-100 p-6 md:p-8 shadow-xs">
            <h2 className="text-xl font-bold text-gray-900 mb-2 flex items-center gap-2">
              <span>🔊</span>
              <span>{isEn ? 'Phoneme Soundboard & Mouth Positions' : 'Интерактивный звуковой пульт и механика рта'}</span>
            </h2>
            <p className="text-gray-500 text-sm mb-6">
              {isEn
                ? 'Select a consonant class to inspect physical tongue placement, Russian contrast tips, and listen to authentic native pronunciation.'
                : 'Выберите категорию согласных, чтобы изучить положение языка, русские риски интерференции и прослушать эталонное звучание.'}
            </p>

            {/* Category Pills */}
            <div className="flex gap-2 overflow-x-auto pb-3 mb-6 scrollbar-none">
              {guide.phonemeCategories.map((cat, idx) => {
                const isActive = idx === activeCategoryIndex;
                return (
                  <button
                    key={idx}
                    onClick={() => setActiveCategoryIndex(idx)}
                    className={`px-4 py-2.5 rounded-2xl font-bold text-xs md:text-sm whitespace-nowrap transition-all duration-150 cursor-pointer ${
                      isActive
                        ? 'bg-amber-500 text-white shadow-md shadow-amber-500/20 translate-y-[-1px]'
                        : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                    }`}
                  >
                    {cat.categoryRu}
                  </button>
                );
              })}
            </div>

            {/* Selected Category Details Card */}
            {activeCategory && (
              <div className="bg-amber-50/50 rounded-2xl p-6 border border-amber-100/70">
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6 pb-6 border-b border-amber-200/50">
                  <div>
                    <span className="text-xs uppercase font-extrabold text-amber-600 tracking-wider">
                      {isEn ? 'Selected Category' : 'Текущая группа'}
                    </span>
                    <h3 className="text-xl font-extrabold text-gray-900 mt-0.5">
                      {activeCategory.categoryRu}
                    </h3>
                  </div>

                  {/* Phoneme chips with speech */}
                  <div className="flex flex-wrap gap-2">
                    {activeCategory.devanagari.map((dev, pIdx) => {
                      const iso = activeCategory.iso[pIdx] || '';
                      const cyr = activeCategory.cyrillicPhonetic[pIdx] || '';
                      return (
                        <div key={pIdx} className="flex items-center gap-1 bg-white rounded-xl border border-amber-200 p-1 shadow-xs">
                          <button
                            onClick={() => speakHindi(dev)}
                            className="flex items-center gap-1.5 px-2.5 py-1.5 hover:bg-amber-50 rounded-lg active:scale-95 transition-all cursor-pointer"
                            title={isEn ? `Listen to ${iso}` : `Послушать ${cyr}`}
                          >
                            {showDevanagari && (
                              <span className="text-lg font-bold text-amber-600 font-hindi">{dev}</span>
                            )}
                            <div className="flex flex-col items-start leading-none">
                              <span className="font-mono font-bold text-xs text-gray-800">[{cyr}]</span>
                              <span className="text-[10px] text-gray-500 font-mono">{iso}</span>
                            </div>
                            <Volume2 className="w-3.5 h-3.5 text-amber-600 ml-1" />
                          </button>
                          <button
                            onClick={() => speakHindi(dev, 0.65)}
                            className="p-1.5 text-slate-500 hover:text-slate-800 text-[11px] font-bold rounded-md hover:bg-slate-100 cursor-pointer"
                            title="Slow speed (0.65x)"
                          >
                            🐢
                          </button>
                        </div>
                      );
                    })}
                  </div>
                </div>

                {/* Mechanics & Warnings */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="bg-white p-4 rounded-xl border border-amber-200/60 shadow-xs">
                    <div className="flex items-center gap-2 text-amber-700 font-bold text-xs uppercase mb-1.5">
                      <CheckCircle2 className="w-4 h-4" />
                      <span>{isEn ? 'Articulatory Mechanism' : 'Артикуляционная механика'}</span>
                    </div>
                    <p className="text-gray-700 text-xs md:text-sm leading-relaxed">
                      {activeCategory.articulatoryMechanism}
                    </p>
                  </div>

                  {activeCategory.russianInterferenceWarning && (
                    <div className="bg-red-50 p-4 rounded-xl border border-red-200 shadow-xs">
                      <div className="flex items-center gap-2 text-red-700 font-bold text-xs uppercase mb-1.5">
                        <AlertTriangle className="w-4 h-4" />
                        <span>{isEn ? 'Russian Interference Warning' : 'Риск русской ошибки'}</span>
                      </div>
                      <p className="text-red-900 text-xs md:text-sm leading-relaxed">
                        {activeCategory.russianInterferenceWarning}
                      </p>
                    </div>
                  )}

                  {activeCategory.tactileDrill && (
                    <div className="bg-white p-4 rounded-xl border border-emerald-200 shadow-xs md:col-span-2">
                      <div className="flex items-center gap-2 text-emerald-700 font-bold text-xs uppercase mb-1.5">
                        <Sparkles className="w-4 h-4" />
                        <span>{isEn ? 'Tactile Drill (Physical Biofeedback)' : 'Тактильное упражнение'}</span>
                      </div>
                      <p className="text-emerald-950 text-xs md:text-sm leading-relaxed">
                        {activeCategory.tactileDrill}
                      </p>
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>

          {/* Minimal Pairs Sound Lab */}
          <div>
            <div className="flex items-center justify-between mb-4">
              <div>
                <h2 className="text-xl font-bold text-gray-900 flex items-center gap-2">
                  <span>⚖️</span>
                  <span>{isEn ? 'Minimal Pairs Drill (Ear Calibration)' : 'Калибровка слуха: Минимальные пары'}</span>
                </h2>
                <p className="text-gray-500 text-xs md:text-sm mt-0.5">
                  {isEn
                    ? 'Listen back-to-back to hear how subtle tongue shifts or breath puffs completely alter Hindi word meanings.'
                    : 'Слушайте пары подряд, чтобы на слух отличать критичные для смысла хинди различия.'}
                </p>
              </div>
            </div>

            <div className="space-y-4">
              {interactiveMinimalPairs.map((pair) => (
                <div
                  key={pair.id}
                  className="bg-white rounded-2xl border border-gray-100 p-5 shadow-xs hover:border-amber-200 transition-all"
                >
                  <div className="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <span className="text-xs font-bold text-amber-700 bg-amber-50 px-2.5 py-1 rounded-md">
                      {pair.type}
                    </span>
                    <span className="text-xs text-gray-400">
                      {isEn ? 'Listen normal or slow (🐢)' : 'Озвучка в обычном или замедленном (🐢) темпе'}
                    </span>
                  </div>

                  {/* The Two Opposing Words */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-3">
                    {/* Word 1 */}
                    <div className="flex items-center justify-between p-3.5 rounded-xl border-2 border-gray-200 hover:border-amber-400 bg-gray-50/50 hover:bg-amber-50/20 text-left transition-all">
                      <div className="flex items-center gap-3">
                        {showDevanagari && (
                          <span className="text-xl font-bold text-gray-800 font-hindi">{pair.word1.dev}</span>
                        )}
                        <div>
                          <div className="font-bold text-gray-900 text-sm">
                            [{pair.word1.cyr}] <span className="text-xs text-gray-500 font-mono">({pair.word1.iso})</span>
                          </div>
                          <div className="text-xs text-gray-600">
                            {isEn ? pair.word1.meaningEn : pair.word1.meaningRu}
                          </div>
                        </div>
                      </div>
                      <div className="flex items-center gap-1 shrink-0">
                        <button
                          onClick={() => speakHindi(pair.word1.dev)}
                          className="p-1.5 rounded-lg hover:bg-amber-100 text-amber-600 active:scale-95 transition-all cursor-pointer"
                          title="Normal speed"
                        >
                          <Volume2 className="w-4 h-4" />
                        </button>
                        <button
                          onClick={() => speakHindi(pair.word1.dev, 0.65)}
                          className="p-1 rounded-md hover:bg-slate-200 text-slate-600 text-xs font-bold active:scale-95 transition-all cursor-pointer"
                          title="Slow speed (0.65x)"
                        >
                          🐢
                        </button>
                      </div>
                    </div>

                    {/* Word 2 */}
                    <div className="flex items-center justify-between p-3.5 rounded-xl border-2 border-gray-200 hover:border-amber-400 bg-gray-50/50 hover:bg-amber-50/20 text-left transition-all">
                      <div className="flex items-center gap-3">
                        {showDevanagari && (
                          <span className="text-xl font-bold text-gray-800 font-hindi">{pair.word2.dev}</span>
                        )}
                        <div>
                          <div className="font-bold text-gray-900 text-sm">
                            [{pair.word2.cyr}] <span className="text-xs text-gray-500 font-mono">({pair.word2.iso})</span>
                          </div>
                          <div className="text-xs text-gray-600">
                            {isEn ? pair.word2.meaningEn : pair.word2.meaningRu}
                          </div>
                        </div>
                      </div>
                      <div className="flex items-center gap-1 shrink-0">
                        <button
                          onClick={() => speakHindi(pair.word2.dev)}
                          className="p-1.5 rounded-lg hover:bg-amber-100 text-amber-600 active:scale-95 transition-all cursor-pointer"
                          title="Normal speed"
                        >
                          <Volume2 className="w-4 h-4" />
                        </button>
                        <button
                          onClick={() => speakHindi(pair.word2.dev, 0.65)}
                          className="p-1 rounded-md hover:bg-slate-200 text-slate-600 text-xs font-bold active:scale-95 transition-all cursor-pointer"
                          title="Slow speed (0.65x)"
                        >
                          🐢
                        </button>
                      </div>
                    </div>
                  </div>

                  {/* Explanatory Tip */}
                  <div className="bg-gray-50 rounded-xl p-3 flex items-start gap-2 text-xs text-gray-600">
                    <HelpCircle className="w-4 h-4 text-amber-500 flex-shrink-0 mt-0.5" />
                    <span>{isEn ? pair.tipEn : pair.tipRu}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  );
};
