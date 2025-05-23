from src.product import Product


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
