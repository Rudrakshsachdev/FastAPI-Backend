from fastapi import FastAPI

# initialize the fastapi app
app = FastAPI()

# define a route for the root URL
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Ecommerce API"}

# define a route for the users URL
@app.get("/users")
def get_users():
    return ["Yug Prakash", "Rudraksh Sachdeva", "Aarav", "Shivansee"]

# define a route for the users URL with a path parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}