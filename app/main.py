from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Backlog Manager")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Server is running perfectly"}