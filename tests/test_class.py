import os
import json

from src.product import Product
from src.category import Category
from src.utils import load_json

# путь к json файлу в папке data
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")


def test_product_init():
    """Проверяем инициализацию Product"""
    p = Product("Товар X", "Описание X", 9.9, 4)
    assert p.name == "Товар X"
    assert p.description == "Описание X"
    assert p.price == 9.9
    assert p.quantity == 4


def test_category_init_empty():
    """Проверяем счетчик при передаче пустого списка"""
    cat = Category("Категория 1", "Пустая категория", [])
    assert cat.name == "Категория 1"
    assert cat.description == "Пустая категория"
    assert cat.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_init_with_products(sample_products):
    """
    Проверяем Category на хранение списка продуктов и правильность работы счетчиков
    """
    cat = Category("Категория 2", "Два товара", sample_products)
    assert cat.name == "Категория 2"
    assert cat.description == "Два товара"
    assert len(cat.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_counters_no_categories():
    """Если не создаём категорий — счётчики остаются нулями."""
    assert Category.category_count == 0
    assert Category.product_count == 0


def test_counters_one_category_two_products(sample_products):
    """Одна категория с двумя товарами — счётчики: 1 и 2."""
    Category("Cat1", "Desc", sample_products)
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_counters_two_categories_three_products(sample_products):
    """Две категории: с 2 и 1 товаром — счётчики: 2 и 3."""
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


def test_product_price_getter_setter():
    """Проверка геттера и сеттера для атрибута price с защитой от некорректной цены"""
    p = Product("Тест", "Описание", 100.0, 1)
    assert p.price == 100.0

    p.price = 250.0
    assert p.price == 250.0

    p.price = 0  # Должно вывести сообщение и не изменить цену
    assert p.price == 250.0

    p.price = -50  # Также должно быть отклонено
    assert p.price == 250.0


def test_product_new_product():
    """Проверка создания продукта через класс-метод new_product"""
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
