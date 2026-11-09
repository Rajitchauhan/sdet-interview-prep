from gemini import widraw_money
import pytest

def test_zero_withdrawal_raises_error():

    with pytest.raises(ValueError) as exc_info:
        widraw_money(balance=2000 , amount=0)

    assert "must be greater than zero" in str(exc_info.value)


def test_insufficient_balance_raises_error():

    with pytest.raises(RuntimeError) as exc_info:
        widraw_money(balance = 1000 , amount=5000) 

    assert "Insufficient funds" in str(exc_info.value)
