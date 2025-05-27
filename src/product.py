from src.base_product import BaseProduct
from src.mixin import CreatLoggerMixin


class Product(CreatLoggerMixin, BaseProduct):
    """Класс для описания товара"""

    # def __init__(self, name: str, description: str, price: float, quantity: int):
    #     """Метод для инициализации экземпляра класса."""
    #     """Задаем значения атрибутам экземпляра."""
    #     self.name = name
    #     self.description = description
    #     self.__price = price
    #     self.quantity = quantity

    def __init__(self, name: str, description: str, price: float, quantity: int):
        # Вызываем конструктор родительского класса (BaseProduct)
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, data: dict):
        """Создание нового товара из словаря"""
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"]
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов.")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    pass
