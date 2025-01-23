import pytest
import products

def test_creating_general_product():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() == True

def test_creating_invalid_details():
    with pytest.raises(ValueError, match ="Every product needs valid name"):
        products.Product("",1450,100)

    with pytest.raises(ValueError, match ="Every product needs price higher than zero"):
        products.Product("MacBook Air M2",-1450,100)

    with pytest.raises(ValueError, match="A negative quantity is physically impossible"):
        products.Product("MacBook Air M2",1450,-100)


def test_product_gets_inactive_reaching_zero():
    product = products.Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.is_active() == False

def test_product_gets_purchesed_modify_quantity_return_output():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(50)
    assert product.get_quantity() == 50
    assert total_price == 72500

def test_buying_more_than_store_can_handle():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert product.buy(101) == None


