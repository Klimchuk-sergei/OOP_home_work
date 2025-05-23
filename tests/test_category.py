import os
import json
import pytest

from src.category import Category
from src.product import Product
from src.utils import load_json

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")


def test_category_init_empty():
    cat = Category("Категория 1", "Пустая категория", [])
    assert cat.name == "Категория 1"
    assert cat.description == "Пустая категория"
    assert cat.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_init_with_products(sample_products):
    cat = Category("Категория 2", "Два товара", sample_products)
    assert cat.name == "Категория 2"
    assert cat.description == "Два товара"
    assert len(cat.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_counters_no_categories():
    assert Category.category_count == 0
    assert Category.product_count == 0


def test_counters_one_category_two_products(sample_products):
    Category("Cat1", "Desc", sample_products)
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_counters_two_categories_three_products(sample_products):
    Category("Cat1", "Desc", sample_products[:2])
    Category("Cat2", "Desc", sample_products[:1])
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_load_json_creates_categories_and_products():
    with open(DATA_PATH, encoding="utf-8") as f:
        raw = json.load(f)

    cats = load_json(DATA_PATH)

    assert len(cats) == len(raw)
    assert Category.category_count == len(raw)

    total_products = sum(len(item["products"]) for item in raw)
    assert Category.product_count == total_products

    first_cat, first_raw = cats[0], raw[0]
    assert isinstance(first_cat, Category)
    assert first_cat.name == first_raw["name"]
    assert first_cat.description == first_raw["description"]
    assert all(isinstance(p, Product) for p in first_cat.products)
    assert [p.name for p in first_cat.products] == [prod["name"] for prod in first_raw["products"]]

def test_category_str():
    p1 = Product("Товар1", "desc", 50.0, 4)
    p2 = Product("Товар2", "desc", 60.0, 6)
    cat = Category("Категория", "Описание", [p1, p2])
    assert str(cat) == "Категория, количество продуктов: 10 шт."

def test_add_valid_product():
    cat = Category("Электроника", "Описание", [])
    p = Product("Товар", "desc", 100.0, 2)
    cat.add_product(p)
    assert len(cat.products) == 1

def test_add_invalid_product_raises():
    cat = Category("Электроника", "Описание", [])
    with pytest.raises(TypeError):
        cat.add_product("непродукт")
