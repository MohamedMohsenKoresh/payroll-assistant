from services.data_loader import load_data
from services.payroll_service import get_employee_data

from ml.intents import detect_intent

from services.payroll_chat_engine import handle_question


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

    intent, confidence = detect_intent(question)

    if confidence < 0.45:

        return {
            "success": False,
            "intent": intent,
            "confidence": round(confidence, 2),
            "answer": "لم أفهم السؤال بشكل كافٍ."
        }

    answer = handle_question(
        intent,
        april,
        may
    )

    return {
        "success": True,
        "intent": intent,
        "confidence": round(confidence, 2),
        "answer": answer
    }