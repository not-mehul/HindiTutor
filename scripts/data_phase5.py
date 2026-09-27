"""
data_phase5.py - Days 33 to 40
Phase 5: Aspectual Tenses, Complex Interactions, and Capstone Immersion
"""

DAYS_PHASE_5 = [
    # Day 33
    {
        "day": 33,
        "phase": 5,
        "title": {
            "en": "Habitual Aspect: Daily Routines and Personal Habits",
            "ru": "Хабитуалис: регулярные действия и привычки (Суффикс -tī hū̃ / -tā hū̃)"
        },
        "theme": "Я говорю на хинди (Main Hindī boltī hū̃), я живу здесь (Main yahā̃ rahtī hū̃), я пью чай каждый день (Main roz chāi peetī hū̃)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция причастного суффикса -tī / -таа и связки hū̃)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Несовершенный вид в русском языке = Хабитуалис в хинди: Я делаю обычно)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Подстановочные ряды привычек: живу в Москве, пью чай, говорю на хинди)",
            "phase4SimulationMinutes": "17:00–20:00 (Беседа за чаем о повседневной жизни)"
        },
        "learningObjectives": {
            "en": [
                "Express habitual and routine actions with imperfective participle (-tā / -tī hū̃)",
                "Map Hindi habitual aspect directly onto Russian imperfective aspect (Несовершенный вид)",
                "Discuss daily habits (boltī hū̃ = I speak, rahtī hū̃ = I live, peetī hū̃ = I drink)"
            ],
            "ru": [
                "Выражать регулярные и привычные действия с помощью несовершенного причастия (-tā для мужчин, -tī для женщин + hū̃)",
                "Опираться на прямое соответствие с русским несовершенным видом (Что делаю обычно? Я говорю, я пью, я живу)",
                "Рассказывать о своих привычках (boltī hū̃ = я говорю, rahtī hū̃ = я живу, peetī hū̃ = я пью)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Зубной звук /t/ в суффиксе женского рода /-tī/ (ती) и носовое hū̃",
            "articulatoryMechanism": "Чистый зубной [т] на резцах с долгим [ии], за которым следует носовое [хууⁿ]: [бол-тии хууⁿ].",
            "russianInterferenceWarning": "Не смягчайте звук [т] перед [и]! Кончик языка плотно прижат к верхним зубам.",
            "drills": [
                {
                    "prompt": "Отработка женского окончания хабитуалиса",
                    "contrastPair": "boltā hū̃ (м.р.) vs boltī hū̃ (ж.р.)",
                    "instructionsRu": "Произнесите от первого лица: Main boltī hū̃ (Я говорю)."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Хабитуальный аспект (Русский несовершенный вид)",
            "russianParallel": "Полная аналогия с русским настоящим временем несовершенного вида: 'Я говорю по-русски' (регулярно) = Main Russian boltī hū̃. Глагольная основа + суффикс рода (-tā м.р. / -tī ж.р.) + связка hū̃ (есмь).",
            "syntacticFormula": "Main + [Объект / Наречие] + [Основа глагола + tī / tā] + hū̃",
            "explanationRu": "Для женщины окончание всегда -tī hū̃. Если вы хотите сказать 'Я пью чай' -> Main chāi peetī hū̃; 'Я живу в России' -> Main Russia mẽ rahtī hū̃.",
            "pieCognateConnection": {
                "root": "*bʰel- / *seh₁-",
                "russian": "болтать / сеять (жить)",
                "hindi": "bōlnā (boltī) / rahnā (rahtī)",
                "meaning": "Праиндоевропейские регулярные действия"
            }
        },
        "vocabulary": [
            {
                "id": "d33_v01",
                "devanagari": "बोलती हूँ / बोलता हूँ",
                "transliterationIso": "Boltī hū̃ (f) / Boltā hū̃ (m)",
                "phoneticCyrillic": "Болтии хууⁿ / Болтаа хууⁿ",
                "translationRu": "Я говорю (обычно / умею)",
                "translationEn": "I speak (habitual)",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Глагол bōlnā (говорить)."
            },
            {
                "id": "d33_v02",
                "devanagari": "रहती हूँ / रहता हूँ",
                "transliterationIso": "Rahtī hū̃ (f) / Rahtā hū̃ (m)",
                "phoneticCyrillic": "Рэхтии хууⁿ / Рэхтаа хууⁿ",
                "translationRu": "Я живу / проживаю",
                "translationEn": "I live / stay",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Глагол rahnā (жить)."
            },
            {
                "id": "d33_v03",
                "devanagari": "पीती हूँ / पीता हूँ",
                "transliterationIso": "Peetī hū̃ (f) / Peetā hū̃ (m)",
                "phoneticCyrillic": "Пиитии хууⁿ / Пиитаа хууⁿ",
                "translationRu": "Я пью",
                "translationEn": "I drink",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Когнат с русским словом 'пить'."
            },
            {
                "id": "d33_v04",
                "devanagari": "रोज़",
                "transliterationIso": "Roz",
                "phoneticCyrillic": "Роз",
                "translationRu": "Каждый день / Ежедневно",
                "translationEn": "Daily / Every day",
                "partOfSpeech": "adverb",
                "gender": "n/a",
                "audioHint": "Звонкий [з]."
            }
        ],
        "exercises": [
            {
                "id": "d33_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите фразу: 'Я говорю на хинди' (женский род: Я + хинди + говорю + есмь)",
                "prompt": "Я говорю на хинди",
                "wordChips": ["Main", "Hindī", "boltī", "hū̃"],
                "correctAnswer": ["Main", "Hindī", "boltī", "hū̃"],
                "phoneticCyrillicTarget": "Мэⁿ Хиндии болтии хууⁿ",
                "explanationRu": "Main Hindī boltī hū̃ — классический хабитуалис."
            },
            {
                "id": "d33_ex02",
                "type": "substitution_drill",
                "instructionRu": "Скажите, что вы живете в Москве (женский род)",
                "prompt": "Main Moscow mẽ _____ hū̃.",
                "options": ["rahtī", "rahtā", "boltī"],
                "correctAnswer": "rahtī",
                "transliterationIsoTarget": "Main Moscow mẽ rahtī hū̃.",
                "explanationRu": "Rahtī hū̃ = я живу (ж.р.)."
            },
            {
                "id": "d33_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Собеседник удивлен: 'Āp Hindī boltī haiñ?' (Вы говорите на хинди?). Подтвердите за 2 секунды: 'Да, я немного говорю на хинди!'",
                "prompt": "Вопрос о знании хинди",
                "options": [
                    "Hā̃, main thōṛī Hindī boltī hū̃!",
                    "Nahī̃, main hotel hū̃!",
                    "Garam khānā dījiye!"
                ],
                "correctAnswer": "Hā̃, main thōṛī Hindī boltī hū̃!",
                "phoneticCyrillicTarget": "Хааⁿ, мэⁿ тхоор͟ии Хиндии болтии хууⁿ!",
                "explanationRu": "Да, я немного говорю на хинди!"
            },
            {
                "id": "d33_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Скажите: 'Я каждый день пью чай масала' (женский род)",
                "prompt": "Main roz masālā chāi _____ hū̃.",
                "options": ["peetī", "khātī", "rahtī"],
                "correctAnswer": "peetī",
                "transliterationIsoTarget": "Main roz masālā chāi peetī hū̃.",
                "explanationRu": "Peetī hū̃ = я пью."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Беседа о жизни и привычках в поезде дальнего следования",
            "setting": "Купе индийского поезда (AC Tier)",
            "partnerRoleRu": "Интеллигентный попутчик",
            "learnerRoleRu": "Путешественница",
            "turns": [
                {
                    "speaker": "Попутчик",
                    "speechRu": "Намастэ! Вы прекрасно говорите. Вы живете в Индии?",
                    "speechIso": "Namastē! Āp bahut acchī Hindī boltī haiñ. Kyā āp India mẽ rahtī haiñ?",
                    "speechCyrillic": "Намастэ! Аап бахут аччхии Хиндии болтии хэⁿ. Кйаа аап Индиа мэⁿ рэхтии хэⁿ?",
                    "learnerHintRu": "Скажите: Нет, я живу в России. Я немного говорю на хинди. (Nahī̃, main Russia mẽ rahtī hū̃)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Нет, я живу в России. Я только немного говорю на хинди.",
                    "speechIso": "Nahī̃, main Russia mẽ rahtī hū̃. Main thōṛī Hindī boltī hū̃.",
                    "speechCyrillic": "Нахииⁿ, мэⁿ Расийа мэⁿ рэхтии хууⁿ. Мэⁿ тхоор͟ии Хиндии болтии хууⁿ.",
                    "acceptableResponsesIso": ["Main Russia mẽ rahtī hū̃. Thōṛī Hindī boltī hū̃."]
                },
                {
                    "speaker": "Попутчик",
                    "speechRu": "Замечательно! Чай будете пить?",
                    "speechIso": "Bahut acchā! Chāi pīyēṅgī?",
                    "speechCyrillic": "Бахут аччхаа! Чаай пииенгии?",
                    "learnerHintRu": "Скажите: Да, я пью чай каждый день, спасибо! (Hā̃, main roz chāi peetī hū̃)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Да, я каждый день пью чай масала! Спасибо.",
                    "speechIso": "Hā̃-jī! Main roz masālā chāi peetī hū̃. Shukriyā!",
                    "speechCyrillic": "Хааⁿ-джии! Мэⁿ роз масаалаа чаай пиитии хууⁿ. Шукрийа!",
                    "acceptableResponsesIso": ["Hā̃-jī, main roz chāi peetī hū̃!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Беседы в индийских поездах",
            "pointsRu": [
                "Поездка на индийском поезде — лучший полигон для разговорной практики в мире.",
                "Попутчики обязательно угостят вас домашней едой и спросят о вашей семье и работе.",
                "Использование форм 'rahtī hū̃' и 'boltī hū̃' производит неизгладимое впечатление культурной чуткости."
            ]
        }
    },

    # Day 34
    {
        "day": 34,
        "phase": 5,
        "title": {
            "en": "Continuous Aspect: Real-Time Actions",
            "ru": "Длительный аспект (Continuous): действия прямо сейчас (Rahā / Rahī hū̃)"
        },
        "theme": "Я иду сейчас (Main jā rahī hū̃), мы выходим (Hum nikal rahē haiñ), я просто смотрю (Main bas dēkh rahī hū̃)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция маркера длительности rahā / rahī)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Настоящее время с 'сейчас' в русском языке = Rahā/Rahī в хинди)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Отработка: я сейчас иду, мы выезжаем, я просто осматриваюсь)",
            "phase4SimulationMinutes": "17:00–20:00 (Вежливое отклонение назойливого торговца: 'Я просто смотрю')"
        },
        "learningObjectives": {
            "en": [
                "Construct present continuous aspect using rahā (m) / rahī (f) + copula",
                "Contrast habitual actions (-tī hū̃) with actions in progress (rahī hū̃)",
                "Deploy essential browsing formula 'Main bas dēkh rahī hū̃' (Just looking)"
            ],
            "ru": [
                "Строить настоящее длительное время с помощью маркера rahā (м.р.) / rahī (ж.р.) + связка hū̃/hai",
                "Различать действие вообще (boltī hū̃) и действие прямо сейчас (jā rahī hū̃)",
                "Использовать защитную фразу от навязчивых продавцов: 'Main bas dēkh rahī hū̃' ('Я просто смотрю')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Глухой выдох /h/ в прогрессивном маркере rahā / rahī (रहा / रही)",
            "articulatoryMechanism": "Раскатистый [р] + краткий гласный [а] + чистый выдох [х] с долгим [аа] или [ии]: [ра-хаа], [ра-хии].",
            "russianInterferenceWarning": "Не проглатывайте звук [х] в середине слова.",
            "drills": [
                {
                    "prompt": "Отработка длительного действия в женском роде",
                    "contrastPair": "jā rahī hū̃ (я иду прямо сейчас)",
                    "instructionsRu": "Произнесите: Main jā rahī hū̃ (Я сейчас иду)."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Длительный вид (Present Continuous с rahā / rahī)",
            "russianParallel": "В русском языке мы добавляем слово 'сейчас' или интонационно подчеркиваем процесс: 'Я [сейчас] иду', 'Мы [в эту секунду] выходим'. В хинди для этого используется вспомогательное причастие rahā (м.р.) / rahī (ж.р.): Main jā rahī hū̃.",
            "syntacticFormula": "[Основа глагола] + [rahī (ж.р.) / rahā (м.р.) / rahē (мн.ч.)] + [hū̃ / hai / haiñ]",
            "explanationRu": "Эта конструкция используется при телефонных разговорах ('Где ты? — Я уже еду: Main aa rahī hū̃') и в магазинах ('Madam, buy this! — Shukriyā, main bas dēkh rahī hū̃: Спасибо, я просто смотрю').",
            "pieCognateConnection": {
                "root": "*reg-",
                "russian": "ряд / прямо",
                "hindi": "rahnā (оставаться / продолжаться)",
                "meaning": "Протяженность процесса во времени"
            }
        },
        "vocabulary": [
            {
                "id": "d34_v01",
                "devanagari": "रही हूँ / रहा हूँ",
                "transliterationIso": "Rahī hū̃ (f) / Rahā hū̃ (m)",
                "phoneticCyrillic": "Рахии хууⁿ / Рахаа хууⁿ",
                "translationRu": "Я делаю прямо сейчас (длительный маркер)",
                "translationEn": "am doing (continuous)",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Маркер процесса прямо сейчас."
            },
            {
                "id": "d34_v02",
                "devanagari": "जा रही हूँ",
                "transliterationIso": "Jā rahī hū̃",
                "phoneticCyrillic": "Джаа рахии хууⁿ",
                "translationRu": "Я иду / еду прямо сейчас",
                "translationEn": "I am going (now)",
                "partOfSpeech": "verb",
                "gender": "f",
                "audioHint": "Jā (основа) + rahī + hū̃."
            },
            {
                "id": "d34_v03",
                "devanagari": "निकल रहे हैं",
                "transliterationIso": "Nikal rahē haiñ",
                "phoneticCyrillic": "Никал рахээ хэⁿ",
                "translationRu": "Мы выходим / выезжаем прямо сейчас",
                "translationEn": "We are leaving (now)",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Nikalnā (выходить / выдвигаться)."
            },
            {
                "id": "d34_v04",
                "devanagari": "देख रही हूँ",
                "transliterationIso": "Dēkh rahī hū̃",
                "phoneticCyrillic": "Дэкх рахии хууⁿ",
                "translationRu": "Я смотрю / осматриваюсь",
                "translationEn": "I am looking / browsing",
                "partOfSpeech": "verb",
                "gender": "f",
                "audioHint": "Dēkh (смотреть) + rahī + hū̃."
            }
        ],
        "exercises": [
            {
                "id": "d34_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите спасительную фразу в магазине: 'Спасибо, я просто смотрю' (женский род)",
                "prompt": "Спасибо, я просто смотрю",
                "wordChips": ["Shukriyā,", "main bas", "dēkh", "rahī", "hū̃"],
                "correctAnswer": ["Shukriyā,", "main bas", "dēkh", "rahī", "hū̃"],
                "phoneticCyrillicTarget": "Шукрийа, мэⁿ бас дэкх рахии хууⁿ",
                "explanationRu": "Main bas dēkh rahī hū̃ = Я просто смотрю."
            },
            {
                "id": "d34_ex02",
                "type": "substitution_drill",
                "instructionRu": "Скажите водителю по телефону: 'Я уже иду!' (женский род)",
                "prompt": "Main aa _____ hū̃. (Я иду/прихожу)",
                "options": ["rahī", "rahā", "boltī"],
                "correctAnswer": "rahī",
                "transliterationIsoTarget": "Main aa rahī hū̃.",
                "explanationRu": "Main aa rahī hū̃ = Я иду прямо сейчас."
            },
            {
                "id": "d34_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Хозяин отеля спрашивает: 'Āp kahā̃ jā rahī haiñ?' (Куда вы идете?). Ответьте за 2 секунды: 'Я иду в отель!'",
                "prompt": "Куда вы идете?",
                "options": [
                    "Main hotel jā rahī hū̃!",
                    "Main hotel mẽ thī!",
                    "Hotel bahut mahangā hai!"
                ],
                "correctAnswer": "Main hotel jā rahī hū̃!",
                "phoneticCyrillicTarget": "Мэⁿ хотел джаа рахии хууⁿ!",
                "explanationRu": "Main hotel jā rahī hū̃ = Я иду в отель."
            },
            {
                "id": "d34_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Скажите попутчикам: 'Мы выходим прямо сейчас'",
                "prompt": "Hum ab _____ rahē haiñ. (Мы выходим)",
                "options": ["nikal", "chāi", "pānī"],
                "correctAnswer": "nikal",
                "transliterationIsoTarget": "Hum ab nikal rahē haiñ.",
                "explanationRu": "Nikal rahē haiñ = выходим / отправляемся."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Прогулка по антикварной лавке без навязывания покупок",
            "setting": "Антикварный магазин в Джайпуре",
            "partnerRoleRu": "Настойчивый консультант",
            "learnerRoleRu": "Спокойная туристка",
            "turns": [
                {
                    "speaker": "Консультант",
                    "speechRu": "Здравствуйте, мадам! Посмотрите сюда, старинные ковры, бронза! Что вы ищете?",
                    "speechIso": "Namastē madam! Carpets, statues! Kyā chāhiye āpkō?",
                    "speechCyrillic": "Намастэ мадам! Карпетс, стэтьюс! Кйаа чаахийе аапко?",
                    "learnerHintRu": "Улыбнитесь и скажите: Спасибо, я просто смотрю! (Shukriyā, main bas dēkh rahī hū̃)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Спасибо, я просто осматриваюсь.",
                    "speechIso": "Shukriyā, main bas dēkh rahī hū̃.",
                    "speechCyrillic": "Шукрийа, мэⁿ бас дэкх рахии хууⁿ.",
                    "acceptableResponsesIso": ["Main bas dēkh rahī hū̃"]
                },
                {
                    "speaker": "Консультант",
                    "speechRu": "Пожалуйста, смотрите спокойно! Если что-то нужно, позовите меня.",
                    "speechIso": "Sure madam, dēkhiye āram sē! Bulāiye jab chāhiye.",
                    "speechCyrillic": "Шур мадам, дэкхие аарам сэ! Булааие джаб чаахийе.",
                    "learnerHintRu": "Ответьте с благодарностью: Ṭhīk hai, shukriyā!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Хорошо, спасибо!",
                    "speechIso": "Ṭhīk hai, shukriyā!",
                    "speechCyrillic": "Т͟хиик хэ, шукрийа!",
                    "acceptableResponsesIso": ["Dhanyavād"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Как защитить личное пространство в магазинах",
            "pointsRu": [
                "В туристических магазинах продавцы могут ходить за вами по пятам.",
                "Фраза на хинди 'Main bas dēkh rahī hū̃' (Я просто смотрю) действует обезоруживающе: консультант понимает, что давить бессмысленно, и отходит в сторону.",
                "Слово 'Ārām sē' означает 'спокойно / не спеша'."
            ]
        }
    },

    # Day 35
    {
        "day": 35,
        "phase": 5,
        "title": {
            "en": "Modal Capacity and Permission with Saknā",
            "ru": "Модальность и разрешение: глагол Saknā (Мочь / Можно)"
        },
        "theme": "Я могу (main saktī hū̃), можно я здесь сяду? (kyā main yahā̃ baith saktī hū̃?), вы можете помочь? (kyā āp madad kar saktē haiñ?)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция модальной связки saktī / сактии)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Модальный глагол мочь в русском языке = Saknā в хинди)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Запрос разрешения: сфотографировать, присесть, войти, помочь)",
            "phase4SimulationMinutes": "17:00–20:00 (Запрос разрешения на фотосъемку в храме/музее)"
        },
        "learningObjectives": {
            "en": [
                "Express capability and permission using modal verb saknā",
                "Formulate polite requests with 'Kyā main ... saktī hū̃?' (May I ...?)",
                "Ask for assistance with 'Kyā āp madad kar saktē haiñ?' (Can you help?)"
            ],
            "ru": [
                "Выражать физическую возможность и разрешение через модальный глагол saknā (мочь)",
                "Формулировать вежливые вопросы о разрешении: 'Kyā main ... saktī hū̃?' ('Можно я ...? / Могу ли я ...?')",
                "Просить о содействии: 'Kyā āp madad kar saktē haiñ?' ('Можете ли вы помочь?')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Зубной звук /s/ и согласный кластер /kt/ в saktī (सकती)",
            "articulatoryMechanism": "Зубной [с] + краткий [а] + плотный смычный переход от [к] к зубному [т] с долгим [ии]: [сак-тии].",
            "russianInterferenceWarning": "Не вставляйте гласный между к и т (не сакати!).",
            "drills": [
                {
                    "prompt": "Отработка модальной формы разрешения",
                    "contrastPair": "baith saktī hū̃ (могу сесть)",
                    "instructionsRu": "Kyā main yahā̃ baith saktī hū̃? (Можно я здесь сяду?)"
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Модальный глагол Saknā (Мочь / Иметь возможность)",
            "russianParallel": "Строго повторяет русскую конструкцию: 'Я могу + инфинитив' или 'Можно мне сесть?'. В хинди берется чистая основа смыслового глагола (без окончания -nā) + форма глагола saknā: Baith (сесть) + saktī (могу) + hū̃ (есмь).",
            "syntacticFormula": "Kyā main + [Основа смыслового глагола] + saktī hū̃?",
            "explanationRu": "Для вопроса о разрешении мы просто ставим в начале знакомую нам частицу Kyā (ли): Kyā main photo lē saktī hū̃? = Могу ли я сделать фото? (Можно сфотографировать?).",
            "pieCognateConnection": {
                "root": "*sekw-",
                "russian": "следовать / соблюдать (сила, мощь)",
                "hindi": "saknā (мочь / быть в силах)",
                "meaning": "Праиндоевропейская способность и возможность"
            }
        },
        "vocabulary": [
            {
                "id": "d35_v01",
                "devanagari": "सकती हूँ / सकता हूँ",
                "transliterationIso": "Saktī hū̃ (f) / Saktā hū̃ (m)",
                "phoneticCyrillic": "Сактии хууⁿ / Сактаа хууⁿ",
                "translationRu": "Я могу (модальный глагол)",
                "translationEn": "I can / am able to",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Модальный глагол мочи."
            },
            {
                "id": "d35_v02",
                "devanagari": "फ़ोटो ले सकती हूँ",
                "transliterationIso": "Photo lē saktī hū̃",
                "phoneticCyrillic": "Фото лее сактии хууⁿ",
                "translationRu": "Могу сфотографировать / снять",
                "translationEn": "Can take a photo",
                "partOfSpeech": "phrase",
                "gender": "f",
                "audioHint": "Lēnā = брать / делать фото."
            },
            {
                "id": "d35_v03",
                "devanagari": "अंदर आ सकती हूँ",
                "transliterationIso": "Andar aa saktī hū̃",
                "phoneticCyrillic": "Андар аа сактии хууⁿ",
                "translationRu": "Могу войти внутрь (Можно войти?)",
                "translationEn": "Can come inside",
                "partOfSpeech": "phrase",
                "gender": "f",
                "audioHint": "Andar = внутри."
            },
            {
                "id": "d35_v04",
                "devanagari": "मदद कर सकते हैं",
                "transliterationIso": "Madad kar saktē haiñ",
                "phoneticCyrillic": "Мадад кар сактээ хэⁿ",
                "translationRu": "Можете помочь (уважительно)",
                "translationEn": "Can help (respectful)",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Обращение на Вы (Āp)."
            }
        ],
        "exercises": [
            {
                "id": "d35_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите вежливый вопрос о разрешении: 'Можно я сделаю фото?' (женский род)",
                "prompt": "Можно я сфотографирую?",
                "wordChips": ["Kyā main", "photo", "lē", "saktī", "hū̃?"],
                "correctAnswer": ["Kyā main", "photo", "lē", "saktī", "hū̃?"],
                "phoneticCyrillicTarget": "Кйаа мэⁿ фото лее сактии хууⁿ?",
                "explanationRu": "Kyā main photo lē saktī hū̃? = Могу ли я сфотографировать?"
            },
            {
                "id": "d35_ex02",
                "type": "substitution_drill",
                "instructionRu": "Спросите вежливо: 'Можно я здесь сяду?'",
                "prompt": "Kyā main yahā̃ _____ saktī hū̃?",
                "options": ["baith", "jā", "khā"],
                "correctAnswer": "baith",
                "transliterationIsoTarget": "Kyā main yahā̃ baith saktī hū̃?",
                "explanationRu": "Baithnā (сидеть) -> основа baith."
            },
            {
                "id": "d35_ex03",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вам тяжело нести сумку. Попросите прохожего о помощи за 2 секунды.",
                "prompt": "Просьба о помощи",
                "options": [
                    "Bhaiyā, kyā āp madad kar saktē haiñ?",
                    "Bhaiyā, sīdhē jāiye!",
                    "Khānā mahangā hai!"
                ],
                "correctAnswer": "Bhaiyā, kyā āp madad kar saktē haiñ?",
                "phoneticCyrillicTarget": "Бхаййаа, кйаа аап мадад кар сактээ хэⁿ?",
                "explanationRu": "Очень вежливая формула просьбы о помощи."
            },
            {
                "id": "d35_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Спросите разрешения войти в храм: 'Можно войти внутрь?'",
                "prompt": "Kyā hum andar aa _____ haiñ?",
                "options": ["saktē", "saktī", "saktā"],
                "correctAnswer": "saktē",
                "transliterationIsoTarget": "Kyā hum andar aa saktē haiñ?",
                "explanationRu": "Для местоимения hum (мы) или вежливости используется форма saktē."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Запрос разрешения на съемку в историческом храме",
            "setting": "Вход в древний храм в Кхаджурахо или Варанаси",
            "partnerRoleRu": "Служитель храма (pujari / guard)",
            "learnerRoleRu": "Уважительная туристка с камерой",
            "turns": [
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте, уважаемый! Можно войти внутрь?",
                    "speechIso": "Namastē jī! Kyā main andar aa saktī hū̃?",
                    "speechCyrillic": "Намастэ джии! Кйаа мэⁿ андар аа сактии хууⁿ?",
                    "learnerHintRu": "Спросите разрешения войти: Kyā main andar aa saktī hū̃?"
                },
                {
                    "speaker": "Служитель",
                    "speechRu": "Здравствуйте! Да, проходите, только снимите обувь здесь.",
                    "speechIso": "Namastē! Hā̃, andar āiye, shoes yahā̃ utāriye.",
                    "speechCyrillic": "Намастэ! Хааⁿ, андар ааие, шууз йахааⁿ утаарие.",
                    "learnerHintRu": "Спросите о фото: А можно сделать фото? (Kyā main photo lē saktī hū̃?)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Хорошо. А здесь можно сфотографировать?",
                    "speechIso": "Ṭhīk hai. Kyā main photo lē saktī hū̃?",
                    "speechCyrillic": "Т͟хиик хэ. Кйаа мэⁿ фото лее сактии хууⁿ?",
                    "acceptableResponsesIso": ["Kyā main photo lē saktī hū̃?"]
                },
                {
                    "speaker": "Служитель",
                    "speechRu": "Снаружи можно, а внутри алтаря фото делать нельзя.",
                    "speechIso": "Bāhar photo lē saktī haiñ, andar nahī̃.",
                    "speechCyrillic": "Баахар фото лее сактии хэⁿ, андар нахииⁿ.",
                    "learnerHintRu": "Ответьте с почтением: Main samjhī, dhanyavād jī!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Я поняла, спасибо большое!",
                    "speechIso": "Main samjhī, bahut dhanyavād jī!",
                    "speechCyrillic": "Мэⁿ самджи, бахут дханьяваад джии!",
                    "acceptableResponsesIso": ["Main samjhī, shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Правила этикета в индийских храмах",
            "pointsRu": [
                "Перед входом в любой индуистский храм, сикхскую гурудвару или мечеть ВСЕГДА снимают обувь.",
                "Вопрос 'Kyā main photo lē saktī hū̃?' демонстрирует глубокое уважение к религиозным чувствам.",
                "В сикхских храмах также обязательно покрывают голову платком (даже мужчинам)."
            ]
        }
    },

    # Day 36
    {
        "day": 36,
        "phase": 5,
        "title": {
            "en": "Future Intentions and Temporal Sequencing",
            "ru": "Планы на будущее и временные маркеры: Завтра (Kal) и «До свидания»"
        },
        "theme": "Завтра/вчера (kal), сегодня (āj), я поеду завтра (main kal jāūṅgī), мы снова встретимся / до свидания (hum phir milēṅgē)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция будущего окончания -ūṅgī / -уунгii и мягкого l в milēṅgē)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Специфика слова Kal: завтра и вчера; формула прощания Hum phir milẽge = До свидания)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Планы: поеду в Дели, встретимся вечером, сделаю завтра)",
            "phase4SimulationMinutes": "17:00–20:00 (Теплое прощание с хозяевами гестхауса)"
        },
        "learningObjectives": {
            "en": [
                "Express future movements using feminine future suffix -ūṅgī (Main jāūṅgī)",
                "Navigate the dual meaning of temporal marker Kal (tomorrow / yesterday)",
                "Master authentic farewell formula 'Hum phir milēṅgē' (We will meet again)"
            ],
            "ru": [
                "Выражать планы на будущее с суффиксом женского рода -ūṅgī (Main kal jāūṅgī = Я завтра поеду)",
                "Понять логику слова Kal (которое значит и 'завтра', и 'вчера' в зависимости от глагола)",
                "Освоить красивую традиционную формулу прощания: 'Hum phir milēṅgē' ('Мы снова встретимся / До свидания')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Назализованный велярный /ṅg/ в будущем времени -ūṅgī (ऊँगी)",
            "articulatoryMechanism": "Долгий [уу] с носовым призвуком переходит в мягкий звонкий [нг] с долгим [ии]: [джаа-уунгii].",
            "russianInterferenceWarning": "Не оглушайте звук [г] на конце суффикса будущего времени.",
            "drills": [
                {
                    "prompt": "Отработка будущего времени",
                    "contrastPair": "Main kal jāūṅgī (Я завтра поеду)",
                    "instructionsRu": "Произнесите связку: Main kal jāūṅgī."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Будущее время и идиома прощания 'До свидания'",
            "russianParallel": "Фраза 'Hum phir milēṅgē' буквально переводится: 'Мы снова встретимся' (Hum = мы, phir = снова, milēṅgē = встретимся). Это точнейший смысловой аналог русского 'До свидания' (до скорого свидания!).",
            "syntacticFormula": "Main + [Время: Kal / Āj] + [Глагол + ūṅgī (ж.р.) / ūṅgā (м.р.)]",
            "explanationRu": "Слово 'Kal' в индийской культуре обозначает 'день, не являющийся сегодняшним' (один шаг от сегодня). Если глагол в будущем — значит завтра; если в прошедшем — значит вчера! Очень удобно.",
            "pieCognateConnection": {
                "root": "*mel- / *mil-",
                "russian": "милый / мелькать (соединение)",
                "hindi": "milnā (встречаться / находить)",
                "meaning": "Встреча и соединение"
            }
        },
        "vocabulary": [
            {
                "id": "d36_v01",
                "devanagari": "कल",
                "transliterationIso": "Kal",
                "phoneticCyrillic": "Кал",
                "translationRu": "Завтра / Вчера (один день от сегодня)",
                "translationEn": "Tomorrow / Yesterday",
                "partOfSpeech": "adverb",
                "gender": "m",
                "audioHint": "Краткое открытое [кал]."
            },
            {
                "id": "d36_v02",
                "devanagari": "आज",
                "transliterationIso": "Āj",
                "phoneticCyrillic": "Аадж",
                "translationRu": "Сегодня",
                "translationEn": "Today",
                "partOfSpeech": "adverb",
                "gender": "m",
                "audioHint": "Долгое 'аа' + звонкое 'дж'."
            },
            {
                "id": "d36_v03",
                "devanagari": "जाऊँगी / जाऊँगा",
                "transliterationIso": "Jāūṅgī (f) / Jāūṅgā (m)",
                "phoneticCyrillic": "Джаауунгii / Джаауунгаа",
                "translationRu": "Я поеду / пойду (будущее время)",
                "translationEn": "I will go",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Будущее время первого лица."
            },
            {
                "id": "d36_v04",
                "devanagari": "फिर मिलेंगे",
                "transliterationIso": "Phir milēṅgē",
                "phoneticCyrillic": "Пхир милээнгээ",
                "translationRu": "Мы снова встретимся / До свидания!",
                "translationEn": "We will meet again / Goodbye",
                "partOfSpeech": "phrase",
                "gender": "both",
                "audioHint": "Красивая формула прощания."
            }
        ],
        "exercises": [
            {
                "id": "d36_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите фразу: 'Я поеду в Дели завтра' (женский род)",
                "prompt": "Я поеду в Дели завтра",
                "wordChips": ["Main", "kal", "Delhi", "jāūṅgī"],
                "correctAnswer": ["Main", "kal", "Delhi", "jāūṅgī"],
                "phoneticCyrillicTarget": "Мэⁿ кал Дели джаауунгii",
                "explanationRu": "Подлежащее + время + направление + глагол будущего времени."
            },
            {
                "id": "d36_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Вы прощаетесь с добрыми хозяевами отеля. Скажите 'До свидания, мы снова встретимся!' за 2 секунды.",
                "prompt": "Прощание при выезде",
                "options": [
                    "Namastē jī, hum phir milēṅgē!",
                    "Main āj khānā khāūṅgī!",
                    "Station kitnē kā hai?"
                ],
                "correctAnswer": "Namastē jī, hum phir milēṅgē!",
                "phoneticCyrillicTarget": "Намастэ джии, хум пхир милээнгээ!",
                "explanationRu": "Hum phir milēṅgē — самая душевная фраза прощания в Индии."
            },
            {
                "id": "d36_ex03",
                "type": "substitution_drill",
                "instructionRu": "Скажите, что вы уезжаете сегодня, а не завтра",
                "prompt": "Main _____ jāūṅgī. (Сегодня поеду)",
                "options": ["āj", "kal", "roz"],
                "correctAnswer": "āj",
                "transliterationIsoTarget": "Main āj jāūṅgī.",
                "explanationRu": "Āj = сегодня."
            },
            {
                "id": "d36_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Назначьте встречу вечером: 'Встретимся вечером'",
                "prompt": "Shām ko (вечером) _____! (Встретимся)",
                "options": ["milēṅgē", "chāhiye", "jānā"],
                "correctAnswer": "milēṅgē",
                "transliterationIsoTarget": "Shām ko milēṅgē!",
                "explanationRu": "Milēṅgē = встретимся."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Прощание с хозяевами дома перед отъездом",
            "setting": "Крыльцо гестхауса, такси ждет у ворот",
            "partnerRoleRu": "Радушный хозяин гестхауса",
            "learnerRoleRu": "Благодарная гостья с чемоданом",
            "turns": [
                {
                    "speaker": "Хозяин",
                    "speechRu": "Сестра, такси уже ждет. Вы сегодня едете в аэропорт?",
                    "speechIso": "Madam, taxi aa gayī. Āp āj jā rahī haiñ?",
                    "speechCyrillic": "Мадам, такси аа гайии. Аап аадж джаа рахии хэⁿ?",
                    "learnerHintRu": "Скажите: Да, я сегодня еду в Дели. Большое спасибо за все! (Hā̃, main āj jāūṅgī)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Да, я сегодня уезжаю в Дели. Большое спасибо за теплый прием!",
                    "speechIso": "Hā̃, main āj Delhi jāūṅgī. Bahut dhanyavād jī!",
                    "speechCyrillic": "Хааⁿ, мэⁿ аадж Дели джаауунгii. Бахут дханьяваад джии!",
                    "acceptableResponsesIso": ["Main āj jāūṅgī. Bahut shukriyā!"]
                },
                {
                    "speaker": "Хозяин",
                    "speechRu": "Приезжайте к нам снова! Счастливого пути!",
                    "speechIso": "Phir āiye hamārē pās! Shubh yātrā!",
                    "speechCyrillic": "Пхир ааие хамааре паас! Шубх йаатраа!",
                    "learnerHintRu": "Тепло попрощайтесь: До свидания, мы снова встретимся! (Namastē, hum phir milēṅgē!)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "До свидания! Мы обязательно снова встретимся.",
                    "speechIso": "Namastē jī, hum phir milēṅgē!",
                    "speechCyrillic": "Намастэ джии, хум пхир милээнгээ!",
                    "acceptableResponsesIso": ["Hum phir milēṅgē!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Культура расставания в Индии",
            "pointsRu": [
                "В индийской традиции говорить человеку прямое 'Прощай' (Alvidā) считается плохой приметой (как будто вы больше никогда не увидитесь).",
                "Вместо этого всегда говорят: 'Hum phir milēṅgē' (Мы снова увидимся / встретимся) или 'Main aatī hū̃' (Я еще вернусь).",
                "Пожелание счастливого пути на санскрите/хинди: 'Shubh yātrā!'."
            ]
        }
    },

    # Day 37
    {
        "day": 37,
        "phase": 5,
        "title": {
            "en": "Health, Safety, and Medical Emergencies",
            "ru": "Здоровье и безопасность: симптомы (Tabīyat kharāb hai) и вызов врача"
        },
        "theme": "Самочувствие плохое (Mērī tabīyat kharāb hai), боль в животе (pēṭ dard), лекарство (davā), вызовите врача (Doctor ko bulāiye)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция медицинских терминов: tabīyat, pēṭ dard, bulāiye)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Русское 'Мое самочувствие плохое' = Mērī tabīyat kharāb hai; винительный ko в Doctor ko bulāiye)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Экстренные фразы: болит живот, нужна аптека, позовите врача)",
            "phase4SimulationMinutes": "17:00–20:00 (Покупка лекарств в аптеке и консультация)"
        },
        "learningObjectives": {
            "en": [
                "Report illness using idiom 'Mērī tabīyat kharāb hai' (I am unwell)",
                "Identify physical symptoms: pēṭ dard (stomach ache), sirdard (headache)",
                "Request medical intervention using 'Doctor ko bulāiye' and find davā (medicine)"
            ],
            "ru": [
                "Сообщать о болезни через идиому: 'Mērī tabīyat kharāb hai' ('Моё самочувствие плохое / Мне нездоровится')",
                "Описывать симптомы: pēṭ dard (боль в животе), sirdard (головная боль)",
                "Вызывать медицинскую помощь: 'Doctor ko bulāiye' ('Позовите доктора') и просить davā (лекарство)"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Зубной звонкий /d/ и раскатистый /r/ в слове dard (दर्द)",
            "articulatoryMechanism": "Два твердых зубных [д] с раскатистым чистым [р] посередине: [дард]. Значит 'боль'.",
            "russianInterferenceWarning": "Не оглушайте звук [д] на конце слова (не 'дарт'!).",
            "drills": [
                {
                    "prompt": "Отработка локализации боли",
                    "contrastPair": "Pēṭ dard (живот болит) vs Sirdard (голова болит)",
                    "instructionsRu": "Pēṭ (живот) + dard (боль)."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Идиома самочувствия и оформление прямого объекта через 'ko'",
            "russianParallel": "Фраза 'Mērī tabīyat kharāb hai' буквально переводится как 'Моё самочувствие плохое' (tabīyat женского рода = самочувствие/здоровье; kharāb = плохое/сломанное). При вызове конкретного одушевленного лица появляется послелог ko (русский винительный падеж): 'Позовите кого? Доктора' = Doctor ko bulāiye!",
            "syntacticFormula": "Mērī tabīyat kharāb hai / [Орган] + dard hai / [Лицо] + ko bulāiye",
            "explanationRu": "Эта лексика — ваша спасательная страховка в любой экстренной ситуации со здоровьем в Индии.",
            "pieCognateConnection": {
                "root": "*der-",
                "russian": "драть / дыра (раздирающая боль)",
                "hindi": "dard (боль / страдание)",
                "meaning": "Праиндоевропейская физическая боль"
            }
        },
        "vocabulary": [
            {
                "id": "d37_v01",
                "devanagari": "तबीयत ख़राब है",
                "transliterationIso": "Tabīyat kharāb hai",
                "phoneticCyrillic": "Табиийат харааб хэ",
                "translationRu": "Мне нездоровится (самочувствие плохое)",
                "translationEn": "I am feeling unwell / sick",
                "partOfSpeech": "phrase",
                "gender": "f",
                "audioHint": "Ключевая фраза о здоровье."
            },
            {
                "id": "d37_v02",
                "devanagari": "दर्द",
                "transliterationIso": "Dard",
                "phoneticCyrillic": "Дард",
                "translationRu": "Боль",
                "translationEn": "Pain / Ache",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Когнат со словом 'драть'."
            },
            {
                "id": "d37_v03",
                "devanagari": "पेट दर्द",
                "transliterationIso": "Pēṭ dard",
                "phoneticCyrillic": "Пеет͟ дард",
                "translationRu": "Боль в животе",
                "translationEn": "Stomach ache",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Ретрофлексный [т͟]."
            },
            {
                "id": "d37_v04",
                "devanagari": "दवा",
                "transliterationIso": "Davā",
                "phoneticCyrillic": "Даваа",
                "translationRu": "Лекарство",
                "translationEn": "Medicine",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Долгое 'аа' на конце."
            },
            {
                "id": "d37_v05",
                "devanagari": "डॉक्टर को बुलाइए",
                "transliterationIso": "Doctor ko bulāiye",
                "phoneticCyrillic": "Доктор ко булааие",
                "translationRu": "Вызовите (позовите) доктора",
                "translationEn": "Please call a doctor",
                "partOfSpeech": "phrase",
                "gender": "both",
                "audioHint": "Bulānā = звать."
            }
        ],
        "exercises": [
            {
                "id": "d37_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите экстренное сообщение: 'Помогите, пожалуйста! Мне нездоровится'",
                "prompt": "Помогите, мне нездоровится",
                "wordChips": ["Madad", "kījiye,", "mērī", "tabīyat", "kharāb", "hai!"],
                "correctAnswer": ["Madad", "kījiye,", "mērī", "tabīyat", "kharāb", "hai!"],
                "phoneticCyrillicTarget": "Мадад кииджие, мерии табиийат харааб хэ!",
                "explanationRu": "Madad kījiye (помогите) + mērī tabīyat kharāb hai (мне нездоровится)."
            },
            {
                "id": "d37_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "У вас сильно разболелся живот. Скажите об этом в аптеке за 2 секунды.",
                "prompt": "Симптом боли в животе",
                "options": [
                    "Bhaiyā, pēṭ dard hai, davā dījiye!",
                    "Mujhē chāi pasand hai!",
                    "Station kahā̃ hai?"
                ],
                "correctAnswer": "Bhaiyā, pēṭ dard hai, davā dījiye!",
                "phoneticCyrillicTarget": "Бхаййаа, пеет͟ дард хэ, даваа дииджие!",
                "explanationRu": "Pēṭ dard hai, davā dījiye = Живот болит, дайте лекарство!"
            },
            {
                "id": "d37_ex03",
                "type": "substitution_drill",
                "instructionRu": "Попросите срочно позвать доктора",
                "prompt": "Doctor ko _____! (Позовите)",
                "options": ["bulāiye", "jāiye", "baithiye"],
                "correctAnswer": "bulāiye",
                "transliterationIsoTarget": "Doctor ko bulāiye!",
                "explanationRu": "Bulāiye = позовите."
            },
            {
                "id": "d37_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Спросите: 'Есть ли здесь лекарство от боли?'",
                "prompt": "Kyā dard kī _____ hai? (Лекарство от боли)",
                "options": ["davā", "chāi", "thailī"],
                "correctAnswer": "davā",
                "transliterationIsoTarget": "Kyā dard kī davā hai?",
                "explanationRu": "Davā = лекарство."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Обращение к администратору отеля при отравлении",
            "setting": "Ресепшн отеля поздно вечером",
            "partnerRoleRu": "Ночной портье",
            "learnerRoleRu": "Заболевшая постоялица",
            "turns": [
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Брат, помогите пожалуйста! Мне очень нездоровится.",
                    "speechIso": "Bhaiyā, madad kījiye! Mērī tabīyat bahut kharāb hai.",
                    "speechCyrillic": "Бхаййаа, мадад кииджие! Мерии табиийат бахут харааб хэ.",
                    "learnerHintRu": "Сообщите о болезни: Mērī tabīyat bahut kharāb hai"
                },
                {
                    "speaker": "Портье",
                    "speechRu": "О господи! Что болит, мадам? Температура или живот?",
                    "speechIso": "Oh! Kyā huā madam? Pēṭ dard hai?",
                    "speechCyrillic": "Ох! Кйаа хуаа мадам? Пеет͟ дард хэ?",
                    "learnerHintRu": "Скажите: Да, сильная боль в животе. Позовите врача или дайте лекарство! (Pēṭ dard hai. Doctor ko bulāiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Да, сильно болит живот. Пожалуйста, вызовите доктора или аптекаря.",
                    "speechIso": "Hā̃, bahut pēṭ dard hai. Doctor ko bulāiye, please!",
                    "speechCyrillic": "Хааⁿ, бахут пеет͟ дард хэ. Доктор ко булааие, плииз!",
                    "acceptableResponsesIso": ["Doctor ko bulāiye!", "Pēṭ dard hai, davā chāhiye."]
                },
                {
                    "speaker": "Портье",
                    "speechRu": "Сейчас же вызываю врача из соседней клиники! Присядьте здесь, выпейте воды.",
                    "speechIso": "Abhī doctor ko bulātā hū̃. Yahā̃ baithiye, pānī lījiye.",
                    "speechCyrillic": "Абхии доктор ко булаатаа хууⁿ. Йахааⁿ бэтхие, паании лииджие.",
                    "learnerHintRu": "Поблагодарите: Bahut shukriyā bhaiyā!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Спасибо огромное, брат!",
                    "speechIso": "Bahut shukriyā bhaiyā!",
                    "speechCyrillic": "Бахут шукрийа бхаййаа!",
                    "acceptableResponsesIso": ["Shukriyā jī!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Медицинская взаимопомощь в Индии",
            "pointsRu": [
                "Индийцы невероятно сердобольны и отзывчивы к заболевшим гостям: вам немедленно вызовут врача, принесут горячий отвар и купят лекарства.",
                "Фраза 'Mērī tabīyat kharāb hai' поднимает на ноги весь персонал отеля за 30 секунд.",
                "Аптекари (chemists) в Индии часто обладают квалификацией фельдшера и могут выдать эффективное средство от расстройства желудка прямо у стойки."
            ]
        }
    },

    # Day 38
    {
        "day": 38,
        "phase": 5,
        "title": {
            "en": "Social Etiquette, Compliments, and Small Talk",
            "ru": "Социальный этикет и комплименты: «Мне очень нравится Индия»"
        },
        "theme": "Индия (Bhārat), мне нравится Индия (Mujhē Bhārat bahut pasand hai), люди здесь прекрасные (yahā̃ kē log bahut acchē haiñ), красивый (sundar)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция придыхательного bh в Bhārat и звука sundar)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Конструкция притяжательного локатива: Yahā̃ kē log = Люди здешние / Люди отсюда)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Искренние комплименты стране, культуре, архитектуре и людям)",
            "phase4SimulationMinutes": "17:00–20:00 (Душевная беседа с попутчиками или хозяевами дома)"
        },
        "learningObjectives": {
            "en": [
                "Exchange social pleasantries and compliments with 'Mujhē Bhārat bahut pasand hai'",
                "Praise hospitality and people using 'Yahā̃ kē log bahut acchē haiñ'",
                "Describe visual beauty with sundar (beautiful)"
            ],
            "ru": [
                "Обмениваться светскими любезностями и делать комплименты: 'Mujhē Bhārat bahut pasand hai' ('Мне очень нравится Индия')",
                "Хвалить местных жителей и гостеприимство: 'Yahā̃ kē log bahut acchē haiñ' ('Люди здесь очень добрые/хорошие')",
                "Описывать красоту словом sundar ('красивый / прекрасный')"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Звонкий придыхательный /bh/ в исконном названии страны Bhārat (भारत)",
            "articulatoryMechanism": "Губы смыкаются для звука [б] и раскрываются с мощным теплым голосовым выдохом [бх] + долгое [аа]: [бхаа-рат].",
            "russianInterferenceWarning": "Не произносите плоское [барат]. Это священное имя страны, оно требует глубокого выдоха.",
            "drills": [
                {
                    "prompt": "Произнесение названия страны",
                    "contrastPair": "Bhārat (Индия)",
                    "instructionsRu": "Произнесите с придыханием: Bhārat bahut sundar hai."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Притяжательный послелог kē с локативом (Yahā̃ kē log)",
            "russianParallel": "Фраза 'Yahā̃ kē log' буквально переводится: 'Здешние люди / Люди этого места' (yahā̃ = здесь, kē = притяжательное множественного числа, log = люди, народ). Порядок предикативного комплимента точно как в русском: Индия очень красивая = Bhārat bahut sundar hai.",
            "syntacticFormula": "[Объект] + bahut sundar hai | Yahā̃ kē log bahut acchē haiñ",
            "explanationRu": "Использование самоназвания 'Bhārat' вместо английского 'India' производит фурор среди местных жителей. Это показывает искреннее уважение к культуре.",
            "pieCognateConnection": {
                "root": "*bʰer- / *sem-",
                "russian": "брать / беречь // сам / семья",
                "hindi": "bhārat (поддерживаемый / несущий свет) / sundar (ладный, красивый)",
                "meaning": "Индоевропейская гармония и созидание"
            }
        },
        "vocabulary": [
            {
                "id": "d38_v01",
                "devanagari": "भारत",
                "transliterationIso": "Bhārat",
                "phoneticCyrillic": "Бхаарат",
                "translationRu": "Индия (официальное самоназвание)",
                "translationEn": "India (endonym)",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Придыхательное [бх]."
            },
            {
                "id": "d38_v02",
                "devanagari": "सुंदर",
                "transliterationIso": "Sundar",
                "phoneticCyrillic": "Сундар",
                "translationRu": "Красивый / Прекрасный",
                "translationEn": "Beautiful",
                "partOfSpeech": "adjective",
                "gender": "both",
                "audioHint": "Ударение на первый слог."
            },
            {
                "id": "d38_v03",
                "devanagari": "लोग",
                "transliterationIso": "Log",
                "phoneticCyrillic": "Лог",
                "translationRu": "Люди / Народ",
                "translationEn": "People",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Чистый гласный 'о'."
            },
            {
                "id": "d38_v04",
                "devanagari": "यहाँ के लोग",
                "transliterationIso": "Yahā̃ kē log",
                "phoneticCyrillic": "Йахааⁿ ке лог",
                "translationRu": "Здешние люди / Люди здесь",
                "translationEn": "People here",
                "partOfSpeech": "phrase",
                "gender": "m",
                "audioHint": "Притяжательная форма."
            }
        ],
        "exercises": [
            {
                "id": "d38_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите душевный комплимент: 'Люди здесь очень хорошие!'",
                "prompt": "Люди здесь очень хорошие",
                "wordChips": ["Yahā̃", "kē", "log", "bahut", "acchē", "haiñ"],
                "correctAnswer": ["Yahā̃", "kē", "log", "bahut", "acchē", "haiñ"],
                "phoneticCyrillicTarget": "Йахааⁿ ке лог бахут аччхээ хэⁿ",
                "explanationRu": "Yahā̃ kē log (люди здесь) + bahut acchē haiñ (очень хорошие)."
            },
            {
                "id": "d38_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Собеседник спрашивает: 'India kaisā lagā?' (Как вам Индия?). Ответьте за 2 секунды с теплотой!",
                "prompt": "Как вам Индия?",
                "options": [
                    "Mujhē Bhārat bahut pasand hai! Bahut sundar hai!",
                    "Mujhē bilkul pasand nahī̃ hai!",
                    "Main station par hū̃!"
                ],
                "correctAnswer": "Mujhē Bhārat bahut pasand hai! Bahut sundar hai!",
                "phoneticCyrillicTarget": "Муджхе Бхаарат бахут пасанд хэ! Бахут сундар хэ!",
                "explanationRu": "Мне очень нравится Индия! Очень красиво!"
            },
            {
                "id": "d38_ex03",
                "type": "substitution_drill",
                "instructionRu": "Сделайте комплимент храму или дворцу: 'Это здание очень красивое'",
                "prompt": "Yeh bahut _____ hai. (Красивое)",
                "options": ["sundar", "kharāb", "tīkhā"],
                "correctAnswer": "sundar",
                "transliterationIsoTarget": "Yeh bahut sundar hai.",
                "explanationRu": "Sundar = красивый."
            },
            {
                "id": "d38_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Сделайте комплимент доброму собеседнику: 'Вы очень хороший человек'",
                "prompt": "Āp bahut _____ haiñ. (Вы очень хороший)",
                "options": ["acchē", "sundar", "garam"],
                "correctAnswer": "acchē",
                "transliterationIsoTarget": "Āp bahut acchē haiñ.",
                "explanationRu": "Āp bahut acchē haiñ = Вы очень добрый/хороший."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Вечерний разговор на террасе с индийской семьей",
            "setting": "Терраса с видом на закат над Гангом или дворцами",
            "partnerRoleRu": "Глава семьи",
            "learnerRoleRu": "Вдохновленная гостья",
            "turns": [
                {
                    "speaker": "Глава семьи",
                    "speechRu": "Добрый вечер, сестра! Как вам наш город и наша страна?",
                    "speechIso": "Namastē madam! Hamārā shahar aur desh kaisā lagā?",
                    "speechCyrillic": "Намастэ мадам! Хамаараа шахар аур дэш кэсаа лагаа?",
                    "learnerHintRu": "Скажите: Мне очень нравится Индия. Здесь очень красиво! (Mujhē Bhārat bahut pasand hai)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Мне очень нравится Индия! Страна необычайно красивая.",
                    "speechIso": "Mujhē Bhārat bahut pasand hai! Bahut sundar desh hai.",
                    "speechCyrillic": "Муджхе Бхаарат бахут пасанд хэ! Бахут сундар дэш хэ.",
                    "acceptableResponsesIso": ["Mujhē Bhārat bahut pasand hai!"]
                },
                {
                    "speaker": "Глава семьи",
                    "speechRu": "А как вам наши люди? Никто вас не обижает?",
                    "speechIso": "Aur yahā̃ kē log kaisē haiñ?",
                    "speechCyrillic": "Аур йахааⁿ ке лог кэсе хэⁿ?",
                    "learnerHintRu": "Ответьте с теплотой: Люди здесь очень добрые и гостеприимные! (Yahā̃ kē log bahut acchē haiñ)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Люди здесь очень добрые и душевные! Вы все очень хорошие.",
                    "speechIso": "Yahā̃ kē log bahut acchē haiñ! Āp sab bahut acchē haiñ.",
                    "speechCyrillic": "Йахааⁿ ке лог бахут аччхээ хэⁿ! Аап саб бахут аччхээ хэⁿ.",
                    "acceptableResponsesIso": ["Yahā̃ kē log bahut acchē haiñ!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Культура комплиментов и сердечность",
            "pointsRu": [
                "Индийцы необычайно чувствительны к искренней любви к их родине.",
                "Фраза 'Yahā̃ kē log bahut acchē haiñ' часто растрогает пожилых людей до слез благословения.",
                "Делая комплимент дому или детям, не забывайте улыбаться и слегка прикладывать правую руку к сердцу."
            ]
        }
    },

    # Day 39
    {
        "day": 39,
        "phase": 5,
        "title": {
            "en": "Travel Disruptions: Delays and Lost Property",
            "ru": "Нештатные ситуации: задержка рейса (Dērī) и потеря багажа (Khō gayā)"
        },
        "theme": "Потерялся (khō gayā/gayī - аналог русского возвратного 'потерялся'), моя сумка потерялась (mērā bag khō gayā hai), задержка (dērī), поезд опаздывает? (kyā train late hai?)",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Артикуляция возвратного прошедшего времени khō gayā / khō gayī)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Сходство с русским возвратным суффиксом -ся: потерял-ся = khō gayā)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Подача заявлений: сумка потерялась, паспорт потерялся, поезд задерживается)",
            "phase4SimulationMinutes": "17:00–20:00 (Обращение в бюро находок или к начальнику вокзала)"
        },
        "learningObjectives": {
            "en": [
                "Report lost belongings using intransitive past 'khō gayā (m) / khō gayī (f)'",
                "Inquire about transit delays using dērī or late (Kyā train late hai?)",
                "Demand administrative tracing at lost-and-found counters calmly"
            ],
            "ru": [
                "Заявлять об утере вещей через форму непереходного прошедшего: 'khō gayā' (м.р.) / 'khō gayī' (ж.р.) (аналог русского 'потерялся / пропал')",
                "Спрашивать о задержках транспорта: 'Dērī' или 'Late' (Kyā train late hai?)",
                "Взаимодействовать со службами вокзала и аэропорта без паники"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Придыхательный велярный /kh/ в глаголе khōnā (खोना) -> khō gayā",
            "articulatoryMechanism": "Мощный легочный выдох [кх] с чистым полузакрытым [оо], за которым следует звонкий звук [гайаа]: [кхоо гайаа].",
            "russianInterferenceWarning": "Не превращайте в русское 'когая'. Должно звучать четкое придыхательное [кх].",
            "drills": [
                {
                    "prompt": "Отработка утери предмета",
                    "contrastPair": "Mērā bag khō gayā hai (Моя сумка потерялась)",
                    "instructionsRu": "Произнесите связку с тревожной, но четкой интонацией."
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Непереходные глаголы изменения состояния (Русские глаголы на -ся)",
            "russianParallel": "В русском языке мы говорим: 'Чемодан потерялся / пропал' (действие произошло само, субъект не виноват). В хинди используется сложный результативный глагол: Khō (терять) + gayā (ушел) = Khō gayā (Потерялся/пропал). Мужской род: Mērā bag khō gayā hai; Женский род: Mērī kitāb khō gayī hai.",
            "syntacticFormula": "[Mērā/Mērī + Предмет] + [khō gayā (м.р.) / khō gayī (ж.р.)] + hai",
            "explanationRu": "Эта конструкция снимает с вас вину (вы не говорите 'я потеряла', а констатируете, что вещь 'сама пропала'). В индийских реалиях это идеальная формулировка для поиска.",
            "pieCognateConnection": {
                "root": "*gʷā- / *gʷem-",
                "russian": "гатить / путь",
                "hindi": "jānā (gayā - ушел)",
                "meaning": "Праиндоевропейское перемещение и исчезновение"
            }
        },
        "vocabulary": [
            {
                "id": "d39_v01",
                "devanagari": "खो गया / खो गई",
                "transliterationIso": "Khō gayā (m) / Khō gayī (f)",
                "phoneticCyrillic": "Кхоо гайаа / Кхоо гайии",
                "translationRu": "Потерялся / Потерялась (пропал)",
                "translationEn": "Lost / Disappeared",
                "partOfSpeech": "verb",
                "gender": "both",
                "audioHint": "Результативный глагол утери."
            },
            {
                "id": "d39_v02",
                "devanagari": "देरी",
                "transliterationIso": "Dērī / Late",
                "phoneticCyrillic": "Дээрии / Лэйт",
                "translationRu": "Задержка / Опоздание",
                "translationEn": "Delay / Late",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Долгое 'ээ' и 'ии'."
            },
            {
                "id": "d39_v03",
                "devanagari": "समय",
                "transliterationIso": "Samay",
                "phoneticCyrillic": "Самай",
                "translationRu": "Время / Срок",
                "translationEn": "Time",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Санскритское слово времени."
            }
        ],
        "exercises": [
            {
                "id": "d39_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите экстренное заявление: 'Извините, моя сумка потерялась!'",
                "prompt": "Моя сумка потерялась",
                "wordChips": ["Māf", "kījiye,", "mērā", "bag", "khō", "gayā", "hai!"],
                "correctAnswer": ["Māf", "kījiye,", "mērā", "bag", "khō", "gayā", "hai!"],
                "phoneticCyrillicTarget": "Мааф кииджие, мераа бэг кхоо гайаа хэ!",
                "explanationRu": "Mērā bag khō gayā hai = Моя сумка потерялась."
            },
            {
                "id": "d39_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Поезд задерживается на табло. Спросите дежурного за 2 секунды: 'Поезд опаздывает?'",
                "prompt": "Поезд задерживается?",
                "options": [
                    "Bhaiyā, kyā train late hai?",
                    "Train bahut svādishṭ hai!",
                    "Khānā khō gayā hai!"
                ],
                "correctAnswer": "Bhaiyā, kyā train late hai?",
                "phoneticCyrillicTarget": "Бхаййаа, кйаа трэйн лэйт хэ?",
                "explanationRu": "Kyā train late hai? — стандартный вопрос на вокзале."
            },
            {
                "id": "d39_ex03",
                "type": "substitution_drill",
                "instructionRu": "Сообщите, что потерялся паспорт (мужской род)",
                "prompt": "Mērā passport _____ hai.",
                "options": ["khō gayā", "khō gayī", "khānā"],
                "correctAnswer": "khō gayā",
                "transliterationIsoTarget": "Mērā passport khō gayā hai.",
                "explanationRu": "Passport мужского рода, поэтому khō gayā."
            },
            {
                "id": "d39_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Спросите о причине задержки рейса",
                "prompt": "Kitnī _____ hai? (Какая задержка?)",
                "options": ["dērī", "chāi", "thailī"],
                "correctAnswer": "dērī",
                "transliterationIsoTarget": "Kitnī dērī hai?",
                "explanationRu": "Dērī = задержка / опоздание."
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Заявление о забытом рюкзаке в бюро находок вокзала",
            "setting": "Офис начальника вокзала (Station Master Office)",
            "partnerRoleRu": "Дежурный офицер вокзала",
            "learnerRoleRu": "Встревоженная пассажирка",
            "turns": [
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте, сэр! Помогите пожалуйста, мой рюкзак потерялся в вагоне.",
                    "speechIso": "Namastē sir! Madad kījiye, mērā bag coach mẽ khō gayā hai.",
                    "speechCyrillic": "Намастэ сэр! Мадад кииджие, мераа бэг коуч мэⁿ кхоо гайаа хэ.",
                    "learnerHintRu": "Заявите о пропаже: Mērā bag khō gayā hai"
                },
                {
                    "speaker": "Офицер",
                    "speechRu": "Спокойно, мадам! Какой номер поезда и какой вагон?",
                    "speechIso": "Chintā mat kījiye madam! Train number aur coach kyā hai?",
                    "speechCyrillic": "Чинтаа мат кииджие мадам! Трэйн намбар аур коуч кйаа хэ?",
                    "learnerHintRu": "Назовите номер и цвет: Train 12002, blue bag hai. Помогите найти! (Madad kījiye)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Поезд Shatabdi, синий рюкзак. Там паспорт и билеты. Помогите!",
                    "speechIso": "Train Shatabdi, blue bag hai. Passport vahā̃ hai. Madad kījiye!",
                    "speechCyrillic": "Трэйн Шатабди, блю бэг хэ. Паспорт вахааⁿ хэ. Мадад кииджие!",
                    "acceptableResponsesIso": ["Blue bag khō gayā hai. Madad kījiye!"]
                },
                {
                    "speaker": "Офицер",
                    "speechRu": "Я прямо сейчас звоню проводнику поезда! Садитесь здесь.",
                    "speechIso": "Main abhī TTE ko call kartā hū̃. Yahā̃ baithiye.",
                    "speechCyrillic": "Мэⁿ абхии Ти-Ти-Ии ко кол картаа хууⁿ. Йахааⁿ бэтхие.",
                    "learnerHintRu": "Поблагодарите с облегчением: Bahut dhanyavād sir!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Большое спасибо, сэр!",
                    "speechIso": "Bahut dhanyavād sir!",
                    "speechCyrillic": "Бахут дханьяваад сэр!",
                    "acceptableResponsesIso": ["Bahut shukriyā!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Разрешение форс-мажоров на транспорте",
            "pointsRu": [
                "На индийской железной дороге работает служба Railway Protection Force (RPF) и дежурные Station Master.",
                "Вежливое обращение на хинди ('Mērā bag khō gayā hai, madad kījiye') включает максимальную вовлеченность дежурных.",
                "Индийские поезда часто задерживаются из-за тумана (зимой на севере) или плотного графика — фраза 'Kitnī dērī hai?' поможет сориентироваться."
            ]
        }
    },

    # Day 40
    {
        "day": 40,
        "phase": 5,
        "title": {
            "en": "Integrated Travel Immersion Capstone",
            "ru": "Финальный интеграционный иммерсив: Большое 20-минутное путешествие по Индии"
        },
        "theme": "Итоговый экзамен из 5 сцен: 1) Такси из аэропорта, 2) Заселение в отель, 3) Заказ в дхабе, 4) Торг на базаре, 5) Прощание",
        "estimatedMinutes": 20,
        "cognitiveTimeAllocation": {
            "phase1WarmupMinutes": "00:00–04:00 (Полный фонетический аудит 40 дней: ретрофлексия, придыхания, носовые гласные)",
            "phase2StructuralCoreMinutes": "04:00–11:00 (Финальная сборка грамматики: SOV, датив состояния, императивы, времена)",
            "phase3ShadowingDrillsMinutes": "11:00–17:00 (Сквозная репетиция 5 сценариев без перевода)",
            "phase4SimulationMinutes": "17:00–20:00 (Финальный 20-минутный иммерсивный диалог без единого слова по-английски!)"
        },
        "learningObjectives": {
            "en": [
                "Complete uninterrupted 20-minute spoken travel simulation entirely in Hindi",
                "Demonstrate spontaneous command of SOV word order, dative experiencers, and numbers",
                "Transition seamlessly across transit, hospitality, dining, bargaining, and social rapport"
            ],
            "ru": [
                "Провести непрерывную 20-минутную иммерсивную симуляцию путешествия строго на хинди",
                "Продемонстрировать спонтанное владение порядком SOV, дативными субъектами (Mujhē chāhiye/pasand) и счетом",
                "Легко переключаться между такси, отелем, рестораном, рыночным торгом и дружеской беседой"
            ]
        },
        "phoneticFocus": {
            "targetSound": "Полная естественная беглость речи и акустическая аутентичность",
            "articulatoryMechanism": "Чистый раскатистый альвеолярный [r], отсутствие редукции гласных (anti-akan'ye), точная ретрофлексия [ṭ, ḍ, ṛ] и взрывное легочное придыхание [kh, th, ph].",
            "russianInterferenceWarning": "Вы говорите свободно! Не бойтесь мелких оговорок рода — коммуникативный успех и уверенность стоят на первом месте.",
            "drills": [
                {
                    "prompt": "Манифест разговорной свободы",
                    "contrastPair": "Main Hindī boltī hū̃! (Я говорю на хинди!)",
                    "instructionsRu": "Произнесите гордо и уверенно: Main Hindī boltī hū̃!"
                }
            ]
        },
        "contrastiveBridge": {
            "grammarConcept": "Триумф прикладной контрастивной лингвистики",
            "russianParallel": "За 40 дней вы превратили общие индоевропейские корни, грамматический род и дативный падеж своего родного русского языка в мощный мотор разговорного хинди. Языковой барьер полностью сломан!",
            "syntacticFormula": "40-Day Mastery: SOV + Dative Experiencers + Polite Directives + Numerical Scaling",
            "explanationRu": "Вы начинали с нуля, а сегодня способны самостоятельно путешествовать по всей Индии, общаться с местными жителями и решать любые жизненные задачи без английского языка.",
            "pieCognateConnection": {
                "root": "*ǵneh₃- / *gʷeyh₃- / *es-",
                "russian": "знать / жить / есмь",
                "hindi": "jānnā / jīnā / hū̃",
                "meaning": "Полное единство языка, жизни и познания"
            }
        },
        "vocabulary": [
            {
                "id": "d40_v01",
                "devanagari": "यात्रा",
                "transliterationIso": "Yātrā",
                "phoneticCyrillic": "Йаатраа",
                "translationRu": "Путешествие / Паломничество",
                "translationEn": "Journey / Travel",
                "partOfSpeech": "noun",
                "gender": "f",
                "audioHint": "Санскритское благословенное слово."
            },
            {
                "id": "d40_v02",
                "devanagari": "शुभ यात्रा",
                "transliterationIso": "Shubh yātrā",
                "phoneticCyrillic": "Шубх йаатраа",
                "translationRu": "Счастливого пути! (Доброго путешествия!)",
                "translationEn": "Bon voyage! / Have a safe journey!",
                "partOfSpeech": "phrase",
                "gender": "f",
                "audioHint": "Традиционное напутствие."
            },
            {
                "id": "d40_v03",
                "devanagari": "मित्र / दोस्त",
                "transliterationIso": "Mitra / Dost",
                "phoneticCyrillic": "Митра / Доост",
                "translationRu": "Друг / Приятель",
                "translationEn": "Friend",
                "partOfSpeech": "noun",
                "gender": "m",
                "audioHint": "Слово дружбы."
            }
        ],
        "exercises": [
            {
                "id": "d40_ex01",
                "type": "word_reorder_sov",
                "instructionRu": "Соберите манифест выпускника курса: 'Я говорю на хинди и очень люблю Индию!'",
                "prompt": "Я говорю на хинди и мне нравится Индия",
                "wordChips": ["Main", "Hindī", "boltī", "hū̃,", "mujhē", "Bhārat", "bahut", "pasand", "hai!"],
                "correctAnswer": ["Main", "Hindī", "boltī", "hū̃,", "mujhē", "Bhārat", "bahut", "pasand", "hai!"],
                "phoneticCyrillicTarget": "Мэⁿ Хиндии болтии хууⁿ, муджхе Бхаарат бахут пасанд хэ!",
                "explanationRu": "Вершина курса: свободное владение речевыми структурами."
            },
            {
                "id": "d40_ex02",
                "type": "rapid_oral_challenge",
                "instructionRu": "Финальный экспресс-тест: таксист пытается завысить цену. Остановите его и потребуйте счетчик!",
                "prompt": "Таксист называет двойную цену",
                "options": [
                    "Bhaiyā nahī̃! Mīṭar chalāo! Sahī dām lagāiye!",
                    "Hā̃, lījiye paisē!",
                    "Khānā tīkhā hai!"
                ],
                "correctAnswer": "Bhaiyā nahī̃! Mīṭar chalāo! Sahī dām lagāiye!",
                "phoneticCyrillicTarget": "Бхаййаа нахииⁿ! Миитар͟ чалаао! Сахии даам лагааие!",
                "explanationRu": "Мгновенное применение речевых формул."
            },
            {
                "id": "d40_ex03",
                "type": "dialogue_roleplay",
                "instructionRu": "Закажите в дхабе горячую еду без перца и закрытую воду",
                "prompt": "Официант: Kyā chāhiye madam?",
                "options": [
                    "Bisleri pānī aur garam dāl chāval, binā mirch kē!",
                    "Main hotel mẽ nahī̃ hū̃!",
                    "Station dūr hai!"
                ],
                "correctAnswer": "Bisleri pānī aur garam dāl chāval, binā mirch kē!",
                "phoneticCyrillicTarget": "Бислери паании аур гарам даал чаавал, бинаа мирч ке!",
                "explanationRu": "Безупречный заказ еды и воды."
            },
            {
                "id": "d40_ex04",
                "type": "fill_in_blank",
                "instructionRu": "Пожелайте друзьям счастливого пути!",
                "prompt": "_____ yātrā! (Счастливого пути)",
                "options": ["Shubh", "Kharāb", "Tīkhā"],
                "correctAnswer": "Shubh",
                "transliterationIsoTarget": "Shubh yātrā!",
                "explanationRu": "Shubh yātrā = Счастливого пути!"
            }
        ],
        "simulationRoleplay": {
            "scenarioTitleRu": "Экзаменационный супер-ролеплей: 5 ключевых ситуаций путешествия",
            "setting": "Непрерывный маршрут: Такси -> Отель -> Дхаба -> Базар -> Прощание",
            "partnerRoleRu": "Экзаменатор / Партнер по учебе (меняет роли)",
            "learnerRoleRu": "Свободно говорящая выпускница курса",
            "turns": [
                {
                    "speaker": "Сцена 1: Таксист",
                    "speechRu": "Куда ехать, мадам?",
                    "speechIso": "Kahā̃ jānā hai madam?",
                    "speechCyrillic": "Кахааⁿ джаанаа хэ мадам?",
                    "learnerHintRu": "Скажите: Брат, нужно в отель Тадж. Включите счетчик! (Bhaiyā, Taj Hotel jānā hai. Mīṭar chalāo)"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Брат, мне нужно в отель Тадж. Включите счетчик, пожалуйста.",
                    "speechIso": "Bhaiyā, Taj Hotel jānā hai. Mīṭar chalāo, please.",
                    "speechCyrillic": "Бхаййаа, Тадж Хотел джаанаа хэ. Миитар͟ чалаао, плииз.",
                    "acceptableResponsesIso": ["Bhaiyā, Taj Hotel jānā hai. Mīṭar chalāo."]
                },
                {
                    "speaker": "Сцена 2: Отель",
                    "speechRu": "Здравствуйте! Меня зовут Радж. Как ваше имя?",
                    "speechIso": "Namastē! Mērā nām Raj hai. Āpkā nām kyā hai?",
                    "speechCyrillic": "Намастэ! Мераа наам Радж хэ. Аапкаа наам кйаа хэ?",
                    "learnerHintRu": "Представьтесь: Namastē jī! Mērā nām Anna hai. Main Russia sē hū̃."
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Здравствуйте! Меня зовут Анна, я приехала из России.",
                    "speechIso": "Namastē jī! Mērā nām Anna hai. Main Russia sē hū̃.",
                    "speechCyrillic": "Намастэ джии! Мераа наам Анна хэ. Мэⁿ Расийа сэ хууⁿ.",
                    "acceptableResponsesIso": ["Mērā nām Anna hai. Main Russia sē hū̃."]
                },
                {
                    "speaker": "Сцена 3: Дхаба",
                    "speechRu": "Что будете кушать?",
                    "speechIso": "Khānē mẽ kyā chāhiye madam?",
                    "speechCyrillic": "Кхаанее мэⁿ кйаа чаахийе мадам?",
                    "learnerHintRu": "Закажите: Dal chāval dījiye, binā mirch kē. Aur packaged pānī!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Дайте дал и рис, пожалуйста, совсем без перца! И бутылку воды Bisleri.",
                    "speechIso": "Dāl aur chāval dījiye, binā mirch kē. Aur ek Bisleri pānī!",
                    "speechCyrillic": "Даал аур чаавал дииджие, бинаа мирч ке. Аур эк Бислери паании!",
                    "acceptableResponsesIso": ["Dāl chāval dījiye, binā mirch kē. Pānī chāhiye."]
                },
                {
                    "speaker": "Сцена 4: Базар",
                    "speechRu": "Красивый сувенир, мадам! Всего восемьсот рупий.",
                    "speechIso": "800 rupayē madam, best price!",
                    "speechCyrillic": "800 рупае мадам, бэст прайс!",
                    "learnerHintRu": "Сбейте цену: Bahut zyādā hai! Sahī dām lagāiye. Chār sau rupayē dījiye!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Слишком много! Назовите честную цену. Отдайте за четыреста рупий!",
                    "speechIso": "Bahut zyādā hai! Sahī dām lagāiye. Chār sau rupayē dījiye!",
                    "speechCyrillic": "Бахут зйаадаа хэ! Сахии даам лагааие. Чаар сау рупае дииджие!",
                    "acceptableResponsesIso": ["Bahut zyādā hai! Chār sau rupayē dījiye!"]
                },
                {
                    "speaker": "Сцена 5: Прощание",
                    "speechRu": "Договорились, забирайте! Вы потрясающе говорите на хинди. Счастливого пути!",
                    "speechIso": "Lījiye madam! Āp bahut acchī Hindī boltī haiñ. Shubh yātrā!",
                    "speechCyrillic": "Лииджие мадам! Аап бахут аччхии Хиндии болтии хэⁿ. Шубх йаатраа!",
                    "learnerHintRu": "Поблагодарите от всего сердца: Bahut dhanyavād jī! Hum phir milēṅgē!"
                },
                {
                    "speaker": "Вы (ученица)",
                    "speechRu": "Большое спасибо от всего сердца! До свидания, мы обязательно снова встретимся!",
                    "speechIso": "Bahut dhanyavād jī! Mujhē Bhārat bahut pasand hai. Hum phir milēṅgē!",
                    "speechCyrillic": "Бахут дханьяваад джии! Муджхе Бхаарат бахут пасанд хэ. Хум пхир милээнгээ!",
                    "acceptableResponsesIso": ["Bahut dhanyavād jī! Hum phir milēṅgē!"]
                }
            ]
        },
        "culturalPragmatics": {
            "titleRu": "Поздравляем с завершением 40-дневного курса!",
            "pointsRu": [
                "Вы проделали грандиозный путь: от нуля до уверенной разговорной речи в реальных жизненных ситуациях.",
                "Вы доказали, что благодаря сопоставительной лингвистике носитель русского языка может освоить хинди быстрее, чем кто-либо в мире.",
                "Индия ждет вас с распростертыми объятиями. Shubh yātrā aur bahut-bahut shukriyā!"
            ]
        }
    }
]
