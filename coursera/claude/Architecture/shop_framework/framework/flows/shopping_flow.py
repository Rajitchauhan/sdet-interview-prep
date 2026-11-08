"""FLOW layer: kai pages ko jodne wale business actions."""
import allure
from playwright.sync_api import Page

from framework.data.users import User
from framework.pages.cart_page import CartPage
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage
from framework.pages.order_complete_page import OrderCompletePage


class ShoppingFlow:
    def __init__(self, page: Page):
        self._page = page

    def login_as(self, user: User) -> InventoryPage:
        with allure.step(f"UI se login karo: {user.username}"):
            LoginPage(self._page).open().login(user.username, user.password)
            return InventoryPage(self._page).wait_until_loaded()

    def buy(self, inventory: InventoryPage, product_names: list[str]) -> OrderCompletePage:
        with allure.step(f"Khareedo: {product_names}"):
            for name in product_names:
                inventory.products.add(name)
            inventory.header.open_cart()
            return CartPage(self._page).wait_until_loaded().checkout()
