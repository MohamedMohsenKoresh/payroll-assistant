from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="Payroll Assistant API",
    description="Payroll Chatbot API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(router)


@app.get("/version")
def version():

    return {
        "application": "Payroll Assistant API",
        "version": "1.0.0"
    }