from services.salary_analysis import explain_salary_change


def handle_question(intent, april, may):

    if intent == "salary_explanation":
        return explain_salary_change(april, may)

    elif intent == "tax":

        tax_difference = may["tax"] - april["tax"]

        if tax_difference > 0:
            return (
                f"زادت الضريبة بمقدار {tax_difference:.2f} جنيه.\n"
                f"والسبب هو زيادة الدخل نتيجة زيادة البونص والأوفر تايم."
            )

        elif tax_difference < 0:
            return (
                f"انخفضت الضريبة بمقدار "
                f"{abs(tax_difference):.2f} جنيه."
            )

        return "لا يوجد تغيير في الضريبة."

    elif intent == "bonus":

        difference = may["bonus"] - april["bonus"]

        return (
            f"البونص في أبريل كان {april['bonus']:.2f} جنيه "
            f"وأصبح {may['bonus']:.2f} جنيه في مايو. "
            f"والفرق {difference:.2f} جنيه."
        )

    elif intent == "overtime":

        difference = may["overtime"] - april["overtime"]

        return (
            f"الأوفر تايم في أبريل كان {april['overtime']:.2f} جنيه "
            f"وأصبح {may['overtime']:.2f} جنيه في مايو. "
            f"والفرق {difference:.2f} جنيه."
        )

    elif intent == "deductions":

        difference = (
            may["total_deduction"]
            - april["total_deduction"]
        )

        return (
            f"إجمالي الخصومات في أبريل "
            f"{april['total_deduction']:.2f} جنيه "
            f"وفي مايو {may['total_deduction']:.2f} جنيه. "
            f"والفرق {difference:.2f} جنيه."
        )

    elif intent == "compare":
        return explain_salary_change(april, may)

    return "عذراً لم أفهم السؤال."


def handle_followup(topic, april, may, question):

    question = question.strip()

    if topic == "tax":

        difference = may["tax"] - april["tax"]

        if "ليه" in question:

            if difference > 0:
                return (
                    "زادت الضريبة بسبب زيادة الدخل "
                    "الخاضع للضريبة."
                )

            elif difference < 0:
                return (
                    "انخفضت الضريبة بسبب انخفاض "
                    "الدخل الخاضع للضريبة."
                )

            return "الضريبة لم تتغير بين الشهرين."

        elif question == "يعني":

            return (
                "يعني تغير الدخل الخاضع للضريبة "
                "يؤثر على قيمة الضريبة المستحقة."
            )

        elif question in ["مع إن", "مع ان"]:

            return (
                "رغم زيادة الضريبة فإن زيادة البونص "
                "والأوفر تايم كانت أكبر لذلك ظل "
                "صافي الراتب أعلى."
            )

        elif question == "بس":

            return (
                "السبب الرئيسي هو تغير الدخل "
                "الخاضع للضريبة."
            )

    elif topic == "bonus":

        difference = may["bonus"] - april["bonus"]

        if "ليه" in question:

            return (
                "قيمة البونص المسجلة في مايو مختلفة "
                "عن أبريل. سبب استحقاق البونص نفسه "
                "يعتمد على بيانات وسياسة البونص."
            )

        elif question == "يعني":

            return (
                f"يعني الفرق في البونص بين الشهرين "
                f"هو {difference:.2f} جنيه."
            )

        return (
            f"الفرق في البونص بين أبريل ومايو "
            f"هو {difference:.2f} جنيه."
        )

    elif topic == "overtime":

        difference = (
            may["overtime"]
            - april["overtime"]
        )

        if "ليه" in question:

            return (
                "قيمة الأوفر تايم في مايو مختلفة عن أبريل. "
                "السبب التفصيلي يحتاج بيانات ساعات الأوفر تايم "
                "أو عدد الساعات المسجلة."
            )

        elif question == "يعني":

            return (
                f"يعني الفرق في الأوفر تايم بين الشهرين "
                f"هو {difference:.2f} جنيه."
            )

        return (
            f"الفرق في الأوفر تايم بين أبريل ومايو "
            f"هو {difference:.2f} جنيه."
        )

    elif topic == "deductions":

        difference = (
            may["total_deduction"]
            - april["total_deduction"]
        )

        if "ليه" in question:

            return (
                "تغير إجمالي الخصومات بسبب تغير "
                "واحد أو أكثر من بنود الخصم."
            )

        elif question == "يعني":

            return (
                f"يعني الفرق في إجمالي الخصومات "
                f"هو {difference:.2f} جنيه."
            )

        return (
            f"الفرق في إجمالي الخصومات بين الشهرين "
            f"هو {difference:.2f} جنيه."
        )

    return "من فضلك وضح سؤالك أكثر."