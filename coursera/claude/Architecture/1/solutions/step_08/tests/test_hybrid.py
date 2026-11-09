from playwright.sync_api import expect

from data.products import BACKPACK
from pages.inventory_page import InventoryPage


def test_item_added_by_api_is_visible_in_ui(authenticated_page, shop_api):
    shop_api.add_to_cart(BACKPACK.id)                      # setup: API se

    inventory = InventoryPage(authenticated_page).open()   # verify: UI se
    expect(inventory.cart_badge).to_have_text("1")
