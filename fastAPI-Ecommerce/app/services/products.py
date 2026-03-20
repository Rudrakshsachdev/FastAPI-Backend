import json
from pathlib import Path
from typing import List, Dict

# path to the products.json file
DATA_FILE = Path(__file__).parent / ".." / "data" / "products.json"

# function to load products from the products.json file, here List[Dict] means it is going to return list of dictionaries
def load_products() -> List[Dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# function to get all products
def get_all_products() -> List[Dict]:
    return load_products()