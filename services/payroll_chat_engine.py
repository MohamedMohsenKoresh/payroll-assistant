from services.salary_analysis import explain_salary_change


def handle_question(intent, april, may):

    if intent == "salary_explanation":

        return explain_salary_change(april, may)

    elif intent == "tax":

        tax_difference = may["tax"] - april["tax"]

        if tax_difference > 0:

            return (
                f"زادت الضريبة بمقدار "
                f"{tax_difference:.2f} جنيه.\n"
                f"والسبب هو زيادة الدخل نتيجة زيادة البونص والأوفر تايم."
            )

        elif tax_difference < 0:

            return (
                f"انخفضت الضريبة بمقدار "
                f"{abs(tax_difference):.2f} جنيه."
            )

        return "لا يوجد تغيير في الضريبة."

    elif intent == "bonus":

        return (
            f"البونص في أبريل كان {april['bonus']} جنيه "
            f"وأصبح {may['bonus']} جنيه في مايو."
        )

    elif intent == "overtime":

        return (
            f"الأوفر تايم في أبريل كان {april['overtime']} جنيه "
            f"وأصبح {may['overtime']} جنيه في مايو."
        )

    elif intent == "deductions":

        return (
            f"إجمالي الخصومات في أبريل "
            f"{april['total_deduction']} جنيه "
            f"وفي مايو {may['total_deduction']} جنيه."
        )

    elif intent == "compare":

        return explain_salary_change(april, may)

    return "عذراً، لم أفهم السؤال."

def handle_followup(topic, april, may):

    if topic == "overtime":

        difference = may["overtime"] - april["overtime"]

        return (
            f"زاد الأوفر تايم بمقدار {difference:.2f} جنيه "
            f"مقارنة بالشهر السابق."
        )

    elif topic == "tax":

        return (
            "زادت الضريبة بسبب زيادة الدخل الخاضع للضريبة."
        )

    elif topic == "bonus":

        difference = may["bonus"] - april["bonus"]

        return (
            f"زاد البونص بمقدار {difference:.2f} جنيه."
        )

    return "من فضلك وضح سؤالك أكثر."