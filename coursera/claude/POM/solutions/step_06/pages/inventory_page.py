from playwright.sync_api import Locator, Page

from core.base_page import BasePage
from pages.cart_page import CartPage


class InventoryPage(BasePage):
    path = "/"

    def __init__(self, page: Page):
        super().__init__(page)
        self._heading = page.get_by_role("heading", name="Products")
        self.cart_badge = page.get_by_test_id("cart-count")
        self._cart_button = page.get_by_role("button", name="View Cart")
        self._cards = page.get_by_test_id("product")

    @property
    def loaded_locator(self) -> Locator:
        return self._heading

    def add_to_cart(self, product_name: str):
        self._cards.filter(has_text=product_name).get_by_role("button", name="Add to cart").click()

    def open_cart(self) -> CartPage:
        self._cart_button.click()
        return CartPage(self.page).wait_until_loaded()
