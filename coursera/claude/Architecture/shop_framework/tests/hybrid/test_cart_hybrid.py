import allure
import pytest
from playwright.sync_api import expect

from framework.data.products import BACKPACK, ONESIE
from framework.pages.cart_page import CartPage
from framework.pages.inventory_page import InventoryPage


@allure.feature("Hybrid")
@pytest.mark.smoke
def test_item_added_by_api_is_visible_in_ui(authenticated_page, shop_api):
    shop_api.add_to_cart(BACKPACK.id)                      # setup: API se (fast, stable)

    inventory = InventoryPage(authenticated_page).open()   # verify: UI se
    expect(inventory.header.cart_badge).to_have_text("1")
    expect(inventory.products.button_for(BACKPACK.name)).to_have_text("Remove")


@allure.feature("Hybrid")
@pytest.mark.regression
def test_order_placed_in_ui_is_stored_in_backend(authenticated_page, shop_api):
    shop_api.add_to_cart(ONESIE.id)                        # setup: API

    inventory = InventoryPage(authenticated_page).open()
    inventory.header.open_cart()
    done = CartPage(authenticated_page).wait_until_loaded().checkout()   # action: UI

    stored_ids = [o["order_id"] for o in shop_api.list_orders().json()]  # verify: API
    assert done.order_id() in stored_ids
