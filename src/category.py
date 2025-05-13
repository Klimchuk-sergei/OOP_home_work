class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = []  # приватый список
        Category.category_count += 1

        for product in products:
            self.add_product(product)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products.copy()

    @property
    def products(self):
        result = []
        for product in self.__products:
            line = f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт."
            result.append(line)
        return "\n".join(result)
