from services.data_loader import load_data
from services.payroll_service import get_employee_data


def login(employee_id):

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

    months = employee_data["month"].tolist()

    return {
        "success": True,
        "employee_id": employee_id,
        "months": months,
        "message": "تم تسجيل الدخول بنجاح"
    }