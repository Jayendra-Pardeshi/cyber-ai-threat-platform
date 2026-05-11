from fastapi import FastAPI
from api.routes.chat import router as chat_router

app = FastAPI(
    title="Cyber AI Platform"
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "Cyber AI Platform Running"
    }