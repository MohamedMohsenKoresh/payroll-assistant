from services.data_loader import load_data
from services.payroll_service import get_employee_data

from ml.intents import detect_intent

from services.payroll_chat_engine import handle_question
from services.payroll_chat_engine import handle_followup

from services.conversation_manager import save_context
from services.conversation_manager import get_last_context

from services.text_normalizer import normalize_text
from services.entity_extractor import extract_entity


def chat(employee_id, question):

    df = load_data()

    employee_data = get_employee_data(
        df,
        employee_id
    )

    if employee_data.empty:

        return {
            "success": False,
            "message": "لم يتم العثور على الموظف"
        }

    april = employee_data[
        employee_data["month"] == "April"
    ].iloc[0]

    may = employee_data[
        employee_data["month"] == "May"
    ].iloc[0]

    normalized_question = normalize_text(question)

    intent, confidence = detect_intent(
        normalized_question
    )

    entity = extract_entity(
        normalized_question
    )

    context = get_last_context(employee_id)

    followup_phrases = [
        "ليه",
        "ليه زاد",
        "ليه قل",
        "طب ليه",
        "ليه كده",
        "يعني",
        "مع إن",
        "مع ان",
        "بس",
        "إزاي"
    ]

    is_followup = (
        intent == "followup"
        or normalized_question in followup_phrases
    )

    if is_followup:

        if context is None:

            return {
                "success": False,
                "answer": "لا توجد محادثة سابقة."
            }

        followup_topic = (
            entity
            if entity is not None
            else context["topic"]
        )

        answer = handle_followup(
            followup_topic,
            april,
            may,
            normalized_question
        )

        save_context(
            employee_id,
            context["intent"],
            followup_topic,
            answer
        )

        return {
            "success": True,
            "intent": "followup",
            "topic": followup_topic,
            "confidence": round(confidence, 2),
            "answer": answer
        }

    if entity is not None:

        intent = entity

        if entity == "salary":
            intent = "salary_explanation"

        answer = handle_question(
            intent,
            april,
            may
        )

        save_context(
            employee_id,
            intent,
            entity,
            answer
        )

        return {
            "success": True,
            "intent": intent,
            "topic": entity,
            "confidence": round(confidence, 2),
            "answer": answer
        }

    if confidence < 0.45:

        return {
            "success": False,
            "intent": intent,
            "topic": None,
            "confidence": round(confidence, 2),
            "answer": "لم أفهم السؤال بشكل كافٍ."
        }

    answer = handle_question(
        intent,
        april,
        may
    )

    save_context(
        employee_id,
        intent,
        intent,
        answer
    )

    return {
        "success": True,
        "intent": intent,
        "topic": intent,
        "confidence": round(confidence, 2),
        "answer": answer
    }