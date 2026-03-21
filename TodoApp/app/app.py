# this app is the main entry point of the application. It defines the FastAPI app and includes the routes from the todo module.

from fastapi import Depends, FastAPI, Request

from typing import Annotated

from app.routes import todo

from test import QueryParams

from fastapi.exceptions import RequestValidationError

from fastapi.responses import JSONResponse


app = FastAPI() # initializes the FastAPI app
app.include_router(todo.router) # includes the routes defined in the todo module

# this is a custom exception handler for handling validation errors. It takes the request and the exception as parameters, extracts the error details, and returns a JSON response with a message and the errors.
app.exception_handler(RequestValidationError)
# this function is called whenever a validation error occurs in the application. It processes the errors and returns a structured response to the client. here async is used because the function is an asynchronous function, which allows it to handle multiple requests concurrently without blocking the execution of other code.
async def validation_exception_handler(request: Request, exc: RequestValidationError):

    errors = {} # initializes an empty dictionary to store the errors

    # iterates through the errors in the exception and populates the errors dictionary with the location and message of each error.
    for error in exc.errors():
        print(error)
        errors[error['loc'][-1]] = error['msg']
    
    # returns a JSON response with a message and the errors, along with a status code of 422 (Unprocessable Entity) to indicate that the request was well-formed but contained semantic errors.
    return JSONResponse(
        {
            "message": "Validation error",
            "errors": errors,
        }, status_code=422
    )


@app.get("/")
def home(query: Annotated[QueryParams, Depends()]):

    
    return {"message": "Welcome to the TodoApp API", "query_params": query}

# @app.post("/todo")
# def create_todo(item: dict):
#     return {"message": "Todo item created", "item": item}