from pydoc import describe


class Product:
    """Класс для описания товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса."""
        """Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
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
