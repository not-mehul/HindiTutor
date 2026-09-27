"""
data_phase4.py - Days 25 to 32
Phase 4: Commercial Negotiations, Numbers, and Market Dynamics
"""

DAYS_PHASE_4 = [
    # Day 25
    {
        "day": 25,
        "phase": 4,
        "title": {
            "en": "Numerical Framework 1–20",
            "ru": "Числовая система от 1 до 20: Индоевропейские числовые параллели"
        },
        "theme": "Счет от 1 до 20: когнаты dva/do, tri/tīn, pyat'/pāñch, desyat'/das",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Фонетика чисел: pāñch с назализацией, chhah с придыханием, gyārah/bārah)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Этимологическое сопоставление русских и хинди числительных)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Быстрый счет от 1 до 20, случайные числа, счет предметов)",
            "phase4SimulationMinutes": "17:00–20:00 (Покупка фруктов поштучно на уличном лотке)"
        },
        "learningObjectives": {
            "en": [
                "Count fluently from 1 to 20 in spoken Hindi",
                "Leverage Proto-Indo-European cognates (Do = Два, Tīn = Три, Pāñch = Пять, Das = Десять)",
                "Identify quantities and item counts without hesitation"
            ],
            "ru": [
                "Свободно считать от 1 до 20 на разговорном хинди",
                "Опираться на праиндоевропейские числовые корни (Do = Два, Tīn = Три, Pāñch = Пять, Das = Десять)",
                "Мгновенно называть и распознавать количество предметов"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Назализованный гласный /ā̃/ в pāñch (पाँच) и придыхание в chhah (छह)",
            "articulatoryMechanism": "В слове pāñch носовой гласный [паанч] переходит в аффрикату [ч]. В слове chhah придыхательный [чх] завершается гортанным выдохом [ах].",
            "russianInterferenceWarning": "Не забывайте носовой звук в числе 5 (pāñch) — это не просто 'панч'.",
            "drills": [
                {
                    "prompt": "Счет от 1 до 5",
                    "contrastPair": "Ek, Do, Tīn, Chār, Pāñch",
                    "instructionsRu": "Считайте вслух, отстукивая ритм пальцами."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Индоевропейская числовая система",
            "russianParallel": "Славянские и индоарийские языки сохранили древнейшую систему счета: Два = Do; Три = Tīn; Пять = Pāñch; Десять = Das. Числа от 11 до 20 построены как сложение основы с десятком: Bārah (12 = два-дцать/две-на-дцать), Tērah (13 = три-на-дцать).",
            "syntacticFormula": "[Числительное] + [Существительное]",
            "explanationRu": "В отличие от русского языка, где существительное после числительных меняет падеж (2 книги, 5 книг), в разговорном хинди существительное часто остается в прямой форме: Do bottle, Pāñch samosa.",
            "pieCognateConnection": {
                "root": "*dwóh₁ / *tréyes / *pénkʷe / *déḱm̥t",
                "russian": "два / три / пять / десять",
                "hindi": "do / tīn / pāñch / das",
                "meaning": "Праиндоевропейские базовые числительные"
            }
        },
        "vocabulary": [
            {
                "id": "d25_v01",
                "devanagari": "एक, दो, तीन, चार, पाँच",
                "transliterationIso": "Ek, Do, Tīn, Chār, Pāñch",
                "phoneticCyrillic": "Эк, До, Тиин, Чаар, Паанч",
                "translationRu": "1, 2, 3, 4, 5",
                "translationEn": "1, 2, 3, 4, 5",
                "partOfSpeech": "numeral",
                "gender": "n/a",
                "audioHint": "Числа от 1 до 5."
            },
            {
                "id": "d25_v02",
                "devanagari": "छह, सात, आठ, नौ, दस",
                "transliterationIso": "Chhah, Sāt, Āṭh, Nau, Das",
                "phoneticCyrillic": "Чхэх, Саат, Аатх, Нау, Дас",
                "translationRu": "6, 7, 8, 9, 10",
                "translationEn": "6, 7, 8, 9, 10",
                "partOfSpeech": "numeral",
                "gender": "n/a",
                "audioHint": "Числа от 6 до 10."
            },
            {
                "id": "d25_v03",
                "devanagari": "ग्यारह, बारह, पंद्रह, बीस",
                "transliterationIso": "Gyārah (11), Bārah (12), Pandrah (15), Bīs (20)",
                "phoneticCyrillic": "Гйаарах, Баарах, Панндрах, Биис",
                "translationRu": "11, 12, 15, 20",
                "translationEn": "11, 12, 15, 20",
                "partOfSpeech": "numeral",
                "gender": "n/a",
                "audioHint": "Ключевые числа второго десятка."
            }
        ],
        "exercises": [
            {
                "id": "d25_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите заказ: 'Дайте два чая и две бутылки воды'",
                "prompt": "Дайте два чая и две воды",
                "wordChips": ["Do", "chāi", "aur do", "pānī", "dījiye"],
                "correctAnswer": ["Do", "chāi", "aur do", "pānī", "dījiye"],
                "phoneticCyrillicTarget": "До чаай аур до паании дииджие",
                "explanationRu": "Числительное стоит перед существительным: Do chāi."
            },
            {
                "id": "d25_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Продавец спрашивает, сколько манго вам взвесить. Ответьте за 2 секунды: 'Пять штук!'",
                "prompt": "Kitnē mango madam?",
                "options": ["Pāñch mango dījiye!", "Das hotel hai!", "Main pāñch hū̃!"],
                "correctAnswer": "Pāñch mango dījiye!",
                "phoneticCyrillicTarget": "Паанч манго дииджие!",
                "explanationRu": "Pāñch = пять."
            },
            {
                "id": "d25_ex03",
                "type": "substitution_drill",
                "instructionRu": "Назовите число 10 (когнат с русским 'десять')",
                "prompt": "У меня есть _____ рупий (10)",
                "options": ["das", "tīn", "ek"],
                "correctAnswer": "das",
                "transliterationIsoTarget": "Das rupayē",
                "explanationRu": "Das = 10."
            },
            {
                "id": "d25_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Вставьте число 20 в фразу '20 рупий'",
                "prompt": "_____ rupayē (20 рупий)",
                "options": ["Bīs", "Do", "Bārah"],
                "correctAnswer": "Bīs",
                "transliterationIsoTarget": "Bīs rupayē",
                "explanationRu": "Bīs = 20."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Покупка фруктов на уличном лотке",
            "setting": "Фруктовая лавка на вечернем базаре",
            "partnerRoleRu": "Продавец фруктов",
            "learnerRoleRu": "Покупательница",
            "turns": [
                {
                    "speaker": "Продавец",
                    "speechRu": "Здравствуйте! Свежие бананы и апельсины. Сколько вам дать?",
                    "speechIso": "Namastē madam! Fresh bananas! Kitnē chāhiye?",
                    "speechCyrillic": "Намастэ мадам! Фрэш бананас! Китнее чаахийе?",
                    "learnerHintRu": "Скажите: Дайте четыре банана (Chār banana dījiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте! Дайте четыре банана и два апельсина.",
                    "speechIso": "Namastē! Chār banana aur do orange dījiye.",
                    "speechCyrillic": "Намастэ! Чаар банана аур до ориндж дииджие.",
                    "acceptableResponsesIso": ["Chār banana dījiye", "Do orange dījiye"]
                },
                {
                    "speaker": "Продавец",
                    "speechRu": "Вот, пожалуйста, держите. Всего двадцать рупий.",
                    "speechIso": "Lījiye madam. Total bīs rupayē.",
                    "speechCyrillic": "Лииджие мадам. Тотал биис рупае.",
                    "learnerHintRu": "Отдайте оплату: Bīs rupayē lījiye, shukriyā!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Возьмите двадцать рупий, спасибо!",
                    "speechIso": "Bīs rupayē lījiye, shukriyā!",
                    "speechCyrillic": "Биис рупае лииджие, шукрийа!",
                    "acceptableResponsesIso": ["Lījiye, shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Счет жестами на индийском базаре",
            "pointsRu": [
                "В Индии часто считают фаланги пальцев большим пальцем (до 12 на одной руке), а не просто загибают пальцы.",
                "Произнесение числительных на хинди (Do, Chār, Das) сразу отсекает наценку для 'наивных туристов'.",
                "Число 12 (Bārah) часто используется как мера счета (дюжина бананов — ek dozen)."
            ]
        }
    },

    # Day 26
    {
        "day": 26,
        "phase": 4,
        "title": {
            "en": "Numerical Scaling: Tens, Hundreds, and Thousands",
            "ru": "Масштабирование чисел: десятки, сотни (Sau) и тысячи (Hazār)"
        },
        "theme": "50 (pachās), 100 (sau), 200 (do sau), 500 (pāñch sau), 1000 (hazār), рупии",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Фонетика sau / сау и hazār / хазаар)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Сложные числительные: точная копия русской модели Двести = Do sau, Пятьсот = Pāñch sau)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Называние цен: 150 рупий, 300 рупий, 1200 рупий)",
            "phase4SimulationMinutes": "17:00–20:00 (Распознавание цен на текстиль и сувениры)"
        },
        "learningObjectives": {
            "en": [
                "Master hundred and thousand compounds (Sau, Hazār)",
                "Identify retail currency values in Rupees effortlessly",
                "Understand the identical compound structure with Russian сотни (Do sau = Двести)"
            ],
            "ru": [
                "Освоить образование сотен и тысяч (Sau = сто, Hazār = тысяча)",
                "Мгновенно распознавать на слух любые денежные суммы в рупиях",
                "Опираться на идентичную русскую модель сложения сотен (Do sau = двести, Pāñch sau = пятьсот)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Дифтонгоид /au/ в sau (सौ) и звонкий /z/ в hazār (हज़ार)",
            "articulatoryMechanism": "В слове sau звук [с] переходит в дифтонг [ау]: [сау]. В hazār четкий звонкий русский [з] и долгое [аа]: [хазаар].",
            "russianInterferenceWarning": "Не оглушайте 'z' в слове hazār (не хасар!).",
            "drills": [
                {
                    "prompt": "Сотни и тысячи",
                    "contrastPair": "Ek sau (100) vs Ek hazār (1000)",
                    "instructionsRu": "Произнесите парно: [эк сау] — [эк хазаар]."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Составные числительные (Сотни и тысячи)",
            "russianParallel": "Хинди образует сотни АБСОЛЮТНО так же, как русский язык: Две + сти = Do + sau (200); Пять + сот = Pāñch + sau (500); Одна + тысяча = Ek + hazār (1000). 150 = Ek sau pachās (Сто пятьдесят). Никакой грамматической сложности!",
            "syntacticFormula": "[Количество] + sau (сотен) / hazār (тысяч) + [десятки] + rupayē",
            "explanationRu": "Эта прозрачная логика позволяет русскоязычному человеку освоить любые ценники за 5 минут практики.",
            "pieCognateConnection": {
                "root": "*ḱm̥tóm",
                "russian": "сто / сотня",
                "hindi": "shat (санскр.) / sau (разг. хинди)",
                "meaning": "Праиндоевропейская сотня"
            }
        },
        "vocabulary": [
            {
                "id": "d26_v01",
                "devanagari": "सौ",
                "transliterationIso": "Sau",
                "phoneticCyrillic": "Сау",
                "translationRu": "Сто (100)",
                "translationEn": "Hundred (100)",
                "partOfSpeech": "numeral",
                "gender": "n/a",
                "audioHint": "Дифтонгоид [сау]."
            },
            {
                "id": "d26_v02",
                "devanagari": "हज़ार",
                "transliterationIso": "Hazār",
                "phoneticCyrillic": "Хазаар",
                "translationRu": "Тысяча (1000)",
                "translationEn": "Thousand (1000)",
                "partOfSpeech": "numeral",
                "gender": "n/a",
                "audioHint": "Звонкое 'з', долгое 'аа'."
            },
            {
                "id": "d26_v03",
                "devanagari": "पचास",
                "transliterationIso": "Pachās",
                "phoneticCyrillic": "Пачаас",
                "translationRu": "Пятьдесят (50)",
                "translationEn": "Fifty (50)",
                "partOfSpeech": "numeral",
                "gender": "n/a",
                "audioHint": "Долгое 'аа' во втором слоге."
            },
            {
                "id": "d26_v04",
                "devanagari": "पचीस",
                "transliterationIso": "Pachīs",
                "phoneticCyrillic": "Пачиис",
                "translationRu": "Двадцать пять (25)",
                "translationEn": "Twenty-five (25)",
                "partOfSpeech": "numeral",
                "gender": "n/a",
                "audioHint": "Долгое 'ии'."
            }
        ],
        "exercises": [
            {
                "id": "d26_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите сумму: 'Пятьсот рупий' (Пять + сотен + рупий)",
                "prompt": "500 рупий",
                "wordChips": ["Pāñch", "sau", "rupayē"],
                "correctAnswer": ["Pāñch", "sau", "rupayē"],
                "phoneticCyrillicTarget": "Паанч сау рупае",
                "explanationRu": "Pāñch sau = 500."
            },
            {
                "id": "d26_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вам называют цену: 'Ek sau pachās rupayē'. Сколько это в цифрах за 2 секунды?",
                "prompt": "Ek sau pachās rupayē",
                "options": ["150 рупий", "250 рупий", "500 рупий"],
                "correctAnswer": "150 рупий",
                "phoneticCyrillicTarget": "150",
                "explanationRu": "Ek sau (100) + pachās (50) = 150 рупий."
            },
            {
                "id": "d26_ex03",
                "type": "substitution_drill",
                "instructionRu": "Назовите сумму 'Одна тысяча рупий'",
                "prompt": "Ek _____ rupayē (1000)",
                "options": ["hazār", "sau", "das"],
                "correctAnswer": "hazār",
                "transliterationIsoTarget": "Ek hazār rupayē",
                "explanationRu": "Hazār = тысяча."
            },
            {
                "id": "d26_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Назовите число 200 (Двести)",
                "prompt": "_____ sau (200)",
                "options": ["Do", "Ek", "Tīn"],
                "correctAnswer": "Do",
                "transliterationIsoTarget": "Do sau",
                "explanationRu": "Do sau = 200 (двести)."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Уточнение ценника на сувенирный палантин",
            "setting": "Магазин кашемира и текстиля",
            "partnerRoleRu": "Продавец платков",
            "learnerRoleRu": "Покупательница",
            "turns": [
                {
                    "speaker": "Продавец",
                    "speechRu": "Посмотрите, мадам, настоящий пашминовый платок! Отличная цена.",
                    "speechIso": "Dēkhiye madam, pure pashmina shawl! Bahut acchā price.",
                    "speechCyrillic": "Дэкхие мадам, пьюр пашмина шол! Бахут аччхаа прайс.",
                    "learnerHintRu": "Спросите: Сколько сотен рупий это стоит? (Kitnē rupayē?)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Сколько стоит этот платок?",
                    "speechIso": "Yeh kitnē kā hai? Kitnē rupayē?",
                    "speechCyrillic": "Йе китнее каа хэ? Китнее рупае?",
                    "acceptableResponsesIso": ["Yeh kitnē kā hai?"]
                },
                {
                    "speaker": "Продавец",
                    "speechRu": "Всего одна тысяча пятьсот рупий, мадам.",
                    "speechIso": "Sirf ek hazār pāñch sau rupayē, madam.",
                    "speechCyrillic": "Сирф эк хазаар паанч сау рупае, мадам.",
                    "learnerHintRu": "Повторите цену с удивлением: Ek hazār pāñch sau?! (1500 рупий?!)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Одна тысяча пятьсот рупий?! Это слишком дорого!",
                    "speechIso": "Ek hazār pāñch sau rupayē?! Bahut mahangā hai!",
                    "speechCyrillic": "Эк хазаар паанч сау рупае?! Бахут махангаа хэ!",
                    "acceptableResponsesIso": ["Ek hazār pāñch sau rupayē?!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Купюры индийской рупии",
            "pointsRu": [
                "Самые ходовые банкноты: 10, 20, 50, 100, 200 и 500 рупий.",
                "Купюра в 2000 рупий была изъята из обращения — если вам пытаются ее дать, категорически отказывайтесь ('Nahī̃ chāhiye').",
                "Всегда проверяйте сдачу с крупных купюр в 500 рупий."
            ]
        }
    },

    # Day 27
    {
        "day": 27,
        "phase": 4,
        "title": {
            "en": "Inquiring About Prices and Merchandise",
            "ru": "Запрос цены: «Почём это?» (Yeh kitnē kā hai?) и «Это дорого» (Mahangā)"
        },
        "theme": "Сколько это стоит (Yeh kitnē kā hai?), какая цена (kyā dām hai?), очень дорого (bahut mahangā hai)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция придыхательного h в mahangā / махангаа)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Послелог kā/kī/kē в согласовании цены: Yeh kitnē kā hai? = Почём это?)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Быстрый опрос цен: это почём? то почём? сколько стоит?)",
            "phase4SimulationMinutes": "17:00–20:00 (Первичный мониторинг цен в сувенирной лавке)"
        },
        "learningObjectives": {
            "en": [
                "Ask prices using genitive formula 'Yeh kitnē kā hai?'",
                "Inquire about cost with dām / kīmat",
                "Express price shock with 'Bahut mahangā hai!' (Very expensive!)"
            ],
            "ru": [
                "Спрашивать цену через формулу согласовательного родительного: 'Yeh kitnē kā hai?' (букв. 'Это со скольки? / Почём это?')",
                "Уточнять стоимость словами dām (цена) и kīmat (стоимость)",
                "Реагировать на завышенную цену фразой 'Bahut mahangā hai!' ('Это очень дорого!')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Звуковой переход /h/ и назализация в слове mahangā (महँगा)",
            "articulatoryMechanism": "Легкий выдох [х] с одновременным носовым резонансом на втором слоге: [ма-хан-гаа].",
            "russianInterferenceWarning": "Не оглушайте звук [г] на конце слова. Должно звучать звонкое долгое [гаа].",
            "drills": [
                {
                    "prompt": "Отработка возмущения ценой",
                    "contrastPair": "Bahut mahangā hai! (Очень дорого!)",
                    "instructionsRu": "Произнесите с экспрессивной интонацией удивления."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Родительный согласовательный вопрос цены (Kitnē kā)",
            "russianParallel": "Фраза 'Yeh kitnē kā hai?' буквально переводится как 'Это почём? / Это со скольки рупий?'. Послелог kā согласуется с опущенным мужским словом rupayē (рупии во мн.ч. -> kitnē kā / kitnē kē).",
            "syntacticFormula": "[Yeh / Voh] + kitnē kā hai? / Kyā dām hai?",
            "explanationRu": "Любой торговец на индийском базаре сразу понимает, что перед ним опытный путешественник, как только слышит чистое 'Yeh kitnē kā hai?' вместо английского 'How much?'.",
            "pieCognateConnection": {
                "root": "*meh₂-",
                "russian": "мера / мерить / махина (большой)",
                "hindi": "mahangā (высокая мера / дорогой)",
                "meaning": "Индоевропейская мера ценности"
            }
        },
        "vocabulary": [
            {
                "id": "d27_v01",
                "devanagari": "कितने का",
                "transliterationIso": "Kitnē kā",
                "phoneticCyrillic": "Китнее каа",
                "translationRu": "Почём? / Сколько стоит?",
                "translationEn": "For how much? / What is the cost?",
                "partOfSpeech": "phrase",
                "gender": "m",
                "audioHint": "Универсальный вопрос цены."
            },
            {
                "id": "d27_v02",
                "devanagari": "दाम",
                "transliterationIso": "Dām",
                "phoneticCyrillic": "Даам",
                "translationRu": "Цена",
                "translationEn": "Price",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Долгое 'аа', зубное 'д'."
            },
            {
                "id": "d27_v03",
                "devanagari": "महँगा",
                "transliterationIso": "Mahangā",
                "phoneticCyrillic": "Махангаа",
                "translationRu": "Дорогой / Дорого",
                "translationEn": "Expensive",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Ударение на второй слог."
            },
            {
                "id": "d27_v04",
                "devanagari": "कीमत",
                "transliterationIso": "Kīmat",
                "phoneticCyrillic": "Киимат",
                "translationRu": "Стоимость",
                "translationEn": "Cost / Value",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Долгое 'ии'."
            }
        ],
        "exercises": [
            {
                "id": "d27_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите вопрос: 'Сколько стоит этот шарф?' (Этот шарф + почём + есть?)",
                "prompt": "Почём этот шарф?",
                "wordChips": ["Yeh", "scarf", "kitnē", "kā", "hai?"],
                "correctAnswer": ["Yeh", "scarf", "kitnē", "kā", "hai?"],
                "phoneticCyrillicTarget": "Йе скарф китнее каа хэ?",
                "explanationRu": "Yeh scarf kitnē kā hai? — классический вопрос на рынке."
            },
            {
                "id": "d27_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Продавец заломил 2000 рупий за простую футболку. Возмутитесь за 2 секунды: 'Очень дорого!'",
                "prompt": "Продавец: 2000 rupees madam!",
                "options": [
                    "Bhaiyā, bahut mahangā hai!",
                    "Bahut svādishṭ hai!",
                    "Main ṭhīk hū̃!"
                ],
                "correctAnswer": "Bhaiyā, bahut mahangā hai!",
                "phoneticCyrillicTarget": "Бхаййаа, бахут махангаа хэ!",
                "explanationRu": "Bahut mahangā hai! — Это очень дорого!"
            },
            {
                "id": "d27_ex03",
                "type": "substitution_drill",
                "instructionRu": "Спросите: 'Какая цена?'",
                "prompt": "Kyā _____ hai?",
                "options": ["dām", "nām", "kamrā"],
                "correctAnswer": "dām",
                "transliterationIsoTarget": "Kyā dām hai?",
                "explanationRu": "Kyā dām hai? = Какая цена?"
            },
            {
                "id": "d27_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Спросите о цене вон того дальнего предмета",
                "prompt": "_____ kitnē kā hai? (Тот почём?)",
                "options": ["Voh", "Main", "Mujhē"],
                "correctAnswer": "Voh",
                "transliterationIsoTarget": "Voh kitnē kā hai?",
                "explanationRu": "Voh = тот (вдали)."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Приценивание на ремесленном базаре",
            "setting": "Рыночный ряд в Чанди Чоук (Дели)",
            "partnerRoleRu": "Продавец резных фигурок слонов",
            "learnerRoleRu": "Любознательная покупательница",
            "turns": [
                {
                    "speaker": "Продавец",
                    "speechRu": "Здравствуйте, мадам! Посмотрите, деревянный слоник ручной работы!",
                    "speechIso": "Namastē madam! Handmade elephant dēkhiye.",
                    "speechCyrillic": "Намастэ мадам! Хэндмейд элефант дэкхие.",
                    "learnerHintRu": "Спросите цену: Bhaiyā, yeh kitnē kā hai?"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте! Брат, почём этот слоник?",
                    "speechIso": "Namastē! Bhaiyā, yeh kitnē kā hai?",
                    "speechCyrillic": "Намастэ! Бхаййаа, йе китнее каа хэ?",
                    "acceptableResponsesIso": ["Yeh kitnē kā hai?", "Kyā dām hai?"]
                },
                {
                    "speaker": "Продавец",
                    "speechRu": "Для вас особая цена — восемьсот рупий!",
                    "speechIso": "Āpkē liye special price — 800 rupayē!",
                    "speechCyrillic": "Аапке лие спэшл прайс — 800 рупае!",
                    "learnerHintRu": "Отреагируйте с улыбкой: Ого! Это слишком дорого! (Bahut mahangā hai!)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Ого! Восемьсот рупий?! Это очень дорого!",
                    "speechIso": "Āṭh sau rupayē?! Bahut mahangā hai!",
                    "speechCyrillic": "Аатх сау рупае?! Бахут махангаа хэ!",
                    "acceptableResponsesIso": ["Bahut mahangā hai!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Правила ценообразования на индийском рынке",
            "pointsRu": [
                "Первоначальная названная цена на базаре почти всегда завышена в 2-3 раза для иностранцев.",
                "Восклицание 'Bahut mahangā hai!' — обязательный первый шаг в ритуале индийского торга.",
                "Торговец никогда не обижается на фразу 'Mahangā hai' — для него это сигнал к началу увлекательного диалога."
            ]
        }
    },

    # Day 28
    {
        "day": 28,
        "phase": 4,
        "title": {
            "en": "Bargaining Strategies and Price Negotiation",
            "ru": "Стратегии торга: «Скиньте цену» (Kam kījiye) и «Назовите честную цену»"
        },
        "theme": "Слишком много (bahut zyādā hai), сделайте дешевле (kam kījiye), назовите честную цену (sahī dām lagāiye), дешево (sastā)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция kam kījiye и sahī dām)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Формулы сбивания цены: Thōṛā kam kījiye = Скиньте немного; Sahī dām lagāiye = Дайте реальную цену)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Парный раунд торга: завышенная цена -> возмущение -> предложение своей цены)",
            "phase4SimulationMinutes": "17:00–20:00 (Реалистичный торг за сувениры на базаре)"
        },
        "learningObjectives": {
            "en": [
                "Negotiate assertively using 'Bahut zyādā hai!' and 'Kam kījiye'",
                "Demand fair pricing with 'Sahī dām lagāiye'",
                "Propose counter-offers courteously with target amounts"
            ],
            "ru": [
                "Уверенно торговаться фразами 'Bahut zyādā hai!' ('Слишком много!') и 'Kam kījiye' ('Сделайте дешевле / Скиньте')",
                "Требовать честную цену: 'Sahī dām lagāiye' ('Назовите правильную/справедливую цену')",
                "Предлагать свою цену в уважительном и доброжелательном тоне"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Зубной звук /s/ и долгое /ī/ в слове sahī (सही)",
            "articulatoryMechanism": "Чистый глухой [с] + легкий выдох [х] с долгим гласным [ии]: [са-хии]. Значит 'правильный, справедливый'.",
            "russianInterferenceWarning": "Не проглатывайте звук [х] в слове sahī.",
            "drills": [
                {
                    "prompt": "Отработка призыва к справедливости",
                    "contrastPair": "Sahī dām lagāiye (Назовите справедливую цену)",
                    "instructionsRu": "Произнесите спокойно и авторитетно."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Императивные формулы торга (Kam kījiye)",
            "russianParallel": "Снова работает наш вежливый суффикс -iye (русское -ите): Kam (мало/меньше) + kījiye (сделайте) = Сделайте подешевле / Скиньте. 'Thōṛā kam kījiye' = Скиньте чуть-чуть. Глагол lagānā в 'dām lagāiye' означает 'назначьте / примените цену'.",
            "syntacticFormula": "[Bahut zyādā hai] + [Kam kījiye / Sahī dām lagāiye] + [Своя сумма + dījiye]",
            "explanationRu": "Торг на индийском рынке — это не драка, а дружелюбный театр. Улыбка, спокойствие и точные фразы на хинди снижают цену ровно вдвое.",
            "pieCognateConnection": {
                "root": "*seh₂-",
                "russian": "суть / сытый (истинный)",
                "hindi": "sahī (правильный / честный)",
                "meaning": "Праиндоевропейская истина и верность"
            }
        },
        "vocabulary": [
            {
                "id": "d28_v01",
                "devanagari": "कम कीजिए",
                "transliterationIso": "Kam kījiye",
                "phoneticCyrillic": "Кам кииджие",
                "translationRu": "Сделайте подешевле / Скиньте цену",
                "translationEn": "Lower it, please / Give a discount",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Kam (мало) + kījiye (сделайте)."
            },
            {
                "id": "d28_v02",
                "devanagari": "सही दाम लगाइए",
                "transliterationIso": "Sahī dām lagāiye",
                "phoneticCyrillic": "Сахии даам лагааие",
                "translationRu": "Назовите честную (справедливую) цену",
                "translationEn": "Quote a fair price",
                "partOfSpeech": "phrase",
                "gender": "both",
                "audioHint": "Ключевая фраза опытных покупателей."
            },
            {
                "id": "d28_v03",
                "devanagari": "सस्ता",
                "transliterationIso": "Sastā",
                "phoneticCyrillic": "Састаа",
                "translationRu": "Дешёвый / Недорогой",
                "translationEn": "Cheap / Inexpensive",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Долгое 'аа' на конце."
            },
            {
                "id": "d28_v04",
                "devanagari": "बहुत ज़्यादा",
                "transliterationIso": "Bahut zyādā",
                "phoneticCyrillic": "Бахут зйаадаа",
                "translationRu": "Слишком много / Чересчур",
                "translationEn": "Too much",
                "partOfSpeech": "phrase",
                "gender": "n/a",
                "audioHint": "Выражение протеста против цены."
            }
        ],
        "exercises": [
            {
                "id": "d28_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите формулу торга: 'Брат, это слишком много! Скиньте немного'",
                "prompt": "Слишком много, скиньте немного",
                "wordChips": ["Bahut", "zyādā", "hai,", "thōṛā", "kam", "kījiye!"],
                "correctAnswer": ["Bahut", "zyādā", "hai,", "thōṛā", "kam", "kījiye!"],
                "phoneticCyrillicTarget": "Бахут зйаадаа хэ, тхоор͟аа кам кииджие!",
                "explanationRu": "Классическая связка торга: Bahut zyādā hai, thōṛā kam kījiye!"
            },
            {
                "id": "d28_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Продавец просит 1000 рупий. Потребуйте назвать честную цену за 2 секунды.",
                "prompt": "Продавец: 1000 rupees last price!",
                "options": [
                    "Nahī̃ bhaiyā, sahī dām lagāiye!",
                    "Hā̃ bhaiyā, lījiye 1000!",
                    "Station kahā̃ hai?"
                ],
                "correctAnswer": "Nahī̃ bhaiyā, sahī dām lagāiye!",
                "phoneticCyrillicTarget": "Нахииⁿ бхаййаа, сахии даам лагааие!",
                "explanationRu": "Sahī dām lagāiye = Назовите честную цену!"
            },
            {
                "id": "d28_ex03",
                "type": "substitution_drill",
                "instructionRu": "Предложите забрать товар за 300 рупий (300 рупий + дайте)",
                "prompt": "Tīn sau rupayē _____! (Отдайте за 300)",
                "options": ["dījiye", "lījiye", "chaliye"],
                "correctAnswer": "dījiye",
                "transliterationIsoTarget": "Tīn sau rupayē dījiye!",
                "explanationRu": "Tīn sau rupayē dījiye = Отдайте за 300 рупий."
            },
            {
                "id": "d28_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Скажите, что вам нужен товар подешевле",
                "prompt": "Mujhē _____ chāhiye. (Мне нужен дешевый)",
                "options": ["sastā", "mahangā", "tīkhā"],
                "correctAnswer": "sastā",
                "transliterationIsoTarget": "Mujhē sastā chāhiye.",
                "explanationRu": "Sastā = дешевый."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Настоящий торг за шелковый платок на базаре",
            "setting": "Текстильная лавка на базаре Джодхпура",
            "partnerRoleRu": "Азартный продавец платков",
            "learnerRoleRu": "Опытная покупательница",
            "turns": [
                {
                    "speaker": "Продавец",
                    "speechRu": "Мадам, прекрасный платок! Шестьсот рупий.",
                    "speechIso": "Chhah sau rupayē madam, best price!",
                    "speechCyrillic": "Чхэх сау рупае мадам, бэст прайс!",
                    "learnerHintRu": "Возмутитесь: Слишком много! Скиньте, отдайте за 300! (Bahut zyādā hai! Tīn sau dījiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Нет, брат! Это слишком дорого. Назовите честную цену. Триста рупий!",
                    "speechIso": "Nahī̃ bhaiyā! Bahut zyādā hai. Sahī dām lagāiye. Tīn sau rupayē dījiye!",
                    "speechCyrillic": "Нахииⁿ бхаййаа! Бахут зйаадаа хэ. Сахии даам лагааие. Тиин сау рупае дииджие!",
                    "acceptableResponsesIso": ["Bahut zyādā hai! Tīn sau rupayē dījiye!"]
                },
                {
                    "speaker": "Продавец",
                    "speechRu": "Триста?! Нет, так нельзя. Давайте четыреста рупий?",
                    "speechIso": "Tīn sau nahī̃ madam! Chār sau rupayē final.",
                    "speechCyrillic": "Тиин сау нахииⁿ мадам! Чаар сау рупае файнал.",
                    "learnerHintRu": "Согласитесь на 350: Sāṛhē tīn sau (350) ṭhīk hai? Chaliye pack kījiye!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Триста пятьдесят рупий, договорились? Заворачивайте!",
                    "speechIso": "350 rupayē, ṭhīk hai? Pack kar dījiye!",
                    "speechCyrillic": "350 рупае, т͟хиик хэ? Пэк кар дииджие!",
                    "acceptableResponsesIso": ["Ṭhīk hai, pack kījiye!"]
                },
                {
                    "speaker": "Продавец",
                    "speechRu": "Ладно, мадам, вы умеете торговаться! Забирайте.",
                    "speechIso": "Ṭhīk hai madam, lījiye!",
                    "speechCyrillic": "Т͟хиик хэ мадам, лииджие!",
                    "learnerHintRu": "Поблагодарите с улыбкой: Bahut shukriyā bhaiyā!"
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Искусство 'Ухода' (The Walk-Away Technique)",
            "pointsRu": [
                "Если продавец не уступает, вежливо улыбнитесь, скажите 'Shukriyā bhaiyā' и сделайте вид, что уходите.",
                "В 80% случаев продавец крикнет вам вслед: 'Madam, suniye! Āiye, le lījiye!' (Мадам, послушайте! Идите сюда, забирайте за вашу цену!).",
                "Торговаться нужно всегда с доброй улыбкой, превращая процесс в позитивную игру."
            ]
        }
    },

    # Day 29
    {
        "day": 29,
        "phase": 4,
        "title": {
            "en": "Adjectival Modifiers: Dimensions and Condition",
            "ru": "Качественные прилагательные: размер (Большой/Маленький) и состояние"
        },
        "theme": "Большой (baṛā/baṛī), маленький (chhōṭā/chhōṭī), испорченный/брак (kharāb), новый (nayā), старый (purānā)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция ретрофлексного flap ṛ в baṛā и придыхательного chh в chhōṭā)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Родовое согласование прилагательных: -ā для мужского рода, -ī для женского рода)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Пары: большой размер, маленькая сумка, бракованная вещь, новая вещь)",
            "phase4SimulationMinutes": "17:00–20:00 (Проверка качества одежды и отбраковка дефектов)"
        },
        "learningObjectives": {
            "en": [
                "Apply gender-concordant dimension adjectives (baṛā/baṛī, chhōṭā/chhōṭī)",
                "Identify product defects using kharāb (damaged / broken)",
                "Contrast temporal qualities nayā (new) and purānā (old)"
            ],
            "ru": [
                "Согласовывать прилагательные размера по родам: baṛā/baṛī (большой/большая), chhōṭā/chhōṭī (маленький/маленькая)",
                "Указывать на брак и дефекты словом kharāb ('сломанный / бракованный')",
                "Различать качество товара: nayā (новый) и purānā (старый)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Ретрофлексный одноударный /ṛ/ в baṛā (बड़ा) и глухой придыхательный /chh/ в chhōṭā (छोटा)",
            "articulatoryMechanism": "В слове baṛā кончик языка быстро смахивает по нёбу: [бар͟аа]. В chhōṭā губы смыкаются для звука [ч] с мощным выдохом [чх] и ретрофлексным зубным [т͟]: [чхоот͟аа].",
            "russianInterferenceWarning": "Не заменяйте звук /ṛ/ на обычный русский [р]! Это принципиально разные звуки.",
            "drills": [
                {
                    "prompt": "Пара 'большой — маленький'",
                    "contrastPair": "Baṛā (большой) vs Chhōṭā (маленький)",
                    "instructionsRu": "Произнесите парно: [бар͟аа] — [чхоот͟аа]."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Родовое согласование прилагательных (-ā / -ī)",
            "russianParallel": "Идентично русскому языку: Большой (м.р.) / Больш-ая (ж.р.). В хинди: мужской род оканчивается на -ā (Baṛā kamrā = большая комната), а женский на -ī (Baṛī gāṛī = большая машина). Слово kharāb (испорченный) не меняется по родам.",
            "syntacticFormula": "[Baṛā/Chhōṭā/Nayā (м.р.) // Baṛī/Chhōṭī/Nayī (ж.р.)] + [Существительное]",
            "explanationRu": "Если товар имеет брак, вы просто показываете на него пальцем и говорите: 'Yeh piece kharāb hai' (Эта вещь бракованная). Торговец сразу же заменит ее.",
            "pieCognateConnection": {
                "root": "*newo-",
                "russian": "новый",
                "hindi": "nayā / nayī",
                "meaning": "Праиндоевропейская новизна"
            }
        },
        "vocabulary": [
            {
                "id": "d29_v01",
                "devanagari": "बड़ा / बड़ी",
                "transliterationIso": "Baṛā (m) / Baṛī (f)",
                "phoneticCyrillic": "Бар͟аа / Бар͟ии",
                "translationRu": "Большой / Большая",
                "translationEn": "Big / Large",
                "partOfSpeech": "adjective",
                "gender": "both",
                "audioHint": "Ретрофлексный flap [р͟]."
            },
            {
                "id": "d29_v02",
                "devanagari": "छोटा / छोटी",
                "transliterationIso": "Chhōṭā (m) / Chhōṭī (f)",
                "phoneticCyrillic": "Чхоот͟аа / Чхоот͟ии",
                "translationRu": "Маленький / Маленькая",
                "translationEn": "Small",
                "partOfSpeech": "adjective",
                "gender": "both",
                "audioHint": "Придыхательное [чх] + ретрофлексный [т͟]."
            },
            {
                "id": "d29_v03",
                "devanagari": "ख़राब",
                "transliterationIso": "Kharāb",
                "phoneticCyrillic": "Харааб",
                "translationRu": "Испорченный / Сломанный / Бракованный",
                "translationEn": "Defective / Damaged / Broken",
                "partOfSpeech": "adjective",
                "gender": "both",
                "audioHint": "Гортанный глухой [х], долгое [аа]."
            },
            {
                "id": "d29_v04",
                "devanagari": "नया / पुरानी",
                "transliterationIso": "Nayā (новый) / Purānā (старый)",
                "phoneticCyrillic": "Найаа / Пураанаа",
                "translationRu": "Новый / Старый",
                "translationEn": "New / Old",
                "partOfSpeech": "adjective",
                "gender": "both",
                "audioHint": "Nayā когнат со словом 'новый'."
            }
        ],
        "exercises": [
            {
                "id": "d29_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите претензию: 'Эта вещь бракованная' (Эта вещь + бракованная + есть)",
                "prompt": "Эта вещь бракованная",
                "wordChips": ["Yeh", "piece", "kharāb", "hai"],
                "correctAnswer": ["Yeh", "piece", "kharāb", "hai"],
                "phoneticCyrillicTarget": "Йе пиис харааб хэ",
                "explanationRu": "Yeh piece kharāb hai = Эта вещь с браком."
            },
            {
                "id": "d29_ex02",
                "type": "substitution_drill",
                "instructionRu": "Попросите размер побольше (Мне нужен большой размер)",
                "prompt": "Mujhē _____ size chāhiye.",
                "options": ["baṛā", "chhōṭā", "kharāb"],
                "correctAnswer": "baṛā",
                "transliterationIsoTarget": "Mujhē baṛā size chāhiye.",
                "explanationRu": "Baṛā size = большой размер."
            },
            {
                "id": "d29_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вам дали рубашку, а она вам слишком мала. Скажите об этом продавцу за 2 секунды.",
                "prompt": "Рубашка слишком маленькая",
                "options": [
                    "Yeh bahut chhōṭā hai!",
                    "Yeh bahut svādishṭ hai!",
                    "Station dūr hai!"
                ],
                "correctAnswer": "Yeh bahut chhōṭā hai!",
                "phoneticCyrillicTarget": "Йе бахут чхоот͟аа хэ!",
                "explanationRu": "Yeh bahut chhōṭā hai! = Это слишком мало!"
            },
            {
                "id": "d29_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Попросите абсолютно новую вещь со склада",
                "prompt": "Mujhē _____ piece dījiye. (Новую вещь)",
                "options": ["nayā", "purānā", "tīkhā"],
                "correctAnswer": "nayā",
                "transliterationIsoTarget": "Mujhē nayā piece dījiye.",
                "explanationRu": "Nayā piece = новая вещь."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Примерка одежды и замена размера",
            "setting": "Магазин индийских курток и туник",
            "partnerRoleRu": "Продавец одежды",
            "learnerRoleRu": "Покупательница у зеркала",
            "turns": [
                {
                    "speaker": "Продавец",
                    "speechRu": "Как сидит туника курта, мадам? Все в порядке?",
                    "speechIso": "Madam, kaisā hai? Fitting ṭhīk hai?",
                    "speechCyrillic": "Мадам, кэсаа хэ? Фиттинг т͟хиик хэ?",
                    "learnerHintRu": "Скажите: Нет, это слишком мало. Мне нужен большой размер. (Yeh bahut chhōṭā hai. Baṛā size chāhiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Нет, это очень мало. Мне нужен большой размер.",
                    "speechIso": "Nahī̃ bhaiyā, yeh bahut chhōṭā hai. Baṛā size chāhiye.",
                    "speechCyrillic": "Нахииⁿ бхаййаа, йе бахут чхоот͟аа хэ. Бар͟аа сайз чаахийе.",
                    "acceptableResponsesIso": ["Yeh bahut chhōṭā hai. Baṛā size chāhiye."]
                },
                {
                    "speaker": "Продавец",
                    "speechRu": "Без проблем! Вот размер L. Посмотрите, пожалуйста.",
                    "speechIso": "Kōī bāt nahī̃ madam! Lījiye baṛā size.",
                    "speechCyrillic": "Коии баат нахииⁿ мадам! Лииджие бар͟аа сайз.",
                    "learnerHintRu": "Осмотрите и заметьте пятно: Ой, эта вещь испорчена! Дайте другую новую. (Yeh piece kharāb hai)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Подождите, здесь пятно, эта вещь бракованная. Дайте новую!",
                    "speechIso": "Rukiye, yeh kharāb hai. Nayā piece dījiye.",
                    "speechCyrillic": "Рукие, йе харааб хэ. Найаа пиис дииджие.",
                    "acceptableResponsesIso": ["Yeh kharāb hai, nayā piece dījiye."]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Контроль качества перед покупкой",
            "pointsRu": [
                "В Индии на базарах действует правило: 'Купленный товар возврату не подлежит'.",
                "Поэтому ВСЕГДА внимательно осматривайте швы, пуговицы и молнии со словами 'Dēkhiye, kharāb hai'.",
                "Продавец без малейших споров достанет вам запечатанный пакет со склада."
            ]
        }
    },

    # Day 30
    {
        "day": 30,
        "phase": 4,
        "title": {
            "en": "Requesting Alternatives, Variations, and Exchanges",
            "ru": "Выбор вариантов: «Покажите другой» (Dūsrā dikhāiye) и цвет (Raṅg)"
        },
        "theme": "Другой/второй (dūsrā - когнат с русским 'второй/другой'), покажите другой (dūsrā dikhāiye), поменяйте это (badal dījiye), цвет (raṅg)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Этимологическая связь dūsrā с русским 'второй / другой')",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Вежливый императив: Dūsrā dikhāiye = Покажите другой; Badal dījiye = Обменяйте)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Запрос вариаций: другой цвет, другой размер, поменяйте это)",
            "phase4SimulationMinutes": "17:00–20:00 (Подбор расцветки и фасона ткани)"
        },
        "learningObjectives": {
            "en": [
                "Request alternate products with 'Dūsrā / Dūsrī dikhāiye' (Show another one)",
                "Leverage PIE cognate Dūsrā (Russian второй / другой)",
                "Request exchange using 'Isē badal dījiye' (Exchange this)"
            ],
            "ru": [
                "Просить показать другие варианты: 'Dūsrā dikhāiye' ('Покажите другой / другую')",
                "Использовать этимологический когнат Dūsrā (русский второй / другой)",
                "Требовать замену товара: 'Isē badal dījiye' ('Обменяйте это')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Долгий гласный /ū/ в слове dūsrā (दूसरा) и придыхательный /kh/ в dikhāiye",
            "articulatoryMechanism": "В слове dūsrā губы округлены для долгого [уу], чистый зубной [с], раскатистый [р]: [дуу-сраа]. В dikhāiye — придыхательное [кх].",
            "russianInterferenceWarning": "Не редуцируйте гласный в слове dūsrā. Он должен звучать протяжно.",
            "drills": [
                {
                    "prompt": "Отработка просьбы показать другой вариант",
                    "contrastPair": "Dūsrā dikhāiye (Покажите другой)",
                    "instructionsRu": "Произнесите слитно с акцентом на 'dikhāiye'."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Индоевропейский когнат Dūsrā и глагол dikhānā (показывать)",
            "russianParallel": "Слово Dūsrā буквально родственно русским словам 'два', 'второй' и 'другой' (восходит к праиндоевропейскому корню *dwo-ter-os). Фраза 'Dūsrā dikhāiye' 100% соответствует русскому: 'Покажите другой!'.",
            "syntacticFormula": "[Dūsrā (м.р.) / Dūsrī (ж.р.)] + dikhāiye / Isē badal dījiye",
            "explanationRu": "Глагол badalnā означает 'менять / обменивать'. С нашим знакомым вежливым суффиксом -iye получается: Badal dījiye = Поменяйте, пожалуйста.",
            "pieCognateConnection": {
                "root": "*dwo-ter-os",
                "russian": "второй / другой",
                "hindi": "dūsrā",
                "meaning": "Праиндоевропейская альтернатива и второй элемент"
            }
        },
        "vocabulary": [
            {
                "id": "d30_v01",
                "devanagari": "दूसरा / दूसरी",
                "transliterationIso": "Dūsrā (m) / Dūsrī (f)",
                "phoneticCyrillic": "Дуусраа / Дуусрии",
                "translationRu": "Другой / Вторая (когнат)",
                "translationEn": "Another / Second / Different",
                "partOfSpeech": "adjective",
                "gender": "both",
                "audioHint": "Когнат с 'второй / другой'."
            },
            {
                "id": "d30_v02",
                "devanagari": "दिखाइए",
                "transliterationIso": "Dikhāiye",
                "phoneticCyrillic": "Дикхааие",
                "translationRu": "Покажите, пожалуйста",
                "translationEn": "Please show",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Придыхательное [кх] + -iye."
            },
            {
                "id": "d30_v03",
                "devanagari": "बदल दीजिए",
                "transliterationIso": "Badal dījiye",
                "phoneticCyrillic": "Бадал дииджие",
                "translationRu": "Поменяйте / Обменяйте",
                "translationEn": "Please exchange / change",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Badal (замена) + dījiye (дайте)."
            },
            {
                "id": "d30_v04",
                "devanagari": "रंग",
                "transliterationIso": "Raṅg",
                "phoneticCyrillic": "Ранг",
                "translationRu": "Цвет / Краска",
                "translationEn": "Color",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Велярный носовой [нг]."
            }
        ],
        "exercises": [
            {
                "id": "d30_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите просьбу: 'Пожалуйста, покажите другой цвет'",
                "prompt": "Покажите другой цвет",
                "wordChips": ["Dūsrā", "raṅg", "dikhāiye"],
                "correctAnswer": ["Dūsrā", "raṅg", "dikhāiye"],
                "phoneticCyrillicTarget": "Дуусраа ранг дикхааие",
                "explanationRu": "Dūsrā raṅg (другой цвет) + dikhāiye (покажите)."
            },
            {
                "id": "d30_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вам показали вещь, фасон вам не нравится. Попросите показать другой вариант за 2 секунды.",
                "prompt": "Нужен другой вариант",
                "options": [
                    "Bhaiyā, dūsrā piece dikhāiye!",
                    "Bhaiyā, sīdhē jāiye!",
                    "Khānā garam hai!"
                ],
                "correctAnswer": "Bhaiyā, dūsrā piece dikhāiye!",
                "phoneticCyrillicTarget": "Бхаййаа, дуусраа пиис дикхааие!",
                "explanationRu": "Dūsrā dikhāiye = Покажите другой!"
            },
            {
                "id": "d30_ex03",
                "type": "substitution_drill",
                "instructionRu": "Попросите обменять эту вещь (Эту вещь + обменяйте)",
                "prompt": "Isē _____ dījiye. (Обменяйте)",
                "options": ["badal", "dēkh", "chalo"],
                "correctAnswer": "badal",
                "transliterationIsoTarget": "Isē badal dījiye.",
                "explanationRu": "Badal dījiye = обменяйте."
            },
            {
                "id": "d30_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Спросите: 'Есть ли другой цвет?'",
                "prompt": "Kyā dūsrā _____ hai?",
                "options": ["raṅg", "nām", "pānī"],
                "correctAnswer": "raṅg",
                "transliterationIsoTarget": "Kyā dūsrā raṅg hai?",
                "explanationRu": "Raṅg = цвет."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Выбор цвета сари или палантина",
            "setting": "Лавка традиционных индийских тканей",
            "partnerRoleRu": "Услужливый продавец",
            "learnerRoleRu": "Взыскательная покупательница",
            "turns": [
                {
                    "speaker": "Продавец",
                    "speechRu": "Посмотрите этот красный платок! Очень красивый цвет.",
                    "speechIso": "Yeh lāl rang shawl dēkhiye madam! Bahut sundar hai.",
                    "speechCyrillic": "Йе лаал ранг шол дэкхие мадам! Бахут сундар хэ.",
                    "learnerHintRu": "Скажите: Мне не нравится красный. Покажите другой цвет! (Dūsrā raṅg dikhāiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Мне не нравится красный цвет. Пожалуйста, покажите другой цвет.",
                    "speechIso": "Mujhē lāl raṅg pasand nahī̃ hai. Dūsrā raṅg dikhāiye.",
                    "speechCyrillic": "Муджхе лаал ранг пасанд нахииⁿ хэ. Дуусраа ранг дикхааие.",
                    "acceptableResponsesIso": ["Dūsrā raṅg dikhāiye", "Dūsrā dikhāiye"]
                },
                {
                    "speaker": "Продавец",
                    "speechRu": "Синий цвет нравится? Вот синий и зеленый варианты.",
                    "speechIso": "Blue rang pasand hai? Yeh blue aur green dēkhiye.",
                    "speechCyrillic": "Блю ранг пасанд хэ? Йе блю аур гриин дэкхие.",
                    "learnerHintRu": "Одобрите синий: Hā̃, yeh bahut acchā hai! Сколько это стоит?"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Да, синий мне очень нравится! Почём этот платок?",
                    "speechIso": "Hā̃! Blue mujhē bahut pasand hai. Yeh kitnē kā hai?",
                    "speechCyrillic": "Хааⁿ! Блю муджхе бахут пасанд хэ. Йе китнее каа хэ?",
                    "acceptableResponsesIso": ["Yeh kitnē kā hai?"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Цветовая символика в индийском текстиле",
            "pointsRu": [
                "Цвет (Raṅg) имеет в Индии глубокое значение: шафрановый и желтый — священные, красный — цвет свадьбы и праздника.",
                "Продавцы тканей готовы развернуть перед вами сотни отрезов ткани, пока вы говорите 'Dūsrā dikhāiye'.",
                "Слово 'Raṅg' также дало название весеннему фестивалю красок — Холи."
            ]
        }
    },

    # Day 31
    {
        "day": 31,
        "phase": 4,
        "title": {
            "en": "Finalizing Purchases, Exact Change, and Packaging",
            "ru": "Завершение покупки: сдача и мелочь (Khullē paisē), упаковка (Pack kar dījiye)"
        },
        "theme": "Мелочь/сдача (khullē paisē), нет сдачи (khullē nahī̃ haiñ), пакет (bag/thailī), упакуйте (pack kar dījiye)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция удвоенного l в khullē / кхуллэ и придыхательного th в thailī)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Khullē paisē = русское 'мелочь / сдача' и Pack kar dījiye = Упакуйте)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Диалог на кассе: есть ли мелочь? упакуйте в пакет, заберите чек)",
            "phase4SimulationMinutes": "17:00–20:00 (Финальный расчет и укладывание покупок)"
        },
        "learningObjectives": {
            "en": [
                "Manage change shortages using 'Khullē paisē haiñ? / Khullē nahī̃ haiñ'",
                "Request packaging with 'Pack kar dījiye' and ask for a bag (bag / thailī)",
                "Close commercial retail exchanges smoothly"
            ],
            "ru": [
                "Решать вечную проблему сдачи в Индии фразами: 'Khullē paisē haiñ?' (Есть мелочь?) / 'Khullē nahī̃ haiñ' (Мелочи нет)",
                "Просить упаковать покупки: 'Pack kar dījiye' и просить пакет (thailī / bag)",
                "Уверенно и быстро завершать покупки на кассе"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Удвоенный латеральный /ll/ и придыхательное /kh/ в khullē (खुले)",
            "articulatoryMechanism": "Выдох на глухом велярном [кх] + задержка на удвоенном [лл] с открытым гласным [э]: [кхуллэ].",
            "russianInterferenceWarning": "Не забывайте придыхание на первом слоге.",
            "drills": [
                {
                    "prompt": "Вопрос о мелочи",
                    "contrastPair": "Khullē paisē haiñ? (Есть сдача / мелочь?)",
                    "instructionsRu": "Произнесите связку: Khullē nahī̃ haiñ (Мелочи нет)."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Идиома Khullē paisē (Мелочь / Разменные деньги)",
            "russianParallel": "Слово khullē буквально значит 'открытые / свободные'. В сочетании с paisē (деньги) это абсолютный эквивалент русского 'мелочь / размен / мелкие купюры'. Если у вас нет мелочи, вы говорите: 'Mērē pās khullē nahī̃ haiñ' (У меня нет мелочи).",
            "syntacticFormula": "Pack kar dījiye + [Khullē paisē lījiye / nahī̃ haiñ]",
            "explanationRu": "Сложный составной глагол: Pack (упаковка) + karnā (делать) + dījiye (дайте) = Pack kar dījiye (Упакуйте, пожалуйста). Это самый популярный тип глаголов в современном хинди!",
            "pieCognateConnection": {
                "root": "*kʷel-",
                "russian": "коло / около",
                "hindi": "khulnā / khullā (открытый / свободный)",
                "meaning": "Развязывание и открытие"
            }
        },
        "vocabulary": [
            {
                "id": "d31_v01",
                "devanagari": "खुले पैसे",
                "transliterationIso": "Khullē paisē",
                "phoneticCyrillic": "Кхуллэ пэсе",
                "translationRu": "Мелочь / Мелкие деньги / Сдача",
                "translationEn": "Small change / Coins",
                "partOfSpeech": "phrase",
                "gender": "m",
                "audioHint": "Удвоенное 'лл'."
            },
            {
                "id": "d31_v02",
                "devanagari": "पैक कर दीजिए",
                "transliterationIso": "Pack kar dījiye",
                "phoneticCyrillic": "Пэк кар дииджие",
                "translationRu": "Упакуйте, пожалуйста / Заверните",
                "translationEn": "Please pack it",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Pack + kar dījiye."
            },
            {
                "id": "d31_v03",
                "devanagari": "थैली / बैग",
                "transliterationIso": "Thailī / Bag",
                "phoneticCyrillic": "Тхэилии / Бэг",
                "translationRu": "Пакет / Сумка",
                "translationEn": "Bag / Carry bag",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Придыхательное 'тх'."
            }
        ],
        "exercises": [
            {
                "id": "d31_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите просьбу: 'Пожалуйста, упакуйте эту вещь в пакет'",
                "prompt": "Упакуйте это, пожалуйста",
                "wordChips": ["Isē", "pack", "kar", "dījiye"],
                "correctAnswer": ["Isē", "pack", "kar", "dījiye"],
                "phoneticCyrillicTarget": "Исе пэк кар дииджие",
                "explanationRu": "Isē pack kar dījiye = Упакуйте это."
            },
            {
                "id": "d31_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Продавец спрашивает: 'Khullē paisē haiñ?' (Есть мелочь?). Ответьте за 2 секунды, что мелочи нет.",
                "prompt": "Продавец просит мелочь",
                "options": [
                    "Nahī̃ bhaiyā, khullē nahī̃ haiñ!",
                    "Hā̃, bahut mahangā hai!",
                    "Main thailī hū̃!"
                ],
                "correctAnswer": "Nahī̃ bhaiyā, khullē nahī̃ haiñ!",
                "phoneticCyrillicTarget": "Нахииⁿ бхаййаа, кхуллэ нахииⁿ хэⁿ!",
                "explanationRu": "Khullē nahī̃ haiñ = Мелочи нет."
            },
            {
                "id": "d31_ex03",
                "type": "substitution_drill",
                "instructionRu": "Попросите пакет (Пакет + дайте)",
                "prompt": "Ek _____ dījiye. (Пакет дайте)",
                "options": ["bag", "namak", "chāval"],
                "correctAnswer": "bag",
                "transliterationIsoTarget": "Ek bag dījiye.",
                "explanationRu": "Ek bag dījiye = Дайте пакет."
            },
            {
                "id": "d31_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Отдайте купюру в 500 рупий",
                "prompt": "Pāñch sau kā note _____! (Возьмите купюру 500)",
                "options": ["lījiye", "dījiye", "jāiye"],
                "correctAnswer": "lījiye",
                "transliterationIsoTarget": "Pāñch sau kā note lījiye!",
                "explanationRu": "Lījiye = возьмите."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Завершение покупки сувениров на кассе",
            "setting": "Касса сувенирного магазина",
            "partnerRoleRu": "Кассир",
            "learnerRoleRu": "Покупательница",
            "turns": [
                {
                    "speaker": "Кассир",
                    "speechRu": "Всего четыреста пятьдесят рупий, мадам. У вас есть мелочь 50 рупий?",
                    "speechIso": "450 rupayē madam. Kyā 50 khullē haiñ?",
                    "speechCyrillic": "450 рупае мадам. Кйаа 50 кхуллэ хэⁿ?",
                    "learnerHintRu": "Скажите: Нет, мелочи нет. Возьмите купюру в 500 рупий. (Khullē nahī̃ haiñ. 500 kā note lījiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Нет, мелочи нет. Возьмите пятьсот рупий.",
                    "speechIso": "Nahī̃, khullē nahī̃ haiñ. Pāñch sau kā note lījiye.",
                    "speechCyrillic": "Нахииⁿ, кхуллэ нахииⁿ хэⁿ. Паанч сау каа ноот лииджие.",
                    "acceptableResponsesIso": ["Khullē nahī̃ haiñ. Pāñch sau kā note lījiye."]
                },
                {
                    "speaker": "Кассир",
                    "speechRu": "Хорошо, вот ваши пятьдесят рупий сдачи. Упаковать в пакет?",
                    "speechIso": "Ṭhīk hai, 50 rupayē change lījiye. Pack kar dū̃?",
                    "speechCyrillic": "Т͟хиик хэ, 50 рупае чейндж лииджие. Пэк кар дууⁿ?",
                    "learnerHintRu": "Попросите: Да, пожалуйста, заверните в пакет. Спасибо! (Hā̃, pack kar dījiye, shukriyā!)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Да, пожалуйста, упакуйте. Большое спасибо!",
                    "speechIso": "Hā̃, pack kar dījiye. Bahut shukriyā!",
                    "speechCyrillic": "Хааⁿ, пэк кар дииджие. Бахут шукрийа!",
                    "acceptableResponsesIso": ["Pack kar dījiye, shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Проблема мелкой сдачи в Индии ('Chillar problem')",
            "pointsRu": [
                "В Индии почти всегда наблюдается нехватка монет и мелких купюр у уличных продавцов.",
                "Иногда вместо 5 или 10 рупий сдачи вам могут предложить мятную конфетку (toffee) — это общепринятая забавная норма.",
                "Всегда полезно иметь при себе несколько купюр по 10, 20 и 50 рупий со словами 'Khullē paisē haiñ'."
            ]
        }
    },

    # Day 32
    {
        "day": 32,
        "phase": 4,
        "title": {
            "en": "Phase 4 Synthesis and Street Market Simulation",
            "ru": "Синтез Фазы 4: сквозная базарная симуляция (поиск, торг, выбор цвета, сдача)"
        },
        "theme": "Полный базарный цикл: сколько стоит, торг, альтернативы, проверка качества, упаковка",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Фонетический аудит коммерческих формул: Kitne ka hai, Mahanga, Kam kijiye, Sahi dam)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Сборка стратегии покупателя: приценивание + сбивание цены на 50% + выбор цвета + сдача)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Сквозной ролевой прогон жесткого базарного диалога без единого слова по-английски)",
            "phase4SimulationMinutes": "17:00–20:00 (Экзаменационная базарная симуляция Фазы 4)"
        },
        "learningObjectives": {
            "en": [
                "Execute full-scale bazaar purchase entirely in spoken Hindi without English",
                "Assertively reduce prices by 40-50% using contrastive linguistic formulas",
                "Demand variant sizing, color choices, and exact change under banter pressure"
            ],
            "ru": [
                "Провести полноценную покупку на индийском базаре от начала до конца строго на хинди",
                "Уверенно снижать цену на 40-50% с помощью правильных языковых формул",
                "Выбирать размеры, цвета, проверять качество и забирать сдачу"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Интонационная напористость и убедительность в коммерческом споре",
            "articulatoryMechanism": "Сохранение долготы гласных в числительных (do sau, pāñch sau) при эмоциональном повышении голоса.",
            "russianInterferenceWarning": "Не переходите на раздраженный крик! Индийский торг ведется с азартом, улыбкой и звонкой артикуляцией.",
            "drills": [
                {
                    "prompt": "Боевой базарный арсенал",
                    "contrastPair": "Kitnē kā hai? -> Bahut mahangā hai! -> Sahī dām lagāiye! -> Pack kar dījiye!",
                    "instructionsRu": "Произнесите 4 фразы с нарастающей уверенностью."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Интеграция коммерческого регистра и чисел",
            "russianParallel": "Фаза 4 превратила вас в неуязвимого покупателя. Все базарные приемы индийских продавцов теперь разбиваются о ваше чистое владение числительными и формулами торга.",
            "syntacticFormula": "Yeh kitnē kā hai? | Bahut zyādā hai! | [Сумма] dījiye | Pack kar dījiye",
            "explanationRu": "Знание счета на хинди экономит туристу в Индии сотни долларов и гарантирует искреннее уважение торговцев.",
            "pieCognateConnection": {
                "root": "*dwóh₁ / *dwo-ter-os / *seh₂-",
                "russian": "два / второй / суть",
                "hindi": "do / dūsrā / sahī",
                "meaning": "Индоевропейская гармония торговли"
            }
        },
        "vocabulary": [
            {
                "id": "d32_v01",
                "devanagari": "बाज़ार",
                "transliterationIso": "Bāzār",
                "phoneticCyrillic": "Баазаар",
                "translationRu": "Рынок / Базар",
                "translationEn": "Market / Bazaar",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Два долгих гласных [баа-заар]."
            },
            {
                "id": "d32_v02",
                "devanagari": "दुकानदार",
                "transliterationIso": "Dukāndār",
                "phoneticCyrillic": "Дукаандаар",
                "translationRu": "Лавочник / Продавец",
                "translationEn": "Shopkeeper",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Dukān (магазин) + dār (держатель)."
            },
            {
                "id": "d32_v03",
                "devanagari": "पसंद आया",
                "transliterationIso": "Pasand āyā",
                "phoneticCyrillic": "Пасанд аайаа",
                "translationRu": "Понравилось",
                "translationEn": "Liked it",
                "partOfSpeech": "phrase",
                "gender": "m",
                "audioHint": "Прошедшее время от pasand."
            }
        ],
        "exercises": [
            {
                "id": "d32_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите комплексное предложение покупателя: 'Брат, эта вещь бракованная, покажите другую за 200 рупий'",
                "prompt": "Это с браком, покажите другую за 200",
                "wordChips": ["Yeh", "kharāb", "hai,", "dūsrā", "piece", "dikhāiye,", "do sau", "rupayē!"],
                "correctAnswer": ["Yeh", "kharāb", "hai,", "dūsrā", "piece", "dikhāiye,", "do sau", "rupayē!"],
                "phoneticCyrillicTarget": "Йе харааб хэ, дуусраа пиис дикхааие, до сау рупае!",
                "explanationRu": "Полная цепочка претензии, замены и встречной цены."
            },
            {
                "id": "d32_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Торговец кричит: '1200 rupees, madam, pure silver!'. Сбейте цену ровно вдвое за 2 секунды!",
                "prompt": "1200 рупий за серебро",
                "options": [
                    "Bahut mahangā hai! Chhah sau rupayē dījiye!",
                    "Hā̃, 1200 rupayē lījiye!",
                    "Main silver hū̃!"
                ],
                "correctAnswer": "Bahut mahangā hai! Chhah sau rupayē dījiye!",
                "phoneticCyrillicTarget": "Бахут махангаа хэ! Чхэх сау рупае дииджие!",
                "explanationRu": "Снижение цены ровно наполовину (600 вместо 1200)."
            },
            {
                "id": "d32_ex03",
                "type": "dialogue_roleplay",
                "instructionRu": "Спросите продавца, есть ли у него сдача с купюры в 500 рупий",
                "prompt": "Кассир: 500 kā note hai?",
                "options": [
                    "Hā̃, kyā āpkē pās khullē paisē haiñ?",
                    "Main bāzār mẽ hū̃!",
                    "Khānā svādishṭ hai!"
                ],
                "correctAnswer": "Hā̃, kyā āpkē pās khullē paisē haiñ?",
                "phoneticCyrillicTarget": "Хааⁿ, кйаа аапке паас кхуллэ пэсе хэⁿ?",
                "explanationRu": "Вопрос о наличии мелких денег для сдачи."
            },
            {
                "id": "d32_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Завершите сделку: 'Хорошо, заворачивайте в пакет!'",
                "prompt": "Ṭhīk hai, _____ kar dījiye!",
                "options": ["pack", "garam", "pās"],
                "correctAnswer": "pack",
                "transliterationIsoTarget": "Ṭhīk hai, pack kar dījiye!",
                "explanationRu": "Pack kar dījiye = Упакуйте."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Экзаменационная симуляция Фазы 4: Битва за сувенир на базаре",
            "setting": "Колоритная лавка специй и сувениров на главном базаре",
            "partnerRoleRu": "Агрессивный, но веселый продавец",
            "learnerRoleRu": "Непробиваемая покупательница",
            "turns": [
                {
                    "speaker": "Продавец",
                    "speechRu": "Намастэ, мадам! Посмотрите на этот резной деревянный сундук. Ручная работа! Всего одна тысяча рупий.",
                    "speechIso": "Namastē madam! Handmade wooden box! Sirf ek hazār rupayē.",
                    "speechCyrillic": "Намастэ мадам! Хэндмейд вуден бокс! Сирф эк хазаар рупае.",
                    "learnerHintRu": "Скажите: Слишком много! Скиньте, назовите честную цену. Пятьсот рупий! (Bahut zyādā hai! Sahī dām lagāiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Нет, брат! Тысяча рупий — это слишком дорого. Назовите честную цену. Пятьсот рупий!",
                    "speechIso": "Nahī̃ bhaiyā! Ek hazār bahut zyādā hai. Sahī dām lagāiye. Pāñch sau rupayē dījiye!",
                    "speechCyrillic": "Нахииⁿ бхаййаа! Эк хазаар бахут зйаадаа хэ. Сахии даам лагааие. Паанч сау рупае дииджие!",
                    "acceptableResponsesIso": ["Bahut zyādā hai! Pāñch sau rupayē dījiye!"]
                },
                {
                    "speaker": "Продавец",
                    "speechRu": "Пятьсот?! Мадам, вы меня разорите! Семьсот рупий — последняя цена.",
                    "speechIso": "Pāñch sau?! Nahī̃ madam, 700 rupayē last price!",
                    "speechCyrillic": "Паанч сау?! Нахииⁿ мадам, 700 рупае ласт прайс!",
                    "learnerHintRu": "Сделайте вид, что уходите: Нет, шестьсот рупий, или я ухожу. (Nahī̃, 600 rupayē final)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Шестьсот рупий — окончательная цена. Договорились? Упакуйте!",
                    "speechIso": "Chhah sau rupayē final. Ṭhīk hai? Pack kar dījiye!",
                    "speechCyrillic": "Чхэх сау рупае файнал. Т͟хиик хэ? Пэк кар дииджие!",
                    "acceptableResponsesIso": ["Chhah sau rupayē final! Pack kar dījiye!"]
                },
                {
                    "speaker": "Продавец",
                    "speechRu": "Хорошо, мадам, вы победили! Заворачиваю. С вас шестьсот рупий.",
                    "speechIso": "Acchā madam, āp jeet gayī̃! Lījiye packed box.",
                    "speechCyrillic": "Аччхаа мадам, аап джиит гайииⁿ! Лииджие пэкт бокс.",
                    "learnerHintRu": "Отдайте оплату: Paisē lījiye, bahut shukriyā!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Возьмите шестьсот рупий. Большое спасибо!",
                    "speechIso": "Chhah sau rupayē lījiye. Bahut shukriyā!",
                    "speechCyrillic": "Чхэх сау рупае лииджие. Бахут шукрийа!",
                    "acceptableResponsesIso": ["Paisē lījiye, shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Итоги Фазы 4: Полное мастерство коммерческого диалога",
            "pointsRu": [
                "Вы свободно считаете до тысяч и оперируете сотнями (Sau) и тысячами (Hazār).",
                "Вы знаете, как сбивать завышенные цены вдвое с улыбкой и достоинством.",
                "Вы умеете требовать варианты цвета, размера, контролировать сдачу и закрывать сделки."
            ]
        }
    }
]
