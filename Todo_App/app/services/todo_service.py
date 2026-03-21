# this Session import is used to type hint the database session in our service functions. 
from sqlalchemy.orm import Query, Session

from models.todos import Todo

from schemas.todos import TodoCreate

from fastapi import HTTPException

# this function creates a new todo item in the database. It takes a database session and a TodoCreate schema as input, creates a new Todo model instance, adds it to the session, commits the transaction to save it to the database, refreshes the instance to get the generated ID, and then returns the newly created todo item.
def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(title=todo.title, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# function to retrieve all todo items from the database. It takes a database session as input and returns a list of all Todo items by querying the database.
def get_all_todos(db: Session):
    return db.query(Todo).all()


# function to retrieve a specific todo item by its ID. It takes a database session and a todo_id as input, queries the database for a Todo item with the matching ID, and returns it. If no such item is found, it raises an HTTPException with a 404 status code indicating that the todo was not found.
def get_todos_by_id(db: Session, todo_id: int):
    # this todo is used to query the database for a specific todo item by its ID.
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


# function to update an existing todo item. It takes a database session, a todo_id, and an updated_todo schema as input. It first retrieves the existing todo item from the database using the get_todos_by_id function. If the item is not found, it raises an HTTPException with a 404 status code. If the item is found, it updates its title and completed status with the values from the updated_todo schema, commits the changes to the database, and returns the updated todo item.
def update_todo(db: Session, todo_id: int, updated_todo: TodoCreate):
    todo = get_todos_by_id(db, todo_id)

    todo.title = updated_todo.title # updating the todo title
    todo.completed = updated_todo.completed # updating the todo completed status

    db.commit() # committing the changes to the database
    db.refresh(todo) # refreshing the todo instance to get the updated values
    return todo

def delete_todo(db: Session, todo_id: int):
    todo = get_todos_by_id(db, todo_id)

    db.delete(todo) # deleting the todo item from the database
    db.commit() # committing the changes to the database
    return {"detail": "Todo deleted"}