from services.text_normalizer import normalize_text


def extract_entity(question):

    question = normalize_text(question)

    entities = {
        "tax": [
            "الضريبة"
        ],
        "bonus": [
            "البونص"
        ],
        "overtime": [
            "الأوفر تايم"
        ],
        "deductions": [
            "الخصومات",
            "الخصم"
        ],
        "salary": [
            "الراتب",
            "صافي الراتب"
        ]
    }

    for entity, keywords in entities.items():

        for keyword in keywords:

            if keyword in question:

                return entity

    return None