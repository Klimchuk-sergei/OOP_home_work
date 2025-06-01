import pytest
from src.product import Product
from src.products_type import Smartphone, LawnGrass


def test_product_init():
    p = Product("Товар X", "Описание X", 9.9, 4)
    assert p.name == "Товар X"
    assert p.description == "Описание X"
    assert p.price == 9.9
    assert p.quantity == 4


def test_product_price_getter_setter():
    p = Product("Тест", "Описание", 100.0, 1)
    assert p.price == 100.0

    p.price = 250.0
    assert p.price == 250.0

    p.price = 0
    assert p.price == 250.0

    p.price = -50
    assert p.price == 250.0


def test_product_new_product():
    data = {
        "name": "Наушники",
        "description": "Bluetooth, шумоподавление",
        "price": 4000.0,
        "quantity": 3
    }
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Наушники"
    assert product.description == "Bluetooth, шумоподавление"
    assert product.price == 4000.0
    assert product.quantity == 3

def test_product_str():
    p = Product("Товар", "Описание", 100.0, 10)
    assert str(p) == "Товар, 100.0 руб. Остаток: 10 шт."

def test_smartphone_creation():
    phone = Smartphone("iPhone", "Смартфон", 999.0, 5, "A15", "13 Pro", 256, "Серый")
    assert phone.model == "13 Pro"
    assert phone.memory == 256
    assert phone.color == "Серый"

def test_lawngrass_creation():
    grass = LawnGrass("Газон", "Трава", 150.0, 3, "Россия", "7 дней", "Зелёный")
    assert grass.country == "Россия"
    assert grass.color == "Зелёный"

def test_add_same_type_products():
    p1 = Smartphone("iPhone", "desc", 100, 2, "A15", "13", 128, "white")
    p2 = Smartphone("Samsung", "desc", 200, 1, "Snap", "S21", 256, "black")
    result = p1 + p2
    assert result == 400

def test_add_different_type_raises():
    p1 = Smartphone("iPhone", "desc", 100, 2, "A15", "13", 128, "white")
    p2 = LawnGrass("Газон", "desc", 50, 3, "RU", "7 дн", "green")
    with pytest.raises(TypeError):
        _ = p1 + p2
