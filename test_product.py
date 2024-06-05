import pytest
import products


def test_normal_product():
    product = products.Product("MacBook Air M2", price=10, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 10
    assert product.quantity == 100


def test_inactive():
    mac = products.Product("MacBook Air M2", price=1000, quantity=100)
    mac.buy(100)
    assert mac.quantity == 0
    assert mac.active == False


def test_quantity():
    mac = products.Product("MacBook Air M2", price=1000, quantity=100)
    mac.buy(80)
    assert mac.quantity == 20


def test_buy():
    mac = products.Product("MacBook Air M2", price=1000, quantity=100)
    assert mac.buy(80) == 1000 * 80
    assert mac.quantity == 20


def test_exceed_purchace():
    mac = products.Product("MacBook Air M2", price=10, quantity=100)
    with pytest.raises(ValueError, match="Not enough stock available"):
        mac.buy(180)


def test_name_empty():
    with pytest.raises(ValueError, match="Product name cannot be empty."):
        products.Product("", price=1450, quantity=100)


def test_name_string():
    with pytest.raises(TypeError, match="Name has to be a string."):
        products.Product(19, price=1450, quantity=100)


def test_price_negative():
    with pytest.raises(ValueError, match="Product price cannot be negative."):
        products.Product("MacBook Air M2", price=-10, quantity=100)


def test_price_string():
    with pytest.raises(TypeError, match="Price has to be an integer or float."):
        products.Product("MacBook Air M2", price="10", quantity=100)


def test_quantity_int():
    with pytest.raises(TypeError, match="Quantity has to be an integer."):
        products.Product("MacBook Air M2", price=10, quantity="100")


def test_quantity_negative():
    with pytest.raises(ValueError, match="Product quantity cannot be negative."):
        products.Product("MacBook Air M2", price=10, quantity=-100)


def test_buy_zero():
    with pytest.raises(ValueError, match="Quantity has to be greater than zero."):
        mac = products.Product("MacBook Air M2", price=10, quantity=100)
        mac.buy(0)


def test_buy_negative():
    with pytest.raises(ValueError, match="Quantity has to be greater than zero."):
        mac = products.Product("MacBook Air M2", price=10, quantity=100)
        mac.buy(-1)


def test_buy_exceed():
    with pytest.raises(ValueError, match="Not enough stock available."):
        mac = products.Product("MacBook Air M2", price=10, quantity=100)
        mac.buy(200)


def test_buy_string():
    with pytest.raises(TypeError, match="Quantity has to be an integer."):
        mac = products.Product("MacBook Air M2", price=10, quantity=100)
        mac.buy("200")


def test_non_stock_product():
    product = products.NonStockedProduct("Windows License", price=125)
    assert product.name == "Windows License"
    assert product.price == 125
    assert product.quantity == 0


def test_always_zero():

    with pytest.raises(
        AttributeError, match="NonStockedProduct quantity cannot be modified."
    ):
        product = products.NonStockedProduct("Windows License", price=125)
        product.quantity = 10


def test_limited_product():
    product = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.name == "Shipping"
    assert product.price == 10
    assert product.quantity == 250
    assert product.maximum == 1


def test_limit_exceed():
    with pytest.raises(ValueError, match="Shipping is limted to add max 1."):
        shipping = products.LimitedProduct(
            "Shipping", price=10, quantity=250, maximum=1
        )
        shipping.buy(2)


def test_limit_quantity_not_enough():
    with pytest.raises(ValueError, match="Not enough stock available."):
        shipping = products.LimitedProduct("Shipping", price=10, quantity=0, maximum=1)
        shipping.buy(1)


def test_limit_buy_zero():
    with pytest.raises(ValueError, match="Quantity has to be greater than zero."):
        shipping = products.LimitedProduct(
            "Shipping", price=10, quantity=250, maximum=1
        )
        shipping.buy(0)


def test_limit_buy_negative():
    with pytest.raises(ValueError, match="Quantity has to be greater than zero."):
        shipping = products.LimitedProduct(
            "Shipping", price=10, quantity=250, maximum=1
        )
        shipping.buy(-1)


def test_limit_buy_exceed():
    with pytest.raises(ValueError, match="Not enough stock available."):
        shipping = products.LimitedProduct(
            "Shipping", price=10, quantity=150, maximum=1
        )
        shipping.buy(200)


def test_limit_buy():
    shipping = products.LimitedProduct("Shipping", price=10, quantity=150, maximum=1)
    assert shipping.buy(1) == 10.0
    assert shipping.quantity == 149


pytest.main()
