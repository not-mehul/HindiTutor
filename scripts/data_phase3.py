"""
data_phase3.py - Days 17 to 24
Phase 3: The Experiencer Register, Food, Dining, and Needs
"""

DAYS_PHASE_3 = [
    # Day 17
    {
        "day": 17,
        "phase": 3,
        "title": {
            "en": "Dative Experiencers 1: Necessity with Chāhiye",
            "ru": "Дативный экспериенцер 1: Конструкция необходимости «Мне нужно» (Mujhē chāhiye)"
        },
        "theme": "Мне нужно: вода (pānī), чай (chāi), счет (bill), помощь (madad)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция аффрикаты ch в chāhiye и долгого гласного ā)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (1:1 сопоставление с русским дательным падежом: 'Мне нужно' = 'Mujhē chāhiye')",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Подстановочные ряды: мне нужна вода, мне нужен чай, мне нужен счет)",
            "phase4SimulationMinutes": "17:00–20:00 (Заказ базовых напитков и просьба о помощи)"
        },
        "learningObjectives": {
            "en": [
                "Master dative experiencer subject 'Mujhē' (to me) with modal predicate 'chāhiye'",
                "Establish direct 1:1 cognitive bridge with Russian 'Мне нужно'",
                "Express essential physical needs (pānī, chāi, madad, bill)"
            ],
            "ru": [
                "Освоить дативный субъект 'Mujhē' (мне) с предикатом необходимости 'chāhiye' (нужно)",
                "Установить прямое когнитивное соответствие с русской конструкцией 'Мне нужно'",
                "Уверенно выражать базовые потребности: воду, чай, помощь, счет"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Глухая палатальная аффриката /ch/ (च) и полугласный /y/ в слове chāhiye (चाहिए)",
            "articulatoryMechanism": "Кончик языка за нижними резцами, спинка языка смыкается с твердым нёбом: [чаа-хийе]. Не придыхательный.",
            "russianInterferenceWarning": "Не произносите с сильным придыханием (не chha!). Это чистый русский мягкий [ч], за которым следует долгое [аа].",
            "drills": [
                {
                    "prompt": "Отработка формулы необходимости",
                    "contrastPair": "Mujhē chāhiye (Мне нужно)",
                    "instructionsRu": "Произнесите связку: [муджхе чаахийе] на одном дыхании."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Дативный субъект состояния (Experiencer Subject)",
            "russianParallel": "Колоссальное преимущество русскоязычного студента: в отличие от англичан, которые говорят номинативно 'I need' (Я нуждаюсь), в русском и хинди субъект ставится в дательный падеж! Русский: 'Мне [Датив] нужен чай [Именительный]'. Хинди: 'Mujhē [Датив] chāi [Именительный] chāhiye [Предикат]'. 100% тождество мысли!",
            "syntacticFormula": "Mujhē + [Желаемый предмет / Потребность] + chāhiye",
            "explanationRu": "В этой конструкции глагол chāhiye не меняется по лицам (я/ты/он). Вы просто ставите Mujhē (мне), затем предмет, и завершаете словом chāhiye.",
            "pieCognateConnection": {
                "root": "*kʷey- / *kʷi-",
                "russian": "чаять (надеяться, ожидать)",
                "hindi": "chāhnā (chāhiye - желанный)",
                "meaning": "Желание и ожидание"
            }
        },
        "vocabulary": [
            {
                "id": "d17_v01",
                "devanagari": "चाहिए",
                "transliterationIso": "Chāhiye",
                "phoneticCyrillic": "Чаахийе",
                "translationRu": "Нужно / Требуется",
                "translationEn": "Need / Want / Required",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Ударение на долгое 'аа'."
            },
            {
                "id": "d17_v02",
                "devanagari": "चाय",
                "transliterationIso": "Chāi",
                "phoneticCyrillic": "Чаай",
                "translationRu": "Чай",
                "translationEn": "Tea",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Идентично русскому слову 'чай'."
            },
            {
                "id": "d17_v03",
                "devanagari": "मदद",
                "transliterationIso": "Madad",
                "phoneticCyrillic": "Мадад",
                "translationRu": "Помощь",
                "translationEn": "Help",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Два зубных [д]."
            },
            {
                "id": "d17_v04",
                "devanagari": "बिल",
                "transliterationIso": "Bill",
                "phoneticCyrillic": "Билл",
                "translationRu": "Счет (в ресторане)",
                "translationEn": "Bill / Check",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Универсальное слово."
            }
        ],
        "exercises": [
            {
                "id": "d17_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите фразу 'Мне нужна вода' (Мне + вода + нужно)",
                "prompt": "Мне нужна вода",
                "wordChips": ["Mujhē", "pānī", "chāhiye"],
                "correctAnswer": ["Mujhē", "pānī", "chāhiye"],
                "phoneticCyrillicTarget": "Муджхе паании чаахийе",
                "explanationRu": "Точная копия русской грамматики: Мне (Mujhē) + вода (pānī) + нужно (chāhiye)."
            },
            {
                "id": "d17_ex02",
                "type": "substitution_drill",
                "instructionRu": "Скажите официанту, что вам нужен счет",
                "prompt": "Mujhē _____ chāhiye.",
                "options": ["bill", "namastē", "bhaiyā"],
                "correctAnswer": "bill",
                "transliterationIsoTarget": "Mujhē bill chāhiye.",
                "explanationRu": "Mujhē bill chāhiye = Мне нужен счет."
            },
            {
                "id": "d17_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вы заблудились на перекрестке. Попросите о помощи за 2 секунды.",
                "prompt": "Срочный запрос о помощи",
                "options": [
                    "Bhaiyā, mujhē madad chāhiye!",
                    "Mujhē chāi chāhiye!",
                    "Main ṭhīk hū̃!"
                ],
                "correctAnswer": "Bhaiyā, mujhē madad chāhiye!",
                "phoneticCyrillicTarget": "Бхаййаа, муджхе мадад чаахийе!",
                "explanationRu": "Bhaiyā, mujhē madad chāhiye! — Брат, мне нужна помощь!"
            },
            {
                "id": "d17_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Вставьте дативное местоимение 'Мне'",
                "prompt": "_____ chāi chāhiye. (Мне нужен чай)",
                "options": ["Mujhē", "Main", "Mērā"],
                "correctAnswer": "Mujhē",
                "transliterationIsoTarget": "Mujhē chāi chāhiye.",
                "explanationRu": "С глаголом chāhiye всегда используется датив Mujhē."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Заказ чая и воды в придорожной чайной (dhābā)",
            "setting": "Традиционная дхаба со скамейками",
            "partnerRoleRu": "Официант дхабы",
            "learnerRoleRu": "Путешественница",
            "turns": [
                {
                    "speaker": "Официант",
                    "speechRu": "Здравствуйте, сестра! Что вам нужно?",
                    "speechIso": "Namastē madam! Kyā chāhiye?",
                    "speechCyrillic": "Намастэ мадам! Кйаа чаахийе?",
                    "learnerHintRu": "Скажите: Мне нужен чай и вода (Mujhē chāi aur pānī chāhiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте! Мне нужен чай и бутылка воды.",
                    "speechIso": "Namastē! Mujhē ek chāi aur pānī chāhiye.",
                    "speechCyrillic": "Намастэ! Муджхе эк чаай аур паании чаахийе.",
                    "acceptableResponsesIso": ["Mujhē chāi aur pānī chāhiye"]
                },
                {
                    "speaker": "Официант",
                    "speechRu": "Сейчас принесу, две минуты.",
                    "speechIso": "Abhī lāyā, do minute.",
                    "speechCyrillic": "Абхии лаайаа, до минат.",
                    "learnerHintRu": "Поблагодарите: Shukriyā!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Спасибо!",
                    "speechIso": "Shukriyā!",
                    "speechCyrillic": "Шукрийа!",
                    "acceptableResponsesIso": ["Dhanyavād"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Чайная культура Индии (Chai culture)",
            "pointsRu": [
                "Масала чай (с молоком, кардамоном, имбирем и сахаром) — главный социальный напиток Индии.",
                "Фраза 'Mujhē ek chāi chāhiye' — пароль к мгновенному гостеприимству в любом уголке страны.",
                "В уличных дхабах чай подают в маленьких стеклянных стаканчиках или глиняных чашечках 'kulhad'."
            ]
        }
    },

    # Day 18
    {
        "day": 18,
        "phase": 3,
        "title": {
            "en": "Dative Experiencers 2: Quantifiers and Polite Negation",
            "ru": "Дативный экспериенцер 2: Квантификаторы и отказ («Мне это не нужно»)"
        },
        "theme": "Немного (thōṛā), слишком много (zyādā), еще один (ek aur), достаточно/хватит (bas)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция придыхательного th и ретрофлексного ṛ в thōṛā / тхоор͟аа)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Отрицание датива: Mujhē yeh nahī̃ chāhiye = Мне это не нужно)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Дозирование: чуть-чуть воды, хватит, слишком много)",
            "phase4SimulationMinutes": "17:00–20:00 (Отказ от лишней добавки блюда за столом)"
        },
        "learningObjectives": {
            "en": [
                "Negate dative needs with 'Mujhē yeh nahī̃ chāhiye'",
                "Quantify requests with thōṛā (a little) and zyādā (more / too much)",
                "Signal sufficiency with emphatic boundary particle 'Bas!' (Enough / Stop)"
            ],
            "ru": [
                "Отказываться от предложенного фразой 'Mujhē yeh nahī̃ chāhiye' ('Мне это не нужно')",
                "Регулировать порции словами thōṛā (чуть-чуть) и zyādā (много / слишком)",
                "Устанавливать границу словом 'Bas!' ('Хватит! / Достаточно!')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Зубной придыхательный /th/ (थ) и ретрофлексный взмах /ṛ/ (ड़) в thōṛā",
            "articulatoryMechanism": "Смычка на резцах с мощным выбросом воздуха [тх] + переход к загибу языка назад [р͟] с ударом по нёбу: [тхоор͟аа].",
            "russianInterferenceWarning": "Не произносите просто русское 'тора' или 'сора'. Это сложнейший звук: придыхание + ретрофлексный взмах.",
            "drills": [
                {
                    "prompt": "Отработка слова 'чуть-чуть'",
                    "contrastPair": "tōrā (ошибка) vs thōṛā (верно: [тхоор͟аа])",
                    "instructionsRu": "Выдохните воздух на 'th', затем щелкните кончиком языка по нёбу на 'ṛā'."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Квантификация и отрицание дативного субъекта",
            "russianParallel": "Русское 'Мне это не нужно' = Mujhē (мне) + yeh (это) + nahī̃ (не) + chāhiye (нужно). Квантификаторы thōṛā (чуть-чуть) и zyādā (слишком много) ставятся ПЕРЕД существительным, точно как в русском языке (Thōṛā pānī = Чуть-чуть воды).",
            "syntacticFormula": "Mujhē + [yeh] + nahī̃ chāhiye / [Thōṛā / Zyādā] + [Объект] + dījiye",
            "explanationRu": "Слово 'Bas!' — абсолютный хит в Индии. Когда вам наливают воду или накладывают рис, громкое и вежливое 'Bas, bas!' мгновенно останавливает официанта (точно как русское 'Хватит, достаточно!').",
            "pieCognateConnection": {
                "root": "*bheg-",
                "russian": "богатый / изобилие",
                "hindi": "bahut / zyādā",
                "meaning": "Количественное превосходство"
            }
        },
        "vocabulary": [
            {
                "id": "d18_v01",
                "devanagari": "थोड़ा",
                "transliterationIso": "Thōṛā",
                "phoneticCyrillic": "Тхоор͟аа",
                "translationRu": "Немного / Чуть-чуть",
                "translationEn": "A little / A bit",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Придыхательное 'тх' + ретрофлексный flap 'р͟'."
            },
            {
                "id": "d18_v02",
                "devanagari": "ज़्यादा",
                "transliterationIso": "Zyādā",
                "phoneticCyrillic": "Зйаадаа",
                "translationRu": "Много / Слишком много",
                "translationEn": "More / Too much",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Звонкий [з] + долгое [аа]."
            },
            {
                "id": "d18_v03",
                "devanagari": "एक और",
                "transliterationIso": "Ek aur",
                "phoneticCyrillic": "Эк аур",
                "translationRu": "Еще один / Еще одну",
                "translationEn": "One more",
                "partOfSpeech": "phrase",
                "gender": "n/a",
                "audioHint": "Ek (один) + aur (еще/и)."
            },
            {
                "id": "d18_v04",
                "devanagari": "बस",
                "transliterationIso": "Bas",
                "phoneticCyrillic": "Бас",
                "translationRu": "Хватит / Достаточно / Только",
                "translationEn": "Enough / Stop / Only",
                "partOfSpeech": "particle",
                "gender": "n/a",
                "audioHint": "Краткое открытое [бас]."
            }
        ],
        "exercises": [
            {
                "id": "d18_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите вежливый отказ: 'Мне это не нужно'",
                "prompt": "Мне это не нужно",
                "wordChips": ["Mujhē", "yeh", "nahī̃", "chāhiye"],
                "correctAnswer": ["Mujhē", "yeh", "nahī̃", "chāhiye"],
                "phoneticCyrillicTarget": "Муджхе йе нахииⁿ чаахийе",
                "explanationRu": "Отрицание nahī̃ ставится перед chāhiye: nahī̃ chāhiye."
            },
            {
                "id": "d18_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вам наливают чай в стакан, порция уже полная. Остановите официанта за 1 секунду!",
                "prompt": "Чай наливается через край",
                "options": [
                    "Bas, bhaiyā, bas! Shukriyā!",
                    "Zyādā dījiye!",
                    "Mērā nām chāi hai!"
                ],
                "correctAnswer": "Bas, bhaiyā, bas! Shukriyā!",
                "phoneticCyrillicTarget": "Бас, бхаййаа, бас! Шукрийа!",
                "explanationRu": "'Bas, bas!' — моментальный сигнал 'Достаточно, хватит!'."
            },
            {
                "id": "d18_ex03",
                "type": "substitution_drill",
                "instructionRu": "Попросите еще один чай (Еще один + чай + дайте)",
                "prompt": "_____ chāi dījiye. (Еще один чай)",
                "options": ["Ek aur", "Thōṛā", "Zyādā"],
                "correctAnswer": "Ek aur",
                "transliterationIsoTarget": "Ek aur chāi dījiye.",
                "explanationRu": "Ek aur = еще один / еще одну."
            },
            {
                "id": "d18_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Попросите немного воды",
                "prompt": "_____ pānī dījiye. (Немного воды дайте)",
                "options": ["Thōṛā", "Bas", "Ek aur"],
                "correctAnswer": "Thōṛā",
                "transliterationIsoTarget": "Thōṛā pānī dījiye.",
                "explanationRu": "Thōṛā pānī = немного воды."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Обед в ресторане: регулирование порций",
            "setting": "Столик в ресторане, официант подливает соус",
            "partnerRoleRu": "Внимательный официант с кувшином соуса",
            "learnerRoleRu": "Осторожная гостья",
            "turns": [
                {
                    "speaker": "Официант",
                    "speechRu": "Мадам, добавить еще соуса дала?",
                    "speechIso": "Madam, aur dāl dū̃?",
                    "speechCyrillic": "Мадам, аур даал дууⁿ?",
                    "learnerHintRu": "Скажите: Только чуть-чуть, спасибо! (Bas thōṛā, shukriyā!)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Только немного, пожалуйста, хватит!",
                    "speechIso": "Bas thōṛā jī, bas! Shukriyā.",
                    "speechCyrillic": "Бас тхоор͟аа джии, бас! Шукрийа.",
                    "acceptableResponsesIso": ["Bas thōṛā, bas!", "Thōṛā dījiye, bas!"]
                },
                {
                    "speaker": "Официант",
                    "speechRu": "Хорошо. Еще одну лепешку роти принести?",
                    "speechIso": "Ṭhīk hai. Ek aur roti lē āū̃?",
                    "speechCyrillic": "Т͟хиик хэ. Эк аур роти лее ааууⁿ?",
                    "learnerHintRu": "Откажитесь: Нет, мне это не нужно, спасибо! (Nahī̃, mujhē nahī̃ chāhiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Нет, спасибо, мне больше не нужно.",
                    "speechIso": "Nahī̃, mujhē nahī̃ chāhiye, shukriyā.",
                    "speechCyrillic": "Нахииⁿ, муджхе нахииⁿ чаахийе, шукрийа.",
                    "acceptableResponsesIso": ["Nahī̃ chāhiye, shukriyā"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Культура индийского хлебосольства (Atithi Devo Bhava)",
            "pointsRu": [
                "В традиционных индийских заведениях (Thali restaurants) еду будут подкладывать бесконечно, пока вы не скажете твердое 'Bas!'.",
                "Если не остановить официанта словом 'Bas!', ваша тарелка всегда будет полна до краев.",
                "Связка 'Bas jī, pet bhar gayā' (Хватит, уважаемый, я сыта) вызывает всеобщий восторг и уважение."
            ]
        }
    },

    # Day 19
    {
        "day": 19,
        "phase": 3,
        "title": {
            "en": "Culinary Ordering: Temperatures, Water Safety, and Staples",
            "ru": "Заказ еды и безопасность воды: температуры (Garam/Ṭhaṇḍā) и бутилированная вода"
        },
        "theme": "Еда (khānā), горячий (garam - когнат с русским 'жар'), холодный (ṭhaṇḍā), бутилированная вода",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Этимологическая связь когната garam с русским словом 'гореть / жар')",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Прилагательные перед существительными: garam pānī, ṭhaṇḍī bottle)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Четкий заказ безопасной запечатанной воды: Bottled / Bisleri pānī)",
            "phase4SimulationMinutes": "17:00–20:00 (Проверка запечатанной пробки и заказ горячего чая)"
        },
        "learningObjectives": {
            "en": [
                "Order temperature-specific staples using garam (hot) and ṭhaṇḍā (cold)",
                "Leverage PIE cognate *gʷʰer- (Russian жар/гореть <-> Hindi garam)",
                "Safeguard health by demanding sealed bottled water (Bisleri / Packaged pānī)"
            ],
            "ru": [
                "Заказывать блюда и напитки нужной температуры: garam (горячий) и ṭhaṇḍā (холодный)",
                "Использовать этимологическую интуицию когната *gʷʰer- (русский жар/гореть = хинди garam)",
                "Защищать здоровье в поездке, заказывая строго бутилированную воду (Bisleri / Packaged pānī)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Ретрофлексный придыхательный /ṭh/ и назализованный ретрофлекс в ṭhaṇḍā (ठंडा)",
            "articulatoryMechanism": "Кончик языка загнут к нёбу. При смычке идет выброс воздуха [тх], носовая фаза [н] и звонкий ретрофлексный отскок [д͟аа]: [тхандаа].",
            "russianInterferenceWarning": "Не заменяйте на мягкое русское 'тянда'! Звук должен быть гулким и твердым.",
            "drills": [
                {
                    "prompt": "Контраст температур",
                    "contrastPair": "Garam (горячий) vs Ṭhaṇḍā (холодный)",
                    "instructionsRu": "Произнесите: Garam pānī (горячая вода) — Ṭhaṇḍā pānī (холодная вода)."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Индоевропейский когнат Garam и порядок определения",
            "russianParallel": "Хинди 'garam' и русское 'гореть / жар' восходят к общему праиндоевропейскому корню *gʷʰer-. Как и в русском языке, прилагательное ВСЕГДА стоит ПЕРЕД определяемым словом: Garam khānā (Горячая еда), Ṭhaṇḍā pānī (Холодная вода).",
            "syntacticFormula": "[Garam / Ṭhaṇḍā] + [Еда / Напиток] + dījiye",
            "explanationRu": "В Индии жизненно важно требовать запечатанную промышленную воду. Бренд 'Bisleri' стал именем нарицательным для безопасной бутилированной воды.",
            "pieCognateConnection": {
                "root": "*gʷʰer-",
                "russian": "гореть / жар / горячий",
                "hindi": "garam",
                "meaning": "Праиндоевропейское тепло и огонь"
            }
        },
        "vocabulary": [
            {
                "id": "d19_v01",
                "devanagari": "गरम",
                "transliterationIso": "Garam",
                "phoneticCyrillic": "Гарам",
                "translationRu": "Горячий / Тёплый",
                "translationEn": "Hot / Warm",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Когнат со словом 'гореть'."
            },
            {
                "id": "d19_v02",
                "devanagari": "ठंडा",
                "transliterationIso": "Ṭhaṇḍā",
                "phoneticCyrillic": "Тхандаа",
                "translationRu": "Холодный",
                "translationEn": "Cold",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Ретрофлексный придыхательный ṭh."
            },
            {
                "id": "d19_v03",
                "devanagari": "खाना",
                "transliterationIso": "Khānā",
                "phoneticCyrillic": "Кхаанаа",
                "translationRu": "Еда / Кушать",
                "translationEn": "Food / To eat",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Придыхательное велярное [кх], два долгих гласных."
            },
            {
                "id": "d19_v04",
                "devanagari": "बॉटल पानी",
                "transliterationIso": "Bottled / Bisleri pānī",
                "phoneticCyrillic": "Ботл / Бислери паании",
                "translationRu": "Бутилированная (запечатанная) вода",
                "translationEn": "Bottled / Packaged water",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Ключевое слово гигиены в поездке."
            }
        ],
        "exercises": [
            {
                "id": "d19_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите заказ: 'Дайте горячий чай, пожалуйста'",
                "prompt": "Дайте горячий чай",
                "wordChips": ["Garam", "chāi", "dījiye"],
                "correctAnswer": ["Garam", "chāi", "dījiye"],
                "phoneticCyrillicTarget": "Гарам чаай дииджие",
                "explanationRu": "Прилагательное перед существительным: Garam chāi dījiye."
            },
            {
                "id": "d19_ex02",
                "type": "substitution_drill",
                "instructionRu": "Попросите холодную воду",
                "prompt": "_____ pānī dījiye.",
                "options": ["Ṭhaṇḍā", "Garam", "Khānā"],
                "correctAnswer": "Ṭhaṇḍā",
                "transliterationIsoTarget": "Ṭhaṇḍā pānī dījiye.",
                "explanationRu": "Ṭhaṇḍā = холодный."
            },
            {
                "id": "d19_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Официант несет открытый кувшин с водой из-под крана. Потребуйте закрытую бутылку Bisleri за 2 секунды!",
                "prompt": "Официант наливает подозрительную воду",
                "options": [
                    "Nahī̃ bhaiyā, Bisleri bottle dījiye!",
                    "Hā̃, yeh pānī acchā hai!",
                    "Garam khānā kahā̃ hai?"
                ],
                "correctAnswer": "Nahī̃ bhaiyā, Bisleri bottle dījiye!",
                "phoneticCyrillicTarget": "Нахииⁿ бхаййаа, Бислери ботл дииджие!",
                "explanationRu": "Защита здоровья: требуйте упакованную воду Bisleri."
            },
            {
                "id": "d19_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Уточните: 'Еда горячая?'",
                "prompt": "Kyā khānā _____ hai?",
                "options": ["garam", "pās", "sē"],
                "correctAnswer": "garam",
                "transliterationIsoTarget": "Kyā khānā garam hai?",
                "explanationRu": "Garam = горячий."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Заказ безопасной воды и горячей еды в кафе",
            "setting": "Уютное кафе в Дхарамсале или Удайпуре",
            "partnerRoleRu": "Официант",
            "learnerRoleRu": "Заботящаяся о здоровье путешественница",
            "turns": [
                {
                    "speaker": "Официант",
                    "speechRu": "Здравствуйте, что будете пить?",
                    "speechIso": "Namastē madam, kyā pīyēṅgī?",
                    "speechCyrillic": "Намастэ мадам, кйаа пииенгии?",
                    "learnerHintRu": "Попросите запечатанную бутылку воды: Ek Bisleri pānī bottle dījiye"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте! Дайте одну закрытую бутылку воды Bisleri, пожалуйста.",
                    "speechIso": "Namastē! Ek Bisleri pānī bottle dījiye.",
                    "speechCyrillic": "Намастэ! Эк Бислери паании ботл дииджие.",
                    "acceptableResponsesIso": ["Bisleri bottle dījiye", "Bottled pānī dījiye"]
                },
                {
                    "speaker": "Официант",
                    "speechRu": "Хорошо, вот вода. А из еды что принести?",
                    "speechIso": "Lījiye packaged pānī. Khānē mẽ kyā chāhiye?",
                    "speechCyrillic": "Лииджие пэкиджд паании. Кхаанее мэⁿ кйаа чаахийе?",
                    "learnerHintRu": "Скажите: Еда должна быть очень горячей! (Khānā garam honā chāhiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Еда должна быть свежей и горячей, пожалуйста.",
                    "speechIso": "Khānā garam honā chāhiye.",
                    "speechCyrillic": "Кхаанаа гарам хонаа чаахийе.",
                    "acceptableResponsesIso": ["Garam khānā dījiye"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Правила водной безопасности в путешествии",
            "pointsRu": [
                "Никогда не пейте сырую воду из графинов на столах уличных заведений.",
                "При покупке бутылки Bisleri обязательно проверяйте целостность пластикового кольца на крышке ('Seal check').",
                "Горячий свежесваренный чай масала кипятится несколько минут, поэтому он микробиологически абсолютно безопасен."
            ]
        }
    },

    # Day 20
    {
        "day": 20,
        "phase": 3,
        "title": {
            "en": "Dietary Restrictions, Spice Management, and Allergies",
            "ru": "Диета и острота: «Я вегетарианка» (Shākāhārī) и «Без перца» (Binā mirch kē)"
        },
        "theme": "Вегетарианство (shākāhārī), перец чили (mirch), без перца (binā mirch kē), не делайте острым (tīkhā mat banāiye)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция шипящего sh в shākāhārī и ретрофлексного t в отрицании mat)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Конструкция Binā [X] kē = русский предлог БЕЗ + Родительный падеж)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Отработка запрета: tīkhā mat banāiye = остро не делайте)",
            "phase4SimulationMinutes": "17:00–20:00 (Инструктаж повара по специям перед приготовлением)"
        },
        "learningObjectives": {
            "en": [
                "Declare vegetarian diet with 'Main shākāhārī hū̃'",
                "Master privative postpositional frame 'Binā [X] kē' (without [X])",
                "Prohibit hot chili spices using 'Tīkhā mat banāiye' and 'Kam mirch'"
            ],
            "ru": [
                "Заявлять о вегетарианстве: 'Main shākāhārī hū̃' ('Я вегетарианка')",
                "Использовать конструкцию лишения 'Binā [X] kē' (русское 'Без [чего-либо]')",
                "Запрещать остроту фразами 'Tīkhā mat banāiye' (Остро не делайте) и 'Kam mirch' (Мало перца)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Глухой ретрофлексный /ṭ/ в отрицательной запретительной частице mat (मत)",
            "articulatoryMechanism": "Зубной звук [м] + краткий гласный [а] + четкий зубной/альвеолярный [т]. Частица mat выражает категорический вежливый запрет (Не делайте!).",
            "russianInterferenceWarning": "Не путайте отрицание nahī̃ (констатация) и mat (запрет действия). С повелительными глаголами используется ТОЛЬКО mat.",
            "drills": [
                {
                    "prompt": "Отработка запрета остроты",
                    "contrastPair": "Tīkhā mat banāiye (Остро не делайте)",
                    "instructionsRu": "Произнесите с твердым ударением на 'mat'."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Послелог отсутствия Binā ... kē (Русский предлог 'Без')",
            "russianParallel": "Прямая калька с русского языка: 'Без сахара' = Binā cheenī kē; 'Без перца' = Binā mirch kē. Слово binā исторически родственно славянскому корню (сравните др.-рус. безъ / от-бывать).",
            "syntacticFormula": "Binā + [Ингредиент] + kē / [Характеристика] + mat banāiye",
            "explanationRu": "Для запрета действия в повелительном наклонении в хинди есть специальная частица 'mat' (русское 'не надо / не смей'): Tīkhā mat banāiye = Острым не делайте!",
            "pieCognateConnection": {
                "root": "*bʰos- / *bē-",
                "russian": "без",
                "hindi": "binā",
                "meaning": "Индоевропейское лишение и отсутствие"
            }
        },
        "vocabulary": [
            {
                "id": "d20_v01",
                "devanagari": "शाकाहारी",
                "transliterationIso": "Shākāhārī",
                "phoneticCyrillic": "Шаакаахаарии",
                "translationRu": "Вегетарианка / Вегетарианский",
                "translationEn": "Vegetarian",
                "partOfSpeech": "adjective",
                "gender": "both",
                "audioHint": "Все гласные долгие [шаа-каа-хаа-рии]."
            },
            {
                "id": "d20_v02",
                "devanagari": "मिर्च",
                "transliterationIso": "Mirch",
                "phoneticCyrillic": "Мирч",
                "translationRu": "Перец / Острый перец чили",
                "translationEn": "Chili / Pepper",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Чистый русский [р]."
            },
            {
                "id": "d20_v03",
                "devanagari": "बिना ... के",
                "transliterationIso": "Binā ... kē",
                "phoneticCyrillic": "Бинаа ... ке",
                "translationRu": "Без ... (послеложная рамка)",
                "translationEn": "Without ...",
                "partOfSpeech": "postposition",
                "gender": "n/a",
                "audioHint": "Binā mirch kē = без перца."
            },
            {
                "id": "d20_v04",
                "devanagari": "तीखा",
                "transliterationIso": "Tīkhā",
                "phoneticCyrillic": "Тиикхаа",
                "translationRu": "Острый / Пряный",
                "translationEn": "Spicy / Hot (taste)",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Зубной [т] + придыхательное [кх]."
            },
            {
                "id": "d20_v05",
                "devanagari": "मत बनाइए",
                "transliterationIso": "Mat banāiye",
                "phoneticCyrillic": "Мат банааие",
                "translationRu": "Не делайте / Не готовьте",
                "translationEn": "Do not make",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Запретительная частица mat."
            }
        ],
        "exercises": [
            {
                "id": "d20_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите важнейшую фразу: 'Пожалуйста, не делайте остро!'",
                "prompt": "Не делайте острым",
                "wordChips": ["Tīkhā", "mat", "banāiye"],
                "correctAnswer": ["Tīkhā", "mat", "banāiye"],
                "phoneticCyrillicTarget": "Тиикхаа мат банааие",
                "explanationRu": "Tīkhā (остро) + mat (не) + banāiye (делайте)."
            },
            {
                "id": "d20_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Официант спрашивает о ваших предпочтениях. Сообщите, что вы вегетарианка за 2 секунды.",
                "prompt": "Официант предлагает мясное карри",
                "options": [
                    "Main shākāhārī hū̃!",
                    "Mujhē mirch chāhiye!",
                    "Station pās hai!"
                ],
                "correctAnswer": "Main shākāhārī hū̃!",
                "phoneticCyrillicTarget": "Мэⁿ шаакаахаарии хууⁿ!",
                "explanationRu": "Main shākāhārī hū̃ = Я вегетарианка."
            },
            {
                "id": "d20_ex03",
                "type": "substitution_drill",
                "instructionRu": "Попросите приготовить блюдо без перца",
                "prompt": "_____ mirch kē banāiye. (Без перца приготовьте)",
                "options": ["Binā", "Sē", "Mẽ"],
                "correctAnswer": "Binā",
                "transliterationIsoTarget": "Binā mirch kē banāiye.",
                "explanationRu": "Binā [X] kē = без [X]."
            },
            {
                "id": "d20_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Попросите положить совсем мало перца",
                "prompt": "_____ mirch, please! (Мало перца)",
                "options": ["Kam", "Zyādā", "Bahut"],
                "correctAnswer": "Kam",
                "transliterationIsoTarget": "Kam mirch, please!",
                "explanationRu": "Kam = мало / слабый."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Заказ ужина с жестким контролем специй",
            "setting": "Ресторан индийской кухни",
            "partnerRoleRu": "Официант, принимающий заказ",
            "learnerRoleRu": "Путешественница с чувствительным желудком",
            "turns": [
                {
                    "speaker": "Официант",
                    "speechRu": "Добрый вечер, мадам! Курицу тикка или панир будете заказывать?",
                    "speechIso": "Namastē madam! Chicken tikka ya Paneer?",
                    "speechCyrillic": "Намастэ мадам! Чикен тикка йа Панир?",
                    "learnerHintRu": "Скажите: Я вегетарианка. Принесите панир. (Main shākāhārī hū̃)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Я вегетарианка. Панир, пожалуйста. И совсем без перца!",
                    "speechIso": "Main shākāhārī hū̃. Paneer dījiye, binā mirch kē.",
                    "speechCyrillic": "Мэⁿ шаакаахаарии хууⁿ. Панир дииджие, бинаа мирч ке.",
                    "acceptableResponsesIso": ["Main shākāhārī hū̃. Binā mirch kē."]
                },
                {
                    "speaker": "Официант",
                    "speechRu": "Немножко перца чили добавить для вкуса?",
                    "speechIso": "Thōṛī mirch ḍāl dū̃?",
                    "speechCyrillic": "Тхоор͟ии мирч д͟аал дууⁿ?",
                    "learnerHintRu": "Ответьте твердо: Нет! Остро совсем не делайте. (Nahī̃! Tīkhā bilkul mat banāiye!)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Нет, перца совсем не надо! Остро не делайте.",
                    "speechIso": "Nahī̃, tīkhā bilkul mat banāiye!",
                    "speechCyrillic": "Нахииⁿ, тиикхаа билкул мат банааие!",
                    "acceptableResponsesIso": ["Tīkhā mat banāiye!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Специфика индийской градации остроты",
            "pointsRu": [
                "Индийское понимание 'Not spicy' (не остро) для европейца часто ощущается как умеренно острое.",
                "Именно фраза на хинди 'Tīkhā bilkul mat banāiye' (Совсем не делайте остро) доходит до шеф-повара на кухне.",
                "Слово 'Shākāhārī' (вегетарианский) в Индии священно: вегетарианские блюда готовятся в отдельной посуде с величайшей строгостью."
            ]
        }
    },

    # Day 21
    {
        "day": 21,
        "phase": 3,
        "title": {
            "en": "Expressing Culinary Evaluation and Quality",
            "ru": "Кулинарная оценка: «Очень вкусно» (Svādishṭ) и специи (Соль, Сахар)"
        },
        "theme": "Вкусно (svādishṭ), соль (namak), сахар (cheenī), сладкий (mīṭhā), очень хорошо",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция санскритского кластера svā- в svādishṭ / сваадишт)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Предикативная оценка качества с копулой: Khānā bahut acchā hai)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Похвала повару и просьба подать соль/сахар)",
            "phase4SimulationMinutes": "17:00–20:00 (Оценка блюда официанту во время обеда)"
        },
        "learningObjectives": {
            "en": [
                "Praise meal quality with 'Khānā bahut svādishṭ / acchā hai'",
                "Request seasoning table adjustments (namak = salt, cheenī = sugar)",
                "Identify sweet flavors using mīṭhā"
            ],
            "ru": [
                "Хвалить качество еды: 'Khānā bahut svādishṭ hai' ('Еда очень вкусная')",
                "Просить недостающие специи к столу: namak (соль), cheenī (сахар)",
                "Описывать сладкий вкус: mīṭhā / mīṭhī chāi"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Звуковой кластер /sv/ и ретрофлексный спирант /ṣṭ/ в слове svādishṭ (स्वादिष्ट)",
            "articulatoryMechanism": "Зубной [с] слитно переходит в [в] с долгим [аа], а на конце кончик языка загибается назад для ретрофлексного кластера [шт͟]: [сваадишт].",
            "russianInterferenceWarning": "Не вставляйте лишний гласный между 'с' и 'в' (не 'савадишт'!).",
            "drills": [
                {
                    "prompt": "Произнесение комплимента еде",
                    "contrastPair": "Svādishṭ (вкусно)",
                    "instructionsRu": "Khānā bahut svādishṭ hai! (Еда очень вкусная!)"
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Предикативная качественная оценка с обязательной связкой",
            "russianParallel": "В русском языке мы говорим: 'Еда [есть] очень вкусная'. В хинди связка hai строго закрывает предложение: Khānā (Еда) + bahut (очень) + svādishṭ (вкусная) + hai (есть). Просьба подать соль: Thōṛā namak dījiye (Немного соли дайте).",
            "syntacticFormula": "[Блюдо] + bahut + [acchā / svādishṭ] + hai",
            "explanationRu": "Искренняя похвала еде на хинди делает повара и официанта вашими лучшими друзьями на все время пребывания.",
            "pieCognateConnection": {
                "root": "*swād-",
                "russian": "сладкий / услада",
                "hindi": "svādishṭ (вкусный) / svād (вкус)",
                "meaning": "Праиндоевропейский корень вкуса и сладости"
            }
        },
        "vocabulary": [
            {
                "id": "d21_v01",
                "devanagari": "स्वादिष्ट",
                "transliterationIso": "Svādishṭ",
                "phoneticCyrillic": "Сваадишт",
                "translationRu": "Вкусный / Аппетитный",
                "translationEn": "Delicious / Tasty",
                "partOfSpeech": "adjective",
                "gender": "both",
                "audioHint": "Когнат со словом 'сладость' и 'услада'."
            },
            {
                "id": "d21_v02",
                "devanagari": "नमक",
                "transliterationIso": "Namak",
                "phoneticCyrillic": "Намак",
                "translationRu": "Соль",
                "translationEn": "Salt",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Ударение на первый слог."
            },
            {
                "id": "d21_v03",
                "devanagari": "चीनी",
                "transliterationIso": "Cheenī",
                "phoneticCyrillic": "Чиинии",
                "translationRu": "Сахар",
                "translationEn": "Sugar",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Два долгих звука [чии-нии]."
            },
            {
                "id": "d21_v04",
                "devanagari": "मीठा",
                "transliterationIso": "Mīṭhā",
                "phoneticCyrillic": "Миитхаа",
                "translationRu": "Сладкий",
                "translationEn": "Sweet",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Придыхательное ретрофлексное ṭh."
            }
        ],
        "exercises": [
            {
                "id": "d21_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите похвалу повару: 'Еда очень вкусная!'",
                "prompt": "Еда очень вкусная",
                "wordChips": ["Khānā", "bahut", "svādishṭ", "hai"],
                "correctAnswer": ["Khānā", "bahut", "svādishṭ", "hai"],
                "phoneticCyrillicTarget": "Кхаанаа бахут сваадишт хэ",
                "explanationRu": "Подлежащее + наречие + прилагательное + связка hai."
            },
            {
                "id": "d21_ex02",
                "type": "substitution_drill",
                "instructionRu": "Попросите принести немного соли к столу",
                "prompt": "Thōṛā _____ dījiye. (Немного соли)",
                "options": ["namak", "cheenī", "mīṭhā"],
                "correctAnswer": "namak",
                "transliterationIsoTarget": "Thōṛā namak dījiye.",
                "explanationRu": "Namak = соль."
            },
            {
                "id": "d21_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Официант подходит и спрашивает: 'Khānā kaisā hai?' (Как вам еда?). Ответьте за 2 секунды с восторгом!",
                "prompt": "Официант интересуется вашим впечатлением",
                "options": [
                    "Bahut acchā hai, bahut svādishṭ!",
                    "Mujhē khānā nahī̃ chāhiye!",
                    "Main Russia sē hū̃!"
                ],
                "correctAnswer": "Bahut acchā hai, bahut svādishṭ!",
                "phoneticCyrillicTarget": "Бахут аччхаа хэ, бахут сваадишт!",
                "explanationRu": "Прекрасный отзыв: Очень хорошо, очень вкусно!"
            },
            {
                "id": "d21_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Скажите, что чай слишком сладкий",
                "prompt": "Chāi bahut _____ hai. (Чай очень сладкий)",
                "options": ["mīṭhī", "namak", "tīkhā"],
                "correctAnswer": "mīṭhī",
                "transliterationIsoTarget": "Chāi bahut mīṭhī hai.",
                "explanationRu": "Слово chāi женского рода, поэтому прилагательное согласуется в форме mīṭhī."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Обратная связь повару во время ужина",
            "setting": "Традиционный ресторан в Варанаси",
            "partnerRoleRu": "Шеф-повар или хозяин ресторана",
            "learnerRoleRu": "Довольная посетительница",
            "turns": [
                {
                    "speaker": "Хозяин",
                    "speechRu": "Намастэ, сестра! Как вам наше карри? Понравилось?",
                    "speechIso": "Namastē madam! Khānā kaisā lagā?",
                    "speechCyrillic": "Намастэ мадам! Кхаанаа кэсаа лагаа?",
                    "learnerHintRu": "Похвалите: Khānā bahut svādishṭ hai! Дайте еще немного риса."
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Еда очень вкусная! Спасибо большое.",
                    "speechIso": "Khānā bahut svādishṭ hai! Bahut shukriyā.",
                    "speechCyrillic": "Кхаанаа бахут сваадишт хэ! Бахут шукрийа.",
                    "acceptableResponsesIso": ["Bahut svādishṭ hai!"]
                },
                {
                    "speaker": "Хозяин",
                    "speechRu": "Большое спасибо! Еще что-нибудь нужно?",
                    "speechIso": "Dhanyavād madam! Aur kuchh chāhiye?",
                    "speechCyrillic": "Дханьяваад мадам! Аур кучх чаахийе?",
                    "learnerHintRu": "Попросите немного соли: Thōṛā namak dījiye"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Да, дайте еще немного соли, пожалуйста.",
                    "speechIso": "Hā̃-jī, thōṛā namak dījiye.",
                    "speechCyrillic": "Хааⁿ-джии, тхоор͟аа намак дииджие.",
                    "acceptableResponsesIso": ["Thōṛā namak dījiye"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Культура комплиментов еде в Индии",
            "pointsRu": [
                "Индийцы гордятся своей кухней превыше всего. Слово 'Svādishṭ' производит магический эффект на владельцев заведений.",
                "Традиционный чай в Индии по умолчанию заваривается с огромным количеством сахара.",
                "Если вы не любите сладкий чай, предупреждайте заранее: 'Binā cheenī kē' (Без сахара)."
            ]
        }
    },

    # Day 22
    {
        "day": 22,
        "phase": 3,
        "title": {
            "en": "Dative Experiencers 3: Preferences with Pasand",
            "ru": "Дативный экспериенцер 3: Конструкция симпатии «Мне нравится» (Mujhē ... pasand hai)"
        },
        "theme": "Мне нравится индийская еда (Mujhē Indian khānā pasand hai), мне это не нравится",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция pasand с чистым зубным nd на конце)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Полное 1:1 совпадение: 'Мне нравится это' = 'Mujhē yeh pasand hai')",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Подстановка: мне нравится чай, Индия, этот город, эта музыка)",
            "phase4SimulationMinutes": "17:00–20:00 (Светская беседа о впечатлениях от индийской кухни)"
        },
        "learningObjectives": {
            "en": [
                "Master dative preference construction 'Mujhē [X] pasand hai'",
                "Negate preferences with 'Mujhē yeh pasand nahī̃ hai'",
                "Map Hindi pasand directly onto Russian 'нравится'"
            ],
            "ru": [
                "Освоить дативную конструкцию предпочтения 'Mujhē [X] pasand hai' ('Мне нравится [X]')",
                "Выражать антипатию: 'Mujhē yeh pasand nahī̃ hai' ('Мне это не нравится')",
                "Опираться на полное структурное совпадение с русским оборотом 'Мне нравится'"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Непридыхательный смычный /p/ и носовая группа /nd/ в слове pasand (पसंद)",
            "articulatoryMechanism": "Губной [п] без придыхания, краткий гласный [а], звонкий зубной переход [нд]: [пасанд].",
            "russianInterferenceWarning": "Не оглушайте [д] на конце слова! Звук должен оставаться звонким.",
            "drills": [
                {
                    "prompt": "Отработка формулы симпатии",
                    "contrastPair": "Mujhē pasand hai (Мне нравится)",
                    "instructionsRu": "Произнесите связку: Mujhē chāi pasand hai (Мне нравится чай)."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Дативная конструкция предпочтения (Мне нравится)",
            "russianParallel": "Снова идеальное 100% совпадение с русской когнитивной моделью: Русский: 'Мне [Датив] нравится [Предикат] индийская еда [Именительный]'. Хинди: 'Mujhē [Датив] Indian khānā [Именительный] pasand hai [Предикат]'. Никакого сопротивления языкового барьера!",
            "syntacticFormula": "Mujhē + [Объект] + [pasand hai / pasand nahī̃ hai]",
            "explanationRu": "Англоязычные студенты мучаются, пытаясь перестроить свой номинатив 'I like' в датив. Русскоязычный студент просто берет свое родное 'Мне нравится' и подставляет Mujhē ... pasand hai!",
            "pieCognateConnection": {
                "root": "*mendʰ-",
                "russian": "мнить / мнение",
                "hindi": "pasand (одобренное / приглянувшееся)",
                "meaning": "Внутренняя оценка и предпочтение"
            }
        },
        "vocabulary": [
            {
                "id": "d22_v01",
                "devanagari": "पसंद",
                "transliterationIso": "Pasand",
                "phoneticCyrillic": "Пасанд",
                "translationRu": "Нравится / Угодный",
                "translationEn": "Pleasing / Liked",
                "partOfSpeech": "adjective",
                "gender": "both",
                "audioHint": "Ударение на второй слог."
            },
            {
                "id": "d22_v02",
                "devanagari": "भारतीय کھانا",
                "transliterationIso": "Indian / Bhāratīya khānā",
                "phoneticCyrillic": "Индиан / Бхааратиийа кхаанаа",
                "translationRu": "Индийская еда",
                "translationEn": "Indian food",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Khānā — еда."
            },
            {
                "id": "d22_v03",
                "devanagari": "मसाला चाय",
                "transliterationIso": "Masālā chāi",
                "phoneticCyrillic": "Масаалаа чаай",
                "translationRu": "Чай со специями (масала чай)",
                "translationEn": "Spiced tea (Masala chai)",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Традиционный чай."
            }
        ],
        "exercises": [
            {
                "id": "d22_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите признание: 'Мне нравится индийская еда' (Мне + индийская еда + нравится + есть)",
                "prompt": "Мне нравится индийская еда",
                "wordChips": ["Mujhē", "Indian khānā", "pasand", "hai"],
                "correctAnswer": ["Mujhē", "Indian khānā", "pasand", "hai"],
                "phoneticCyrillicTarget": "Муджхе индиан кхаанаа пасанд хэ",
                "explanationRu": "Mujhē (мне) + Объект + pasand hai (нравится)."
            },
            {
                "id": "d22_ex02",
                "type": "substitution_drill",
                "instructionRu": "Скажите, что вам не нравится это блюдо",
                "prompt": "Mujhē yeh _____ nahī̃ hai.",
                "options": ["pasand", "shukriyā", "chaliye"],
                "correctAnswer": "pasand",
                "transliterationIsoTarget": "Mujhē yeh pasand nahī̃ hai.",
                "explanationRu": "Mujhē yeh pasand nahī̃ hai = Мне это не нравится."
            },
            {
                "id": "d22_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Хозяин отеля спрашивает: 'Kyā āpkō masālā chāi pasand hai?'. Ответьте с улыбкой за 2 секунды.",
                "prompt": "Вам нравится чай масала?",
                "options": [
                    "Hā̃! Mujhē masālā chāi bahut pasand hai!",
                    "Nahī̃, main hotel mẽ hū̃!",
                    "Kitnā time lagēgā?"
                ],
                "correctAnswer": "Hā̃! Mujhē masālā chāi bahut pasand hai!",
                "phoneticCyrillicTarget": "Хааⁿ! Муджхе масаалаа чаай бахут пасанд хэ!",
                "explanationRu": "Да, мне очень нравится чай масала!"
            },
            {
                "id": "d22_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Задайте вопрос: 'Вам нравится Дели?'",
                "prompt": "Kyā āpkō Delhi _____ hai?",
                "options": ["pasand", "chāhiye", "garam"],
                "correctAnswer": "pasand",
                "transliterationIsoTarget": "Kyā āpkō Delhi pasand hai?",
                "explanationRu": "Āpkō (вам) + Delhi + pasand hai (нравится)?"
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Беседа о впечатлениях от индийской кухни",
            "setting": "Гостиная в гестхаусе после завтрака",
            "partnerRoleRu": "Хозяйка дома",
            "learnerRoleRu": "Гостья",
            "turns": [
                {
                    "speaker": "Хозяйка",
                    "speechRu": "Доброе утро! Вам понравился индийский завтрак?",
                    "speechIso": "Namastē! Kyā āpkō Indian breakfast pasand hai?",
                    "speechCyrillic": "Намастэ! Кйаа аапко индиан брэкфаст пасанд хэ?",
                    "learnerHintRu": "Скажите: Да, мне очень нравится индийская еда! (Hā̃, mujhē Indian khānā bahut pasand hai)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Да, мне очень нравится индийская кухня! Все очень вкусно.",
                    "speechIso": "Hā̃-jī! Mujhē Indian khānā bahut pasand hai. Bahut svādishṭ hai!",
                    "speechCyrillic": "Хааⁿ-джии! Муджхе индиан кхаанаа бахут пасанд хэ. Бахут сваадишт хэ!",
                    "acceptableResponsesIso": ["Mujhē Indian khānā bahut pasand hai!"]
                },
                {
                    "speaker": "Хозяйка",
                    "speechRu": "Как приятно слышать! Еще чашечку масала чая налить?",
                    "speechIso": "Bahut acchā! Ek aur masālā chāi dū̃?",
                    "speechCyrillic": "Бахут аччхаа! Эк аур масаалаа чаай дууⁿ?",
                    "learnerHintRu": "Согласитесь с радостью: Hā̃-jī, shukriyā!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Да, пожалуйста! Большое спасибо.",
                    "speechIso": "Hā̃-jī, ek aur chāi dījiye. Shukriyā!",
                    "speechCyrillic": "Хааⁿ-джии, эк аур чаай дииджие. Шукрийа!",
                    "acceptableResponsesIso": ["Hā̃-jī, shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Искренность в индийском диалоге",
            "pointsRu": [
                "Фраза 'Mujhē Bhārat pasand hai' (Мне нравится Индия) открывает любые двери и растапливает любые сердца.",
                "Индийцы обожают расспрашивать иностранцев об их вкусах и всегда стараются угостить любимым блюдом.",
                "Конструкция с pasand употребляется как для еды, так и для городов, музыки и людей."
            ]
        }
    },

    # Day 23
    {
        "day": 23,
        "phase": 3,
        "title": {
            "en": "Billing Inquiries and Payment Settlement",
            "ru": "Расчет в ресторане: «Принесите счет» (Bill lē āiye) и «Сколько вышло?» (Kitnā huā?)"
        },
        "theme": "Принесите счет (bill lē āiye), сколько вышло (kitnā huā?), работает ли карта (card chalēgā?)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Фонетика идиоматического глагола chalēgā / чалээгаа)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Kitnā huā? = Сколько вышло? и Card chalēgā? = Карта пойдет/пройдет?)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Диалог закрытия счета: чек, безналичная оплата, сдача)",
            "phase4SimulationMinutes": "17:00–20:00 (Полная процедура оплаты обеда в кафе)"
        },
        "learningObjectives": {
            "en": [
                "Request the restaurant check using 'Bill lē āiye'",
                "Ask total cost with 'Kitnā huā?' (How much did it come to?)",
                "Verify card and digital payments with idiomatic 'Card / UPI chalēgā?'"
            ],
            "ru": [
                "Просить счет в ресторане: 'Bill lē āiye' ('Принесите счет')",
                "Спрашивать итоговую сумму: 'Kitnā huā?' ('Сколько вышло?')",
                "Проверять возможность безналичной оплаты: 'Card chalēgā?' (русское разговорное 'Карта пойдет / пройдет?')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Глагольная форма будущего времени chalēgā (चलेगा)",
            "articulatoryMechanism": "Мягкий [ч] + зубной [л] с гласным [э] + звонкий велярный [г] с долгим [аа]: [ча-лээ-гаа].",
            "russianInterferenceWarning": "Не редуцируйте гласный [э] в безударной позиции.",
            "drills": [
                {
                    "prompt": "Отработка вопроса об оплате картой",
                    "contrastPair": "Card chalēgā? (Карта пойдет / сработает?)",
                    "instructionsRu": "Произнесите связку: Card chalēgā ya cash?"
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Идиоматическое употребление глагола chalnā и вопрос Kitnā huā?",
            "russianParallel": "Поразительное сходство с русской разговорной речью: 1. 'Kitnā huā?' буквально переводится как 'Сколько вышло? / Сколько получилось?' (huā = стало, вышло). 2. Глагол chalnā (идти, двигаться) в форме 'chalēgā' абсолютно точно совпадает с русским: 'Карта пойдет?' / 'Карта пройдет?'.",
            "syntacticFormula": "Bill lē āiye + Kitnā huā? + [Card / UPI] + chalēgā?",
            "explanationRu": "В Индии невероятно развита система мгновенных платежей UPI (Google Pay / PhonePe). Вопрос 'UPI chalēgā?' поймет даже продавец кокосов на улице.",
            "pieCognateConnection": {
                "root": "*kʷel-",
                "russian": "колесо / колобродить (движение)",
                "hindi": "chalnā (идти / двигаться / работать)",
                "meaning": "Индоевропейское круговое движение и действие"
            }
        },
        "vocabulary": [
            {
                "id": "d23_v01",
                "devanagari": "ले आइए",
                "transliterationIso": "Lē āiye",
                "phoneticCyrillic": "Лее ааие",
                "translationRu": "Принесите (букв. взяв, придите)",
                "translationEn": "Please bring",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Сложный глагол: lē (взять) + āiye (придите)."
            },
            {
                "id": "d23_v02",
                "devanagari": "कितना हुआ",
                "transliterationIso": "Kitnā huā",
                "phoneticCyrillic": "Китнаа хуаа",
                "translationRu": "Сколько вышло? / Сколько получилось?",
                "translationEn": "How much did it come to? / What's the total?",
                "partOfSpeech": "phrase",
                "gender": "m",
                "audioHint": "Kitnā (сколько) + huā (вышло)."
            },
            {
                "id": "d23_v03",
                "devanagari": "चलेगा",
                "transliterationIso": "Chalēgā",
                "phoneticCyrillic": "Чалээгаа",
                "translationRu": "Пойдет? / Сработает? / Принимается?",
                "translationEn": "Will it work? / Do you accept?",
                "partOfSpeech": "verb",
                "gender": "m",
                "audioHint": "Идиоматическое 'пойдет'."
            },
            {
                "id": "d23_v04",
                "devanagari": "कार्ड",
                "transliterationIso": "Card",
                "phoneticCyrillic": "Кард",
                "translationRu": "Банковская карта",
                "translationEn": "Card",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Банковская карта."
            }
        ],
        "exercises": [
            {
                "id": "d23_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите вежливую просьбу: 'Брат, принесите счет, пожалуйста'",
                "prompt": "Принесите счет",
                "wordChips": ["Bhaiyā,", "bill", "lē", "āiye"],
                "correctAnswer": ["Bhaiyā,", "bill", "lē", "āiye"],
                "phoneticCyrillicTarget": "Бхаййаа, билл лее ааие",
                "explanationRu": "Bhaiyā, bill lē āiye = Брат, принесите счет."
            },
            {
                "id": "d23_ex02",
                "type": "substitution_drill",
                "instructionRu": "Спросите, сколько вышло к оплате",
                "prompt": "Bhaiyā, kitnā _____? (Сколько вышло?)",
                "options": ["huā", "hai", "chalēgā"],
                "correctAnswer": "huā",
                "transliterationIsoTarget": "Bhaiyā, kitnā huā?",
                "explanationRu": "Kitnā huā? = Сколько вышло?"
            },
            {
                "id": "d23_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вы хотите расплатиться банковской картой. Спросите официанта за 2 секунды.",
                "prompt": "Принимаете карты?",
                "options": [
                    "Card chalēgā?",
                    "Mērā card hai!",
                    "Card kahan hai?"
                ],
                "correctAnswer": "Card chalēgā?",
                "phoneticCyrillicTarget": "Кард чалээгаа?",
                "explanationRu": "Card chalēgā? — точный и естественный вопрос."
            },
            {
                "id": "d23_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Уточните, принимают ли оплату через UPI (Google Pay)",
                "prompt": "UPI / G-Pay _____?",
                "options": ["chalēgā", "lījiye", "chāhiye"],
                "correctAnswer": "chalēgā",
                "transliterationIsoTarget": "UPI / G-Pay chalēgā?",
                "explanationRu": "Chalēgā означает 'сработает / принимается'."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Закрытие счета и оплата картой в ресторане",
            "setting": "Завершение ужина в городском ресторане",
            "partnerRoleRu": "Официант ресторана",
            "learnerRoleRu": "Посетительница",
            "turns": [
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Брат, принесите счет, пожалуйста!",
                    "speechIso": "Bhaiyā, bill lē āiye!",
                    "speechCyrillic": "Бхаййаа, билл лее ааие!",
                    "learnerHintRu": "Попросите счет: Bhaiyā, bill lē āiye!"
                },
                {
                    "speaker": "Официант",
                    "speechRu": "Вот ваш счет, мадам. Семьсот пятьдесят рупий.",
                    "speechIso": "Lījiye bill madam. 750 rupayē.",
                    "speechCyrillic": "Лииджие билл мадам. 750 рупае.",
                    "learnerHintRu": "Спросите: Карта пойдет? (Card chalēgā?)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Сколько вышло? Банковская карта пройдет?",
                    "speechIso": "Kitnā huā? Card chalēgā?",
                    "speechCyrillic": "Китнаа хуаа? Кард чалээгаа?",
                    "acceptableResponsesIso": ["Card chalēgā?"]
                },
                {
                    "speaker": "Официант",
                    "speechRu": "Да, конечно, карточный терминал работает!",
                    "speechIso": "Hā̃-jī bilkul, card chalēgā.",
                    "speechCyrillic": "Хааⁿ-джии билкул, кард чалээгаа.",
                    "learnerHintRu": "Передайте карту: Lījiye, shukriyā!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Возьмите, пожалуйста! Большое спасибо.",
                    "speechIso": "Lījiye card. Bahut shukriyā!",
                    "speechCyrillic": "Лииджие кард. Бахут шукрийа!",
                    "acceptableResponsesIso": ["Lījiye, shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Культура чаевых и оплата в Индии",
            "pointsRu": [
                "В большинстве ресторанов в счет уже включен сервисный сбор (Service charge 5-10%).",
                "Если сбор не включен, принято оставлять около 50-100 рупий чаевых за хороший сервис.",
                "Вопрос 'Kitnā huā?' звучит предельно естественно и авторитетно."
            ]
        }
    },

    # Day 24
    {
        "day": 24,
        "phase": 3,
        "title": {
            "en": "Phase 3 Synthesis and Authentic Dhābā Dining Simulation",
            "ru": "Синтез Фазы 3: сквозная гастрономическая симуляция в индийской дхабе"
        },
        "theme": "Полный цикл: посадка, заказ безопасной воды, блюд без перца, соль, похвала, расчет",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Фонетический аудит дативных конструкций: Mujhe chahiye, Mujhe pasand hai, Garam/Thanda)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Сборка гастрономического сценария: вода + специи + похвала + счет)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Сквозной ролевой прогон заказа без единого английского слова)",
            "phase4SimulationMinutes": "17:00–20:00 (Экзаменационная гастрономическая симуляция Фазы 3)"
        },
        "learningObjectives": {
            "en": [
                "Execute complete dining transaction in spoken Hindi from seating to billing",
                "Enforce strict non-spicy dietary constraints without miscommunication",
                "Seamlessly navigate dative needs, compliments, and payments under pressure"
            ],
            "ru": [
                "Провести полный ресторанный диалог от рассадки до оплаты исключительно на хинди",
                "Четко задать диетические ограничения по остроте (binā mirch kē, tīkhā mat banāiye)",
                "Легко переключаться между дативом необходимости, комплиментами и расчетом"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Слитность и естественный темп разговорных фраз за столом",
            "articulatoryMechanism": "Свободное переключение между носовыми гласными (pānī, hū̃), придыханиями (thōṛā, tīkhā) и дативными местоимениями (mujhē).",
            "russianInterferenceWarning": "Не забывайте: в хинди глаголы стоят на конце, а отрицание mat используется только для запрета!",
            "drills": [
                {
                    "prompt": "Сквозная гастрономическая цепочка",
                    "contrastPair": "Bisleri pānī dījiye -> Tīkhā mat banāiye -> Bahut svādishṭ hai -> Bill lē āiye",
                    "instructionsRu": "Произнесите 4 ключевые фразы заказа подряд."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Консолидация экспериенциального дативного регистра",
            "russianParallel": "Фаза 3 закрепила мощнейшее преимущество русскоязычного студента: дативные субъекты 'Mujhē chāhiye' (Мне нужно) и 'Mujhē pasand hai' (Мне нравится) стали вашей второй натурой.",
            "syntacticFormula": "Mujhē + [Объект] + chāhiye / pasand hai | Bill lē āiye | Kitnā huā?",
            "explanationRu": "Теперь вы способны безопасно, вкусно и уверенно питаться в любом заведении Индии — от скромной уличной дхабы до элитного ресторана.",
            "pieCognateConnection": {
                "root": "*gʷʰer- / *swād- / *kʷel-",
                "russian": "жар / услада / колесо",
                "hindi": "garam / svādishṭ / chalēgā",
                "meaning": "Индоевропейское культурное наследие"
            }
        },
        "vocabulary": [
            {
                "id": "d24_v01",
                "devanagari": "ढाबा",
                "transliterationIso": "Dhābā",
                "phoneticCyrillic": "Дхаабаа",
                "translationRu": "Дхаба (традиционное индийское придорожное кафе)",
                "translationEn": "Dhaba (traditional roadside diner)",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Придыхательное [дх]."
            },
            {
                "id": "d24_v02",
                "devanagari": "रोटी",
                "transliterationIso": "Rotī",
                "phoneticCyrillic": "Ротии",
                "translationRu": "Лепешка роти (традиционный хлеб)",
                "translationEn": "Roti (flatbread)",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Ретрофлексный 'ṭ'."
            },
            {
                "id": "d24_v03",
                "devanagari": "दाल",
                "transliterationIso": "Dāl",
                "phoneticCyrillic": "Даал",
                "translationRu": "Дал (традиционный суп/соус из чечевицы)",
                "translationEn": "Dal (lentil curry)",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Зубной звук [д]."
            },
            {
                "id": "d24_v04",
                "devanagari": "चावल",
                "transliterationIso": "Chāval",
                "phoneticCyrillic": "Чаавал",
                "translationRu": "Рис",
                "translationEn": "Rice",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Долгое 'аа'."
            }
        ],
        "exercises": [
            {
                "id": "d24_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите полный заказ: 'Мне нужен дал, рис и лепешка роти'",
                "prompt": "Мне нужен дал, рис и роти",
                "wordChips": ["Mujhē", "dāl,", "chāval", "aur roti", "chāhiye"],
                "correctAnswer": ["Mujhē", "dāl,", "chāval", "aur roti", "chāhiye"],
                "phoneticCyrillicTarget": "Муджхе даал, чаавал аур роти чаахийе",
                "explanationRu": "Mujhē + перечисление блюд + chāhiye."
            },
            {
                "id": "d24_ex02",
                "type": "dialogue_roleplay",
                "instructionRu": "Официант спрашивает, все ли вам понравилось",
                "prompt": "Официант: Madam, khānā kaisā lagā?",
                "options": [
                    "Khānā bahut svādishṭ thā! Bill lē āiye.",
                    "Mujhē metro station jānā hai!",
                    "Main Russia sē hū̃!"
                ],
                "correctAnswer": "Khānā bahut svādishṭ thā! Bill lē āiye.",
                "phoneticCyrillicTarget": "Кхаанаа бахут сваадишт тхаа! Билл лее ааие.",
                "explanationRu": "Похвала еде + просьба принести счет."
            },
            {
                "id": "d24_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Повар собирается посыпать ваше блюдо острым красным перцем. Остановите его за 1 секунду!",
                "prompt": "Повар заносит ложку с перцем чили",
                "options": [
                    "Bhaiyā nahī̃! Mirch mat ḍāliye! Binā mirch kē!",
                    "Bahut acchā, shukriyā!",
                    "Garam pānī dījiye!"
                ],
                "correctAnswer": "Bhaiyā nahī̃! Mirch mat ḍāliye! Binā mirch kē!",
                "phoneticCyrillicTarget": "Бхаййаа нахииⁿ! Мирч мат д͟аалие! Бинаа мирч ке!",
                "explanationRu": "Мгновенная реакция запрета остроты!"
            },
            {
                "id": "d24_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Спросите о возможности оплаты наличными или картой",
                "prompt": "Kitnā huā? Card _____?",
                "options": ["chalēgā", "hai", "jāūṅgī"],
                "correctAnswer": "chalēgā",
                "transliterationIsoTarget": "Kitnā huā? Card chalēgā?",
                "explanationRu": "Card chalēgā? = Карта пройдет?"
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Экзаменационная симуляция Фазы 3: Полный обед в традиционной дхабе",
            "setting": "Аутентичная дхаба в Пенджабе или Раджастхане",
            "partnerRoleRu": "Колоритный хозяин дхабы",
            "learnerRoleRu": "Уверенная путешественница",
            "turns": [
                {
                    "speaker": "Хозяин",
                    "speechRu": "Добро пожаловать, сестра! Проходите, садитесь! Что вам принести?",
                    "speechIso": "Namastē madam! Āiye baithiye! Kyā chāhiye?",
                    "speechCyrillic": "Намастэ мадам! Ааие бэтхие! Кйаа чаахийе?",
                    "learnerHintRu": "Закажите запечатанную воду и дал с рисом без перца: Bisleri pānī aur dāl chāval, binā mirch kē"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте! Мне нужна бутылка воды Bisleri, дал и рис. Пожалуйста, совсем без перца!",
                    "speechIso": "Namastē! Ek Bisleri pānī, dāl aur chāval chāhiye. Binā mirch kē!",
                    "speechCyrillic": "Намастэ! Эк Бислери паании, даал аур чаавал чаахийе. Бинаа мирч ке!",
                    "acceptableResponsesIso": ["Bisleri pānī aur dāl chāval chāhiye, binā mirch kē"]
                },
                {
                    "speaker": "Хозяин",
                    "speechRu": "Понял! Готовим совсем не остро. Вот горячая еда!",
                    "speechIso": "Bilkul tīkhā nahī̃ banāyā. Lījiye garam khānā!",
                    "speechCyrillic": "Билкул тиикхаа нахииⁿ банаайаа. Лииджие гарам кхаанаа!",
                    "learnerHintRu": "Попробуйте и похвалите: Bahut svādishṭ hai! Принесите счет."
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Очень вкусно! Большое спасибо. Брат, принесите счет.",
                    "speechIso": "Bahut svādishṭ hai! Shukriyā. Bhaiyā, bill lē āiye.",
                    "speechCyrillic": "Бахут сваадишт хэ! Шукрийа. Бхаййаа, билл лее ааие.",
                    "acceptableResponsesIso": ["Bahut svādishṭ hai! Bill lē āiye."]
                },
                {
                    "speaker": "Хозяин",
                    "speechRu": "Всего двести пятьдесят рупий, сестра.",
                    "speechIso": "Sirf 250 rupayē madam.",
                    "speechCyrillic": "Сирф 250 рупае мадам.",
                    "learnerHintRu": "Отдайте оплату со словами: Paisē lījiye, bahut dhanyavād!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Возьмите деньги, спасибо большое!",
                    "speechIso": "Paisē lījiye, bahut dhanyavād!",
                    "speechCyrillic": "Пэсе лииджие, бахут дханьяваад!",
                    "acceptableResponsesIso": ["Paisē lījiye, shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Итоги Фазы 3: Полная автономия в питании",
            "pointsRu": [
                "Вы освоили фундаментальную дативную грамматику (Mujhē chāhiye, Mujhē pasand hai).",
                "Вы умеете управлять безопасностью питания (бутилированная вода, горячая еда, запрет чили).",
                "Вы умеете благодарить персонал и закрывать счета без единого слова по-английски."
            ]
        }
    }
]
