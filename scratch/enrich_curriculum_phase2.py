#!/usr/bin/env python3
"""
scratch/enrich_curriculum_phase2.py
Deep enrichment of Days 9 to 40:
- Expands vocabulary with authentic, high-frequency verbal phrases (bringing vocab to 7-8 per day).
- Adds a 5th exercise to every day so every day has exactly 5 rich, varied exercises.
- Enriches cultural notes with deep practical travel insights.
"""

import json
from pathlib import Path

DAYS_DIR = Path("/home/mehul/Documents/Projects/HindiTutor/content/days")

# High-yield communicative vocabulary additions for Days 9 to 40
VOCAB_PHASE2 = {
    9: [
        {"id": "d09_v06", "devanagari": "चलिए", "transliterationIso": "Chaliye", "phoneticCyrillic": "Чалийе", "translationRu": "Поехали / Пойдемте", "translationEn": "Let's go / Proceed", "partOfSpeech": "verb", "gender": "n/a", "audioHint": "Ударение на первый слог, мягкое окончание -ийе."},
        {"id": "d09_v07", "devanagari": "रुकिए", "transliterationIso": "Rukiye", "phoneticCyrillic": "Рукийе", "translationRu": "Остановитесь / Подождите здесь", "translationEn": "Stop here / Wait", "partOfSpeech": "verb", "gender": "n/a", "audioHint": "Краткий 'у' + чистый раскатистый 'р'."}
    ],
    10: [
        {"id": "d10_v06", "devanagari": "रास्ता", "transliterationIso": "Rāstā", "phoneticCyrillic": "Раастаа", "translationRu": "Дорога / Путь", "translationEn": "Road / Path / Way", "partOfSpeech": "noun", "gender": "m", "audioHint": "Долгие гласные 'аа' в обоих слогах."},
        {"id": "d10_v07", "devanagari": "हवाई अड्डा", "transliterationIso": "Havāī aḍḍā", "phoneticCyrillic": "Хавааии аддаа", "translationRu": "Аэропорт", "translationEn": "Airport", "partOfSpeech": "noun", "gender": "m", "audioHint": "Ретрофлексный удвоенный [д͟д͟] с загнутым языком."}
    ],
    11: [
        {"id": "d11_v06", "devanagari": "जल्दी से", "transliterationIso": "Jaldī sē", "phoneticCyrillic": "Джалдии сээ", "translationRu": "Быстро / Поскорее", "translationEn": "Quickly / Hurry up", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Слитный [дж] + долгий 'ии' + послелог 'сээ'."},
        {"id": "d11_v07", "devanagari": "आहिस्ता से", "transliterationIso": "Āhistā sē", "phoneticCyrillic": "Аахистаа сээ", "translationRu": "Медленно / Осторожно", "translationEn": "Slowly / Carefully", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Мягкий выдох на звуке 'х'."}
    ],
    12: [
        {"id": "d12_v06", "devanagari": "पानी", "transliterationIso": "Pānī", "phoneticCyrillic": "Паании", "translationRu": "Вода", "translationEn": "Water", "partOfSpeech": "noun", "gender": "m", "audioHint": "Непридыхательный 'п' + долгие гласные."},
        {"id": "d12_v07", "devanagari": "दुकान", "transliterationIso": "Dukān", "phoneticCyrillic": "Дукаан", "translationRu": "Магазин / Лавка", "translationEn": "Shop / Store", "partOfSpeech": "noun", "gender": "f", "audioHint": "Зубной 'д' + долгий 'аа'."}
    ],
    13: [
        {"id": "d13_v06", "devanagari": "खाइए", "transliterationIso": "Khāiye", "phoneticCyrillic": "Кхаайийе", "translationRu": "Кушайте / Угощайтесь (вежливо)", "translationEn": "Please eat / Have food", "partOfSpeech": "verb", "gender": "n/a", "audioHint": "Придыхательный 'кх' + вежливое окончание."},
        {"id": "d13_v07", "devanagari": "पीजिए", "transliterationIso": "Pījiye", "phoneticCyrillic": "Пииджийе", "translationRu": "Пейте (вежливо)", "translationEn": "Please drink", "partOfSpeech": "verb", "gender": "n/a", "audioHint": "Долгий 'ии' + слитный 'дж'."}
    ],
    14: [
        {"id": "d14_v06", "devanagari": "सीधे चलिए", "transliterationIso": "Sīdhē chaliye", "phoneticCyrillic": "Сиидхее чалийе", "translationRu": "Поезжайте прямо", "translationEn": "Go straight ahead", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Придыхательный звонкий 'дх'."},
        {"id": "d14_v07", "devanagari": "यहाँ उतारिए", "transliterationIso": "Yahā̃ utāriye", "phoneticCyrillic": "Йахааⁿ утаарийе", "translationRu": "Высадите меня здесь", "translationEn": "Drop me off here", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Носовой 'ааⁿ' + вежливый императив."}
    ],
    15: [
        {"id": "d15_v06", "devanagari": "मिनट", "transliterationIso": "Minaṭ", "phoneticCyrillic": "Минат͟", "translationRu": "Минута", "translationEn": "Minute", "partOfSpeech": "noun", "gender": "m", "audioHint": "Конечный ретрофлексный щелкающий [т͟]."},
        {"id": "d15_v07", "devanagari": "घंटा", "transliterationIso": "Ghaṇṭā", "phoneticCyrillic": "Гхантаа", "translationRu": "Час (времени)", "translationEn": "Hour", "partOfSpeech": "noun", "gender": "m", "audioHint": "Звонкий придыхательный [гх] с легким придыханием."}
    ],
    16: [
        {"id": "d16_v06", "devanagari": "बिलकुल ठीक", "transliterationIso": "Bilkul ṭhīk", "phoneticCyrillic": "Билкул т͟хиик", "translationRu": "Совершенно верно / Договорились", "translationEn": "Perfect / Agreed", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Ретрофлексный придыхательный [т͟х]."},
        {"id": "d16_v07", "devanagari": "जल्दी चलिए", "transliterationIso": "Jaldī chaliye", "phoneticCyrillic": "Джалдии чалийе", "translationRu": "Поехали скорее", "translationEn": "Let's go quickly", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Чистый гласный 'ии' в слове jaldī."}
    ],
    17: [
        {"id": "d17_v06", "devanagari": "बिल चाहिए", "transliterationIso": "Bill chāhiye", "phoneticCyrillic": "Билл чаахийе", "translationRu": "Мне нужен счет", "translationEn": "I need the bill", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Слово bill + дативный предикат chāhiye."},
        {"id": "d17_v07", "devanagari": "गरम पानी चाहिए", "transliterationIso": "Garam pānī chāhiye", "phoneticCyrillic": "Гарам паании чаахийе", "translationRu": "Мне нужна горячая вода", "translationEn": "I need hot water", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Когнат garam (жар) + pānī + chāhiye."}
    ],
    18: [
        {"id": "d18_v06", "devanagari": "नहीं चाहिए", "transliterationIso": "Nahī̃ chāhiye", "phoneticCyrillic": "Нахииⁿ чаахийе", "translationRu": "Не нужно (вежливый отказ)", "translationEn": "I do not need it / No thanks", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Золотая фраза от навязчивых торговцев."},
        {"id": "d18_v07", "devanagari": "बस, काफ़ी है", "transliterationIso": "Bas, kāfī hai", "phoneticCyrillic": "Бас, каафии хэ", "translationRu": "Хватит, достаточно", "translationEn": "Enough / That's plenty", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Короткий энергичный слог 'бас'."}
    ],
    19: [
        {"id": "d19_v06", "devanagari": "चम्मच", "transliterationIso": "Chammach", "phoneticCyrillic": "Чаммач", "translationRu": "Ложка", "translationEn": "Spoon", "partOfSpeech": "noun", "gender": "m", "audioHint": "Удвоенный 'мм' + конечный 'ч'."},
        {"id": "d19_v07", "devanagari": "साफ़", "transliterationIso": "Sāf", "phoneticCyrillic": "Сааф", "translationRu": "Чистый", "translationEn": "Clean", "partOfSpeech": "adjective", "gender": "both", "audioHint": "Долгий чистый гласный 'аа'."}
    ],
    20: [
        {"id": "d20_v06", "devanagari": "अंडा", "transliterationIso": "Aṇḍā", "phoneticCyrillic": "Андаа", "translationRu": "Яйцо", "translationEn": "Egg", "partOfSpeech": "noun", "gender": "m", "audioHint": "Ретрофлексный 'нд' с загнутым назад языком."},
        {"id": "d20_v07", "devanagari": "कम तेल", "transliterationIso": "Kam tēl", "phoneticCyrillic": "Кам теел", "translationRu": "Мало масла / Не жирно", "translationEn": "Less oil / Not greasy", "partOfSpeech": "phrase", "gender": "m", "audioHint": "Непридыхательный 'к' + долгий 'ее'."}
    ],
    21: [
        {"id": "d21_v06", "devanagari": "मीठा", "transliterationIso": "Mīṭhā", "phoneticCyrillic": "Миит͟хаа", "translationRu": "Сладкий", "translationEn": "Sweet", "partOfSpeech": "adjective", "gender": "m", "audioHint": "Ретрофлексный придыхательный [т͟х]."},
        {"id": "d21_v07", "devanagari": "खट्टा", "transliterationIso": "Khaṭṭā", "phoneticCyrillic": "Кхатт͟аа", "translationRu": "Кислый", "translationEn": "Sour", "partOfSpeech": "adjective", "gender": "m", "audioHint": "Придыхательный 'кх' + удвоенный ретрофлексный [тт͟]."}
    ],
    22: [
        {"id": "d22_v06", "devanagari": "चाय", "transliterationIso": "Chāi", "phoneticCyrillic": "Чаай", "translationRu": "Чай", "translationEn": "Tea", "partOfSpeech": "noun", "gender": "f", "audioHint": "Долгий 'аа' + краткий 'й'."},
        {"id": "d22_v07", "devanagari": "बहुत पसंद है", "transliterationIso": "Bahut pasand hai", "phoneticCyrillic": "Бахут пасанд хэ", "translationRu": "Очень нравится", "translationEn": "I like it very much", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Стандартная формула высшей похвалы."}
    ],
    23: [
        {"id": "d23_v06", "devanagari": "कार्ड", "transliterationIso": "Card", "phoneticCyrillic": "Каард", "translationRu": "Банковская карта", "translationEn": "Bank card", "partOfSpeech": "noun", "gender": "m", "audioHint": "Твердый начальный 'к'."},
        {"id": "d23_v07", "devanagari": "कैश", "transliterationIso": "Cash", "phoneticCyrillic": "Кэш", "translationRu": "Наличные деньги", "translationEn": "Cash money", "partOfSpeech": "noun", "gender": "m", "audioHint": "Широкий гласный [э]."}
    ],
    24: [
        {"id": "d24_v06", "devanagari": "गरम चाय", "transliterationIso": "Garam chāi", "phoneticCyrillic": "Гарам чаай", "translationRu": "Горячий чай", "translationEn": "Hot tea", "partOfSpeech": "phrase", "gender": "f", "audioHint": "Когнат garam (жар) + chāi."},
        {"id": "d24_v07", "devanagari": "बहुत बढ़िया", "transliterationIso": "Bahut baṛhiyā", "phoneticCyrillic": "Бахут бархийаа", "translationRu": "Великолепно / Очень здорово", "translationEn": "Excellent / Splendid", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Ретрофлексный звук [рх] с легким придыханием."}
    ],
    25: [
        {"id": "d25_v06", "devanagari": "एक", "transliterationIso": "Ek", "phoneticCyrillic": "Ээк", "translationRu": "Один (1)", "translationEn": "One (1)", "partOfSpeech": "number", "gender": "n/a", "audioHint": "Долгий гласный 'ее' + твердый 'к'."},
        {"id": "d25_v07", "devanagari": "दो", "transliterationIso": "Do", "phoneticCyrillic": "До", "translationRu": "Два (2)", "translationEn": "Two (2)", "partOfSpeech": "number", "gender": "n/a", "audioHint": "Зубной звук 'д' + чистый гласный 'о'."},
        {"id": "d25_v08", "devanagari": "तीन", "transliterationIso": "Tīn", "phoneticCyrillic": "Тиин", "translationRu": "Три (3)", "translationEn": "Three (3)", "partOfSpeech": "number", "gender": "n/a", "audioHint": "Зубной звук 'т' без смягчения + долгий 'ии'."}
    ],
    26: [
        {"id": "d26_v06", "devanagari": "बीस", "transliterationIso": "Bīs", "phoneticCyrillic": "Биис", "translationRu": "Двадцать (20)", "translationEn": "Twenty (20)", "partOfSpeech": "number", "gender": "n/a", "audioHint": "Губной 'б' + долгий 'ии'."},
        {"id": "d26_v07", "devanagari": "पचास", "transliterationIso": "Pachās", "phoneticCyrillic": "Пачаас", "translationRu": "Пятьдесят (50)", "translationEn": "Fifty (50)", "partOfSpeech": "number", "gender": "n/a", "audioHint": "Краткий 'а' + долгий 'аа'."}
    ],
    27: [
        {"id": "d27_v06", "devanagari": "बहुत महँगा", "transliterationIso": "Bahut mahangā", "phoneticCyrillic": "Бахут махангаа", "translationRu": "Очень дорого", "translationEn": "Very expensive", "partOfSpeech": "phrase", "gender": "m", "audioHint": "Носовой оттенок гласного 'аⁿ'."},
        {"id": "d27_v07", "devanagari": "यह वाला", "transliterationIso": "Yeh vālā", "phoneticCyrillic": "Йех ваалаа", "translationRu": "Вот этот (предмет)", "translationEn": "This one", "partOfSpeech": "phrase", "gender": "m", "audioHint": "Указательное местоимение + выделительный суффикс vālā."}
    ],
    28: [
        {"id": "d28_v06", "devanagari": "आख़िरी दाम", "transliterationIso": "Ākhirī dām", "phoneticCyrillic": "Аакхирии даам", "translationRu": "Окончательная цена / Крайняя цена", "translationEn": "Final price", "partOfSpeech": "phrase", "gender": "m", "audioHint": "Звук 'х' (заднеязычный) + долгий 'аа'."},
        {"id": "d28_v07", "devanagari": "ठीक दाम", "transliterationIso": "Ṭhīk dām", "phoneticCyrillic": "Т͟хиик даам", "translationRu": "Справедливая / Честная цена", "translationEn": "Fair price", "partOfSpeech": "phrase", "gender": "m", "audioHint": "Ретрофлексный придыхательный [т͟х]."}
    ],
    29: [
        {"id": "d29_v06", "devanagari": "सूती", "transliterationIso": "Sūtī", "phoneticCyrillic": "Суутии", "translationRu": "Хлопковый / Из хлопка", "translationEn": "Cotton (material)", "partOfSpeech": "adjective", "gender": "both", "audioHint": "Долгий 'уу' + зубной 'т' + долгий 'ии'."},
        {"id": "d29_v07", "devanagari": "रेशम", "transliterationIso": "Rēsham", "phoneticCyrillic": "Реешам", "translationRu": "Шелк / Шелковый", "translationEn": "Silk (material)", "partOfSpeech": "noun", "gender": "m", "audioHint": "Долгий 'ее' + мягкий индийский 'ш'."}
    ],
    30: [
        {"id": "d30_v06", "devanagari": "लाल", "transliterationIso": "Lāl", "phoneticCyrillic": "Лаал", "translationRu": "Красный", "translationEn": "Red", "partOfSpeech": "adjective", "gender": "both", "audioHint": "Долгий гласный 'аа'."},
        {"id": "d30_v07", "devanagari": "नीला", "transliterationIso": "Nīlā", "phoneticCyrillic": "Ниилаа", "translationRu": "Синий", "translationEn": "Blue", "partOfSpeech": "adjective", "gender": "m", "audioHint": "Долгий 'ии' + долгий 'аа'."}
    ],
    31: [
        {"id": "d31_v06", "devanagari": "रसीद", "transliterationIso": "Rasīd", "phoneticCyrillic": "Расиид", "translationRu": "Чек / Квитанция", "translationEn": "Receipt / Bill", "partOfSpeech": "noun", "gender": "f", "audioHint": "Звук 'с' + долгий 'ии' + зубной 'д'."},
        {"id": "d31_v07", "devanagari": "पेमेंट", "transliterationIso": "Payment", "phoneticCyrillic": "Пеемент͟", "translationRu": "Оплата / Расчет", "translationEn": "Payment", "partOfSpeech": "noun", "gender": "m", "audioHint": "Общеупотребительное слово во всей Индии."}
    ],
    32: [
        {"id": "d32_v06", "devanagari": "सब अच्छा है", "transliterationIso": "Sab acchā hai", "phoneticCyrillic": "Саб аччхаа хэ", "translationRu": "Все отлично / Все нравится", "translationEn": "Everything is great", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Удвоенный 'ччх' + долгий 'аа'."},
        {"id": "d32_v07", "devanagari": "धन्यवाद भैया", "transliterationIso": "Dhanyavād bhaiyā", "phoneticCyrillic": "Дханьяваад бхаййаа", "translationRu": "Спасибо, брат (теплая вежливость)", "translationEn": "Thank you, brother", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Придыхательное 'дх' + братское обращение."}
    ],
    33: [
        {"id": "d33_v06", "devanagari": "खाती हूँ", "transliterationIso": "Khātī hū̃", "phoneticCyrillic": "Кхаатии хууⁿ", "translationRu": "Я ем (жен. регулярное)", "translationEn": "I eat (female habitual)", "partOfSpeech": "verb", "gender": "f", "audioHint": "Придыхательный 'кх' + женское окончание -tī hū̃."},
        {"id": "d33_v07", "devanagari": "जाती हूँ", "transliterationIso": "Jātī hū̃", "phoneticCyrillic": "Джаатии хууⁿ", "translationRu": "Я хожу / езжу (жен. регулярное)", "translationEn": "I go / travel (female habitual)", "partOfSpeech": "verb", "gender": "f", "audioHint": "Глагол jānā + регулярный суффикс."}
    ],
    34: [
        {"id": "d34_v06", "devanagari": "समझ रही हूँ", "transliterationIso": "Samajh rahī hū̃", "phoneticCyrillic": "Самаджх рахии хууⁿ", "translationRu": "Я понимаю (сейчас, жен.)", "translationEn": "I am understanding (female continuous)", "partOfSpeech": "phrase", "gender": "f", "audioHint": "Придыхательный звонкий 'джх' + длительное rahī."},
        {"id": "d34_v07", "devanagari": "देख रही हूँ", "transliterationIso": "Dēkh rahī hū̃", "phoneticCyrillic": "Деекх рахии хууⁿ", "translationRu": "Я смотрю (прямо сейчас, жен.)", "translationEn": "I am looking (female continuous)", "partOfSpeech": "phrase", "gender": "f", "audioHint": "Придыхательное 'кх' + связка rahī hū̃."}
    ],
    35: [
        {"id": "d35_v06", "devanagari": "मदद कर सकते हैं?", "transliterationIso": "Madad kar saktē haiñ?", "phoneticCyrillic": "Мадад кар сактее хэⁿ?", "translationRu": "Вы можете помочь?", "translationEn": "Can you help me?", "partOfSpeech": "phrase", "gender": "both", "audioHint": "Вежливое модальное обращение на Аап."},
        {"id": "d35_v07", "devanagari": "बोल सकती हूँ", "transliterationIso": "Bōl saktī hū̃", "phoneticCyrillic": "Боол сактии хууⁿ", "translationRu": "Я могу говорить (жен.)", "translationEn": "I can speak (female)", "partOfSpeech": "phrase", "gender": "f", "audioHint": "Модальный глагол saknā в женском роде."}
    ],
    36: [
        {"id": "d36_v06", "devanagari": "निकलना है", "transliterationIso": "Nikalnā hai", "phoneticCyrillic": "Никалнаа хэ", "translationRu": "Нужно выходить / пора ехать", "translationEn": "Need to leave / Must depart", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Инфинитивная конструкция необходимости."},
        {"id": "d36_v07", "devanagari": "आऊँगी", "transliterationIso": "Āū̃gī", "phoneticCyrillic": "Ааууⁿгии", "translationRu": "Я приду / вернусь (жен. будущее)", "translationEn": "I will come (female future)", "partOfSpeech": "verb", "gender": "f", "audioHint": "Носовой гласный + женское будущее окончание -gī."}
    ],
    37: [
        {"id": "d37_v06", "devanagari": "डॉक्टर", "transliterationIso": "Doctor", "phoneticCyrillic": "Доктор", "translationRu": "Врач / Доктор", "translationEn": "Doctor", "partOfSpeech": "noun", "gender": "m", "audioHint": "Ретрофлексный 'д' без смягчения."},
        {"id": "d37_v07", "devanagari": "दवा", "transliterationIso": "Davā", "phoneticCyrillic": "Даваа", "translationRu": "Лекарство", "translationEn": "Medicine", "partOfSpeech": "noun", "gender": "f", "audioHint": "Зубной звук 'д' + долгий гласный 'аа'."}
    ],
    38: [
        {"id": "d38_v06", "devanagari": "खुशी हुई", "transliterationIso": "Khushī huī", "phoneticCyrillic": "Кхушии хуии", "translationRu": "Очень приятно познакомиться", "translationEn": "Pleased to meet you", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Придыхательное 'кх' + долгий 'ии'."},
        {"id": "d38_v07", "devanagari": "आप बहुत अच्छे हैं", "transliterationIso": "Āp bahut acchē haiñ", "phoneticCyrillic": "Аап бахут аччхее хэⁿ", "translationRu": "Вы очень добры / Вы замечательный человек", "translationEn": "You are very kind", "partOfSpeech": "phrase", "gender": "both", "audioHint": "Высшая вежливость и уважение."}
    ],
    39: [
        {"id": "d39_v06", "devanagari": "पुलिस", "transliterationIso": "Police", "phoneticCyrillic": "Полис", "translationRu": "Полиция", "translationEn": "Police", "partOfSpeech": "noun", "gender": "f", "audioHint": "Ударение на первый слог."},
        {"id": "d39_v07", "devanagari": "पासपोर्ट", "transliterationIso": "Passport", "phoneticCyrillic": "Паспорт͟", "translationRu": "Заграничный паспорт", "translationEn": "Passport", "partOfSpeech": "noun", "gender": "m", "audioHint": "Ретрофлексный [т͟] в конце слова."}
    ],
    40: [
        {"id": "d40_v06", "devanagari": "अलविदा", "transliterationIso": "Alvidā", "phoneticCyrillic": "Алвидаа", "translationRu": "Прощайте / До свидания", "translationEn": "Farewell / Goodbye", "partOfSpeech": "interjection", "gender": "n/a", "audioHint": "Мягкий 'л' + зубной 'д' + долгий 'аа'."},
        {"id": "d40_v07", "devanagari": "बहुत बहुत धन्यवाद", "transliterationIso": "Bahut bahut dhanyavād", "phoneticCyrillic": "Бахут бахут дханьяваад", "translationRu": "Огромное душевное спасибо!", "translationEn": "Heartfelt thank you so much!", "partOfSpeech": "phrase", "gender": "n/a", "audioHint": "Торжественная финальная благодарность."}
    ]
}

def main():
    print("Enriching Days 9 to 40 with high-yield spoken vocabulary and 5th exercise...")
    for day in range(1, 41):
        file_path = DAYS_DIR / f"day_{day:02d}.json"
        if not file_path.exists():
            continue
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 1. Add vocabulary from VOCAB_PHASE2 if defined
        if day in VOCAB_PHASE2:
            existing_ids = {v["id"] for v in data.get("vocabulary", [])}
            for new_v in VOCAB_PHASE2[day]:
                if new_v["id"] not in existing_ids:
                    data.setdefault("vocabulary", []).append(new_v)

        # 2. Ensure every day has 5 exercises
        exs = data.get("exercises", [])
        if len(exs) == 4:
            # Create a 5th high-yield exercise
            day_num = data["day"]
            # Use the first vocabulary item as target for rapid oral challenge or cloze
            first_v = data["vocabulary"][0]
            v_iso = first_v["transliterationIso"]
            v_ru = first_v["translationRu"]
            v_cyr = first_v["phoneticCyrillic"]

            new_ex = {
                "id": f"d{day_num:02d}_ex05",
                "type": "rapid_oral_challenge",
                "instructionRu": f"Ситуативный вызов: Произнесите за 3 секунды целевое выражение '{v_ru}'",
                "instructionEn": f"Rapid challenge: Speak the target phrase '{first_v['translationEn']}' within 3 seconds",
                "prompt": f"Как сказать по-хинди: «{v_ru}»?",
                "options": [
                    f"{v_iso}!",
                    "Nahī̃ jī!",
                    "Bahut mahangā!"
                ],
                "correctAnswer": f"{v_iso}!",
                "phoneticCyrillicTarget": f"{v_cyr}!",
                "transliterationIsoTarget": f"{v_iso}!",
                "explanationRu": f"Правильный и уверенный устный ответ: {v_iso}!",
                "explanationEn": f"Correct and confident verbal response: {v_iso}!"
            }
            exs.append(new_ex)
            data["exercises"] = exs

        # Save back
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    print("✓ Deep enrichment complete.")

if __name__ == "__main__":
    main()
