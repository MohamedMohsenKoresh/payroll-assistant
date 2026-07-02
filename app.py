from data_loader import load_data

from services.payroll_service import get_employee_data
from intents import detect_intent
from payroll_chat_engine import handle_question
from payroll_chat_engine import handle_followup

from services.conversation_manager import save_context
from services.conversation_manager import get_last_intent
from services.conversation_manager import get_last_topic

from services.text_normalizer import normalize_text

df = load_data()

print("Hello")
print("ادخل رقم الموظف")

employee_id = int(input("ادخل رقم الموظف: "))

employee_data = get_employee_data(df, employee_id)

if len(employee_data) == 0:
    print("لم يتم العثور على الموظف")
    exit()

april = employee_data[employee_data["month"] == "April"].iloc[0]
may = employee_data[employee_data["month"] == "May"].iloc[0]

print("\nتم تسجيل الدخول بنجاح")
print("اكتب exit للخروج")

while True:

    question = input("\nأنت: ")

    question = normalize_text(question)

    if question.lower() == "exit":

        print("\nالبوت: شكراً لاستخدام Payroll Chatbot")
        break

    if "يعني" in question:

        last_intent = get_last_intent()

        if last_intent == "salary_explanation":

            print("\nالبوت:")

            print(
                f"التغيير يعني الفرق بين صافي المرتب في أبريل ومايو.\n"
                f"صافي أبريل = {april['net_salary']:.2f} جنيه\n"
                f"صافي مايو = {may['net_salary']:.2f} جنيه"
            )

            continue

    if "مع ان" in question or "مع إن" in question:

        topic = get_last_topic()

        print("\nالبوت:")

        if topic == "tax":

            print(
                "نعم، هذا طبيعي. قد تزيد الضريبة وفي نفس الوقت يزيد صافي المرتب "
                "إذا كانت زيادة البونص والأوفر تايم أكبر من الزيادة في الضريبة."
            )

        elif topic == "salary_explanation":

            print(
                "نعم، رغم زيادة الضريبة فإن البونص والأوفر تايم زادا بقيمة أكبر "
                "لذلك ارتفع صافي المرتب في النهاية."
            )

        else:

            print("من فضلك وضح سؤالك أكثر.")

        continue

    if question.strip() in ["بس", "بس كده", "فقط"]:

        topic = get_last_topic()

        print("\nالبوت:")

        if topic == "tax":

            print(
                "نعم، السبب الرئيسي هو زيادة الدخل الخاضع للضريبة."
            )

        elif topic == "salary_explanation":

            print(
                "باختصار، الزيادة جاءت من البونص والأوفر تايم بعد خصم الزيادة في الضريبة."
            )

        else:

            print(
                "هل لديك أي استفسار آخر؟"
            )

        continue

    if question.strip() in ["ليه", "ليه زاد", "طب ليه"]:

        topic = get_last_topic()

        print("\nالبوت:")

        print(
            handle_followup(
                topic,
                april,
                may
            )
        )

        continue

    intent, confidence = detect_intent(question)

    print(f"\n[DEBUG] Intent = {intent}")
    print(f"[DEBUG] Confidence = {confidence:.2f}")

    if confidence < 0.50:

        print("\nالبوت:")
        print(
            "لم أفهم السؤال بشكل كافٍ.\n"
            "هل تقصد المرتب أم الضريبة أم الأوفر تايم أم الخصومات؟"
        )

        continue

    response = handle_question(
        intent,
        april,
        may
    )

    save_context(
        intent,
        intent,
        response
    )

    print("\nالبوت:")
    print(response)