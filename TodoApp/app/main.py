from fastapi import Depends, FastAPI, Request

from typing import Annotated

from test import QueryParams


app = FastAPI()

@app.get("/")
def home(query: Annotated[QueryParams, Depends()]):

    
    return {"message": "Welcome to the TodoApp API", "query_params": query}

@app.post("/todo")
def create_todo(item: dict):
    return {"message": "Todo item created", "item": item}