import pytest

from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасываем счетчик после каждого теста"""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    """Получаем список из двух продуктов"""
    return [
        Product("Товар 1", "Описание 1", 1.1, 1),
        Product("Товар 2", "Описание 2", 2.2, 2)
    ]
