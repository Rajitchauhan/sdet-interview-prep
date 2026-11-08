import allure
import pytest
from playwright.sync_api import expect

from framework.data.products import BACKPACK, ONESIE
from framework.flows.shopping_flow import ShoppingFlow


@allure.feature("Checkout")
@pytest.mark.smoke
def test_user_can_buy_two_products_through_ui(page, user):
    shopping = ShoppingFlow(page)
    inventory = shopping.login_as(user)

    done = shopping.buy(inventory, [BACKPACK.name, ONESIE.name])

    expect(done.heading).to_be_visible()
    assert done.order_id() > 1000
