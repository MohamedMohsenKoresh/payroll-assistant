def explain_salary_change(april, may):

    net_difference = may["net_salary"] - april["net_salary"]

    bonus_difference = may["bonus"] - april["bonus"]
    overtime_difference = may["overtime"] - april["overtime"]
    tax_difference = may["tax"] - april["tax"]

    if net_difference > 0:

        response = (
            f"في الواقع صافي المرتب لم ينخفض.\n"
            f"بل زاد بمقدار {net_difference:.2f} جنيه مقارنة بالشهر السابق.\n\n"
        )

        if bonus_difference > 0:
            response += (
                f"سبب الزيادة الرئيسي هو زيادة البونص "
                f"بمقدار {bonus_difference:.2f} جنيه.\n"
            )

        if overtime_difference > 0:
            response += (
                f"كما زاد الأوفر تايم بمقدار "
                f"{overtime_difference:.2f} جنيه.\n"
            )

        if tax_difference > 0:
            response += (
                f"وفي المقابل زادت الضريبة "
                f"بمقدار {tax_difference:.2f} جنيه."
            )

        return response

    elif net_difference < 0:

        return (
            f"صافي المرتب انخفض بمقدار "
            f"{abs(net_difference):.2f} جنيه مقارنة بالشهر السابق."
        )

    return "لا يوجد تغيير في صافي المرتب."