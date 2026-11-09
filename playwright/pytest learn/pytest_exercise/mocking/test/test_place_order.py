

# Tumhe iska Pytest test suite banana hai.

# Requirements
# Test 1 — Successful payment

# Payment:

# pay(500) → "success"

# Expected:

# "order_placed"

# Verify:

# payment.pay(500) → exactly once
# email.send("Order placed successfully") → exactly once


import place_order as po
import pytest
from unittest.mock import Mock

def test_place_order():
    payment_service = Mock()
    payment_service.pay.return_value = 'success'
    
    email_service = Mock()

    result = po.place_order(payment_service , email_service , 500)


    assert result == "order_placed"
    
    payment_service.pay.assert_called_once_with(500)
    email_service.send.assert_called_once_with("Order placed successfully")



