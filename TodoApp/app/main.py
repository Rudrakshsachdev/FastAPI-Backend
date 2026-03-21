from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home(request :Request):

    params = request.query_params
    return {"message": "Welcome to the TodoApp API", "query_params": params}

@app.post("/todo")
def create_todo(item: dict):
    return {"message": "Todo item created", "item": item}