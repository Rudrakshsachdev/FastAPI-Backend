from fastapi import FastAPI, HTTPException

from services.products import get_all_products

# initialize the fastapi app
app = FastAPI()

# define a route for the root URL
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Ecommerce API"}

# define a dynamic route for the users URL
@app.get("/users/{id}")
def get_users(id: int):
    users = ["Yug Prakash", "Rudraksh Sachdeva", "Aarav", "Shivansee"]
    return (
        users[id]
        if id < len(users)
        else HTTPException(status_code=404, detail="User not found")
    )

# define a route for the users URL with a path parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# define a route for the products URL
@app.get("/products")
def get_products():
    return get_all_products()
