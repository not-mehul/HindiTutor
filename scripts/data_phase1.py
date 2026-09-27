"""
data_phase1.py - Days 01 to 08
Phase 1: Phonetic Calibration, Survival Formulas, and Polite Registers
"""

DAYS_PHASE_1 = [
    # Day 1
    {
        "day": 1,
        "phase": 1,
        "title": {
            "en": "Articulatory Architecture, Greetings, and Respectful Interaction",
            "ru": "Артикуляционная база, приветствия и уважительный регистр"
        },
        "theme": "Приветствия, базовые формулы вежливости и жест Añjali Mudrā",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Калибровка дентальных त vs ретрофлексных ट)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Намастэ, частица джи, уважительное Вы - Аап)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Шейдоуинг-повторение связок с джи)",
            "phase4SimulationMinutes": "17:00–20:00 (Симуляция первой встречи в аэропорту/отеле)"
        },
        "learningObjectives": {
            "en": [
                "Master true laminal dental contact for त vs retroflex curl for ट",
                "Learn core respectful greeting Namastē and gratitude forms",
                "Understand the pragmatic function of deferential particle Jī"
            ],
            "ru": [
                "Освоить чистое зубное त и ретрофлексный загиб ट без русского смягчения (ть)",
                "Выучить приветствие 'Намастэ' и формулы благодарности 'Дханьяваад' и 'Шукрия'",
                "Понять социолингвистическую функцию уважительной частицы 'Джи' (аналог 'да, конечно')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Дентальный /t/ (त) против ретрофлексного /ṭ/ (ट)",
            "articulatoryMechanism": "Для त лопатка языка плоско прижимается к верхним резцам. Для ट кончик языка загибается назад к твердому нёбу.",
            "russianInterferenceWarning": "Не заменяйте ретрофлексию русской мягкой 'ть'! Язык должен быть загнут назад, создавая сухой щелкающий звук.",
            "drills": [
                {
                    "prompt": "Контраст зубного и загнутого звуков",
                    "contrastPair": "tāl (зубной) vs ṭāl (ретрофлексный)",
                    "instructionsRu": "Произнесите 'таал', прижав язык к резцам, затем 'т͟аал', загнув кончик к куполу нёба."
                },
                {
                    "prompt": "Устранение палатализации",
                    "contrastPair": "namastē (не смягчать 'т'!)",
                    "instructionsRu": "Следите, чтобы в 'Namastē' слог 'tē' звучал твердо [тэ], а не [те]."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Уважительный регистр и вежливые частицы",
            "russianParallel": "Соответствие русскому 'Здравствуйте' (с жестом намастэ) и уважительному обращению на 'Вы' (Аап). Частица 'Jī' работает как русский смягчающий маркер согласия.",
            "syntacticFormula": "[Приветствие / Ответ] + Jī",
            "explanationRu": "В хинди обращение к незнакомым людям всегда строится в уважительном регистре 'Āp' (русское 'Вы'). Добавление частицы 'jī' к любому слову превращает его в подчеркнуто вежливое (hā̃ -> hā̃-jī).",
            "pieCognateConnection": {
                "root": "*tew-",
                "russian": "твой / ты",
                "hindi": "tū / tērā",
                "meaning": "Индоевропейское личное местоимение второго лица"
            }
        },
        "vocabulary": [
            {
                "id": "d01_v01",
                "devanagari": "नमस्ते",
                "transliterationIso": "Namastē",
                "phoneticCyrillic": "Намастэ",
                "translationRu": "Здравствуйте / Приветствую",
                "translationEn": "Hello / Greetings",
                "partOfSpeech": "interjection",
                "gender": "n/a",
                "audioHint": "Ударение на второй слог, 'т' твердое зубное."
            },
            {
                "id": "d01_v02",
                "devanagari": "धन्यवाद",
                "transliterationIso": "Dhanyavād",
                "phoneticCyrillic": "Дханьяваад",
                "translationRu": "Спасибо (формальное / высокое)",
                "translationEn": "Thank you (formal)",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Придыхательное 'дх' + долгий гласный 'аа' в конце."
            },
            {
                "id": "d01_v03",
                "devanagari": "शुक्रिया",
                "transliterationIso": "Shukriyā",
                "phoneticCyrillic": "Шукрийа",
                "translationRu": "Спасибо (разговорное)",
                "translationEn": "Thank you (colloquial)",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Мягкое индийское 'ш', раскатистый чистый русский 'р'."
            },
            {
                "id": "d01_v04",
                "devanagari": "आप",
                "transliterationIso": "Āp",
                "phoneticCyrillic": "Аап",
                "translationRu": "Вы (вежливое обращение)",
                "translationEn": "You (formal / respectful)",
                "partOfSpeech": "pronoun",
                "gender": "both",
                "audioHint": "Долгий чистый гласный 'аа', губной непридыхательный 'п'."
            },
            {
                "id": "d01_v05",
                "devanagari": "जी",
                "transliterationIso": "Jī",
                "phoneticCyrillic": "Джии",
                "translationRu": "Уважительная частица (да / уважаемый)",
                "translationEn": "Respectful honorific marker",
                "partOfSpeech": "particle",
                "gender": "n/a",
                "audioHint": "Слитный звонкий аффрикат [дж] + долгий 'ии'."
            }
        ],
        "exercises": [
            {
                "id": "d01_ex01",
                "type": "phonetic_discrimination",
                "instructionRu": "Выберите слово с твердым зубным согласным без русского смягчения (не 'те', а 'тэ')",
                "prompt": "Какое произношение слова 'Namastē' является правильным?",
                "options": ["Намасьте (с мягким т')", "Намастэ (с чистым зубным т)", "Намаштэ (с шипящим)"],
                "correctAnswer": "Намастэ (с чистым зубным т)",
                "explanationRu": "В хинди звук /t/ перед 'e' не смягчается; язык упирается в резцы."
            },
            {
                "id": "d01_ex02",
                "type": "listen_and_repeat",
                "instructionRu": "Повторите фразу с уважительной частицей, удерживая долгие гласные",
                "prompt": "Намастэ джи (Здравствуйте!)",
                "phoneticCyrillicTarget": "Намастэ джии",
                "transliterationIsoTarget": "Namastē jī",
                "correctAnswer": "Namastē jī",
                "explanationRu": "Добавление 'jī' придает приветствию максимальную теплоту и вежливость."
            },
            {
                "id": "d01_ex03",
                "type": "fill_in_blank",
                "instructionRu": "Вставьте подходящее разговорное слово 'спасибо'",
                "prompt": "Bahut _____ (Большое спасибо!)",
                "options": ["shukriyā", "āp", "namastē"],
                "correctAnswer": "shukriyā",
                "transliterationIsoTarget": "Bahut shukriyā",
                "explanationRu": "Bahut (очень) + shukriyā (спасибо) = Большое спасибо."
            },
            {
                "id": "d01_ex04",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вам навстречу идет пожилой хозяин дома и складывает руки в приветствии. Что вы ответите за 3 секунды?",
                "prompt": "Хозяин: Namastē!",
                "options": ["Namastē jī!", "Shukriyā āp!", "Āp kaun?"],
                "correctAnswer": "Namastē jī!",
                "phoneticCyrillicTarget": "Намастэ джии!",
                "explanationRu": "Вежливый и мгновенный ответ — Namastē jī!"
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Первое приветствие в аэропорту / хостеле",
            "setting": "Зона прилета в Дели, встреча с водителем или администратором",
            "partnerRoleRu": "Встречающий менеджер отеля",
            "learnerRoleRu": "Прибывший путешественник",
            "turns": [
                {
                    "speaker": "Менеджер",
                    "speechRu": "Здравствуйте! Добро пожаловать!",
                    "speechIso": "Namastē jī! Welcome!",
                    "speechCyrillic": "Намастэ джии! Вэлкам!",
                    "learnerHintRu": "Ответьте вежливым приветствием со словом джи"
                },
                {
                    "speaker": "Вы (ученик)",
                    "speechRu": "Здравствуйте, спасибо большое!",
                    "speechIso": "Namastē jī, bahut shukriyā!",
                    "speechCyrillic": "Намастэ джии, бахут шукрийа!",
                    "acceptableResponsesIso": ["Namastē jī", "Namastē jī, shukriyā"]
                },
                {
                    "speaker": "Менеджер",
                    "speechRu": "Пожалуйста, проходите сюда.",
                    "speechIso": "Āiye jī, yahā̃ āiye.",
                    "speechCyrillic": "Ааие джии, йахааⁿ ааие.",
                    "learnerHintRu": "Поблагодарите уважительным словом Dhanyavād jī"
                },
                {
                    "speaker": "Вы (ученик)",
                    "speechRu": "Большое спасибо!",
                    "speechIso": "Dhanyavād jī!",
                    "speechCyrillic": "Дханьяваад джии!",
                    "acceptableResponsesIso": ["Dhanyavād jī", "Bahut shukriyā jī"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Культурный код жеста Намастэ",
            "pointsRu": [
                "Жест 'añjali mudrā' (ладони сложены на уровне груди с легким поклоном головы) передает глубокое почтение.",
                "Женщинам в Индии традиционно не протягивают руку для рукопожатия первыми — жест Намастэ является идеальной и безопасной нормой.",
                "Частица 'jī' ставится после имен (например, Anna-jī) или после утверждений (Hā̃-jī)."
            ]
        }
    },

    # Day 2
    {
        "day": 2,
        "phase": 1,
        "title": {
            "en": "Personal Identity and State of Being (Copula Honā)",
            "ru": "Личная идентичность и бытийный глагол (Связка Honā)"
        },
        "theme": "Имя, происхождение (из России) и глагол-связка hū̃ (есмь)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Назализация hū̃ / хууⁿ, недопущение согласного [н])",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Конструкция Main ... hū̃ и послелог сэ)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Подстановочные упражнения с именами и городами)",
            "phase4SimulationMinutes": "17:00–20:00 (Диалог знакомства при заселении)"
        },
        "learningObjectives": {
            "en": [
                "State name and origin using copula hū̃",
                "Bridge the omitted Russian copula to obligatory Hindi terminal verb",
                "Master postposition sē for origin ('из / с')"
            ],
            "ru": [
                "Называть свое имя и страну происхождения с помощью глагола-связки hū̃",
                "Преодолеть привычку опускать связку в настоящем времени (Я Анна -> Main Anna hū̃)",
                "Использовать послелог 'sē' в значении 'из / с' (Russia sē)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Назализованный гласный /ū̃/ (ूँ) в связке hū̃",
            "articulatoryMechanism": "Воздух выходит через рот и носовую полость одновременно. Губы вытянуты вперед для 'уу'.",
            "russianInterferenceWarning": "Не прибавляйте на конце согласную 'н' или 'м'! Должно звучать чистое носовое [хууⁿ], а не 'хун'.",
            "drills": [
                {
                    "prompt": "Отработка чистой носовой долготы",
                    "contrastPair": "hū (чистый у) vs hū̃ (носовой ууⁿ)",
                    "instructionsRu": "Опустите нёбную занавеску и направьте часть звука в нос: 'хууⁿ'."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Обязательная конечная глагол-связка (Copula)",
            "russianParallel": "В современном русском языке связка опускается ('Я турист', 'Я из Москвы'). В хинди связка обязательна и закрывает предложение (исторически родственно церковнославянскому 'Аз есмь').",
            "syntacticFormula": "Main + [Имя / Характеристика / Страна + sē] + hū̃",
            "explanationRu": "В конце утверждения с 'Main' (Я) всегда стоит 'hū̃' (есмь). Послелог 'sē' ставится ПОСЛЕ существительного: Russia sē = из России.",
            "pieCognateConnection": {
                "root": "*es-",
                "russian": "есмь / есть",
                "hindi": "hū̃ / hai",
                "meaning": "Праиндоевропейский корень бытия"
            }
        },
        "vocabulary": [
            {
                "id": "d02_v01",
                "devanagari": "मैं",
                "transliterationIso": "Main",
                "phoneticCyrillic": "Мэⁿ",
                "translationRu": "Я",
                "translationEn": "I",
                "partOfSpeech": "pronoun",
                "gender": "both",
                "audioHint": "Носовой широкий звук [мэⁿ], не путать с английским 'main'."
            },
            {
                "id": "d02_v02",
                "devanagari": "हूँ",
                "transliterationIso": "hū̃",
                "phoneticCyrillic": "хууⁿ",
                "translationRu": "есмь (форма глагола 'быть' для 'я')",
                "translationEn": "am (first person copula)",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Носовое долгое 'ууⁿ' на выдохе."
            },
            {
                "id": "d02_v03",
                "devanagari": "मेरा",
                "transliterationIso": "Mērā",
                "phoneticCyrillic": "Мераа",
                "translationRu": "Мой / Моё",
                "translationEn": "My",
                "partOfSpeech": "pronoun",
                "gender": "m",
                "audioHint": "Чистый русский 'р', долгое 'аа' на конце."
            },
            {
                "id": "d02_v04",
                "devanagari": "नाम",
                "transliterationIso": "Nām",
                "phoneticCyrillic": "Наам",
                "translationRu": "Имя",
                "translationEn": "Name",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Когнат с русским 'имя' через индоевропейский корень *h₁nómn̥."
            },
            {
                "id": "d02_v05",
                "devanagari": "से",
                "transliterationIso": "Sē",
                "phoneticCyrillic": "Сэ",
                "translationRu": "из / с / от",
                "translationEn": "from / by",
                "partOfSpeech": "postposition",
                "gender": "n/a",
                "audioHint": "Твердое зубное 'сэ'."
            },
            {
                "id": "d02_v06",
                "devanagari": "है",
                "transliterationIso": "hai",
                "phoneticCyrillic": "хэ",
                "translationRu": "есть / является (для 3-го лица: он/она/оно)",
                "translationEn": "is (third person singular copula)",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Широкий открытый [хэ]."
            }
        ],
        "exercises": [
            {
                "id": "d02_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите фразу 'Я из России' в строгом порядке хинди (Подлежащее + Обстоятельство + Связка)",
                "prompt": "Я из России (буквально: Я Россия из есмь)",
                "wordChips": ["Main", "Russia", "sē", "hū̃"],
                "correctAnswer": ["Main", "Russia", "sē", "hū̃"],
                "phoneticCyrillicTarget": "Мэⁿ Расийа сэ хууⁿ",
                "explanationRu": "В хинди глагол-связка hū̃ строго закрывает предложение."
            },
            {
                "id": "d02_ex02",
                "type": "substitution_drill",
                "instructionRu": "Вставьте глагол-связку в фразу 'Меня зовут Анна'",
                "prompt": "Mērā nām Anna _____",
                "options": ["hai", "hū̃", "sē"],
                "correctAnswer": "hai",
                "transliterationIsoTarget": "Mērā nām Anna hai",
                "explanationRu": "Субъект здесь 'nām' (имя — оно), поэтому связка для 3-го лица: 'hai'."
            },
            {
                "id": "d02_ex03",
                "type": "listen_and_repeat",
                "instructionRu": "Произнесите фразу 'Я турист/туристка', следя за носовым 'hū̃'",
                "prompt": "Main tourist hū̃",
                "phoneticCyrillicTarget": "Мэⁿ турист хууⁿ",
                "transliterationIsoTarget": "Main tourist hū̃",
                "correctAnswer": "Main tourist hū̃",
                "explanationRu": "Никогда не забывайте связку hū̃ на конце!"
            },
            {
                "id": "d02_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Выберите правильный послелог 'из'",
                "prompt": "Main Moscow _____ hū̃.",
                "options": ["sē", "mẽ", "par"],
                "correctAnswer": "sē",
                "transliterationIsoTarget": "Main Moscow sē hū̃",
                "explanationRu": "Sē передает значение происхождения (из Москвы)."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Знакомство при заселении в гестхаус",
            "setting": "Стойка регистрации в Ришикеше или Дели",
            "partnerRoleRu": "Владелец гестхауса",
            "learnerRoleRu": "Гость",
            "turns": [
                {
                    "speaker": "Хозяин",
                    "speechRu": "Здравствуйте! Как ваше имя?",
                    "speechIso": "Namastē jī! Āpkā nām kyā hai?",
                    "speechCyrillic": "Намастэ джии! Аапкаа наам кйаа хэ?",
                    "learnerHintRu": "Назовите свое имя: Mērā nām [Имя] hai"
                },
                {
                    "speaker": "Вы (ученик)",
                    "speechRu": "Здравствуйте! Меня зовут Анна.",
                    "speechIso": "Namastē jī! Mērā nām Anna hai.",
                    "speechCyrillic": "Намастэ джии! Мераа наам Анна хэ.",
                    "acceptableResponsesIso": ["Mērā nām Anna hai", "Main Anna hū̃"]
                },
                {
                    "speaker": "Хозяин",
                    "speechRu": "Очень приятно! Откуда вы приехали?",
                    "speechIso": "Āp kahā̃ sē haiñ?",
                    "speechCyrillic": "Аап кахааⁿ сэ хэⁿ?",
                    "learnerHintRu": "Скажите: Я из России (Main Russia sē hū̃)"
                },
                {
                    "speaker": "Вы (ученик)",
                    "speechRu": "Я из России. Я турист.",
                    "speechIso": "Main Russia sē hū̃. Main tourist hū̃.",
                    "speechCyrillic": "Мэⁿ Расийа сэ хууⁿ. Мэⁿ турист хууⁿ.",
                    "acceptableResponsesIso": ["Main Russia sē hū̃"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Разговоры о стране происхождения",
            "pointsRu": [
                "В Индии к путешественникам из России относятся очень тепло (историческое 'Хинди-руси бхай-бхай').",
                "Фраза 'Main Russia sē hū̃' моментально вызывает улыбку и дружелюбие собеседника.",
                "Слово 'tourist' абсолютно естественно используется в повседневном хинди (hinglish)."
            ]
        }
    },

    # Day 3
    {
        "day": 3,
        "phase": 1,
        "title": {
            "en": "Inquiring Wellbeing and Adjectival Gender Agreement",
            "ru": "Вопрос о самочувствии и родовое согласование прилагательных"
        },
        "theme": "Как дела? Согласование по женскому (-ī) и мужскому (-ē) роду",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция ретрофлексного ṭh в ṭhīk / тхиик)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Согласование kaisē / kaisī и окончание -ī)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Парный диалог: самочувствие и взаимный ответ)",
            "phase4SimulationMinutes": "17:00–20:00 (Встреча знакомого на улице)"
        },
        "learningObjectives": {
            "en": [
                "Ask how someone is doing in formal register (Āp kaisī/kaisē haiñ?)",
                "Answer using adjectival agreement (Main ṭhīk hū̃)",
                "Deploy reciprocation phrase 'Aur āp?' (And you?)"
            ],
            "ru": [
                "Спрашивать 'Как ваши дела?' в уважительном регистре с учетом пола собеседника",
                "Отвечать 'Я в порядке' (Main ṭhīk hū̃) и 'Очень хорошо' (Bahut acchā)",
                "Использовать связку взаимности 'Aur āp?' (А вы?)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Ретрофлексный придыхательный /ṭh/ (ठ) в слове ṭhīk",
            "articulatoryMechanism": "Кончик языка загибается назад к нёбу и с резким придыхательным выбросом воздуха размыкается.",
            "russianInterferenceWarning": "Не заменяйте на русское мягкое 'ть'! Это твердый загнутый звук с дыханием: [т͟хиик].",
            "drills": [
                {
                    "prompt": "Тест с бумажкой на слово ṭhīk",
                    "contrastPair": "ṭīk (без придыхания) vs ṭhīk (с выбросом воздуха)",
                    "instructionsRu": "Бумажка перед губами должна резко колыхнуться на звуке 'ṭhīk'."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Родовое согласование предикативных прилагательных",
            "russianParallel": "Полная аналогия с русским языком: какой (м.р.) / какая (ж.р.). К женщине обращаются: Āp kaisī haiñ? К мужчине: Āp kaisē haiñ?",
            "syntacticFormula": "Āp + [kaisē (м.р.) / kaisī (ж.р.)] + haiñ?",
            "explanationRu": "Суффикс -ā / -ē маркирует мужской род, суффикс -ī маркирует женский род. При обращении на 'Āp' используется форма множественного числа/вежливости (kaisē / haiñ).",
            "pieCognateConnection": {
                "root": "*kʷo- / *kʷi-",
                "russian": "какой / как",
                "hindi": "kaisā / kaisī",
                "meaning": "Вопросительное местоимение качества"
            }
        },
        "vocabulary": [
            {
                "id": "d03_v01",
                "devanagari": "कैसी",
                "transliterationIso": "Kaisī",
                "phoneticCyrillic": "Кэсии",
                "translationRu": "Как / Какая (для женщины)",
                "translationEn": "How (feminine)",
                "partOfSpeech": "adjective",
                "gender": "f",
                "audioHint": "Долгое чистое 'ии' на конце."
            },
            {
                "id": "d03_v02",
                "devanagari": "कैसे",
                "transliterationIso": "Kaisē",
                "phoneticCyrillic": "Кэсе",
                "translationRu": "Как / Какой (для мужчины / вежливая форма)",
                "translationEn": "How (masculine honorific)",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Твердое э на конце."
            },
            {
                "id": "d03_v03",
                "devanagari": "ठीक",
                "transliterationIso": "Ṭhīk",
                "phoneticCyrillic": "Т͟хиик",
                "translationRu": "Хорошо / В порядке / Нормально",
                "translationEn": "Fine / Okay / All right",
                "partOfSpeech": "adjective",
                "gender": "both",
                "audioHint": "Ретрофлексный загиб кончика языка + придыхание."
            },
            {
                "id": "d03_v04",
                "devanagari": "बहुत",
                "transliterationIso": "Bahut",
                "phoneticCyrillic": "Бахут",
                "translationRu": "Очень / Много",
                "translationEn": "Very / Much",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Легкий выдох на 'х', зубное 'т'."
            },
            {
                "id": "d03_v05",
                "devanagari": "अच्छा",
                "transliterationIso": "Acchā",
                "phoneticCyrillic": "Аччхаа",
                "translationRu": "Хороший / Хорошо",
                "translationEn": "Good",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Удвоенное придыхательное 'ччх'."
            },
            {
                "id": "d03_v06",
                "devanagari": "और",
                "transliterationIso": "Aur",
                "phoneticCyrillic": "Аур",
                "translationRu": "И / А (союз)",
                "translationEn": "And",
                "partOfSpeech": "conjunction",
                "gender": "n/a",
                "audioHint": "Раскатистый чистый 'р'."
            }
        ],
        "exercises": [
            {
                "id": "d03_ex01",
                "type": "substitution_drill",
                "instructionRu": "Обратитесь к женщине с вопросом 'Как ваши дела?'",
                "prompt": "Āp _____ haiñ?",
                "options": ["kaisī", "kaisē", "kaisā"],
                "correctAnswer": "kaisī",
                "transliterationIsoTarget": "Āp kaisī haiñ?",
                "explanationRu": "Для женского рода согласовательное окончание всегда -ī (kaisī)."
            },
            {
                "id": "d03_ex02",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите фразу 'Я в порядке' (Я + в порядке + есмь)",
                "prompt": "Я в порядке",
                "wordChips": ["Main", "ṭhīk", "hū̃"],
                "correctAnswer": ["Main", "ṭhīk", "hū̃"],
                "phoneticCyrillicTarget": "Мэⁿ т͟хиик хууⁿ",
                "explanationRu": "Main (Я) + ṭhīk (в порядке) + hū̃ (есмь)."
            },
            {
                "id": "d03_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вас спросили: 'Āp kaisī haiñ?'. Ответьте, что у вас все отлично, и поблагодарите.",
                "prompt": "Собеседник: Āp kaisī haiñ?",
                "options": [
                    "Main ṭhīk hū̃, shukriyā!",
                    "Main Russia sē hū̃!",
                    "Bahut nām hai!"
                ],
                "correctAnswer": "Main ṭhīk hū̃, shukriyā!",
                "phoneticCyrillicTarget": "Мэⁿ т͟хиик хууⁿ, шукрийа!",
                "explanationRu": "Классический вежливый ответ: Main ṭhīk hū̃, shukriyā!"
            },
            {
                "id": "d03_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Вставьте союз 'А вы?'",
                "prompt": "_____ āp? (А вы?)",
                "options": ["Aur", "Sē", "Jī"],
                "correctAnswer": "Aur",
                "transliterationIsoTarget": "Aur āp?",
                "explanationRu": "Aur означает 'и / а'."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Утренний обмен любезностями с администратором",
            "setting": "Лобби отеля утром",
            "partnerRoleRu": "Сотрудник отеля (мужчина)",
            "learnerRoleRu": "Гостья",
            "turns": [
                {
                    "speaker": "Администратор",
                    "speechRu": "Доброе утро! Как вы поживаете?",
                    "speechIso": "Namastē jī! Āp kaisī haiñ?",
                    "speechCyrillic": "Намастэ джии! Аап кэсии хэⁿ?",
                    "learnerHintRu": "Ответьте: Я в порядке, спасибо! А вы?"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Я в порядке, спасибо! А вы как?",
                    "speechIso": "Main ṭhīk hū̃, dhanyavād! Aur āp?",
                    "speechCyrillic": "Мэⁿ т͟хиик хууⁿ, дханьяваад! Аур аап?",
                    "acceptableResponsesIso": ["Main ṭhīk hū̃, shukriyā! Aur āp?"]
                },
                {
                    "speaker": "Администратор",
                    "speechRu": "Я тоже в полном порядке. Очень хорошо!",
                    "speechIso": "Main bhī ṭhīk hū̃. Bahut acchā!",
                    "speechCyrillic": "Мэⁿ бхии т͟хиик хууⁿ. Бахут аччхаа!",
                    "learnerHintRu": "Улыбнитесь и скажите 'Acchā jī, shukriyā'"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Прекрасно, спасибо!",
                    "speechIso": "Acchā jī, shukriyā!",
                    "speechCyrillic": "Аччхаа джии, шукрийа!",
                    "acceptableResponsesIso": ["Bahut acchā, shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Интонация слова 'Acchā'",
            "pointsRu": [
                "Слово 'Acchā' в Индии — универсальный маркер активного слушания (как русское 'понятно', 'хорошо', 'ага').",
                "С восходящей интонацией ('Acchā?') означает 'Правда? Да ладно!'.",
                "С нисходящей спокойной интонацией ('Acchā...') означает 'Ясно / Договорились'."
            ]
        }
    },

    # Day 4
    {
        "day": 4,
        "phase": 1,
        "title": {
            "en": "Core Politeness, Affirmation, and Negation",
            "ru": "Базовая вежливость, утверждение, отрицание и извинения"
        },
        "theme": "Да, нет, ладно, извините (Māf kījiye) и ничего страшного (Kōī bāt nahī̃)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Контраст Hā̃ с носовым ааⁿ vs Nahī̃ с носовым ииⁿ)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Императив -iye как русский суффикс -ите в Извините)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Быстрое реагирование на бытовые предложения)",
            "phase4SimulationMinutes": "17:00–20:00 (Реакция на случайный толчок в толпе или отказ от навязчивого гида)"
        },
        "learningObjectives": {
            "en": [
                "Master polite affirmation (Hā̃-jī) and soft negation (Nahī̃-jī)",
                "Apologize using formal imperative Māf kījiye",
                "Dismiss trivial issues with Kōī bāt nahī̃"
            ],
            "ru": [
                "Уверенно использовать вежливое 'да' (Hā̃-jī) и мягкое 'нет' (Nahī̃-jī)",
                "Извиняться с помощью вежливого императива Māf kījiye (аналог русского 'Извините')",
                "Снимать напряжение фразой Kōī bāt nahī̃ ('Ничего страшного / Пустяки')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Носовые гласные в Hā̃ (हाँ) и Nahī̃ (नहीं)",
            "articulatoryMechanism": "Звук идет в нос. В слове 'Hā̃' открытый носовой гласный, в 'Nahī̃' — долгий высокий носовой 'ииⁿ'.",
            "russianInterferenceWarning": "Не произносите четкое русское [н] на конце слова. Должно звучать [Хааⁿ] и [Нахииⁿ].",
            "drills": [
                {
                    "prompt": "Парное произнесение утверждения и отрицания",
                    "contrastPair": "Hā̃-jī (Хааⁿ-джи) vs Nahī̃-jī (Нахииⁿ-джи)",
                    "instructionsRu": "Держите носовой резонанс без прибавки твердого согласного."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Вежливый императив на -iye и фразеология вежливости",
            "russianParallel": "Суффикс вежливости -iye строго соответствует русскому суффиксу -ите (Māf kījiye = Извин-ите; Kījiye = Сделайте). Kōī bāt nahī̃ семантически равна фразе 'Ничего страшного' (нет никакого вопроса/разговора).",
            "syntacticFormula": "Глагольная основа + -iye (вежливая просьба)",
            "explanationRu": "Форма на -iye используется всегда при обращении на Вы (Āp). Для извинения берется арабское заимствование māf (прощение) + kījiye (сделайте) = Простите / Извините.",
            "pieCognateConnection": {
                "root": "*ne / *nē",
                "russian": "не / нет",
                "hindi": "nahī̃ / na",
                "meaning": "Индоевропейская отрицательная частица"
            }
        },
        "vocabulary": [
            {
                "id": "d04_v01",
                "devanagari": "हाँ",
                "transliterationIso": "Hā̃",
                "phoneticCyrillic": "Хааⁿ",
                "translationRu": "Да",
                "translationEn": "Yes",
                "partOfSpeech": "particle",
                "gender": "n/a",
                "audioHint": "Носовое открытое 'ааⁿ'."
            },
            {
                "id": "d04_v02",
                "devanagari": "नहीं",
                "transliterationIso": "Nahī̃",
                "phoneticCyrillic": "Нахииⁿ",
                "translationRu": "Нет / Не",
                "translationEn": "No / Not",
                "partOfSpeech": "particle",
                "gender": "n/a",
                "audioHint": "Ударение на второй долгий носовой слог."
            },
            {
                "id": "d04_v03",
                "devanagari": "ठीक है",
                "transliterationIso": "Ṭhīk hai",
                "phoneticCyrillic": "Т͟хиик хэ",
                "translationRu": "Ладно / Хорошо / Договорились",
                "translationEn": "All right / Okay",
                "partOfSpeech": "interjection",
                "gender": "n/a",
                "audioHint": "Ретрофлексный придыхательный ṭh."
            },
            {
                "id": "d04_v04",
                "devanagari": "माफ़ कीजिए",
                "transliterationIso": "Māf kījiye",
                "phoneticCyrillic": "Мааф кииджие",
                "translationRu": "Извините / Простите",
                "translationEn": "Excuse me / Sorry",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Долгое 'аа', окончание -iye."
            },
            {
                "id": "d04_v05",
                "devanagari": "कोई बात नहीं",
                "transliterationIso": "Kōī bāt nahī̃",
                "phoneticCyrillic": "Коии баат нахииⁿ",
                "translationRu": "Ничего страшного / Без проблем",
                "translationEn": "No problem / It doesn't matter",
                "partOfSpeech": "interjection",
                "gender": "n/a",
                "audioHint": "Буквально: 'никакого разговора нет'."
            }
        ],
        "exercises": [
            {
                "id": "d04_ex01",
                "type": "rapid_oral_challenge",
                "instructionRu": "На улице торговец настойчиво предлагает купить барабан. Откажитесь вежливо, но твердо за 2 секунды.",
                "prompt": "Торговец: Madam, take this! Very good drum!",
                "options": [
                    "Nahī̃-jī, shukriyā!",
                    "Hā̃-jī, bilkul!",
                    "Mērā nām drum hai!"
                ],
                "correctAnswer": "Nahī̃-jī, shukriyā!",
                "phoneticCyrillicTarget": "Нахииⁿ-джии, шукрийа!",
                "explanationRu": "Формула 'Nahī̃-jī, shukriyā' (Нет, уважаемый, спасибо) — лучший культурный щит от навязчивых предложений."
            },
            {
                "id": "d04_ex02",
                "type": "fill_in_blank",
                "instructionRu": "Вставьте форму вежливого извинения",
                "prompt": "_____, station kahā̃ hai? (Извините, где вокзал?)",
                "options": ["Māf kījiye", "Bahut acchā", "Kōī bāt nahī̃"],
                "correctAnswer": "Māf kījiye",
                "transliterationIsoTarget": "Māf kījiye, station kahā̃ hai?",
                "explanationRu": "Māf kījiye используется для привлечения внимания или извинения."
            },
            {
                "id": "d04_ex03",
                "type": "listen_and_repeat",
                "instructionRu": "Произнесите фразу успокоения собеседника 'Ничего страшного'",
                "prompt": "Kōī bāt nahī̃",
                "phoneticCyrillicTarget": "Коии баат нахииⁿ",
                "transliterationIsoTarget": "Kōī bāt nahī̃",
                "correctAnswer": "Kōī bāt nahī̃",
                "explanationRu": "Фраза Kōī bāt nahī̃ мгновенно разряжает любую неловкость."
            },
            {
                "id": "d04_ex04",
                "type": "substitution_drill",
                "instructionRu": "Подтвердите согласие с собеседником",
                "prompt": "Чай готов? Ответьте: 'Да, хорошо!'",
                "options": [
                    "Hā̃, ṭhīk hai!",
                    "Nahī̃, māf kījiye!",
                    "Main tourist hū̃!"
                ],
                "correctAnswer": "Hā̃, ṭhīk hai!",
                "transliterationIsoTarget": "Hā̃, ṭhīk hai!",
                "explanationRu": "Hā̃ (да) + ṭhīk hai (ладно / хорошо)."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Неловкая ситуация в узком коридоре",
            "setting": "Коридор отеля или посадка в поезд",
            "partnerRoleRu": "Попутчик с чемоданом",
            "learnerRoleRu": "Путешественник",
            "turns": [
                {
                    "speaker": "Попутчик",
                    "speechRu": "Ой, извините пожалуйста! Я задел ваш багаж.",
                    "speechIso": "Oh, māf kījiye jī!",
                    "speechCyrillic": "Ох, мааф кииджие джии!",
                    "learnerHintRu": "Успокойте его: Ничего страшного, все в порядке!"
                },
                {
                    "speaker": "Вы (ученик)",
                    "speechRu": "Ничего страшного, все хорошо!",
                    "speechIso": "Kōī bāt nahī̃, ṭhīk hai!",
                    "speechCyrillic": "Коии баат нахииⁿ, т͟хиик хэ!",
                    "acceptableResponsesIso": ["Kōī bāt nahī̃", "Ṭhīk hai jī, kōī bāt nahī̃"]
                },
                {
                    "speaker": "Попутчик",
                    "speechRu": "Большое спасибо за понимание!",
                    "speechIso": "Bahut shukriyā!",
                    "speechCyrillic": "Бахут шукрийа!",
                    "learnerHintRu": "Ответьте вежливым кивком 'Shukriyā jī'"
                },
                {
                    "speaker": "Вы (ученик)",
                    "speechRu": "Пожалуйста!",
                    "speechIso": "Shukriyā jī!",
                    "speechCyrillic": "Шукрийа джии!",
                    "acceptableResponsesIso": ["Dhanyavād jī"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Культура отказа и личные границы",
            "pointsRu": [
                "Резкое русское 'Нет!' может восприниматься в Индии как излишняя агрессия.",
                "Связка 'Nahī̃-jī, shukriyā' в сочетании с легким покачиванием головы из стороны в сторону выражает мягкий, но непререкаемый отказ.",
                "Индийское покачивание головой ('head bobble') часто означает согласие, подтверждение или уважительное 'понимаю вас'."
            ]
        }
    },

    # Day 5
    {
        "day": 5,
        "phase": 1,
        "title": {
            "en": "Interrogative Formulations and the Question Particle",
            "ru": "Вопросительные конструкции и вопросительная частица Kyā"
        },
        "theme": "Общие вопросы (частица Kyā как русское 'Ли') и специальные вопросы на К",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция согласных серии К: непридыхательный k vs ky)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Начальная частица Kyā и вопросы Где? Кто? Когда? Как?)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Трансформация утверждений в общие вопросы)",
            "phase4SimulationMinutes": "17:00–20:00 (Расспрос прохожего о вокзале и гостинице)"
        },
        "learningObjectives": {
            "en": [
                "Formulate polar questions using clause-initial particle Kyā",
                "Master K-interrogative question words (Kahā̃, Kaun, Kab, Kyū̃, Kaisē)",
                "Maintain sentence-final copula hai in questions"
            ],
            "ru": [
                "Строить общие вопросы с помощью начальной частицы Kyā (аналог русской частицы 'Ли')",
                "Освоить вопросительные слова на букву К (Kahā̃ = где, Kaun = кто, Kab = когда, Kaisē = как)",
                "Сохранять обязательную глагол-связку hai в конце вопросительного предложения"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Непридыхательный велярный /k/ (क) и назализованный /ā̃/ в kahā̃",
            "articulatoryMechanism": "Задняя спинка языка смыкается с мягким нёбом. Без придыхания. В слове kahā̃ второй слог назализуется: [кахааⁿ].",
            "russianInterferenceWarning": "Не забывайте носовой звук в вопросе 'Где?' (Kahā̃). Если сказать просто 'каха', это звучит грубо и фонетически искаженно.",
            "drills": [
                {
                    "prompt": "Отработка вопроса 'Где?'",
                    "contrastPair": "kahā (ошибка) vs kahā̃ (верно: носовой гласный)",
                    "instructionsRu": "Направьте гласный в нос на втором слоге: [кахааⁿ]."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Двойная роль слова Kyā (Что? vs Вопросительная частица)",
            "russianParallel": "Если Kyā стоит в САМОМ НАЧАЛЕ фразы, оно не переводится как 'что', а работает как русская частица 'Ли' (Kyā yeh hotel hai? = Отель ли это? / Это отель?). В середине предложения Kyā значит 'что' (Yeh kyā hai? = Что это?).",
            "syntacticFormula": "Kyā + [Подлежащее] + [Сказуемое] + [hai]?",
            "explanationRu": "Все базовые вопросительные слова в хинди начинаются на букву К (как в русском: кто, когда, куда, какой). Связка hai ВСЕГДА стоит на последнем месте: Station kahā̃ hai? (Вокзал где есть?).",
            "pieCognateConnection": {
                "root": "*kʷi- / *kʷo-",
                "russian": "кто / когда / какой",
                "hindi": "kaun / kab / kaisā",
                "meaning": "Индоевропейский вопросительный класс на K"
            }
        },
        "vocabulary": [
            {
                "id": "d05_v01",
                "devanagari": "क्या",
                "transliterationIso": "Kyā",
                "phoneticCyrillic": "Кйаа",
                "translationRu": "Что? / Вопросительная частица (Ли)",
                "translationEn": "What / Polar question marker",
                "partOfSpeech": "pronoun",
                "gender": "n/a",
                "audioHint": "Короткий [кй] + долгое [аа]."
            },
            {
                "id": "d05_v02",
                "devanagari": "कहाँ",
                "transliterationIso": "Kahā̃",
                "phoneticCyrillic": "Кахааⁿ",
                "translationRu": "Где? / Куда?",
                "translationEn": "Where",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Носовой звук на конце: [кахааⁿ]."
            },
            {
                "id": "d05_v03",
                "devanagari": "कौन",
                "transliterationIso": "Kaun",
                "phoneticCyrillic": "Каун",
                "translationRu": "Кто?",
                "translationEn": "Who",
                "partOfSpeech": "pronoun",
                "gender": "both",
                "audioHint": "Дифтонгоид [ау], твердый зубной [н]."
            },
            {
                "id": "d05_v04",
                "devanagari": "कब",
                "transliterationIso": "Kab",
                "phoneticCyrillic": "Каб",
                "translationRu": "Когда?",
                "translationEn": "When",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Короткий гласный [а], звонкий [б]."
            },
            {
                "id": "d05_v05",
                "devanagari": "क्यों",
                "transliterationIso": "Kyū̃",
                "phoneticCyrillic": "Кйууⁿ",
                "translationRu": "Почему? / Зачем?",
                "translationEn": "Why",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Долгое носовое [ууⁿ]."
            }
        ],
        "exercises": [
            {
                "id": "d05_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите вопрос 'Где находится станция?' (Станция + где + есть?)",
                "prompt": "Где станция метро?",
                "wordChips": ["Metro station", "kahā̃", "hai"],
                "correctAnswer": ["Metro station", "kahā̃", "hai"],
                "phoneticCyrillicTarget": "Мэтро стэшн кахааⁿ хэ",
                "explanationRu": "Вопросительное слово ставится перед конечным глаголом: Объект + kahā̃ + hai?"
            },
            {
                "id": "d05_ex02",
                "type": "fill_in_blank",
                "instructionRu": "Превратите утверждение 'Yeh hotel hai' (Это отель) в вопрос 'Это отель?'",
                "prompt": "_____ yeh hotel hai?",
                "options": ["Kyā", "Kahā̃", "Kaun"],
                "correctAnswer": "Kyā",
                "transliterationIsoTarget": "Kyā yeh hotel hai?",
                "explanationRu": "Kyā в начале предложения делает из него общий вопрос (да/нет)."
            },
            {
                "id": "d05_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Укажите на незнакомый предмет и спросите 'Что это?'",
                "prompt": "Что это?",
                "options": ["Yeh kyā hai?", "Kyā yeh hai?", "Kahā̃ yeh hai?"],
                "correctAnswer": "Yeh kyā hai?",
                "phoneticCyrillicTarget": "Йе кйаа хэ?",
                "explanationRu": "Yeh (это) + kyā (что) + hai (есть)?"
            },
            {
                "id": "d05_ex04",
                "type": "substitution_drill",
                "instructionRu": "Спросите 'Когда прибудет поезд?' (Поезд + когда + есть?)",
                "prompt": "Train _____ hai?",
                "options": ["kab", "kyū̃", "kaun"],
                "correctAnswer": "kab",
                "transliterationIsoTarget": "Train kab hai?",
                "explanationRu": "Kab означает 'когда'."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Поиск стойки информации на вокзале",
            "setting": "Шумный железнодорожный вокзал Нью-Дели",
            "partnerRoleRu": "Дежурный по станции",
            "learnerRoleRu": "Пассажирка",
            "turns": [
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Извините, пожалуйста! Где стойка информации?",
                    "speechIso": "Māf kījiye jī! Information counter kahā̃ hai?",
                    "speechCyrillic": "Мааф кииджие джии! Информэйшн каунтер кахааⁿ хэ?",
                    "learnerHintRu": "Задайте вопрос с вежливым Māf kījiye"
                },
                {
                    "speaker": "Дежурный",
                    "speechRu": "Стойка информации там, прямо.",
                    "speechIso": "Information counter vahā̃ hai, sīdhē.",
                    "speechCyrillic": "Информэйшн каунтер вахааⁿ хэ, сиидхэ.",
                    "learnerHintRu": "Уточните: Это рядом? (Kyā pās hai?)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Это рядом?",
                    "speechIso": "Kyā pās hai?",
                    "speechCyrillic": "Кйаа паас хэ?",
                    "acceptableResponsesIso": ["Kyā yeh pās hai?"]
                },
                {
                    "speaker": "Дежурный",
                    "speechRu": "Да, совсем рядом. Большое спасибо!",
                    "speechIso": "Hā̃-jī, bilkul pās hai.",
                    "speechCyrillic": "Хааⁿ-джии, билкул паас хэ.",
                    "learnerHintRu": "Поблагодарите: Shukriyā jī!"
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Как обращаться к незнакомцам с вопросом",
            "pointsRu": [
                "Всегда предваряйте вопрос формулой 'Māf kījiye' (Извините) или вежливым словом 'Sunye jī' (Послушайте, пожалуйста).",
                "К мужчинам-работникам вокзала или водителям принято обращаться 'Bhaiyā' (брат / молодой человек) — это звучит уважительно и дружелюбно.",
                "Связка 'hai' на конце предложения обязательна даже в быстром диалоге."
            ]
        }
    },

    # Day 6
    {
        "day": 6,
        "phase": 1,
        "title": {
            "en": "Conversational Repair and Comprehension Boundaries",
            "ru": "Языковой ремонт: управление непониманием и просьба говорить медленнее"
        },
        "theme": "Я не говорю на хинди, говорите медленнее, повторите еще раз",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция придыхательного dh в dhīrē / дхиирэ)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Дативная конструкция Mujhe Hindi nahĩ ati = Мне хинди не приходит)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Шейдоуинг защитных речевых фраз)",
            "phase4SimulationMinutes": "17:00–20:00 (Отражение стремительной речи собеседника)"
        },
        "learningObjectives": {
            "en": [
                "Decline fluent speech with dative experiencer 'Mujhē Hindī nahī̃ ātī'",
                "Request slow speech using polite imperative 'Dhīrē bōliye'",
                "Acknowledge non-comprehension with feminine past marker 'Main nahī̃ samjhī'"
            ],
            "ru": [
                "Сообщать о незнании языка через дативную конструкцию 'Mujhē Hindī nahī̃ ātī' ('Мне хинди не приходит')",
                "Просить говорить медленнее с помощью вежливой просьбы 'Dhīrē bōliye'",
                "Заявлять о непонимании в женском роде 'Main nahī̃ samjhī' ('Я не поняла')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Звонкий придыхательный дентальный /dh/ (ध) в слове dhīrē",
            "articulatoryMechanism": "Лопатка языка на резцах. Одновременно с голосом идет сильный выдох (шепотная фонация).",
            "russianInterferenceWarning": "Не заменяйте на глухой звук 'т' или английский межзубный [th]. Это чистый звонкий русский [д] с глубоким выдохом [дх].",
            "drills": [
                {
                    "prompt": "Произнесение слова 'медленно'",
                    "contrastPair": "dīrē (без выдоха) vs dhīrē (с мощным теплым выдохом)",
                    "instructionsRu": "Почувствуйте теплое дыхание на ладони при слоге 'dhī'."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Дативный субъект восприятия (Experiencer Subject)",
            "russianParallel": "Прямое совпадение с русским дательным падежом: 'Мне не понятно' / 'Мне хинди не дается'. В хинди: Mujhē (Мне) + Hindī (хинди) + nahī̃ ātī (не приходит).",
            "syntacticFormula": "Mujhē + [Язык] + nahī̃ ātī (hai)",
            "explanationRu": "Знание языка в хинди мыслится как способность, которая 'приходит' к человеку (глагол ānā = приходить). Поэтому субъект стоит в дативе: Mujhē (мне). Для женщин 'я не поняла' звучит: Main nahī̃ samjhī (-ī указывает на женский род).",
            "pieCognateConnection": {
                "root": "*bʰel- / *bʰol-",
                "russian": "болтать / баять",
                "hindi": "bōlnā (bōliye)",
                "meaning": "Говорить / звучать"
            }
        },
        "vocabulary": [
            {
                "id": "d06_v01",
                "devanagari": "मुझे",
                "transliterationIso": "Mujhē",
                "phoneticCyrillic": "Муджхе",
                "translationRu": "Мне (дательный падеж от 'я')",
                "translationEn": "To me / Me (dative)",
                "partOfSpeech": "pronoun",
                "gender": "both",
                "audioHint": "Звук [джх] с придыханием."
            },
            {
                "id": "d06_v02",
                "devanagari": "धीरे",
                "transliterationIso": "Dhīrē",
                "phoneticCyrillic": "Дхиирэ",
                "translationRu": "Медленно / Спокойно",
                "translationEn": "Slowly",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Придыхательное звонкое [дх]."
            },
            {
                "id": "d06_v03",
                "devanagari": "बोलिए",
                "transliterationIso": "Bōliye",
                "phoneticCyrillic": "Болие",
                "translationRu": "Говорите / Скажите (вежливо)",
                "translationEn": "Speak / Please say",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Чистый гласный 'о', суффикс -iye."
            },
            {
                "id": "d06_v04",
                "devanagari": "फिर से",
                "transliterationIso": "Phir sē",
                "phoneticCyrillic": "Пхир сэ",
                "translationRu": "Снова / Еще раз",
                "translationEn": "Again / Once more",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Придыхательное [пх], раскатистый [р]."
            },
            {
                "id": "d06_v05",
                "devanagari": "समझी",
                "transliterationIso": "Samjhī",
                "phoneticCyrillic": "Самджи",
                "translationRu": "Поняла (женский род)",
                "translationEn": "Understood (feminine)",
                "partOfSpeech": "verb",
                "gender": "f",
                "audioHint": "Окончание -ī указывает на говорящую женщину."
            }
        ],
        "exercises": [
            {
                "id": "d06_ex01",
                "type": "substitution_drill",
                "instructionRu": "Сформулируйте фразу: 'Я не говорю на хинди' (буквально: 'Мне хинди не приходит')",
                "prompt": "_____ Hindī nahī̃ ātī.",
                "options": ["Mujhē", "Main", "Mērā"],
                "correctAnswer": "Mujhē",
                "transliterationIsoTarget": "Mujhē Hindī nahī̃ ātī",
                "explanationRu": "В конструкциях владения языком используется дативный субъект Mujhē (мне)."
            },
            {
                "id": "d06_ex02",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите вежливую просьбу говорить медленнее (Медленно + говорите)",
                "prompt": "Говорите медленнее, пожалуйста",
                "wordChips": ["Dhīrē", "bōliye"],
                "correctAnswer": ["Dhīrē", "bōliye"],
                "phoneticCyrillicTarget": "Дхиирэ болие",
                "explanationRu": "Обстоятельство предшествует вежливому глаголу: Dhīrē bōliye."
            },
            {
                "id": "d06_ex03",
                "type": "listen_and_repeat",
                "instructionRu": "Произнесите просьбу повторить еще раз",
                "prompt": "Phir sē bōliye (Повторите еще раз)",
                "phoneticCyrillicTarget": "Пхир сэ болие",
                "transliterationIsoTarget": "Phir sē bōliye",
                "correctAnswer": "Phir sē bōliye",
                "explanationRu": "Phir sē (снова) + bōliye (скажите)."
            },
            {
                "id": "d06_ex04",
                "type": "rapid_oral_challenge",
                "instructionRu": "Собеседник говорит слишком быстро. Остановите его и попросите говорить медленно за 3 секунды.",
                "prompt": "Собеседник говорит со скоростью пулемета",
                "options": [
                    "Māf kījiye, dhīrē bōliye!",
                    "Bahut acchā, shukriyā!",
                    "Main Moscow sē hū̃!"
                ],
                "correctAnswer": "Māf kījiye, dhīrē bōliye!",
                "phoneticCyrillicTarget": "Мааф кииджие, дхиирэ болие!",
                "explanationRu": "Идеальная связка: Извините, говорите медленнее!"
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Преодоление языкового барьера с водителем",
            "setting": "Остановка такси, водитель быстро сыплет вопросами",
            "partnerRoleRu": "Эмоциональный таксист",
            "learnerRoleRu": "Путешественница",
            "turns": [
                {
                    "speaker": "Таксист",
                    "speechRu": "Куда едем, мадам? В отель или на рынок? Быстро довезу!",
                    "speechIso": "Kahā̃ jānā hai, madam? Hotel ya market? Chalo chalo!",
                    "speechCyrillic": "Кахааⁿ джаанаа хэ, мадам? Хотел йа маркет? Чало чало!",
                    "learnerHintRu": "Скажите: Извините, я не знаю хинди. Говорите медленнее."
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Извините, я не говорю на хинди. Пожалуйста, говорите медленно.",
                    "speechIso": "Māf kījiye, mujhē Hindī nahī̃ ātī. Dhīrē bōliye.",
                    "speechCyrillic": "Мааф кииджие, муджхе Хиндии нахииⁿ аатии. Дхиирэ болие.",
                    "acceptableResponsesIso": ["Mujhē Hindī nahī̃ ātī. Dhīrē bōliye."]
                },
                {
                    "speaker": "Таксист",
                    "speechRu": "А, хорошо, мадам. Вы говорите по-английски?",
                    "speechIso": "Acchā, acchā. Kyā āpkō English ātī hai?",
                    "speechCyrillic": "Аччхаа, аччхаа. Кйаа аапко инглиш аатии хэ?",
                    "learnerHintRu": "Ответьте: Да, я знаю английский (Hā̃-jī)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Да, английский знаю.",
                    "speechIso": "Hā̃-jī, English ātī hai.",
                    "speechCyrillic": "Хааⁿ-джии, инглиш аатии хэ.",
                    "acceptableResponsesIso": ["Hā̃-jī"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Психологическая уверенность при непонимании",
            "pointsRu": [
                "Никогда не смущайтесь фразы 'Mujhē Hindī nahī̃ ātī' — индийцы мгновенно адаптируют темп речи.",
                "Использование حتی нескольких слов на хинди вызывает колоссальное уважение местных жителей.",
                "Спокойный тон и вежливая улыбка устраняют 99% недопониманий в путешествии."
            ]
        }
    },

    # Day 7
    {
        "day": 7,
        "phase": 1,
        "title": {
            "en": "Spatial Deixis and Demonstratives",
            "ru": "Пространственная дейксис: указательные местоимения (Этот/Тот, Здесь/Там)"
        },
        "theme": "Yeh (этот/он/она) и Voh (тот/он/она), Yahā̃ (здесь) и Vahā̃ (там)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция кратких гласных в Yeh / Voh и назализации в Yahā̃ / Vahā̃)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Нейтрализация рода местоимений 3-го лица: Yeh = он/она/это)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Указание на ближние и дальние объекты)",
            "phase4SimulationMinutes": "17:00–20:00 (Ориентирование в номере гостиницы)"
        },
        "learningObjectives": {
            "en": [
                "Contrast proximal (Yeh, Yahā̃) and distal (Voh, Vahā̃) demonstratives",
                "Understand that 3rd person pronouns collapse gender distinctions",
                "Direct people using Yahā̃ baithiye (Sit here) and Vahā̃ jāiye (Go there)"
            ],
            "ru": [
                "Различать ближний (Yeh, Yahā̃ = этот, здесь) и дальний (Voh, Vahā̃ = тот, там) дейксис",
                "Усвоить, что местоимения Yeh и Voh заменяют слова 'он', 'она', 'оно' без различия рода",
                "Использовать связки с указанием места: 'Yahā̃ baithiye' (садитесь здесь), 'Vahā̃ jāiye' (идите туда)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Лабиодентальный /v/ (व) и полугласный /y/ (य) в начале дейктиков",
            "articulatoryMechanism": "Для 'Voh' губы слегка сближаются (звук средний между русским [в] и английским [w]). В 'Yahā̃' чистый [йахааⁿ].",
            "russianInterferenceWarning": "Не оглушайте 'v' на конце слогов. Следите за долготой носового гласного в yahā̃ / vahā̃.",
            "drills": [
                {
                    "prompt": "Пары 'здесь — там'",
                    "contrastPair": "Yahā̃ (здесь) vs Vahā̃ (там)",
                    "instructionsRu": "Произносите парно с указательным жестом рукой: [йахааⁿ] — [вахааⁿ]."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Пространственный дейксис и местоимения 3-го лица",
            "russianParallel": "Строгое соответствие русской паре 'этот / тот' и 'здесь / там'. Главное отличие от русского языка: в хинди местоимения 3-го лица НЕ делятся по родам! Yeh значит и 'он', и 'она', и 'это' (близко); Voh значит 'он', 'она', 'то' (далеко).",
            "syntacticFormula": "[Yeh / Voh] + [Существительное] + [hai]",
            "explanationRu": "В разговорной речи Yeh часто произносится как [ye] или [e], а Voh как [vo] или [o]. Это колоссально упрощает общение, так как не нужно думать о роде местоимения при указании на предмет.",
            "pieCognateConnection": {
                "root": "*e- / *ey-",
                "russian": "этот / эта",
                "hindi": "yeh / yahā̃",
                "meaning": "Праиндоевропейская дейктическая основа"
            }
        },
        "vocabulary": [
            {
                "id": "d07_v01",
                "devanagari": "यह",
                "transliterationIso": "Yeh",
                "phoneticCyrillic": "Йе",
                "translationRu": "Этот / Эта / Это / Он / Она (вблизи)",
                "translationEn": "This / He / She / It (proximal)",
                "partOfSpeech": "pronoun",
                "gender": "both",
                "audioHint": "В разговорной речи звучит как краткое открытое [йе]."
            },
            {
                "id": "d07_v02",
                "devanagari": "वह",
                "transliterationIso": "Voh",
                "phoneticCyrillic": "Во",
                "translationRu": "Тот / Та / То / Он / Она (вдали)",
                "translationEn": "That / He / She / It (distal)",
                "partOfSpeech": "pronoun",
                "gender": "both",
                "audioHint": "Звучит как [во] или [о]."
            },
            {
                "id": "d07_v03",
                "devanagari": "यहाँ",
                "transliterationIso": "Yahā̃",
                "phoneticCyrillic": "Йахааⁿ",
                "translationRu": "Здесь / Сюда",
                "translationEn": "Here",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Носовой звук на конце."
            },
            {
                "id": "d07_v04",
                "devanagari": "वहाँ",
                "transliterationIso": "Vahā̃",
                "phoneticCyrillic": "Вахааⁿ",
                "translationRu": "Там / Туда",
                "translationEn": "There",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Носовой звук на конце."
            },
            {
                "id": "d07_v05",
                "devanagari": "बैठिए",
                "transliterationIso": "Baithiye",
                "phoneticCyrillic": "Бэтхие",
                "translationRu": "Садитесь, пожалуйста",
                "translationEn": "Please sit",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Придыхательное [тх], суффикс вежливости -iye."
            }
        ],
        "exercises": [
            {
                "id": "d07_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите предложение: 'Это отель' (Этот + отель + есть)",
                "prompt": "Это гостиница",
                "wordChips": ["Yeh", "hotel", "hai"],
                "correctAnswer": ["Yeh", "hotel", "hai"],
                "phoneticCyrillicTarget": "Йе хотел хэ",
                "explanationRu": "Yeh (это) + hotel + hai (есть)."
            },
            {
                "id": "d07_ex02",
                "type": "substitution_drill",
                "instructionRu": "Предложите гостю: 'Садитесь сюда, пожалуйста'",
                "prompt": "_____ baithiye (Садитесь здесь)",
                "options": ["Yahā̃", "Vahā̃", "Kyā"],
                "correctAnswer": "Yahā̃",
                "transliterationIsoTarget": "Yahā̃ baithiye",
                "explanationRu": "Yahā̃ означает 'здесь / сюда'."
            },
            {
                "id": "d07_ex03",
                "type": "fill_in_blank",
                "instructionRu": "Укажите на дальний объект (Вон там)",
                "prompt": "Station _____ hai. (Вокзал вон там)",
                "options": ["vahā̃", "yahā̃", "yeh"],
                "correctAnswer": "vahā̃",
                "transliterationIsoTarget": "Station vahā̃ hai",
                "explanationRu": "Vahā̃ означает 'там / вон там'."
            },
            {
                "id": "d07_ex04",
                "type": "rapid_oral_challenge",
                "instructionRu": "Укажите на блюдо на столе и спросите: 'Что это?'",
                "prompt": "Что это?",
                "options": ["Yeh kyā hai?", "Voh kahā̃ hai?", "Kyā hai yeh?"],
                "correctAnswer": "Yeh kyā hai?",
                "phoneticCyrillicTarget": "Йе кйаа хэ?",
                "explanationRu": "Yeh kyā hai? — универсальный вопрос при изучении индийских блюд и предметов."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Заселение в номер и осмотр удобств",
            "setting": "Гостиничный номер",
            "partnerRoleRu": "Коридорный / портье",
            "learnerRoleRu": "Постоялица",
            "turns": [
                {
                    "speaker": "Портье",
                    "speechRu": "Пожалуйста, проходите. Это ваш номер.",
                    "speechIso": "Āiye jī, yeh āpkā room hai.",
                    "speechCyrillic": "Ааие джии, йе аапкаа руум хэ.",
                    "learnerHintRu": "Поблагодарите: Bahut acchā, shukriyā!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Очень хорошо, спасибо!",
                    "speechIso": "Bahut acchā, shukriyā!",
                    "speechCyrillic": "Бахут аччхаа, шукрийа!",
                    "acceptableResponsesIso": ["Shukriyā jī", "Bahut acchā!"]
                },
                {
                    "speaker": "Портье",
                    "speechRu": "Садитесь здесь, пожалуйста. Вода вон там.",
                    "speechIso": "Yahā̃ baithiye. Pānī vahā̃ hai.",
                    "speechCyrillic": "Йахааⁿ бэтхие. Паании вахааⁿ хэ.",
                    "learnerHintRu": "Скажите 'Ṭhīk hai, dhanyavād!'"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Хорошо, спасибо большое!",
                    "speechIso": "Ṭhīk hai, dhanyavād!",
                    "speechCyrillic": "Т͟хиик хэ, дханьяваад!",
                    "acceptableResponsesIso": ["Ṭhīk hai jī"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Жесты указания на предметы и людей",
            "pointsRu": [
                "В Индии указывать на человека одним указательным пальцем считается невежливым.",
                "Используйте открытую ладонь или кивок подбородка при словах 'Yeh' (этот человек / предмет) или 'Voh'.",
                "Приглашение сесть 'Baithiye' всегда произносится с теплым жестом ладони к креслу."
            ]
        }
    },

    # Day 8
    {
        "day": 8,
        "phase": 1,
        "title": {
            "en": "Phase 1 Synthesis, Articulatory Review, and Introductory Simulation",
            "ru": "Синтез Фазы 1: интеграционный диалог заселения и закрепление фонетики"
        },
        "theme": "Полная 20-минутная симуляция приезда: встреча, имя, страна, вопросы, ремонт",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Фонетический аудит всех звуков: dental t vs retroflex ṭ, aspirate dh/ṭh, nasals)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Сборка структур: приветствие + имя + происхождение + вежливость)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Сквозной ролевой прогон без использования английского языка)",
            "phase4SimulationMinutes": "17:00–20:00 (Экзаменационная ситуативная ролевая игра Фазы 1)"
        },
        "learningObjectives": {
            "en": [
                "Integrate greetings, origin, questions, and comprehension repair into continuous speech",
                "Execute the complete arrival dialogue without reverting to English",
                "Ensure consistent dental vs retroflex distinction under conversational pressure"
            ],
            "ru": [
                "Объединить приветствия, имя, страну происхождения и языковой ремонт в связную речь",
                "Провести непрерывный диалог приезда без перехода на английский язык",
                "Автоматизировать различие зубных и ретрофлексных звуков в спонтанном потоке речи"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Комплексный контроль: устранение палатализации и сохранение безударной долготы",
            "articulatoryMechanism": "Держите долгие гласные (ā, ī, ū) в безударных позициях, не допуская русского аканья (например, в dhanyavād не превращать первый слог в [дхъньяват]).",
            "russianInterferenceWarning": "Главная опасность — русская редукция. Все гласные должны звучать четко и полнозвучно!",
            "drills": [
                {
                    "prompt": "Сквозной фонетический марш",
                    "contrastPair": "Namastē -> Main ṭhīk hū̃ -> Russia sē -> Māf kījiye",
                    "instructionsRu": "Произнесите связку на одном дыхании с максимальной четкостью артикуляции."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Консолидация синтаксического ядра: SOV и связка hai/hū̃",
            "russianParallel": "Закрепление фундамента: глагол всегда на конце предложения, уважительное Вы (Āp) требует окончания -ē или частицы jī, дативные переживания (Mujhē Hindī nahī̃ ātī).",
            "syntacticFormula": "[Приветствие] + [Main ... hū̃] + [Āp kaisē/kaisī haiñ?] + [Вопрос / Запрос]",
            "explanationRu": "Фаза 1 полностью сформировала ваш речевой аппарат и базовый этикет. Теперь вы способны выдержать первый контакт в Индии исключительно на разговорном хинди!",
            "pieCognateConnection": {
                "root": "*bʰrehtēr / *meh₂tēr / *dʰwer-",
                "russian": "брат / мать / дверь",
                "hindi": "bhāī / mātā / dvār",
                "meaning": "Общий фонд индоевропейского словарного запаса"
            }
        },
        "vocabulary": [
            {
                "id": "d08_v01",
                "devanagari": "नमस्ते जी",
                "transliterationIso": "Namastē jī",
                "phoneticCyrillic": "Намастэ джии",
                "translationRu": "Здравствуйте (вежливо)",
                "translationEn": "Greetings (respectful)",
                "partOfSpeech": "interjection",
                "gender": "n/a",
                "audioHint": "Уважительная форма."
            },
            {
                "id": "d08_v02",
                "devanagari": "धन्यवाद जी",
                "transliterationIso": "Dhanyavād jī",
                "phoneticCyrillic": "Дханьяваад джии",
                "translationRu": "Большое спасибо",
                "translationEn": "Thank you very much",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Долгое 'аа'."
            },
            {
                "id": "d08_v03",
                "devanagari": "भाई",
                "transliterationIso": "Bhāī",
                "phoneticCyrillic": "Бхааии",
                "translationRu": "Брат / Обращение к мужчине",
                "translationEn": "Brother",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Когнат с русским 'брат'."
            },
            {
                "id": "d08_v04",
                "devanagari": "होटल",
                "transliterationIso": "Hotel",
                "phoneticCyrillic": "Хотел",
                "translationRu": "Отель / Гостиница",
                "translationEn": "Hotel",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Общеупотребительное слово."
            }
        ],
        "exercises": [
            {
                "id": "d08_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите комплексное предложение: 'Здравствуйте, меня зовут Анна, я из России'",
                "prompt": "Здравствуйте, меня зовут Анна, я из России",
                "wordChips": ["Namastē jī,", "mērā nām", "Anna hai,", "main Russia sē", "hū̃"],
                "correctAnswer": ["Namastē jī,", "mērā nām", "Anna hai,", "main Russia sē", "hū̃"],
                "phoneticCyrillicTarget": "Намастэ джии, мераа наам Анна хэ, мэⁿ Расийа сэ хууⁿ",
                "explanationRu": "Полная цепочка самопрезентации первого контакта."
            },
            {
                "id": "d08_ex02",
                "type": "dialogue_roleplay",
                "instructionRu": "Ответьте на вопрос о вашем самочувствии и спросите в ответ",
                "prompt": "Хозяин: Āp kaisī haiñ?",
                "options": [
                    "Main ṭhīk hū̃, dhanyavād! Aur āp?",
                    "Mērā nām Moscow hai!",
                    "Yeh station vahā̃ hai!"
                ],
                "correctAnswer": "Main ṭhīk hū̃, dhanyavād! Aur āp?",
                "phoneticCyrillicTarget": "Мэⁿ т͟хиик хууⁿ, дханьяваад! Аур аап?",
                "explanationRu": "Вежливый ответ с благодарностью и встречным вопросом."
            },
            {
                "id": "d08_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Хозяин отеля говорит очень быстро. Попросите его говорить медленно.",
                "prompt": "Хозяин тараторит условия проживания",
                "options": [
                    "Māf kījiye, dhīrē bōliye!",
                    "Shukriyā, main acchā hū̃!",
                    "Nahī̃, yeh hotel hai!"
                ],
                "correctAnswer": "Māf kījiye, dhīrē bōliye!",
                "phoneticCyrillicTarget": "Мааф кииджие, дхиирэ болие!",
                "explanationRu": "Языковой тормоз: Извините, говорите помедленнее."
            },
            {
                "id": "d08_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Завершите фразу согласия: 'Да, все хорошо!'",
                "prompt": "Hā̃-jī, _____ hai.",
                "options": ["ṭhīk", "kahan", "kaun"],
                "correctAnswer": "ṭhīk",
                "transliterationIsoTarget": "Hā̃-jī, ṭhīk hai",
                "explanationRu": "Ṭhīk hai = все хорошо / в порядке."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Экзаменационная симуляция Фазы 1: Полное заселение",
            "setting": "Холл семейного гестхауса в Варанаси или Джайпуре",
            "partnerRoleRu": "Владелец гестхауса",
            "learnerRoleRu": "Путешественница",
            "turns": [
                {
                    "speaker": "Владелец",
                    "speechRu": "Намастэ! Добро пожаловать! Как вас зовут?",
                    "speechIso": "Namastē jī! Welcome! Āpkā nām kyā hai?",
                    "speechCyrillic": "Намастэ джии! Вэлкам! Аапкаа наам кйаа хэ?",
                    "learnerHintRu": "Поприветствуйте и назовите имя: Namastē jī! Mērā nām [Имя] hai."
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте! Меня зовут Анна. Я из России.",
                    "speechIso": "Namastē jī! Mērā nām Anna hai. Main Russia sē hū̃.",
                    "speechCyrillic": "Намастэ джии! Мераа наам Анна хэ. Мэⁿ Расийа сэ хууⁿ.",
                    "acceptableResponsesIso": ["Namastē jī! Mērā nām Anna hai.", "Main Russia sē hū̃."]
                },
                {
                    "speaker": "Владелец",
                    "speechRu": "Очень приятно! Как ваши дела? Все в порядке?",
                    "speechIso": "Bahut acchā! Āp kaisī haiñ? Sab ṭhīk?",
                    "speechCyrillic": "Бахут аччхаа! Аап кэсии хэⁿ? Саб т͟хиик?",
                    "learnerHintRu": "Ответьте: Main ṭhīk hū̃, dhanyavād! Aur āp?"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Я в порядке, спасибо! А как ваши дела?",
                    "speechIso": "Main ṭhīk hū̃, dhanyavād! Aur āp?",
                    "speechCyrillic": "Мэⁿ т͟хиик хууⁿ, дханьяваад! Аур аап?",
                    "acceptableResponsesIso": ["Main ṭhīk hū̃, shukriyā!"]
                },
                {
                    "speaker": "Владелец",
                    "speechRu": "Все отлично! Проходите, комната номер 3 направо.",
                    "speechIso": "Main bhī ṭhīk hū̃! Āiye jī, room number 3 vahā̃ hai.",
                    "speechCyrillic": "Мэⁿ бхии т͟хиик хууⁿ! Ааие джии, руум намбар 3 вахааⁿ хэ.",
                    "learnerHintRu": "Поблагодарите: Bahut shukriyā jī!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Большое спасибо!",
                    "speechIso": "Bahut shukriyā jī!",
                    "speechCyrillic": "Бахут шукрийа джии!",
                    "acceptableResponsesIso": ["Dhanyavād jī!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Итоги Фазы 1: Преодоление первого речевого барьера",
            "pointsRu": [
                "Вы освоили главный ключ к вежливости в Индии: связку жеста Намастэ и частицы Джи.",
                "Вы привыкли к тому, что глагол-связка hū̃/hai обязательно стоит на конце предложения.",
                "Вы умеете управлять темпом беседы и не боитесь переспросить 'Dhīrē bōliye'."
            ]
        }
    }
]
