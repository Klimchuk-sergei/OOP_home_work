import pytest
from src.product import Product
from src.category import Category


def test_product_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_average_price_returns_correct_value():
    products = [
        Product("Товар 1", "Описание", 100.0, 5),
        Product("Товар 2", "Описание", 200.0, 3)
    ]
    category = Category("Категория", "Тестовая категория", products)
    assert category.middle_price() == 150.0


def test_average_price_returns_zero_for_empty_list():
    category = Category("Пустая", "Нет товаров", [])
    assert category.middle_price() == 0
