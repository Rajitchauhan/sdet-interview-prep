from playwright.sync_api import Locator, Page

from core.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._heading = page.get_by_role("heading", name="Your Cart")
        self._checkout_button = page.get_by_role("button", name="Checkout")

    @property
    def loaded_locator(self) -> Locator:
        return self._heading

    def checkout(self):
        self._checkout_button.click()
