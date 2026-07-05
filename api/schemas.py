from pydantic import BaseModel


class LoginRequest(BaseModel):
    employee_id: int


class LoginResponse(BaseModel):
    success: bool
    employee_id: int | None = None
    months: list[str] | None = None
    message: str


class ChatRequest(BaseModel):
    employee_id: int
    question: str


class ChatResponse(BaseModel):
    success: bool
    intent: str | None = None
    confidence: float | None = None
    answer: str