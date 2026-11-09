# order.py

from services import payment
from services import email

def process_order():
    payment_result = payment.pay(500)
    email.send("Order successful")

    return payment_result

# payment.pay() mock karo.
# email.send() mock karo.
# payment.pay() should return "success".
# Actual process_order() call karo.
# Assert result "success".

from unittest.mock import patch 

@patch('order.email.send')
@patch('order.payment.pay')
def test_process_order(mock_pay , mock_send):
    mock_pay.return_value = "success"

    result = order.process_order()

    assert result == 'success'

    mock_pay.assert_called_once_with(1000)
    mock_send.assert_called_once_with("Order placed")


@patch.object(APIClient , 'fetch')
def test_1(mock_fetch):
    pass


from unittest.mock import Mock

def test_users():

    api = Mock()

    # Configure here
    api.get_user.side_effect = [101 , 102 , 103]
    first = api.get_user()
    second = api.get_user()
    third = api.get_user()

    assert first == 101
    assert second == 102
    assert third == 103