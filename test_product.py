import pytest
import products


def test_normal_product():
    product = products.Product("MacBook Air M2", price=10, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 10
    assert product.quantity == 100


def test_inactive():
    mac = products.Product("MacBook Air M2", price=10, quantity=100)
    mac.buy(100)
    assert mac.active == False


def test_quantity():
    mac = products.Product("MacBook Air M2", price=10, quantity=100)
    mac.buy(80)
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


pytest.main()
