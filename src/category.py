class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def product_details(self):

        return "\n".join(
            f"{p.name},{int(p.price)} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )
