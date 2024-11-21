import json
import os

from src.category import Category
from src.product import Product


def read_file_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_category_from_json(data):
    categories = []
    for categ in data:
        products = []
        for prod in categ["products"]:
            products.append(Product(**prod))
        categ["products"] = products
        categories.append(Category(**categ))
    return categories


if __name__ == "__main__":
    raw_data = read_file_json("../data/products.json")
    user_date = create_category_from_json(raw_data)
    print(user_date[0].name)
