import pytest

import store

@pytest.fixture
def populated_cart():
    cart = store.Cart()
    cart.add_item("Shirt", 500, 2)
    cart.add_item("Jeans", 1000, 1)
    return cart 

def test_subtotal(populated_cart):
    assert populated_cart.calculate_subtotal() == 2000.0 , "excepted 2k"

@pytest.mark.parametrize("coupon, expected_total" , [("FLAT100" , 1900.0) , ("DISCOUNT10" , 1800.0) ,
                                                     ("NOCODE" , 2000.0)])
def test_coupon_discounts(populated_cart, coupon, expected_total):
    assert (populated_cart.apply_coupon(coupon) == expected_total) , f"must be = {expected_total}"

def test_add_negative_price_raises_error():
    cart = store.Cart()
    with pytest.raises(ValueError) as exc:
        cart.add_item("t-shirt" , -100 , 1) 
    assert "Price cannot be negative" in str(exc.value) 

def test_add_zero_quantity_raises_error():
    cart = store.Cart()

    with pytest.raises(ValueError) as exc:
        cart.add_item("ball" , 200 , 0)
    assert "Quantity must be at least 1" in str(exc.value)