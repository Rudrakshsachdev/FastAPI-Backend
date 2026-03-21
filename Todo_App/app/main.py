# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# todos = []

# class Todo(BaseModel):
#     id: int
#     title: str
#     description: str = None
#     is_completed: bool = False

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.post("/todos", response_model=Todo)
# def create_todo(todo: Todo):
#     todos.append(todo)
#     return todo

# @app.get("/todos", response_model=list[Todo])
# def get_todos():
#     return todos


# @app.get("/todos/{todo_id}", response_model=Todo)
# def get_todo(todo_id: int):
#     for todo in todos:
#         if todo.id == todo_id:
#             return todo
#     raise HTTPException(status_code=404, detail="Todo not found")


# @app.put("/todos/{todo_id}", response_model=Todo)
# def update_todo(todo_id: int, updated_todo: Todo):
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             todos[index] = updated_todo
#             return updated_todo
#     raise HTTPException(status_code=404, detail="Todo not found")

# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id: int):
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             del todos[index]
#             return {"detail": "Todo deleted"}
#     raise HTTPException(status_code=404, detail="Todo not found")


from fastapi import FastAPI
from api.v1.endpoints import todos
from db.session import SessionLocal, engine
from db.base import Base
from schemas.todos import TodoCreate
from fastapi.middleware.cors import CORSMiddleware
from api.v1.endpoints import auth



# Read all the models & create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
# here we include the router for the todos endpoints, with a prefix and tags for better organization
app.include_router(todos.router, prefix="/api/v1/todos", tags=["todos"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)