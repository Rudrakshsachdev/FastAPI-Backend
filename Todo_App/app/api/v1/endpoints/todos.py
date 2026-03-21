from fastapi import APIRouter
from services.todo_service import get_all_todos

router = APIRouter()

@router.get("/")
def get_todos():
    return get_all_todos()