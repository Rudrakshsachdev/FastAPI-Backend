from fastapi import FastAPI

# initialize the fastapi app
app = FastAPI()

# define a route for the root URL
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Ecommerce API"}