"""
data_phase2.py - Days 09 to 16
Phase 2: Spatial Navigation, Locatives, and Transit Logistics
"""

DAYS_PHASE_2 = [
    # Day 9
    {
        "day": 9,
        "phase": 2,
        "title": {
            "en": "Syntactic Realignment: Establishing Fixed SOV Order",
            "ru": "Синтаксическая перестройка: жесткий порядок слов SOV и направления"
        },
        "theme": "Налево, направо, прямо, идите, остановитесь. Перестройка с русского SVO на хинди SOV",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Назализация bāē̃ / дааеⁿ и ретрофлексный flap в rukiye)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Правило: Направление ВСЕГДА стоит ПЕРЕД глаголом: Sīdhē jāiye)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Команды водителю на поворотах: налево, направо, стоп)",
            "phase4SimulationMinutes": "17:00–20:00 (Управление водителем тук-тука на развилке)"
        },
        "learningObjectives": {
            "en": [
                "Realign Russian SVO word order to strict Hindi SOV (Direction before Verb)",
                "Master directional directives (Bāē̃, Dāē̃, Sīdhē)",
                "Command stops politely using Rukiye (Please stop)"
            ],
            "ru": [
                "Перестроить мышление с русского SVO на строгий порядок хинди SOV (направление ставится ПЕРЕД глаголом)",
                "Освоить указатели поворотов: Bāē̃ (налево), Dāē̃ (направо), Sīdhē (прямо)",
                "Вежливо командовать остановку: Rukiye (Остановитесь, пожалуйста) и Yahā̃ rukiye (Здесь остановитесь)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Назализованный дифтонг /āē̃/ в bāē̃ (बाएँ) и dāē̃ (दाएँ)",
            "articulatoryMechanism": "Переход от долгого 'аа' к открытому 'э' с одновременным выходом воздуха через нос: [бааеⁿ], [дааеⁿ].",
            "russianInterferenceWarning": "Не произносите согласный звук [н] в конце слова! Ни в коем случае не 'баен' или 'даен', только чистый носовой гласный.",
            "drills": [
                {
                    "prompt": "Пара налево / направо",
                    "contrastPair": "Bāē̃ (налево) vs Dāē̃ (направо)",
                    "instructionsRu": "Произносите парно: налево [бааеⁿ], направо [дааеⁿ]."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Инверсия русского порядка слов глагол-направление",
            "russianParallel": "В русском языке мы говорим: 'Идите прямо' или 'Поверните направо' (Глагол + Направление). В хинди порядок СТРОГО обратный: Sīdhē jāiye (Прямо идите), Bāē̃ jāiye (Налево идите). Конечный глагол ВСЕГДА закрывает фразу!",
            "syntacticFormula": "[Ориентир / Направление] + [Повелительный глагол (Императив)]",
            "explanationRu": "Глагол в хинди выполняет роль точки в конце предложения. Любые указатели пути, направления и расстояния обязаны стоять ДО глагола.",
            "pieCognateConnection": {
                "root": "*sed- / *sidh-",
                "russian": "сесть / сидеть",
                "hindi": "sīdhē (прямой путь / праведный)",
                "meaning": "Индоевропейская ориентация и порядок"
            }
        },
        "vocabulary": [
            {
                "id": "d09_v01",
                "devanagari": "बाएँ",
                "transliterationIso": "Bāē̃",
                "phoneticCyrillic": "Бааеⁿ",
                "translationRu": "Налево / Слева",
                "translationEn": "Left",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Носовой дифтонг на конце."
            },
            {
                "id": "d09_v02",
                "devanagari": "दाएँ",
                "transliterationIso": "Dāē̃",
                "phoneticCyrillic": "Дааеⁿ",
                "translationRu": "Направо / Справа",
                "translationEn": "Right",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Зубной звук [д], носовой дифтонг."
            },
            {
                "id": "d09_v03",
                "devanagari": "सीधे",
                "transliterationIso": "Sīdhē",
                "phoneticCyrillic": "Сиидхэ",
                "translationRu": "Прямо",
                "translationEn": "Straight",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Долгое 'ии', придыхательное 'дх'."
            },
            {
                "id": "d09_v04",
                "devanagari": "जाइए",
                "transliterationIso": "Jāiye",
                "phoneticCyrillic": "Джааие",
                "translationRu": "Идите / Поезжайте (вежливо)",
                "translationEn": "Please go",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Слитный [дж] + суффикс -iye."
            },
            {
                "id": "d09_v05",
                "devanagari": "रुकिए",
                "transliterationIso": "Rukiye",
                "phoneticCyrillic": "Рукие",
                "translationRu": "Остановитесь / Подождите (вежливо)",
                "translationEn": "Please stop",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Раскатистый 'р', краткое 'у'."
            }
        ],
        "exercises": [
            {
                "id": "d09_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите указание водителю 'Поезжайте прямо' (Прямо + поезжайте)",
                "prompt": "Поезжайте прямо (русский: Идите прямо)",
                "wordChips": ["Sīdhē", "jāiye"],
                "correctAnswer": ["Sīdhē", "jāiye"],
                "phoneticCyrillicTarget": "Сиидхэ джааие",
                "explanationRu": "В хинди направление предшествует глаголу: Sīdhē jāiye."
            },
            {
                "id": "d09_ex02",
                "type": "substitution_drill",
                "instructionRu": "Скажите водителю повернуть налево",
                "prompt": "_____ jāiye! (Поверните налево)",
                "options": ["Bāē̃", "Dāē̃", "Sīdhē"],
                "correctAnswer": "Bāē̃",
                "transliterationIsoTarget": "Bāē̃ jāiye!",
                "explanationRu": "Bāē̃ = налево."
            },
            {
                "id": "d09_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вы подъехали к своему отелю. Скомандуйте водителю: 'Остановитесь здесь!' за 2 секунды.",
                "prompt": "Водитель проезжает нужный дом",
                "options": [
                    "Yahā̃ rukiye!",
                    "Vahā̃ jāiye!",
                    "Sīdhē chalo!"
                ],
                "correctAnswer": "Yahā̃ rukiye!",
                "phoneticCyrillicTarget": "Йахааⁿ рукие!",
                "explanationRu": "Yahā̃ (здесь) + rukiye (остановитесь)."
            },
            {
                "id": "d09_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Вставьте глагол 'поезжайте / идите' в приказ 'Направо, пожалуйста'",
                "prompt": "Dāē̃ _____! (Поверните направо)",
                "options": ["jāiye", "rukiye", "hai"],
                "correctAnswer": "jāiye",
                "transliterationIsoTarget": "Dāē̃ jāiye!",
                "explanationRu": "Dāē̃ jāiye = поезжайте направо."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Навигация авторикши в лабиринте старого города",
            "setting": "Авторикша на перекрестке в Дели или Джайпуре",
            "partnerRoleRu": "Водитель рикши (спрашивает дорогу)",
            "learnerRoleRu": "Пассажирка с навигатором",
            "turns": [
                {
                    "speaker": "Водитель",
                    "speechRu": "Сестра, куда поворачивать? Налево или направо?",
                    "speechIso": "Madam, bāē̃ ya dāē̃?",
                    "speechCyrillic": "Мадам, бааеⁿ йа дааеⁿ?",
                    "learnerHintRu": "Скажите: Прямо поезжайте (Sīdhē jāiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Езжайте прямо.",
                    "speechIso": "Sīdhē jāiye.",
                    "speechCyrillic": "Сиидхэ джааие.",
                    "acceptableResponsesIso": ["Sīdhē jāiye"]
                },
                {
                    "speaker": "Водитель",
                    "speechRu": "Понял, едем прямо. А теперь куда?",
                    "speechIso": "Acchā jī. Ab kahā̃?",
                    "speechCyrillic": "Аччхаа джии. Аб кахааⁿ?",
                    "learnerHintRu": "Скажите: Налево, а затем остановитесь здесь!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Поверните налево. Остановитесь прямо здесь!",
                    "speechIso": "Bāē̃ jāiye. Yahā̃ rukiye!",
                    "speechCyrillic": "Бааеⁿ джааие. Йахааⁿ рукие!",
                    "acceptableResponsesIso": ["Bāē̃ jāiye, yahā̃ rukiye!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Как подсказывать дорогу в индийском транспорте",
            "pointsRu": [
                "Водители рикш часто не смотрят в мобильные навигаторы, а полагаются на живые подсказки пассажира.",
                "Связка 'Bhaiyā, sīdhē jāiye' звучит уважительно и сразу дает водителю нужный ориентир.",
                "Громкая и четкая команда 'Bhaiyā, yahā̃ rukiye!' спасет от проезда нужного переулка."
            ]
        }
    },

    # Day 10
    {
        "day": 10,
        "phase": 2,
        "title": {
            "en": "Inessive and Adessive Postpositions (Mẽ and Par)",
            "ru": "Локативные послелоги: Mẽ (В) и Par (На/У)"
        },
        "theme": "Локализация в пространстве: в отеле (hotel mẽ), на станции (station par), в машине (gāṛī mẽ)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Назализация /ẽ/ в mẽ vs твердый губной p в par)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Концепция послелога: русские предлоги В и НА ставятся ПОСЛЕ слова)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Трансформация: в машине, на столе, на вокзале, в комнате)",
            "phase4SimulationMinutes": "17:00–20:00 (Поиск оставленных вещей в гостинице и машине)"
        },
        "learningObjectives": {
            "en": [
                "Shift prepositions 'in' and 'on' into postpositions mẽ and par",
                "Express spatial containment using mẽ (gāṛī mẽ, room mẽ)",
                "Express surface contact and transport hubs using par (station par, mēz par)"
            ],
            "ru": [
                "Превратить русские предлоги 'В' и 'НА' в послелоги mẽ и par, ставя их строго ПОСЛЕ существительного",
                "Обозначать нахождение внутри объекта с помощью 'mẽ' (hotel mẽ = в отеле, gāṛī mẽ = в машине)",
                "Обозначать нахождение на поверхности или объекте с помощью 'par' (station par = на вокзале, mēz par = на столе)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Носовой гласный /ẽ/ в послелоге mẽ (में)",
            "articulatoryMechanism": "Широкий гласный [э] направляется в носовую полость. На конце не должно быть согласного звука 'н'.",
            "russianInterferenceWarning": "Не путать с русским местоимением 'мне'! В хинди mẽ звучит как [мэⁿ].",
            "drills": [
                {
                    "prompt": "Отработка послелогов места",
                    "contrastPair": "mẽ (внутри) vs par (на поверхности)",
                    "instructionsRu": "Hotel mẽ (в отеле) — Station par (на вокзале)."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Послелоги вместо предлогов (Postpositions)",
            "russianParallel": "В русском языке предлоги стоят ПЕРЕД словом (В отеле, НА столе). В хинди они стоят ПОСЛЕ слова (Hotel mẽ, Mēz par). Семантически они абсолютно точно соответствуют русскому предложному падежу (в чём? на чём?).",
            "syntacticFormula": "[Существительное / Место] + [mẽ (в) / par (на)] + [hai]",
            "explanationRu": "Это ключевое открытие для русскоязычного студента: категория предложного падежа уже есть в вашем мозгу, нужно лишь механически переставить предлог за существительное.",
            "pieCognateConnection": {
                "root": "*per- / *pro-",
                "russian": "через / при / перед",
                "hindi": "par (на / при)",
                "meaning": "Индоевропейский локативно-поверхностный корень"
            }
        },
        "vocabulary": [
            {
                "id": "d10_v01",
                "devanagari": "में",
                "transliterationIso": "Mẽ",
                "phoneticCyrillic": "Мэⁿ",
                "translationRu": "в / внутри (послелог)",
                "translationEn": "in / inside",
                "partOfSpeech": "postposition",
                "gender": "n/a",
                "audioHint": "Носовое [мэⁿ]."
            },
            {
                "id": "d10_v02",
                "devanagari": "पर",
                "transliterationIso": "Par",
                "phoneticCyrillic": "Пар",
                "translationRu": "на / у / при (послелог)",
                "translationEn": "on / at",
                "partOfSpeech": "postposition",
                "gender": "n/a",
                "audioHint": "Непридыхательный 'п', раскатистый 'р'."
            },
            {
                "id": "d10_v03",
                "devanagari": "गाड़ी",
                "transliterationIso": "Gāṛī",
                "phoneticCyrillic": "Гаар͟ии",
                "translationRu": "Машина / Автомобиль / Поезд",
                "translationEn": "Car / Vehicle / Train",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Ретрофлексный flap [р͟]."
            },
            {
                "id": "d10_v04",
                "devanagari": "मेज़",
                "transliterationIso": "Mēz",
                "phoneticCyrillic": "Мэз",
                "translationRu": "Стол",
                "translationEn": "Table",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Звонкий [з]."
            },
            {
                "id": "d10_v05",
                "devanagari": "कमरा",
                "transliterationIso": "Kamrā",
                "phoneticCyrillic": "Камраа",
                "translationRu": "Комната / Номер",
                "translationEn": "Room",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Долгое 'аа' на конце."
            }
        ],
        "exercises": [
            {
                "id": "d10_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите предложение 'Багаж в машине' (Багаж + машине в + есть)",
                "prompt": "Багаж в машине",
                "wordChips": ["Luggage", "gāṛī", "mẽ", "hai"],
                "correctAnswer": ["Luggage", "gāṛī", "mẽ", "hai"],
                "phoneticCyrillicTarget": "Лаггидж гаар͟ии мэⁿ хэ",
                "explanationRu": "Послелог mẽ ставится строго после слова gāṛī: gāṛī mẽ."
            },
            {
                "id": "d10_ex02",
                "type": "substitution_drill",
                "instructionRu": "Скажите, что паспорт лежит на столе",
                "prompt": "Passport mēz _____ hai.",
                "options": ["par", "mẽ", "sē"],
                "correctAnswer": "par",
                "transliterationIsoTarget": "Passport mēz par hai",
                "explanationRu": "Для нахождения на поверхности используется послелог par (на столе = mēz par)."
            },
            {
                "id": "d10_ex03",
                "type": "fill_in_blank",
                "instructionRu": "Спросите: 'Водитель в машине?'",
                "prompt": "Kyā driver gāṛī _____ hai?",
                "options": ["mẽ", "par", "sē"],
                "correctAnswer": "mẽ",
                "transliterationIsoTarget": "Kyā driver gāṛī mẽ hai?",
                "explanationRu": "Внутри машины — gāṛī mẽ."
            },
            {
                "id": "d10_ex04",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вам звонят и спрашивают, где вы. Ответьте за 3 секунды: 'Я в гостинице!'",
                "prompt": "Āp kahā̃ haiñ?",
                "options": [
                    "Main hotel mẽ hū̃!",
                    "Main station par hū̃!",
                    "Yeh hotel hai!"
                ],
                "correctAnswer": "Main hotel mẽ hū̃!",
                "phoneticCyrillicTarget": "Мэⁿ хотел мэⁿ хууⁿ!",
                "explanationRu": "Main (Я) + hotel mẽ (в отеле) + hū̃ (есмь)."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Поиск забытого телефона в машине",
            "setting": "У входа в отель сразу после высадки из такси",
            "partnerRoleRu": "Водитель такси",
            "learnerRoleRu": "Пассажирка",
            "turns": [
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Брат, подождите пожалуйста! Мой телефон в машине.",
                    "speechIso": "Bhaiyā, rukiye! Mērā phone gāṛī mẽ hai.",
                    "speechCyrillic": "Бхаййаа, рукие! Мераа фон гаар͟ии мэⁿ хэ.",
                    "learnerHintRu": "Скажите водителю притормозить и укажите на телефон в машине"
                },
                {
                    "speaker": "Водитель",
                    "speechRu": "Телефон в машине? Где он лежит?",
                    "speechIso": "Phone gāṛī mẽ hai? Kahā̃ hai?",
                    "speechCyrillic": "Фон гаар͟ии мэⁿ хэ? Кахааⁿ хэ?",
                    "learnerHintRu": "Скажите: На сиденье! (Seat par hai)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Он на сиденье.",
                    "speechIso": "Seat par hai.",
                    "speechCyrillic": "Сиит пар хэ.",
                    "acceptableResponsesIso": ["Seat par hai", "Vahā̃ seat par hai"]
                },
                {
                    "speaker": "Водитель",
                    "speechRu": "Да, вот он! Пожалуйста, возьмите.",
                    "speechIso": "Hā̃-jī, mil gayā! Lījiye.",
                    "speechCyrillic": "Хааⁿ-джии, мил гайаа! Лиджие.",
                    "learnerHintRu": "Поблагодарите от души: Bahut shukriyā jī!"
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Локативы в индийской повседневности",
            "pointsRu": [
                "Слово 'Gāṛī' в Индии обозначает любое колесное транспортное средство: автомобиль, такси, поезд и даже тележку.",
                "Когда вы говорите 'Main station par hū̃', это сразу локализует вас у здания вокзала.",
                "Послелоги mẽ и par всегда произносятся слитно со словом, к которому относятся."
            ]
        }
    },

    # Day 11
    {
        "day": 11,
        "phase": 2,
        "title": {
            "en": "The Multi-Functional Postposition Sē (Ablative and Instrumental)",
            "ru": "Многофункциональный послелог Sē: инструмент (чем?) и источник (откуда?)"
        },
        "theme": "На поезде (train sē), на метро (metro sē), отсюда (yahā̃ sē), далеко (dūr)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция твердого зубного s и долгого ū в dūr)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Sē объединяет русский творительный падеж без предлога и предлоги из/от)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Отработка: поездом, на метро, на такси, отсюда до вокзала)",
            "phase4SimulationMinutes": "17:00–20:00 (Вопрос о выборе транспорта у прохожего)"
        },
        "learningObjectives": {
            "en": [
                "Master postposition sē for transport instruments (train sē, auto sē)",
                "Express source and distance using sē (yahā̃ sē kitnī dūr hai?)",
                "Merge Russian Instrumental and Ablative cases into single particle sē"
            ],
            "ru": [
                "Использовать послелог sē для обозначения транспорта (train sē = поездом, metro sē = на метро)",
                "Выражать отправную точку и дистанцию (yahā̃ sē = отсюда, kitnī dūr hai = как далеко?)",
                "Объединить русские функции творительного (кем/чем) и родительного (откуда) падежей в одном слове sē"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Долгий огубленный гласный /ū/ в слове dūr (दूर)",
            "articulatoryMechanism": "Губы сильно округляются и вытягиваются вперед. Звук чистый, монофтонгический, без дифтонгизации.",
            "russianInterferenceWarning": "Не редуцируйте гласный! Звук [дуур] должен быть протяжным.",
            "drills": [
                {
                    "prompt": "Отработка вопроса о расстоянии",
                    "contrastPair": "dūr (далеко) vs pās (близко)",
                    "instructionsRu": "Yahā̃ sē dūr hai? (Отсюда далеко?)"
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Многофункциональность послелога Sē (Творительный + Отложительный)",
            "russianParallel": "В русском языке мы говорим: 'Ехать поездом' (Творительный падеж без предлога) и 'Выехать из Москвы' (Предлог ИЗ + Родительный падеж). В хинди ОБЕ эти функции выполняет ОДНО слово — Sē: Train sē = поездом; Yahā̃ sē = отсюда.",
            "syntacticFormula": "[Транспорт / Место] + sē + [Глагол движения / dūr hai]",
            "explanationRu": "Послелог Sē также используется для выражения сравнения (быстрее ЧЕМ) и начала времени (С понедельника). Это самый продуктивный послелог в языке!",
            "pieCognateConnection": {
                "root": "*sokʷ- / *se-",
                "russian": "с / со",
                "hindi": "sē",
                "meaning": "Индоевропейский предлог совместности и исхода"
            }
        },
        "vocabulary": [
            {
                "id": "d11_v01",
                "devanagari": "दूर",
                "transliterationIso": "Dūr",
                "phoneticCyrillic": "Дуур",
                "translationRu": "Далеко",
                "translationEn": "Far",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Долгое 'уу', раскатистый 'р'."
            },
            {
                "id": "d11_v02",
                "devanagari": "पास",
                "transliterationIso": "Pās",
                "phoneticCyrillic": "Паас",
                "translationRu": "Близко / Рядом",
                "translationEn": "Near / Close",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Долгое 'аа', зубное глухое 'с'."
            },
            {
                "id": "d11_v03",
                "devanagari": "मेट्रो",
                "transliterationIso": "Metro",
                "phoneticCyrillic": "Мэтро",
                "translationRu": "Метро",
                "translationEn": "Metro",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Зубное 'т'."
            },
            {
                "id": "d11_v04",
                "devanagari": "ऑटो",
                "transliterationIso": "Auto",
                "phoneticCyrillic": "Оото",
                "translationRu": "Авторикша / Моторикша",
                "translationEn": "Auto-rickshaw",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Ретрофлексный 'т'."
            },
            {
                "id": "d11_v05",
                "devanagari": "कितनी",
                "transliterationIso": "Kitnī",
                "phoneticCyrillic": "Китнии",
                "translationRu": "Сколько? / Как? (женский род / для дистанции dūrī)",
                "translationEn": "How much (feminine)",
                "partOfSpeech": "adjective",
                "gender": "f",
                "audioHint": "Окончание -ī согласуется с dūr (дистанция)."
            }
        ],
        "exercises": [
            {
                "id": "d11_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите вопрос 'Как далеко это отсюда?' (Отсюда + как далеко + есть?)",
                "prompt": "Как далеко отсюда?",
                "wordChips": ["Yahā̃", "sē", "kitnī", "dūr", "hai"],
                "correctAnswer": ["Yahā̃", "sē", "kitnī", "dūr", "hai"],
                "phoneticCyrillicTarget": "Йахааⁿ сэ китнии дуур хэ",
                "explanationRu": "Yahā̃ sē (отсюда) + kitnī dūr (как далеко) + hai (есть)?"
            },
            {
                "id": "d11_ex02",
                "type": "substitution_drill",
                "instructionRu": "Посоветуйте поехать на метро (На метро + поезжайте)",
                "prompt": "Metro _____ jāiye!",
                "options": ["sē", "mẽ", "par"],
                "correctAnswer": "sē",
                "transliterationIsoTarget": "Metro sē jāiye!",
                "explanationRu": "Транспорт как средство передвижения оформляется послелогом sē (metro sē = на метро)."
            },
            {
                "id": "d11_ex03",
                "type": "fill_in_blank",
                "instructionRu": "Ответьте, что объект находится рядом, а не далеко",
                "prompt": "Dūr nahī̃ hai, _____ hai. (Не далеко, рядом)",
                "options": ["pās", "sē", "par"],
                "correctAnswer": "pās",
                "transliterationIsoTarget": "Dūr nahī̃ hai, pās hai.",
                "explanationRu": "Pās = близко / рядом."
            },
            {
                "id": "d11_ex04",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вам предлагают поехать на авторикше: 'Auto sē jāiye'. Согласитесь за 2 секунды.",
                "prompt": "Собеседник: Auto sē jāiye!",
                "options": [
                    "Hā̃-jī, ṭhīk hai! Auto sē jāūṅgī.",
                    "Nahī̃, main Russia sē hū̃!",
                    "Yeh station hai!"
                ],
                "correctAnswer": "Hā̃-jī, ṭhīk hai! Auto sē jāūṅgī.",
                "phoneticCyrillicTarget": "Хааⁿ-джии, т͟хиик хэ! Оото сэ джаауунгii.",
                "explanationRu": "Да, хорошо! Поеду на авторикше."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Расспрос консьержа о дороге в центр города",
            "setting": "Ресепшн отеля в Дели",
            "partnerRoleRu": "Консьерж отеля",
            "learnerRoleRu": "Туристка",
            "turns": [
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте! Скажите пожалуйста, рынок Connaught Place отсюда далеко?",
                    "speechIso": "Namastē jī! Connaught Place yahā̃ sē kitnī dūr hai?",
                    "speechCyrillic": "Намастэ джии! Коннот Плейс йахааⁿ сэ китнии дуур хэ?",
                    "learnerHintRu": "Задайте вопрос с конструкцией Yahā̃ sē kitnī dūr hai?"
                },
                {
                    "speaker": "Консьерж",
                    "speechRu": "Нет, сестра, не далеко. Близко!",
                    "speechIso": "Nahī̃ jī, dūr nahī̃ hai. Pās hai.",
                    "speechCyrillic": "Нахииⁿ джии, дуур нахииⁿ хэ. Паас хэ.",
                    "learnerHintRu": "Спросите: Поехать на метро или на авторикше? (Metro sē ya auto sē?)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "На метро поехать или на авторикше?",
                    "speechIso": "Metro sē ya auto sē?",
                    "speechCyrillic": "Мэтро сэ йа оото сэ?",
                    "acceptableResponsesIso": ["Metro sē jāiye ya auto sē?"]
                },
                {
                    "speaker": "Консьерж",
                    "speechRu": "Поезжайте на метро, так быстрее и удобнее.",
                    "speechIso": "Metro sē jāiye, bahut acchā hai.",
                    "speechCyrillic": "Мэтро сэ джааие, бахут аччхаа хэ.",
                    "learnerHintRu": "Поблагодарите: Dhanyavād jī!"
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Логистика метро в индийских мегаполисах",
            "pointsRu": [
                "Метро Дели — одно из самых чистых, современных и безопасных в мире.",
                "В каждом поезде метро первый вагон зарезервирован строго для женщин (Women Only).",
                "Конструкция 'Metro sē jāiye' всегда рекомендуется местными жителями в часы пик."
            ]
        }
    },

    # Day 12
    {
        "day": 12,
        "phase": 2,
        "title": {
            "en": "Inquiring About Urban Infrastructure and Facilities",
            "ru": "Городская инфраструктура: поиск туалетов, касс и банкоматов"
        },
        "theme": "Где туалет? Где банкомат (ATM)? Где аптека? Pās mẽ (поблизости)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция каверзных заимствованных слов: toilet, pharmacy, counter)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Связка: Объект + kahā̃ hai? и наличие рядом: Kyā pās mẽ ... hai?)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Срочные запросы объектов первой необходимости)",
            "phase4SimulationMinutes": "17:00–20:00 (Поиск туалета и обменника на вокзале)"
        },
        "learningObjectives": {
            "en": [
                "Inquire about critical amenities (toilet/washroom, ATM, pharmacy)",
                "Use the spatial frame 'pās mẽ' (nearby / in the vicinity)",
                "Formulate urgent infrastructural requests courteously"
            ],
            "ru": [
                "Спрашивать о жизненно важных объектах (туалет, банкомат, аптека, касса)",
                "Использовать конструкцию 'pās mẽ' (поблизости / неподалеку)",
                "Формулировать срочные просьбы вежливо и быстро"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Зубной звук /t/ в заимствованиях и открытый гласный /ā/ в pās",
            "articulatoryMechanism": "Слово 'pās' произносится с широким долгим 'аа'. В слове 'kahā̃' держите носовой резонанс.",
            "russianInterferenceWarning": "Не забывайте конечное связочное слово 'hai'. Без него вопрос звучит оборванно.",
            "drills": [
                {
                    "prompt": "Связка вопроса о местонахождении",
                    "contrastPair": "Toilet kahā̃ hai? (Где туалет?)",
                    "instructionsRu": "Произнесите слитно с вопросительной интонацией на слове 'kahā̃'."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Конструкция локализации с 'pās mẽ' (Вблизи)",
            "russianParallel": "Прямое соответствие русскому выражению: 'Есть ли поблизости отель / аптека?'. В хинди: Kyā (Ли) + pās mẽ (вблизи) + pharmacy (аптека) + hai (есть)?",
            "syntacticFormula": "Kyā + pās mẽ + [Объект] + hai?",
            "explanationRu": "Для точного поиска объекта в шаговой доступности используется слово pās (близко) с послелогом mẽ = pās mẽ (рядом, поблизости).",
            "pieCognateConnection": {
                "root": "*bʰā-",
                "russian": "баять / речь",
                "hindi": "pās (близость / присутствие)",
                "meaning": "Пространственная локализация"
            }
        },
        "vocabulary": [
            {
                "id": "d12_v01",
                "devanagari": "शौचालय",
                "transliterationIso": "Shaucālay / Toilet",
                "phoneticCyrillic": "Шаучалай / Тойлет",
                "translationRu": "Туалет / Уборная",
                "translationEn": "Toilet / Restroom",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "В живой речи в 99% случаев используется английское слово Toilet или Washroom."
            },
            {
                "id": "d12_v02",
                "devanagari": "दवा की दुकान",
                "transliterationIso": "Davā kī dukān / Pharmacy",
                "phoneticCyrillic": "Даваа кии дукаан / Фармаси",
                "translationRu": "Аптека (букв. магазин лекарств)",
                "translationEn": "Pharmacy / Medical store",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Davā (лекарство) + kī dukān (магазин)."
            },
            {
                "id": "d12_v03",
                "devanagari": "एटीएम",
                "transliterationIso": "ATM",
                "phoneticCyrillic": "Эй-Тии-Эм",
                "translationRu": "Банкомат",
                "translationEn": "ATM",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Произносится как по-английски."
            },
            {
                "id": "d12_v04",
                "devanagari": "टिकट काउंटर",
                "transliterationIso": "Ticket counter",
                "phoneticCyrillic": "Тикат каунтер",
                "translationRu": "Билетная касса",
                "translationEn": "Ticket counter",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Универсальный индийский термин."
            },
            {
                "id": "d12_v05",
                "devanagari": "पास में",
                "transliterationIso": "Pās mẽ",
                "phoneticCyrillic": "Паас мэⁿ",
                "translationRu": "Поблизости / Рядом",
                "translationEn": "Nearby / In the vicinity",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Носовое 'мэⁿ'."
            }
        ],
        "exercises": [
            {
                "id": "d12_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите вопрос: 'Где туалет?' (Туалет + где + есть?)",
                "prompt": "Где туалет?",
                "wordChips": ["Washroom", "kahā̃", "hai"],
                "correctAnswer": ["Washroom", "kahā̃", "hai"],
                "phoneticCyrillicTarget": "Вашруум кахааⁿ хэ",
                "explanationRu": "Washroom / Toilet + kahā̃ + hai?"
            },
            {
                "id": "d12_ex02",
                "type": "fill_in_blank",
                "instructionRu": "Спросите: 'Есть ли поблизости банкомат?'",
                "prompt": "Kyā _____ ATM hai?",
                "options": ["pās mẽ", "vahā̃ sē", "gāṛī mẽ"],
                "correctAnswer": "pās mẽ",
                "transliterationIsoTarget": "Kyā pās mẽ ATM hai?",
                "explanationRu": "Pās mẽ = поблизости."
            },
            {
                "id": "d12_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вам срочно нужна аптека. Спросите прохожего за 3 секунды.",
                "prompt": "Срочный поиск аптеки",
                "options": [
                    "Māf kījiye, pharmacy kahā̃ hai?",
                    "Main pharmacy hū̃!",
                    "Pharmacy bahut acchā hai!"
                ],
                "correctAnswer": "Māf kījiye, pharmacy kahā̃ hai?",
                "phoneticCyrillicTarget": "Мааф кииджие, фармаси кахааⁿ хэ?",
                "explanationRu": "Вежливое обращение + объект + kahā̃ hai?"
            },
            {
                "id": "d12_ex04",
                "type": "substitution_drill",
                "instructionRu": "Уточните, где билетная касса",
                "prompt": "Ticket counter _____ hai?",
                "options": ["kahā̃", "kaun", "kyū̃"],
                "correctAnswer": "kahā̃",
                "transliterationIsoTarget": "Ticket counter kahā̃ hai?",
                "explanationRu": "Kahā̃ = где."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Поиск банкомата и туалета на вокзале",
            "setting": "Главный вестибюль вокзала",
            "partnerRoleRu": "Сотрудник вокзала в форме",
            "learnerRoleRu": "Пассажирка с рюкзаком",
            "turns": [
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Извините, пожалуйста! Где здесь туалет?",
                    "speechIso": "Māf kījiye jī! Toilet kahā̃ hai?",
                    "speechCyrillic": "Мааф кииджие джии! Тойлет кахааⁿ хэ?",
                    "learnerHintRu": "Задайте вежливый вопрос о туалете"
                },
                {
                    "speaker": "Сотрудник",
                    "speechRu": "Туалет вон там, прямо и направо.",
                    "speechIso": "Toilet vahā̃ hai, sīdhē aur dāē̃.",
                    "speechCyrillic": "Тойлет вахааⁿ хэ, сиидхэ аур дааеⁿ.",
                    "learnerHintRu": "Спросите: А банкомат поблизости есть? (Kyā pās mẽ ATM hai?)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "А поблизости есть банкомат?",
                    "speechIso": "Aur kyā pās mẽ ATM hai?",
                    "speechCyrillic": "Аур кйаа паас мэⁿ Эй-Тии-Эм хэ?",
                    "acceptableResponsesIso": ["Kyā pās mẽ ATM hai?"]
                },
                {
                    "speaker": "Сотрудник",
                    "speechRu": "Да, банкомат прямо возле выхода номер 1.",
                    "speechIso": "Hā̃, gate number 1 kē pās ATM hai.",
                    "speechCyrillic": "Хааⁿ, гейт намбар 1 ке паас Эй-Тии-Эм хэ.",
                    "learnerHintRu": "Поблагодарите: Bahut dhanyavād jī!"
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Слова 'Washroom' и 'Medical store' в Индии",
            "pointsRu": [
                "Слово 'Washroom' считается в индийском английском более деликатным и вежливым, чем 'Toilet'.",
                "Аптеки в Индии почти всегда называются вывеской 'Chemist' или 'Medical Store'.",
                "Банкоматы (ATM) часто имеют отдельного охранника у двери — не пугайтесь, он просто помогает с очередью."
            ]
        }
    },

    # Day 13
    {
        "day": 13,
        "phase": 2,
        "title": {
            "en": "Formal Imperatives and Social Directives (-iye)",
            "ru": "Вежливые императивы и директивы: суффикс -iye (аналог русского -ите)"
        },
        "theme": "Пройдите (āiye), садитесь (baithiye), возьмите (lījiye), дайте (dījiye), посмотрите (dēkhiye)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция суффикса вежливости -iye: слитное произношение)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Глагольные основы: dē- / lē- / ā- / jā- и их вежливые формы dījiye / lījiye)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Подстановка: дайте воду, возьмите деньги, посмотрите сюда)",
            "phase4SimulationMinutes": "17:00–20:00 (Взаимодействие с персоналом отеля и водителем)"
        },
        "learningObjectives": {
            "en": [
                "Master high-frequency polite imperatives with suffix -iye",
                "Form irregular honorific commands: Dījiye (give), Lījiye (take), Kījiye (do)",
                "Map Hindi -iye directly to Russian formal imperative suffix -ите"
            ],
            "ru": [
                "Освоить главные вежливые глагольные директивы с суффиксом -iye",
                "Запомнить формы: Dījiye (дайте), Lījiye (возьмите), Āiye (пройдите), Dēkhiye (посмотрите)",
                "Опираться на 100% совпадение с русским суффиксом вежливости -ите (да-йте, возьм-ите, посмотр-ите)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Гласный /ī/ и безударный полугласный переход в суффиксе /-iye/",
            "articulatoryMechanism": "Долгий [ии] мягко переходит в краткое [е]: [дииджие], [лиджие]. Без резких пауз.",
            "russianInterferenceWarning": "Не проглатывайте окончание! Четко произносите форму вежливости.",
            "drills": [
                {
                    "prompt": "Пара 'дайте — возьмите'",
                    "contrastPair": "Dījiye (дайте) vs Lījiye (возьмите)",
                    "instructionsRu": "Произносите в быстром темпе: Dījiye — Lījiye."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Вежливый императив на -iye (Соответствие русскому -ите)",
            "russianParallel": "Грамматическое совпадение абсолютно: в русском языке к основе прибавляется -ите (Пройд-ите, Сад-итесь, Посмотр-ите). В хинди прибавляется -iye: Ā-iye, Baith-iye, Dēkh-iye. Глаголы 'давать' (dēnā) и 'брать' (lēnā) имеют формы Dījiye (дайте) и Lījiye (возьмите).",
            "syntacticFormula": "[Объект] + [Dījiye / Lījiye / Dēkhiye]",
            "explanationRu": "Использование формы на -iye защищает иностранца от любого подозрения в грубости. В путешествии вы будете применять эти 5 глаголов сотни раз в день.",
            "pieCognateConnection": {
                "root": "*deh₃-",
                "russian": "дать / даю / дай",
                "hindi": "dēnā (dījiye)",
                "meaning": "Праиндоевропейский корень дарения"
            }
        },
        "vocabulary": [
            {
                "id": "d13_v01",
                "devanagari": "दीजिए",
                "transliterationIso": "Dījiye",
                "phoneticCyrillic": "Дииджие",
                "translationRu": "Дайте, пожалуйста",
                "translationEn": "Please give",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Долгое 'ии' + мягкое джи-е."
            },
            {
                "id": "d13_v02",
                "devanagari": "लीजिए",
                "transliterationIso": "Lījiye",
                "phoneticCyrillic": "Лииджие",
                "translationRu": "Возьмите, пожалуйста",
                "translationEn": "Please take",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Долгое 'ии'."
            },
            {
                "id": "d13_v03",
                "devanagari": "आइए",
                "transliterationIso": "Āiye",
                "phoneticCyrillic": "Ааие",
                "translationRu": "Входите / Проходите, пожалуйста",
                "translationEn": "Please come in",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Широкое 'аа' в начале."
            },
            {
                "id": "d13_v04",
                "devanagari": "देखिए",
                "transliterationIso": "Dēkhiye",
                "phoneticCyrillic": "Дэкхие",
                "translationRu": "Посмотрите, пожалуйста",
                "translationEn": "Please look / see",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Придыхательное велярное [кх]."
            },
            {
                "id": "d13_v05",
                "devanagari": "पानी",
                "transliterationIso": "Pānī",
                "phoneticCyrillic": "Паании",
                "translationRu": "Вода",
                "translationEn": "Water",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Два долгих гласных [паа-нии]."
            }
        ],
        "exercises": [
            {
                "id": "d13_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите вежливую просьбу: 'Дайте воду, пожалуйста' (Воду + дайте)",
                "prompt": "Дайте воду, пожалуйста",
                "wordChips": ["Pānī", "dījiye"],
                "correctAnswer": ["Pānī", "dījiye"],
                "phoneticCyrillicTarget": "Паании дииджие",
                "explanationRu": "Объект стоит перед глаголом: Pānī dījiye."
            },
            {
                "id": "d13_ex02",
                "type": "substitution_drill",
                "instructionRu": "Передайте деньги и скажите: 'Возьмите, пожалуйста'",
                "prompt": "Paisē (деньги) _____! (Возьмите)",
                "options": ["lījiye", "dījiye", "āiye"],
                "correctAnswer": "lījiye",
                "transliterationIsoTarget": "Paisē lījiye!",
                "explanationRu": "Lījiye означает 'возьмите'."
            },
            {
                "id": "d13_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Обратите внимание собеседника на расписание: 'Посмотрите сюда!'",
                "prompt": "Посмотрите сюда!",
                "options": [
                    "Yahā̃ dēkhiye!",
                    "Vahā̃ jāiye!",
                    "Yahā̃ rukiye!"
                ],
                "correctAnswer": "Yahā̃ dēkhiye!",
                "phoneticCyrillicTarget": "Йахааⁿ дэкхие!",
                "explanationRu": "Yahā̃ (сюда) + dēkhiye (посмотрите)."
            },
            {
                "id": "d13_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Пригласите гостя войти: 'Проходите, пожалуйста!'",
                "prompt": "Andar (внутрь) _____!",
                "options": ["āiye", "dījiye", "lījiye"],
                "correctAnswer": "āiye",
                "transliterationIsoTarget": "Andar āiye!",
                "explanationRu": "Āiye означает 'проходите / входите'."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Заказ воды и расчет в придорожном кафе",
            "setting": "Чайная (Chai shop) у дороги",
            "partnerRoleRu": "Хозяин чайной",
            "learnerRoleRu": "Путешественница",
            "turns": [
                {
                    "speaker": "Хозяин",
                    "speechRu": "Добро пожаловать, сестра! Проходите, присаживайтесь.",
                    "speechIso": "Namastē madam! Āiye, yahā̃ baithiye.",
                    "speechCyrillic": "Намастэ мадам! Ааие, йахааⁿ бэтхие.",
                    "learnerHintRu": "Попросите воду: Pānī dījiye, пожалуйста"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте! Дайте бутылку воды, пожалуйста.",
                    "speechIso": "Namastē jī! Ek bottle pānī dījiye.",
                    "speechCyrillic": "Намастэ джии! Эк ботл паании дииджие.",
                    "acceptableResponsesIso": ["Pānī dījiye", "Ek bottle pānī dījiye"]
                },
                {
                    "speaker": "Хозяин",
                    "speechRu": "Вот, пожалуйста, холодная вода. Двадцать рупий.",
                    "speechIso": "Lījiye, ṭhaṇḍā pānī. Bīs rupayē.",
                    "speechCyrillic": "Лииджие, тхандаа паании. Биис рупае.",
                    "learnerHintRu": "Протяните деньги со словами: Возьмите деньги, спасибо! (Paisē lījiye, shukriyā!)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Возьмите, пожалуйста. Большое спасибо!",
                    "speechIso": "Paisē lījiye. Bahut shukriyā!",
                    "speechCyrillic": "Пэсе лииджие. Бахут шукрийа!",
                    "acceptableResponsesIso": ["Lījiye, shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Правило правой руки при передаче предметов",
            "pointsRu": [
                "В Индии передавать предметы, деньги и еду со словами 'Lījiye' (Возьмите) или 'Dījiye' принято СТРОГО правой рукой.",
                "Левая рука традиционно считается 'нечистой' (санитарно-бытовой).",
                "Если нужно подать что-то двумя руками в знак особого почтения, левая рука поддерживает правое запястье."
            ]
        }
    },

    # Day 14
    {
        "day": 14,
        "phase": 2,
        "title": {
            "en": "Transit Negotiations: Auto-Rickshaws and Cabs",
            "ru": "Переговоры с транспортом: авторикши, такси и счетчик"
        },
        "theme": "Брат (Bhaiyā), мне нужно ехать в... (jānā hai), включите счетчик (mīṭar chalāo)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция придыхательного bh в Bhaiyā и ретрофлексного ṭ в mīṭar)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Конструкция необходимости: Инфинитив + hai: Jānā hai = нужно ехать)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Диалог посадки: пункт назначения, включение счетчика, поехали)",
            "phase4SimulationMinutes": "17:00–20:00 (Жесткие, но вежливые переговоры с рикшей у вокзала)"
        },
        "learningObjectives": {
            "en": [
                "Hail transport using polite kinship term Bhaiyā",
                "State destination with infinitive of obligation (Airport jānā hai)",
                "Insist on metered fare using 'Mīṭar chalāo / Mīṭar sē chaliye'"
            ],
            "ru": [
                "Окликать водителей вежливым народным термином Bhaiyā (брат / молодой человек)",
                "Называть пункт назначения с помощью инфинитива необходимости: [Место] + jānā hai (нужно ехать в...)",
                "Настаивать на поездке по счетчику: 'Mīṭar chalāo' или 'Mīṭar sē chaliye'"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Звонкий придыхательный губной /bh/ (भ) в слове Bhaiyā (भैया)",
            "articulatoryMechanism": "Губы смыкаются для звука [б] и размыкаются с сильным голосовым выдохом [бх].",
            "russianInterferenceWarning": "Не превращайте в глухой звук [пх] или английский [v]. Это плотный русский [б] с дыханием.",
            "drills": [
                {
                    "prompt": "Отработка обращения к водителю",
                    "contrastPair": "bāī (ошибка) vs bhaiyā (верно: придыхание [бхаййаа])",
                    "instructionsRu": "Произнесите уверенно и приветливо: 'Bhaiyā!'."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Инфинитив с hai как выражение необходимости",
            "russianParallel": "В русском языке мы говорим инфинитивом: 'Мне нужно ехать' или безлично 'Ехать на вокзал'. В хинди используется инфинитив jānā (ехать) + связка hai: 'Station jānā hai' (Нужно ехать на вокзал).",
            "syntacticFormula": "[Пункт назначения] + jānā hai",
            "explanationRu": "Конструкция с jānā hai избавляет от необходимости спрягать глагол по лицам. Вы просто называете место и говорите jānā hai!",
            "pieCognateConnection": {
                "root": "*bʰréh₂tēr",
                "russian": "брат",
                "hindi": "bhāī / bhaiyā",
                "meaning": "Праиндоевропейское братство и обращение"
            }
        },
        "vocabulary": [
            {
                "id": "d14_v01",
                "devanagari": "भैया",
                "transliterationIso": "Bhaiyā",
                "phoneticCyrillic": "Бхаййаа",
                "translationRu": "Брат / Молодой человек (уважительное обращение)",
                "translationEn": "Brother (polite address for drivers/vendors)",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Придыхательное 'бх', ударение на первый слог."
            },
            {
                "id": "d14_v02",
                "devanagari": "जाना है",
                "transliterationIso": "Jānā hai",
                "phoneticCyrillic": "Джаанаа хэ",
                "translationRu": "Нужно ехать / иду (букв. ехать есть)",
                "translationEn": "Need to go / Have to go",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Инфинитив jānā + связка hai."
            },
            {
                "id": "d14_v03",
                "devanagari": "मीटर",
                "transliterationIso": "Mīṭar",
                "phoneticCyrillic": "Миитар͟",
                "translationRu": "Счетчик (таксометр)",
                "translationEn": "Meter",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Ретрофлексный 'ṭ'."
            },
            {
                "id": "d14_v04",
                "devanagari": "चलाओ",
                "transliterationIso": "Chalāo",
                "phoneticCyrillic": "Чалаао",
                "translationRu": "Включи / Запусти / Веди машину",
                "translationEn": "Turn on / Drive",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Ударение на второй слог."
            },
            {
                "id": "d14_v05",
                "devanagari": "चलिए",
                "transliterationIso": "Chaliye",
                "phoneticCyrillic": "Чалие",
                "translationRu": "Поехали! / Пойдемте! (вежливо)",
                "translationEn": "Let's go (polite)",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Суффикс -iye."
            }
        ],
        "exercises": [
            {
                "id": "d14_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите фразу: 'Брат, нужно ехать в аэропорт'",
                "prompt": "Брат, в аэропорт нужно ехать",
                "wordChips": ["Bhaiyā,", "Airport", "jānā", "hai"],
                "correctAnswer": ["Bhaiyā,", "Airport", "jānā", "hai"],
                "phoneticCyrillicTarget": "Бхаййаа, эрпорт джаанаа хэ",
                "explanationRu": "Bhaiyā + Место + jānā hai."
            },
            {
                "id": "d14_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Водитель рикши хочет назвать завышенную цену без счетчика. Потребуйте включить счетчик за 2 секунды.",
                "prompt": "Водитель: 500 rupees, madam!",
                "options": [
                    "Nahī̃ bhaiyā, mīṭar chalāo!",
                    "Hā̃ bhaiyā, bahut acchā!",
                    "Mērā nām mīṭar hai!"
                ],
                "correctAnswer": "Nahī̃ bhaiyā, mīṭar chalāo!",
                "phoneticCyrillicTarget": "Нахииⁿ бхаййаа, миитар͟ чалаао!",
                "explanationRu": "Mīṭar chalāo (включи счетчик) пресекает накрутку цен."
            },
            {
                "id": "d14_ex03",
                "type": "substitution_drill",
                "instructionRu": "Скажите, что вам нужно ехать на вокзал",
                "prompt": "Station _____ hai.",
                "options": ["jānā", "khānā", "pīnā"],
                "correctAnswer": "jānā",
                "transliterationIsoTarget": "Station jānā hai.",
                "explanationRu": "Jānā hai = нужно ехать."
            },
            {
                "id": "d14_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Скомандуйте водителю отправляться: 'Поехали!'",
                "prompt": "Ṭhīk hai bhaiyā, _____! (Поехали)",
                "options": ["chaliye", "rukiye", "dēkhiye"],
                "correctAnswer": "chaliye",
                "transliterationIsoTarget": "Ṭhīk hai bhaiyā, chaliye!",
                "explanationRu": "Chaliye = поехали / пойдемте."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Найм авторикши у выхода с вокзала",
            "setting": "Стоянка рикш возле железнодорожного вокзала",
            "partnerRoleRu": "Водитель авторикши",
            "learnerRoleRu": "Путешественница",
            "turns": [
                {
                    "speaker": "Водитель",
                    "speechRu": "Такси, рикша! Куда вам нужно ехать?",
                    "speechIso": "Madam! Kahā̃ jānā hai?",
                    "speechCyrillic": "Мадам! Кахааⁿ джаанаа хэ?",
                    "learnerHintRu": "Скажите: Брат, нужно ехать в отель Taj (Bhaiyā, Taj Hotel jānā hai)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Брат, мне нужно в отель Тадж. Включите счетчик!",
                    "speechIso": "Bhaiyā, Taj Hotel jānā hai. Mīṭar chalāo.",
                    "speechCyrillic": "Бхаййаа, Тадж Хотел джаанаа хэ. Миитар͟ чалаао.",
                    "acceptableResponsesIso": ["Bhaiyā, Taj Hotel jānā hai.", "Mīṭar chalāo."]
                },
                {
                    "speaker": "Водитель",
                    "speechRu": "Ладно, мадам, садитесь! Поехали по счетчику.",
                    "speechIso": "Ṭhīk hai madam, baithiye! Mīṭar sē chalēṅgē.",
                    "speechCyrillic": "Т͟хиик хэ мадам, бэтхие! Миитар͟ сэ чалэнгээ.",
                    "learnerHintRu": "Скажите: Отлично, поехали! (Bahut acchā, chaliye!)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Очень хорошо, поехали!",
                    "speechIso": "Bahut acchā, chaliye!",
                    "speechCyrillic": "Бахут аччхаа, чалие!",
                    "acceptableResponsesIso": ["Chaliye!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Психология переговоров с водителями",
            "pointsRu": [
                "Обращение 'Bhaiyā' (брат) мгновенно переводит диалог из плоскости 'богатый иностранец — продавец' в плоскость человеческого уважения.",
                "Фраза на хинди 'Mīṭar chalāo' показывает, что вы ориентируетесь в местных порядках и обмануть вас не удастся.",
                "Уверенная интонация без суеты всегда экономит от 50% до 70% стоимости поездки."
            ]
        }
    },

    # Day 15
    {
        "day": 15,
        "phase": 2,
        "title": {
            "en": "Time Calculations and Transit Duration",
            "ru": "Расчет времени в пути: глагол Lagnā (требоваться)"
        },
        "theme": "Сколько времени потребуется? (Kitnā time lagēgā?), 10 минут (das minute), следующая остановка",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Фонетика будущего времени lagēgā / лагээгаа и числительного das)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Глагол lagnā как аналог русского 'уйдет / потребуется по времени')",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Шаблоны: 5 минут, 10 минут, полчаса, сколько времени)",
            "phase4SimulationMinutes": "17:00–20:00 (Уточнение времени до прибытия в пробке)"
        },
        "learningObjectives": {
            "en": [
                "Inquire about transit duration using 'Kitnā vaqt / time lagēgā?'",
                "Master idiomatic experiential verb lagnā for elapsed time",
                "Recognize time responses (Das minute, aglā stop)"
            ],
            "ru": [
                "Спрашивать о времени в пути: 'Kitnā time lagēgā?' / 'Kitnā vaqt lagēgā?'",
                "Усвоить глагол lagnā в значении затрат времени (русское 'уйдет 10 минут / потребуется')",
                "Понимать ориентиры по времени (Das minute = десять минут, aglā stop = следующая остановка)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Зубной звук /d/ в слове das (दस) и гласный /ē/ в lagēgā",
            "articulatoryMechanism": "Зубной [д] на резцах. В форме 'lagēgā' чистый звук [э] без русского призвука 'и' и долгое конечное [аа].",
            "russianInterferenceWarning": "Не редуцируйте безударные гласные в слове 'lagēgā' [ла-гээ-гаа].",
            "drills": [
                {
                    "prompt": "Отработка вопроса времени в пути",
                    "contrastPair": "Kitnā time lagēgā? (Сколько времени уйдет?)",
                    "instructionsRu": "Произнесите слитную фразу с легким ударением на 'time'."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Глагол Lagnā (Требоваться / Уходить по времени)",
            "russianParallel": "В русском языке мы спрашиваем: 'Сколько времени потребуется?' или 'Сколько времени уйдёт?'. В хинди для этого служит универсальный глагол lagnā в будущем времени — lagēgā (потребуется).",
            "syntacticFormula": "Kitnā [time / vaqt] + lagēgā?",
            "explanationRu": "Ответ строится точно так же: [Количество минут] + lagēgā (Das minute lagēgā = Уйдет десять минут). Слово 'time' повсеместно используется наравне с хинди-словом 'vaqt'.",
            "pieCognateConnection": {
                "root": "*déḱm̥t",
                "russian": "десять",
                "hindi": "das",
                "meaning": "Праиндоевропейское числительное 10"
            }
        },
        "vocabulary": [
            {
                "id": "d15_v01",
                "devanagari": "कितना",
                "transliterationIso": "Kitnā",
                "phoneticCyrillic": "Китнаа",
                "translationRu": "Сколько? (мужской род)",
                "translationEn": "How much",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Долгое 'аа' на конце."
            },
            {
                "id": "d15_v02",
                "devanagari": "वक़्त",
                "transliterationIso": "Vaqt / Time",
                "phoneticCyrillic": "Вакт / Тайм",
                "translationRu": "Время",
                "translationEn": "Time",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Твердое 'к-т'."
            },
            {
                "id": "d15_v03",
                "devanagari": "लगेगा",
                "transliterationIso": "Lagēgā",
                "phoneticCyrillic": "Лагээгаа",
                "translationRu": "Потребуется / Уйдет (по времени)",
                "translationEn": "Will take (time)",
                "partOfSpeech": "verb",
                "gender": "m",
                "audioHint": "Чистый гласный 'е', долгое 'аа'."
            },
            {
                "id": "d15_v04",
                "devanagari": "दस",
                "transliterationIso": "Das",
                "phoneticCyrillic": "Дас",
                "translationRu": "Десять (10)",
                "translationEn": "Ten (10)",
                "partOfSpeech": "numeral",
                "gender": "n/a",
                "audioHint": "Когнат с русским словом 'десять'."
            },
            {
                "id": "d15_v05",
                "devanagari": "अगला",
                "transliterationIso": "Aglā",
                "phoneticCyrillic": "Аглаа",
                "translationRu": "Следующий",
                "translationEn": "Next",
                "partOfSpeech": "adjective",
                "gender": "m",
                "audioHint": "Ударение на долгое 'аа'."
            }
        ],
        "exercises": [
            {
                "id": "d15_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите вопрос: 'Сколько времени потребуется?'",
                "prompt": "Сколько времени займет дорога?",
                "wordChips": ["Kitnā", "time", "lagēgā?"],
                "correctAnswer": ["Kitnā", "time", "lagēgā?"],
                "phoneticCyrillicTarget": "Китнаа тайм лагээгаа?",
                "explanationRu": "Kitnā time lagēgā? — стандартный вопрос о времени в пути."
            },
            {
                "id": "d15_ex02",
                "type": "fill_in_blank",
                "instructionRu": "Ответьте: 'Потребуется 10 минут'",
                "prompt": "Das minute _____.",
                "options": ["lagēgā", "hai", "jānā"],
                "correctAnswer": "lagēgā",
                "transliterationIsoTarget": "Das minute lagēgā.",
                "explanationRu": "Das minute lagēgā = Уйдет десять минут."
            },
            {
                "id": "d15_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вы стоите в пробке. Спросите водителя за 2 секунды, сколько времени потребуется.",
                "prompt": "Машина застряла в заторе",
                "options": [
                    "Bhaiyā, kitnā time lagēgā?",
                    "Bhaiyā, mīṭar chalāo!",
                    "Station kahā̃ hai?"
                ],
                "correctAnswer": "Bhaiyā, kitnā time lagēgā?",
                "phoneticCyrillicTarget": "Бхаййаа, китнаа тайм лагээгаа?",
                "explanationRu": "Вежливое обращение Bhaiyā + вопрос о времени."
            },
            {
                "id": "d15_ex04",
                "type": "substitution_drill",
                "instructionRu": "Уточните: 'Следующая остановка — аэропорт?'",
                "prompt": "_____ stop airport hai?",
                "options": ["Aglā", "Kitnā", "Das"],
                "correctAnswer": "Aglā",
                "transliterationIsoTarget": "Aglā stop airport hai?",
                "explanationRu": "Aglā = следующий."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Контроль времени в пробке по пути в аэропорт",
            "setting": "Такси, остановившееся в плотном трафике Дели",
            "partnerRoleRu": "Водитель такси",
            "learnerRoleRu": "Беспокоящаяся пассажирка",
            "turns": [
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Брат, здесь сильная пробка. Сколько времени потребуется до аэропорта?",
                    "speechIso": "Bhaiyā, traffic hai. Airport kitnā time lagēgā?",
                    "speechCyrillic": "Бхаййаа, трафик хэ. Эрпорт китнаа тайм лагээгаа?",
                    "learnerHintRu": "Задайте вопрос: Airport kitnā time lagēgā?"
                },
                {
                    "speaker": "Водитель",
                    "speechRu": "Не волнуйтесь, мадам. Всего десять-пятнадцать минут потребуется.",
                    "speechIso": "Chintā mat kījiye madam. Das-pandrah minute lagēgā.",
                    "speechCyrillic": "Чинтаа мат кииджие мадам. Дас-панндрах минат лагээгаа.",
                    "learnerHintRu": "Уточните: Следующий съезд уже аэропорт? (Aglā stop airport hai?)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Следующая остановка аэропорт?",
                    "speechIso": "Aglā stop airport hai?",
                    "speechCyrillic": "Аглаа стоп эрпорт хэ?",
                    "acceptableResponsesIso": ["Aglā stop airport hai?"]
                },
                {
                    "speaker": "Водитель",
                    "speechRu": "Да, именно так! Скоро приедем.",
                    "speechIso": "Hā̃-jī, aglā stop airport hai.",
                    "speechCyrillic": "Хааⁿ-джии, аглаа стоп эрпорт хэ.",
                    "learnerHintRu": "Скажите с облегчением: Ṭhīk hai, shukriyā!"
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Индийское восприятие времени ('Indian Stretchable Time')",
            "pointsRu": [
                "В Индии фраза 'Das minute lagēgā' (займет 10 минут) часто означает от 15 до 25 минут из-за трафика.",
                "Вопрос 'Kitnā time lagēgā?' побуждает водителя выбрать объездной маршрут.",
                "Слово 'Chintā mat kījiye' (не волнуйтесь) — любимая фраза индийцев для успокоения путешественников."
            ]
        }
    },

    # Day 16
    {
        "day": 16,
        "phase": 2,
        "title": {
            "en": "Phase 2 Synthesis and Urban Navigation Simulation",
            "ru": "Синтез Фазы 2: сквозная транспортная симуляция от аэропорта до отеля"
        },
        "theme": "Полный маршрут: выбор рикши, торг за счетчик, ведение по поворотам, прибытие",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Комплексный фонетический тренинг: послелоги mẽ, par, sē, команды поворотов)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Сборка конструкций: Bhaiyā + jānā hai + mīṭar chalāo + bāē̃/dāē̃ + rukiye)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Сквозная ролевая тренировка с напористым водителем)",
            "phase4SimulationMinutes": "17:00–20:00 (Экзаменационная транспортная симуляция Фазы 2)"
        },
        "learningObjectives": {
            "en": [
                "Conduct end-to-end transit interaction entirely in Hindi without English",
                "Apply postpositions, imperatives, and directionals under conversational pressure",
                "Successfully direct a driver to a destination and halt smoothly"
            ],
            "ru": [
                "Провести полный цикл транспортных переговоров исключительно на хинди",
                "Безошибочно применять послелоги (sē, mẽ, par), вежливые императивы (-iye) и направления",
                "Успешно доехать до пункта назначения, корректируя водителя по ходу движения"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Ритмическая устойчивость при быстрой смене речевых формул",
            "articulatoryMechanism": "Синхронизация зубных смычек (dāē̃, sīdhē) с придыханиями (bhaiyā, dhīrē) в спонтанном потоке речи.",
            "russianInterferenceWarning": "Не сбивайтесь на русский порядок слов SVO при стрессе! Глаголы rukiye и jāiye всегда закрывают фразу.",
            "drills": [
                {
                    "prompt": "Связка транспортных команд на одном дыхании",
                    "contrastPair": "Bhaiyā, sīdhē jāiye -> bāē̃ jāiye -> yahā̃ rukiye!",
                    "instructionsRu": "Произнесите последовательность команд четко и уверенно."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Синтаксическая интеграция SOV в логистике",
            "russianParallel": "Вы окончательно преодолели интерференцию русского порядка слов. Теперь связки 'прямо езжайте' (sīdhē jāiye) и 'здесь остановитесь' (yahā̃ rukiye) формируются автоматически.",
            "syntacticFormula": "[Субъект/Обращение] + [Локатив / Направление] + [Терминальный глагол]",
            "explanationRu": "Фаза 2 вооружила вас полным суверенитетом в городском пространстве Индии: вы умеете находить любые объекты и руководить любым водителем.",
            "pieCognateConnection": {
                "root": "*dʰwer- / *wódr̥ / *sed-",
                "russian": "дверь / вода / сидеть",
                "hindi": "dvār / pānī / baithiye",
                "meaning": "Индоевропейская лексическая база"
            }
        },
        "vocabulary": [
            {
                "id": "d16_v01",
                "devanagari": "चालक / ड्राइवर",
                "transliterationIso": "Driver / Bhaiyā",
                "phoneticCyrillic": "Драйвер / Бхаййаа",
                "translationRu": "Водитель / Брат",
                "translationEn": "Driver",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Универсальное обращение."
            },
            {
                "id": "d16_v02",
                "devanagari": "रास्ता",
                "transliterationIso": "Rāstā",
                "phoneticCyrillic": "Раастаа",
                "translationRu": "Дорога / Путь",
                "translationEn": "Way / Road",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Два долгих гласных [раа-стаа]."
            },
            {
                "id": "d16_v03",
                "devanagari": "रुपये",
                "transliterationIso": "Rupayē",
                "phoneticCyrillic": "Рупае",
                "translationRu": "Рупии",
                "translationEn": "Rupees",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Индийская валюта."
            },
            {
                "id": "d16_v04",
                "devanagari": "यहाँ पर",
                "transliterationIso": "Yahā̃ par",
                "phoneticCyrillic": "Йахааⁿ пар",
                "translationRu": "Прямо здесь / Вот тут",
                "translationEn": "Right here",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Усилительный послелог par."
            }
        ],
        "exercises": [
            {
                "id": "d16_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите комплексное указание водителю: 'Брат, сначала поезжайте направо, затем налево'",
                "prompt": "Сначала направо, потом налево",
                "wordChips": ["Pahlē", "dāē̃", "jāiye,", "phir", "bāē̃", "jāiye"],
                "correctAnswer": ["Pahlē", "dāē̃", "jāiye,", "phir", "bāē̃", "jāiye"],
                "phoneticCyrillicTarget": "Пэхле дааеⁿ джааие, пхир бааеⁿ джааие",
                "explanationRu": "Последовательность команд с предлогами pahlē (сначала) и phir (затем)."
            },
            {
                "id": "d16_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Водитель пытается проехать нужные ворота. Скомандуйте немедленную остановку!",
                "prompt": "Водитель мчит мимо цели",
                "options": [
                    "Bhaiyā, yahā̃ par rukiye!",
                    "Bhaiyā, sīdhē jāiye!",
                    "Kitnā time lagēgā?"
                ],
                "correctAnswer": "Bhaiyā, yahā̃ par rukiye!",
                "phoneticCyrillicTarget": "Бхаййаа, йахааⁿ пар рукие!",
                "explanationRu": "Yahā̃ par rukiye! — Остановитесь прямо здесь!"
            },
            {
                "id": "d16_ex03",
                "type": "fill_in_blank",
                "instructionRu": "Спросите о стоимости по счетчику",
                "prompt": "Mīṭar _____ kitnā huā? (По счетчику сколько вышло?)",
                "options": ["sē", "mẽ", "par"],
                "correctAnswer": "sē",
                "transliterationIsoTarget": "Mīṭar sē kitnā huā?",
                "explanationRu": "Mīṭar sē = по счетчику (инструментальный sē)."
            },
            {
                "id": "d16_ex04",
                "type": "dialogue_roleplay",
                "instructionRu": "Завершите поездку и отдайте деньги",
                "prompt": "Водитель: Hum pahuñch gayē madam (Мы приехали, мадам)",
                "options": [
                    "Bahut shukriyā bhaiyā! Paisē lījiye.",
                    "Main hotel mẽ hū̃!",
                    "Station kahā̃ hai?"
                ],
                "correctAnswer": "Bahut shukriyā bhaiyā! Paisē lījiye.",
                "phoneticCyrillicTarget": "Бахут шукрийа бхаййаа! Пэсе лииджие.",
                "explanationRu": "Благодарность + передача оплаты: Paisē lījiye."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Экзаменационная симуляция Фазы 2: Поездка от вокзала до отеля",
            "setting": "Привокзальная площадь и маршрут по старым улицам",
            "partnerRoleRu": "Упрямый водитель рикши",
            "learnerRoleRu": "Уверенная путешественница",
            "turns": [
                {
                    "speaker": "Водитель",
                    "speechRu": "Эй, мадам! Садись, 300 рупий до отеля!",
                    "speechIso": "Madam! 300 rupees hotel kē liye!",
                    "speechCyrillic": "Мадам! 300 рупиис хотел ке лие!",
                    "learnerHintRu": "Скажите: Нет, брат! Включи счетчик. Поехали по счетчику."
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Нет, брат! Включи счетчик. Поедем по счетчику.",
                    "speechIso": "Nahī̃ bhaiyā! Mīṭar chalāo. Mīṭar sē chaliye.",
                    "speechCyrillic": "Нахииⁿ бхаййаа! Миитар͟ чалаао. Миитар͟ сэ чалие.",
                    "acceptableResponsesIso": ["Nahī̃ bhaiyā! Mīṭar chalāo.", "Mīṭar sē chaliye."]
                },
                {
                    "speaker": "Водитель",
                    "speechRu": "Ладно, садись! Куда поворачивать у рынка?",
                    "speechIso": "Acchā, baithiye! Market kē pās kahā̃ jānā hai?",
                    "speechCyrillic": "Аччхаа, бэтхие! Маркет ке паас кахааⁿ джаанаа хэ?",
                    "learnerHintRu": "Скомандуйте: Сначала прямо, потом налево. (Pahlē sīdhē, phir bāē̃ jāiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Сначала поезжайте прямо, потом поверните налево.",
                    "speechIso": "Pahlē sīdhē jāiye, phir bāē̃ jāiye.",
                    "speechCyrillic": "Пэхле сиидхэ джааие, пхир бааеⁿ джааие.",
                    "acceptableResponsesIso": ["Sīdhē jāiye, phir bāē̃ jāiye."]
                },
                {
                    "speaker": "Водитель",
                    "speechRu": "Вот этот отель?",
                    "speechIso": "Yeh hotel hai madam?",
                    "speechCyrillic": "Йе хотел хэ мадам?",
                    "learnerHintRu": "Подтвердите: Да! Остановитесь прямо здесь. Возьмите деньги, спасибо!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Да! Остановитесь прямо здесь. Возьмите деньги, большое спасибо!",
                    "speechIso": "Hā̃-jī! Yahā̃ par rukiye. Paisē lījiye, bahut shukriyā!",
                    "speechCyrillic": "Хааⁿ-джии! Йахааⁿ пар рукие. Пэсе лииджие, бахут шукрийа!",
                    "acceptableResponsesIso": ["Yahā̃ par rukiye! Paisē lījiye, shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Итоги Фазы 2: Полный навигационный суверенитет",
            "pointsRu": [
                "Вы научились мыслить синтаксисом SOV: направление всегда стоит перед глаголом.",
                "Вы виртуозно используете послелоги: В машине (gāṛī mẽ), на метро (metro sē), на вокзале (station par).",
                "Вы контролируете любую поездку и не переплачиваете за транспорт."
            ]
        }
    }
]
