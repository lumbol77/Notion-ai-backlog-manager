from fastapi import APIRouter
from pydantic import BaseModel
from app.ai_agent import generate_tasks_from_idea

router = APIRouter()

class IdeaRequest(BaseModel):
    idea: str

@router.post("/generate-tasks")
def generate_tasks(request: IdeaRequest):
    tasks = generate_tasks_from_idea(request.idea)
    return {"idea": request.idea, "tasks": tasks}