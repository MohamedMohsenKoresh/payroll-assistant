def normalize_text(text):

    text = text.strip()

    replacements = {

        "الضرايب": "الضريبة",
        "الضريبه": "الضريبة",

        "الاوفر": "الأوفر تايم",
        "الاوفر تام": "الأوفر تايم",
        "الاوفر تيم": "الأوفر تايم",

        "المرتب": "الراتب",
        "القبض": "الراتب",

        "النت": "صافي الراتب",
        "الصافى": "صافي الراتب",
        "الصافي": "صافي الراتب",


        
    }

    for old, new in replacements.items():

        text = text.replace(old, new)

    return text