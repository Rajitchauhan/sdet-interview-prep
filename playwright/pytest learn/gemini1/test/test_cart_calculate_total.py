from gemini import cart
import pytest 

@pytest.fixture
def sample_cart():
    data = [{"name": "Mouse", "price": 500} , {"name": "Keyboard", "price": 1500}]

    return data 

def test_calculate_total(sample_cart):
    total = cart.calculate_total_price(sample_cart)

    assert total == 2000
