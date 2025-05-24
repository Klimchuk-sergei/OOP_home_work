import pytest
from src.product import Product
from src.base_product import BaseProduct


def test_base_product_cannot_be_instantiated():
    """Нельзя создать объект абстрактного класса BaseProduct"""
    with pytest.raises(TypeError):
        BaseProduct("Name", "Description", 100.0, 5)


def test_creation_logger_mixin_prints_log(capsys):
    """Mixin должен печатать лог при создании объекта"""
    p = Product("TestProduct", "Test", 100.0, 10)
    captured = capsys.readouterr()
    assert "LOG" in captured.out
    assert "Product" in captured.out
    assert "TestProduct" in captured.out


def test_product_inherits_base_and_mixin():
    """Проверка, что Product наследует нужные классы"""
    p = Product("Test", "Description", 100.0, 1)
    assert isinstance(p, Product)
    assert hasattr(p, "price")
