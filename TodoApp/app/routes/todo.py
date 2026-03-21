# this file defines the routes for the todo module. It includes a single route for reading todos, which currently returns a simple message. You can expand this file to include more routes for creating, updating, and deleting todos as needed.

from fastapi import APIRouter

from app.models.todo import CreateTodo

# initializes the APIRouter with a prefix of "/todo", which means that all routes defined in this router will be prefixed with "/todo". For example, the route defined as @router.get("/") will be accessible at "/todo/".
router = APIRouter(
    prefix="/todo"
)

@router.get("/")
def read_todos():
    return {"message": "Hello, World!"}


@router.post("/")
def store(item: CreateTodo):
    return {"message": "Todo item created", "item": item.model_dump()}