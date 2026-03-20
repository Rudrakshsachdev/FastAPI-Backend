from fastapi import FastAPI, HTTPException, Query

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
@app.get("/product")
def get_products():
    return get_all_products()


@app.get("/products")
# define a query parameter for the products URL with a default value of None and a minimum length of 1 and a maximum length of 50 and a description of "Search by product name (case insensitive)"
def list_products(
    name : str = Query(
        default=None, 
        min_length=1, 
        max_length=50, 
        description="Search by product name (case insensitive)")
    ):

    # list out all the products
    products = get_all_products()

    # if the name is not None, then filter the products based on the name
    if name:
        # strip the name of any leading or trailing whitespace and convert it to lowercase
        needle = name.strip().lower()
        # filter the products based on the name
        products = [p for p in products if needle in p.get("name", "").lower()]

        # if the products are not found, then raise an HTTPException
        if not products:
            raise HTTPException(status_code=404, detail="Product not found")
        
        # get the total number of products
        total = len(products)
    
    # return the total number of products and the list of products
    return {"total": total, "products": products}