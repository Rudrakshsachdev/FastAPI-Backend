# this app is the main entry point of the application. It defines the FastAPI app and includes the routes from the todo module.

from fastapi import Depends, FastAPI, Request

from typing import Annotated

from app.routes import todo

from test import QueryParams


app = FastAPI()
app.include_router(todo.router)

@app.get("/")
def home(query: Annotated[QueryParams, Depends()]):

    
    return {"message": "Welcome to the TodoApp API", "query_params": query}

# @app.post("/todo")
# def create_todo(item: dict):
#     return {"message": "Todo item created", "item": item}