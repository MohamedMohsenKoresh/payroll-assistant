from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Payroll Assistant API",
    description="Payroll Chatbot API",
    version="1.0.0"
)

app.include_router(router)