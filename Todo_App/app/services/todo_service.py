# this Session import is used to type hint the database session in our service functions. 
from sqlalchemy.orm import Session

from models.todos import Todo

from schemas.todos import TodoCreate


def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(title=todo.title, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_all_todos(db: Session):
    return db.query(Todo).all()