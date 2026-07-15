import joblib

from services.text_normalizer import normalize_text


model = joblib.load("models/intent_model.joblib")
vectorizer = joblib.load("models/vectorizer.joblib")


def detect_intent(question):

    normalized_question = normalize_text(question)

    question_vector = vectorizer.transform(
        [normalized_question]
    )

    probabilities = model.predict_proba(
        question_vector
    )[0]

    max_probability = max(probabilities)

    prediction = model.predict(
        question_vector
    )[0]

    return prediction, max_probability