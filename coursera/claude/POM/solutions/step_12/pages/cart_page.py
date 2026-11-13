from playwright.sync_api import Locator, Page

from core.base_page import BasePage
from pages.order_complete_page import OrderCompletePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._heading = page.get_by_role("heading", name="Your Cart")
        self._checkout_button = page.get_by_role("button", name="Checkout")

    @property
    def loaded_locator(self) -> Locator:
        return self._heading

    def checkout(self) -> OrderCompletePage:
        self._checkout_button.click()
        return OrderCompletePage(self.page).wait_until_loaded()
