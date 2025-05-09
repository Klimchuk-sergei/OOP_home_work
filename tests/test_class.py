import pytest
from src.Product import Product
from src.Category import Category

def test_product():
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

def test_category():
    p1 = Product()