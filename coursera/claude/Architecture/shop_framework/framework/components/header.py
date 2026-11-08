"""COMPONENT: header (cart badge, cart button, logout). Kai pages par dikhta hai."""
from playwright.sync_api import Locator, Page

from framework.core.steps import step


class Header:
    def __init__(self, page: Page):
        self.cart_badge: Locator = page.get_by_test_id("cart-count")
        self._cart_button = page.get_by_role("button", name="View Cart")
        self._logout_button = page.get_by_role("button", name="Logout")

    @step("Cart kholo")
    def open_cart(self):
        self._cart_button.click()

    @step("Logout karo")
    def logout(self):
        self._logout_button.click()
