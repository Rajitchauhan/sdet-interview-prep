from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.order_complete_page import OrderCompletePage


class ShoppingFlow:
    def __init__(self, page: Page):
        self._page = page

    def buy(self, inventory: InventoryPage, product_names: list[str]) -> OrderCompletePage:
        for name in product_names:
            inventory.add_to_cart(name)
        inventory.open_cart()
        CartPage(self._page).wait_until_loaded().checkout()
        return OrderCompletePage(self._page).wait_until_loaded()
