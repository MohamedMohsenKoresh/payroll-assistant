from pydantic import BaseModel


class LoginRequest(BaseModel):
    employee_id: int


class ChatRequest(BaseModel):
    employee_id: int
    question: str