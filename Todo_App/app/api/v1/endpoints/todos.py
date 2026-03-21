from fastapi import APIRouter, Depends, HTTPException
from services.todo_service import get_all_todos
from db.deps import get_db
from sqlalchemy.orm import Session
from schemas.todos import TodoCreate, TodoResponse
from services.todo_service import create_todo

router = APIRouter()

@router.post("/", response_model=TodoResponse)
def create(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)


@router.get("/", response_model=list[TodoResponse])
def read(db: Session = Depends(get_db)):
    return get_all_todos(db)