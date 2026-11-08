import allure
import pytest

from framework.api.shop_api import ShopApi
from framework.data.products import BACKPACK, ONESIE


@allure.feature("Cart API")
def test_cart_requires_authentication(settings):
    anonymous = ShopApi(settings.api_url, settings.api_timeout_s)   # token nahi
    try:
        assert anonymous.get_cart().status_code == 401
    finally:
        anonymous.close()


@allure.feature("Cart API")
@pytest.mark.smoke
def test_add_product_to_cart(shop_api):
    response = shop_api.add_to_cart(BACKPACK.id)

    assert response.status_code == 201
    assert response.json() == {"items": [BACKPACK.id], "count": 1}


@allure.feature("Cart API")
def test_unknown_product_is_rejected(shop_api):
    assert shop_api.add_to_cart("does-not-exist").status_code == 404


@allure.feature("Checkout API")
def test_checkout_with_empty_cart_is_rejected(shop_api):
    response = shop_api.checkout()

    assert response.status_code == 400
    assert response.json()["error"] == "Cart is empty"


@allure.feature("Checkout API")
@pytest.mark.regression
def test_checkout_creates_order_and_empties_cart(shop_api):
    shop_api.add_to_cart(BACKPACK.id)
    shop_api.add_to_cart(ONESIE.id)

    checkout = shop_api.checkout()

    assert checkout.status_code == 201
    order_id = checkout.json()["order_id"]
    assert order_id in [o["order_id"] for o in shop_api.list_orders().json()]
    assert shop_api.get_cart().json()["count"] == 0
