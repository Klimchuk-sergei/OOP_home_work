import json
from src.product import Product
from src.category import Category


def load_json(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    categories = []
    for item in data:
        products = [
            Product(prod["name"], prod["description"], prod["price"], prod["quantity"])
            for prod in item["products"]
        ]
        categories.append(Category(item["name"], item["description"], products))

    return categories
