import React, { useState, useMemo, useEffect } from 'react';
import { useApp } from '../context/AppContext';
import {
  Search,
  Volume2,
  Sparkles,
  BookOpen,
  Compass,
  ArrowRight,
  RotateCw,
  Shuffle,
  CheckCircle2,
  HelpCircle,
  Trophy,
  Layers,
  Grid
} from 'lucide-react';
import confetti from 'canvas-confetti';
import { speakHindi, sfx } from '../utils/audio';
import type { CognateItem } from '../data/types';

export const CognatesExplorer: React.FC = () => {
  const { uiLanguage, showDevanagari, courseBundle, addXp } = useApp();
  const cognatesData = courseBundle.cognatesIndex;
  const isEn = uiLanguage === 'en';

  // Navigation mode: 'grid' (dictionary) or 'flashcards' (spaced review)
  const [viewMode, setViewMode] = useState<'grid' | 'flashcards'>('grid');

  // Search & Filter state
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedField, setSelectedField] = useState<string>('all');

  // Flashcard Deck State
  const [cardIndex, setCardIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [deck, setDeck] = useState<CognateItem[]>([]);
  const [masteredIds, setMasteredIds] = useState<Set<string>>(new Set());
  const [sessionCompleted, setSessionCompleted] = useState(false);

  const allCognates: readonly CognateItem[] = useMemo(() => {
    return (cognatesData.cognates as unknown) as readonly CognateItem[];
  }, [cognatesData]);

  // Extract unique semantic fields
  const semanticFields = useMemo(() => {
    const fields = new Set<string>();
    allCognates.forEach(c => {
      if (c.semanticFieldRu) fields.add(c.semanticFieldRu);
    });
    return Array.from(fields);
  }, [allCognates]);

  // Filter cognates for Grid view
  const filteredCognates = useMemo(() => {
    return allCognates.filter(item => {
      const matchesField = selectedField === 'all' || item.semanticFieldRu === selectedField;
      const q = searchQuery.toLowerCase().trim();
      if (!q) return matchesField;

      const matchesSearch =
        item.russianWord.toLowerCase().includes(q) ||
        item.hindiWordIso.toLowerCase().includes(q) ||
        item.hindiPhoneticCyrillic.toLowerCase().includes(q) ||
        (item.hindiDevanagari && item.hindiDevanagari.includes(q)) ||
        item.pieRoot.toLowerCase().includes(q) ||
        (item.semanticFieldRu && item.semanticFieldRu.toLowerCase().includes(q));

      return Boolean(matchesField && matchesSearch);
    });
  }, [allCognates, searchQuery, selectedField]);

  // Initialize or re-filter flashcard deck whenever selectedField changes or mode switches to flashcards
  useEffect(() => {
    const pool = allCognates.filter(
      item => selectedField === 'all' || item.semanticFieldRu === selectedField
    );
    setDeck([...pool]);
    setCardIndex(0);
    setIsFlipped(false);
    setSessionCompleted(false);
  }, [allCognates, selectedField, viewMode]);

  // Shuffle flashcard deck
  const handleShuffleDeck = () => {
    sfx.playTap();
    const shuffled = [...deck].sort(() => Math.random() - 0.5);
    setDeck(shuffled);
    setCardIndex(0);
    setIsFlipped(false);
    setSessionCompleted(false);
  };

  // Flip active flashcard
  const handleFlip = () => {
    sfx.playTap();
    const nextFlipped = !isFlipped;
    setIsFlipped(nextFlipped);

    // Speak Hindi target when flipped to the back
    if (nextFlipped && deck[cardIndex]) {
      const target = deck[cardIndex].hindiDevanagari || deck[cardIndex].hindiWordIso;
      speakHindi(target, 1.0);
    }
  };

  // Flashcard answer actions
  const handleNextCard = (mastered: boolean) => {
    const currentCard = deck[cardIndex];
    if (!currentCard) return;

    if (mastered) {
      sfx.playSuccess();
      addXp(5);
      setMasteredIds(prev => new Set(prev).add(currentCard.pieRoot + currentCard.russianWord));
    } else {
      sfx.playTap();
    }

    if (cardIndex + 1 < deck.length) {
      setCardIndex(prev => prev + 1);
      setIsFlipped(false);
    } else {
      // Completed all cards in current deck!
      setSessionCompleted(true);
      confetti({
        particleCount: 80,
        spread: 70,
        origin: { y: 0.6 }
      });
      sfx.playComplete();
    }
  };

  const currentCard = deck[cardIndex];

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 pb-24 md:pb-12">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-emerald-600 to-teal-600 rounded-3xl p-6 md:p-8 text-white shadow-lg mb-8">
        <div className="flex items-center justify-between gap-4 flex-wrap mb-2">
          <div className="flex items-center gap-3">
            <span className="p-2.5 bg-white/20 rounded-2xl backdrop-blur-md">
              <Compass className="w-6 h-6 text-teal-200" />
            </span>
            <span className="text-xs uppercase tracking-wider font-extrabold bg-black/20 px-3 py-1 rounded-full">
              {isEn ? 'Indo-European Cognate Bridge' : 'Праиндоевропейский лексический мост'}
            </span>
          </div>

          {/* Mode Switcher Tabs */}
          <div className="bg-black/25 p-1 rounded-2xl flex items-center gap-1 backdrop-blur-md border border-white/10">
            <button
              onClick={() => {
                sfx.playTap();
                setViewMode('grid');
              }}
              className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs font-black transition-all ${
                viewMode === 'grid'
                  ? 'bg-white text-emerald-800 shadow-sm'
                  : 'text-white/80 hover:text-white'
              }`}
            >
              <Grid className="w-3.5 h-3.5" />
              <span>{isEn ? 'Dictionary Grid' : 'Словарь'}</span>
            </button>
            <button
              onClick={() => {
                sfx.playTap();
                setViewMode('flashcards');
              }}
              className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs font-black transition-all ${
                viewMode === 'flashcards'
                  ? 'bg-white text-emerald-800 shadow-sm'
                  : 'text-white/80 hover:text-white'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              <span>{isEn ? 'Flashcard Gym' : 'Карточки'}</span>
            </button>
          </div>
        </div>

        <h1 className="text-2xl md:text-3xl font-extrabold mb-2">
          {isEn ? cognatesData.titleEn : cognatesData.titleRu}
        </h1>
        <p className="text-emerald-100 text-sm md:text-base max-w-3xl leading-relaxed">
          {isEn
            ? 'Russian and Hindi both descend from Proto-Indo-European (PIE). Russian speakers already know hundreds of Hindi root words through deep genetic linguistic heritage.'
            : cognatesData.descriptionRu}
        </p>
      </div>

      {/* Memory Advantage Pedagogical Card */}
      <div className="bg-emerald-50 rounded-2xl border border-emerald-100 p-5 mb-8 flex flex-col md:flex-row items-center gap-4">
        <div className="w-12 h-12 rounded-2xl bg-emerald-500 text-white flex items-center justify-center flex-shrink-0 shadow-md">
          <Sparkles className="w-6 h-6" />
        </div>
        <div>
          <h2 className="font-extrabold text-gray-900 text-base">
            {isEn ? 'The 5,000-Year-Old Secret of Fast Memorization' : 'Секрет мгновенного запоминания корней'}
          </h2>
          <p className="text-emerald-950 text-xs md:text-sm mt-0.5 leading-relaxed">
            {isEn
              ? 'Instead of rote memorizing abstract sounds, Russian learners can anchor Hindi vocabulary directly to native Russian cognates (e.g., дверь → dvār, огонь → agni, два → do, три → tīn, живой → jīv).'
              : 'Вместо механической зубрежки привязывайте слова хинди к их прямым русским родственникам. Общий корень делает лексику интуитивно понятной с первой секунды.'}
          </p>
        </div>
      </div>

      {/* ==================== FLASHCARDS MODE ==================== */}
      {viewMode === 'flashcards' && (
        <div className="space-y-6">
          {/* Deck Controls Header */}
          <div className="bg-white rounded-2xl border border-gray-200 p-4 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-xs">
            {/* Category Filter */}
            <div className="flex items-center gap-2 overflow-x-auto w-full sm:w-auto pb-1 sm:pb-0 scrollbar-none">
              <span className="text-xs font-bold text-gray-400 shrink-0">
                {isEn ? 'Topic:' : 'Тема:'}
              </span>
              <button
                onClick={() => setSelectedField('all')}
                className={`px-3 py-1 rounded-xl text-xs font-bold transition-all shrink-0 ${
                  selectedField === 'all'
                    ? 'bg-emerald-600 text-white shadow-xs'
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                }`}
              >
                {isEn ? 'All' : 'Все'} ({allCognates.length})
              </button>
              {semanticFields.map((field, idx) => (
                <button
                  key={idx}
                  onClick={() => setSelectedField(field)}
                  className={`px-3 py-1 rounded-xl text-xs font-bold transition-all shrink-0 ${
                    selectedField === field
                      ? 'bg-emerald-600 text-white shadow-xs'
                      : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                  }`}
                >
                  {field}
                </button>
              ))}
            </div>

            {/* Shuffle and Counter */}
            <div className="flex items-center gap-3 shrink-0">
              <button
                onClick={handleShuffleDeck}
                className="flex items-center gap-1.5 px-3 py-1.5 bg-gray-100 hover:bg-gray-200 active:scale-95 rounded-xl text-xs font-bold text-gray-700 transition-all cursor-pointer"
                title={isEn ? 'Shuffle flashcard deck' : 'Перемешать колоду'}
              >
                <Shuffle className="w-3.5 h-3.5 text-gray-500" />
                <span>{isEn ? 'Shuffle' : 'Перемешать'}</span>
              </button>
              <span className="text-xs font-extrabold text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-xl">
                {deck.length > 0 ? `${cardIndex + 1} / ${deck.length}` : '0 / 0'}
              </span>
            </div>
          </div>

          {/* Progress bar */}
          {deck.length > 0 && !sessionCompleted && (
            <div className="w-full bg-gray-100 h-2 rounded-full overflow-hidden border border-gray-200">
              <div
                className="bg-emerald-500 h-full transition-all duration-300"
                style={{ width: `${((cardIndex + 1) / deck.length) * 100}%` }}
              />
            </div>
          )}

          {/* Flashcard Main Display */}
          {!sessionCompleted && currentCard ? (
            <div className="perspective-1000 max-w-xl mx-auto">
              <div
                onClick={handleFlip}
                className={`relative w-full min-h-[340px] bg-white rounded-3xl border-2 transition-all duration-300 p-8 flex flex-col justify-between cursor-pointer select-none shadow-md hover:shadow-lg ${
                  isFlipped
                    ? 'border-emerald-400 bg-gradient-to-b from-white to-emerald-50/30'
                    : 'border-gray-200 hover:border-emerald-300'
                }`}
              >
                {/* Card Top Metadata */}
                <div className="flex items-center justify-between">
                  <span className="font-mono text-xs font-bold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded-lg border border-emerald-200">
                    PIE {currentCard.pieRoot}
                  </span>
                  <span className="text-xs font-semibold text-gray-400">
                    {currentCard.semanticFieldRu}
                  </span>
                </div>

                {/* Card Core Content */}
                {!isFlipped ? (
                  /* FRONT: Russian Cognate Prompt */
                  <div className="text-center py-6 my-auto">
                    <span className="text-xs uppercase font-extrabold tracking-wider text-gray-400 block mb-2">
                      {isEn ? 'Russian Cognate Prompt' : 'Русское слово-родственник'}
                    </span>
                    <h3 className="text-3xl md:text-4xl font-black text-gray-900 mb-3 tracking-tight">
                      «{currentCard.russianWord}»
                    </h3>
                    <p className="text-xs md:text-sm text-gray-500 max-w-xs mx-auto">
                      {isEn
                        ? 'How is this ancient Indo-European root pronounced in Hindi?'
                        : 'Как звучит этот общий индоевропейский корень на хинди?'}
                    </p>
                    <div className="mt-6 inline-flex items-center gap-2 text-xs font-extrabold text-emerald-600 bg-emerald-50 px-4 py-2 rounded-2xl border border-emerald-200/60 animate-pulse">
                      <RotateCw className="w-3.5 h-3.5" />
                      <span>{isEn ? 'Tap to reveal Hindi pronunciation' : 'Нажмите, чтобы перевернуть'}</span>
                    </div>
                  </div>
                ) : (
                  /* BACK: Hindi Target & Etymology */
                  <div className="text-center py-4 my-auto animate-in fade-in zoom-in-95 duration-200">
                    <span className="text-xs uppercase font-extrabold tracking-wider text-emerald-600 block mb-2">
                      {isEn ? 'Hindi Target Match' : 'Целевое слово на хинди'}
                    </span>

                    {/* Big Phonetics */}
                    <div className="text-3xl md:text-4xl font-black text-emerald-800 tracking-tight mb-1">
                      [{currentCard.hindiPhoneticCyrillic}]
                    </div>

                    {showDevanagari && currentCard.hindiDevanagari && (
                      <div className="text-xl font-bold text-gray-700 font-hindi mb-1">
                        {currentCard.hindiDevanagari}
                      </div>
                    )}

                    <div className="text-sm font-mono text-gray-500 font-bold mb-4">
                      {currentCard.hindiWordIso}
                    </div>

                    {/* Dual Audio Buttons */}
                    <div className="flex items-center justify-center gap-2 mb-4" onClick={e => e.stopPropagation()}>
                      <button
                        onClick={() => speakHindi(currentCard.hindiDevanagari || currentCard.hindiWordIso, 1.0)}
                        className="flex items-center gap-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-extrabold shadow-sm active:scale-95 transition-all"
                        title="Normal speed"
                      >
                        <Volume2 className="w-4 h-4" />
                        <span>1.0x</span>
                      </button>
                      <button
                        onClick={() => speakHindi(currentCard.hindiDevanagari || currentCard.hindiWordIso, 0.65)}
                        className="flex items-center gap-1.5 px-3 py-1.5 bg-emerald-100 hover:bg-emerald-200 text-emerald-900 rounded-xl text-xs font-extrabold border border-emerald-300 active:scale-95 transition-all"
                        title="Slow pronunciation"
                      >
                        <span>🐢 0.65x</span>
                      </button>
                    </div>

                    {/* Etymological Note */}
                    <div className="text-xs text-gray-600 bg-gray-50/80 rounded-xl p-3 border border-gray-100 text-left flex items-start gap-2 max-w-sm mx-auto">
                      <BookOpen className="w-3.5 h-3.5 text-gray-400 shrink-0 mt-0.5" />
                      <p className="leading-relaxed">
                        {currentCard.notesRu}
                      </p>
                    </div>
                  </div>
                )}

                {/* Card Footer prompt */}
                <div className="text-center text-[11px] font-semibold text-gray-400">
                  {isFlipped
                    ? (isEn ? 'Rate your recall below:' : 'Оцените свое запоминание:')
                    : (isEn ? 'Tap anywhere to reveal' : 'Коснитесь карточки для проверки')}
                </div>
              </div>

              {/* Action Buttons for Flipped State */}
              {isFlipped && (
                <div className="mt-4 flex items-center gap-3">
                  <button
                    onClick={() => handleNextCard(false)}
                    className="flex-1 py-3 px-4 rounded-2xl border-2 border-gray-200 bg-white hover:bg-gray-50 text-gray-700 font-extrabold text-xs sm:text-sm flex items-center justify-center gap-2 cursor-pointer shadow-xs active:scale-95 transition-all"
                  >
                    <HelpCircle className="w-4 h-4 text-gray-400" />
                    <span>{isEn ? 'Review Later' : 'Еще повторить'}</span>
                  </button>

                  <button
                    onClick={() => handleNextCard(true)}
                    className="flex-1 py-3 px-4 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs sm:text-sm flex items-center justify-center gap-2 cursor-pointer shadow-md active:scale-95 transition-all"
                  >
                    <CheckCircle2 className="w-4 h-4" />
                    <span>{isEn ? 'Mastered! (+5 XP)' : 'Запомнил! (+5 XP)'}</span>
                  </button>
                </div>
              )}
            </div>
          ) : sessionCompleted ? (
            /* Session Completed Screen */
            <div className="max-w-md mx-auto bg-white rounded-3xl border-2 border-emerald-200 p-8 text-center shadow-lg animate-in zoom-in-95 duration-200">
              <div className="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mx-auto mb-4">
                <Trophy className="w-8 h-8" />
              </div>
              <h3 className="text-2xl font-black text-gray-900 mb-1">
                {isEn ? 'Flashcard Deck Mastered!' : 'Отличная работа!'}
              </h3>
              <p className="text-sm text-gray-500 mb-4">
                {isEn
                  ? `You reviewed ${deck.length} Indo-European cognates in this session.`
                  : `Вы закрепили ${deck.length} индоевропейских корней в этой сессии.`}
              </p>

              <div className="bg-emerald-50 rounded-2xl p-4 border border-emerald-200 mb-6 flex items-center justify-around">
                <div>
                  <div className="text-2xl font-black text-emerald-800">{deck.length}</div>
                  <div className="text-[11px] font-bold text-emerald-600 uppercase">
                    {isEn ? 'Cards Reviewed' : 'Карточек'}
                  </div>
                </div>
                <div className="h-8 w-px bg-emerald-200" />
                <div>
                  <div className="text-2xl font-black text-emerald-800">+{masteredIds.size * 5}</div>
                  <div className="text-[11px] font-bold text-emerald-600 uppercase">XP</div>
                </div>
              </div>

              <div className="flex flex-col gap-2.5">
                <button
                  onClick={handleShuffleDeck}
                  className="w-full py-3 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm shadow-md active:scale-95 transition-all cursor-pointer"
                >
                  {isEn ? 'Practice Again' : 'Повторить снова'}
                </button>
                <button
                  onClick={() => setViewMode('grid')}
                  className="w-full py-3 rounded-2xl bg-gray-100 hover:bg-gray-200 text-gray-700 font-extrabold text-sm active:scale-95 transition-all cursor-pointer"
                >
                  {isEn ? 'Back to Dictionary' : 'Вернуться к словарю'}
                </button>
              </div>
            </div>
          ) : null}
        </div>
      )}

      {/* ==================== DICTIONARY GRID MODE ==================== */}
      {viewMode === 'grid' && (
        <>
          {/* Search and Filters */}
          <div className="mb-6 space-y-4">
            {/* Search Bar */}
            <div className="relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input
                type="text"
                value={searchQuery}
                onChange={e => setSearchQuery(e.target.value)}
                placeholder={
                  isEn
                    ? 'Search by Russian, Hindi, PIE root, or topic (e.g. fire, agni, дверь, family)...'
                    : 'Поиск по русскому слову, корню или хинди (дверь, огонь, agni, брат)...'
                }
                className="w-full pl-12 pr-4 py-3.5 bg-white rounded-2xl border-2 border-gray-200 focus:border-emerald-500 focus:outline-hidden text-sm md:text-base font-medium shadow-xs"
              />
              {searchQuery && (
                <button
                  onClick={() => setSearchQuery('')}
                  className="absolute right-4 top-1/2 -translate-y-1/2 text-xs font-bold text-gray-400 hover:text-gray-600 bg-gray-100 px-2 py-1 rounded-md cursor-pointer"
                >
                  {isEn ? 'Clear' : 'Очистить'}
                </button>
              )}
            </div>

            {/* Semantic Field Filter Tabs */}
            <div className="flex gap-2 overflow-x-auto pb-2 scrollbar-none">
              <button
                onClick={() => setSelectedField('all')}
                className={`px-3.5 py-1.5 rounded-xl text-xs md:text-sm font-bold whitespace-nowrap transition-colors cursor-pointer ${
                  selectedField === 'all'
                    ? 'bg-emerald-600 text-white shadow-xs'
                    : 'bg-white text-gray-600 border border-gray-200 hover:bg-gray-50'
                }`}
              >
                {isEn ? 'All Categories' : 'Все категории'} ({cognatesData.cognates.length})
              </button>
              {semanticFields.map((field, idx) => (
                <button
                  key={idx}
                  onClick={() => setSelectedField(field)}
                  className={`px-3.5 py-1.5 rounded-xl text-xs md:text-sm font-bold whitespace-nowrap transition-colors cursor-pointer ${
                    selectedField === field
                      ? 'bg-emerald-600 text-white shadow-xs'
                      : 'bg-white text-gray-600 border border-gray-200 hover:bg-gray-50'
                  }`}
                >
                  {field}
                </button>
              ))}
            </div>
          </div>

          {/* Results Count */}
          <div className="text-xs text-gray-500 font-bold mb-4 px-1">
            {isEn
              ? `Showing ${filteredCognates.length} of ${cognatesData.cognates.length} cognates`
              : `Найдено когнатов: ${filteredCognates.length} из ${cognatesData.cognates.length}`}
          </div>

          {/* Cognates Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {filteredCognates.map((item, idx) => {
              const targetHindi = item.hindiDevanagari || item.hindiWordIso;
              return (
                <div
                  key={idx}
                  className="bg-white rounded-2xl border-2 border-gray-100 hover:border-emerald-200 p-5 shadow-xs hover:shadow-md transition-all flex flex-col justify-between"
                >
                  <div>
                    {/* PIE Root & Category */}
                    <div className="flex items-center justify-between gap-2 mb-3">
                      <span className="font-mono text-xs font-bold text-emerald-800 bg-emerald-50 px-2.5 py-0.5 rounded-md border border-emerald-100">
                        PIE {item.pieRoot}
                      </span>
                      <span className="text-[11px] font-semibold text-gray-400">
                        {item.semanticFieldRu}
                      </span>
                    </div>

                    {/* Side-by-side linguistic comparison */}
                    <div className="grid grid-cols-11 items-center gap-2 mb-4 bg-gray-50/70 p-3 rounded-xl border border-gray-100">
                      {/* Russian Side */}
                      <div className="col-span-5 text-left">
                        <span className="text-[10px] uppercase font-bold text-gray-400 block mb-0.5">
                          {isEn ? 'Russian' : 'Русский'}
                        </span>
                        <span className="font-extrabold text-gray-900 text-base">
                          {item.russianWord}
                        </span>
                      </div>

                      {/* Connector Arrow */}
                      <div className="col-span-1 flex justify-center">
                        <ArrowRight className="w-4 h-4 text-emerald-500" />
                      </div>

                      {/* Hindi Side */}
                      <div className="col-span-5 text-right">
                        <span className="text-[10px] uppercase font-bold text-emerald-600 block mb-0.5">
                          {isEn ? 'Hindi Target' : 'Хинди'}
                        </span>
                        <div className="flex items-center justify-end gap-1.5 flex-wrap">
                          <span className="font-extrabold text-emerald-700 text-sm md:text-base">
                            [{item.hindiPhoneticCyrillic}]
                          </span>
                          <div className="flex items-center gap-0.5">
                            <button
                              onClick={() => speakHindi(targetHindi, 1.0)}
                              className="p-1 rounded-lg hover:bg-emerald-100 text-emerald-600 transition-colors cursor-pointer"
                              title={isEn ? `Listen to ${item.hindiWordIso}` : `Послушать ${item.hindiPhoneticCyrillic}`}
                            >
                              <Volume2 className="w-4 h-4" />
                            </button>
                            <button
                              onClick={() => speakHindi(targetHindi, 0.65)}
                              className="p-1 rounded-lg hover:bg-emerald-100 text-emerald-600 transition-colors cursor-pointer text-xs"
                              title={isEn ? 'Slow pronunciation' : 'Медленное произношение'}
                            >
                              🐢
                            </button>
                          </div>
                        </div>
                        {showDevanagari && item.hindiDevanagari && (
                          <span className="block text-xs font-bold text-gray-700 font-hindi">
                            {item.hindiDevanagari}
                          </span>
                        )}
                        <span className="block text-[11px] text-gray-400 font-mono">
                          {item.hindiWordIso}
                        </span>
                      </div>
                    </div>
                  </div>

                  {/* Etymological Note */}
                  <div className="text-xs text-gray-600 border-t border-gray-100 pt-3 flex items-start gap-2">
                    <BookOpen className="w-3.5 h-3.5 text-gray-400 shrink-0 mt-0.5" />
                    <p className="leading-relaxed">
                      {item.notesRu}
                    </p>
                  </div>
                </div>
              );
            })}

            {filteredCognates.length === 0 && (
              <div className="col-span-full text-center py-12 bg-white rounded-3xl border border-dashed border-gray-200 p-8">
                <p className="text-gray-400 text-sm font-medium mb-3">
                  {isEn ? 'No cognates found matching your search.' : 'Когнатов по вашему запросу не найдено.'}
                </p>
                <button
                  onClick={() => {
                    setSearchQuery('');
                    setSelectedField('all');
                  }}
                  className="text-xs font-bold text-emerald-600 hover:text-emerald-700 underline cursor-pointer"
                >
                  {isEn ? 'Reset search filters' : 'Сбросить фильтры'}
                </button>
              </div>
            )}
          </div>
        </>
      )}
    </div>
  );
};
