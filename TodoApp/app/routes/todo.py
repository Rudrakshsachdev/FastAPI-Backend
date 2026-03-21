# this file defines the routes for the todo module. It includes a single route for reading todos, which currently returns a simple message. You can expand this file to include more routes for creating, updating, and deleting todos as needed.

from fastapi import APIRouter

router = APIRouter(
    prefix="/todo"
)

@router.get("/")
def read_todos():
    return {"message": "Hello, World!"}
