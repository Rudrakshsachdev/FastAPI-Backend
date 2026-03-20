from fastapi import FastAPI, HTTPException, Query, Path

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
# define a query parameter for the products URL with a default value of None and a minimum length of 1 and a maximum length of 50 and a description of "Search by product name (case insensitive) or sort by price (True for ascending, False for descending) or order of the products (asc for ascending, desc for descending) or limit the number of products to return or pagination offset"
def list_products(
    # search by product name (case insensitive)
    name : str = Query(
        default=None, 
        min_length=1, 
        max_length=50, 
        description="Search by product name (case insensitive)"),

    # sort by price (True for ascending, False for descending)
    sort_by_price: bool = Query(
            default=False,
            description="Sort products by price (True for ascending, False for descending)"
        ),
    # order of the products (asc for ascending, desc for descending)
    order: str = Query(
            default="asc",
            description="Order of the products (asc for ascending, desc for descending)"
        ),
    # limit the number of products to return
    limit: int = Query(
            default=10,
            ge=1,
            le=100,
            description="Limit the number of products to return"
        ),
    # pagination offset, pagination is used to return the products in pages
    offset: int = Query(
            default=0,
            ge=0,
            description="Pagination Offset"
        )
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
    
    if sort_by_price:
        reverse = order == "desc"
        products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)
        
    # get the total number of products
    total = len(products)

    # get the products based on the limit and offset
    product_list = products[offset:offset+limit]
    
    # return the total number of products and the list of products
    return {"total": total, "limit": limit, "offset": offset, "products": product_list}




# define a route for the products URL with a path parameter
@app.get("/products/{product_id}")
def get_product(product_id: str = Path(
    ...,
    description="Product ID",
    min_length=36,
    max_length=36,
    example="000444ea-ce3f-4dd7-bee0-f4ccc70fea6a",
)):
    products = get_all_products()
    
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", status_code=201)
def create_products(product):
    return product