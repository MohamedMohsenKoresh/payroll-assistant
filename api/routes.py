from fastapi import APIRouter

from api.schemas import LoginRequest

from services.data_loader import load_data
from services.payroll_service import get_employee_data

router = APIRouter()


@router.get("/")
def home():

    return {
        "message": "Payroll Assistant API is running"
    }


@router.get("/health")
def health():

    return {
        "status": "OK"
    }


@router.post("/login")
def login(request: LoginRequest):

    df = load_data()

    employee_data = get_employee_data(
        df,
        request.employee_id
    )

    if employee_data.empty:

        return {
            "success": False,
            "message": "لم يتم العثور على الموظف"
        }

    months = employee_data["month"].tolist()

    return {
        "success": True,
        "employee_id": request.employee_id,
        "months": months,
        "message": "تم تسجيل الدخول بنجاح"
    }