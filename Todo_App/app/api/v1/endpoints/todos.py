from fastapi import APIRouter, Depends, HTTPException
from services.todo_service import get_all_todos
from db.deps import get_db
from sqlalchemy.orm import Session
from schemas.todos import TodoCreate, TodoResponse
from services.todo_service import( 
    create_todo,
    get_todos_by_id,
    get_all_todos,
    update_todo,
    delete_todo
)

router = APIRouter()

@router.post("/", response_model=TodoResponse)
def create(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)


@router.get("/", response_model=list[TodoResponse])
def read(db: Session = Depends(get_db)):
    return get_all_todos(db)

@router.get("/{todo_id}", response_model=TodoResponse)
def read_by_id(todo_id: int, db: Session = Depends(get_db)):
    return get_todos_by_id(db, todo_id)

@router.put("/{todo_id}", response_model=TodoResponse)
def update(todo_id: int, updated_todo: TodoCreate, db: Session = Depends(get_db)):
    return update_todo(db, todo_id, updated_todo)

@router.delete("/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):    
    return delete_todo(db, todo_id)

