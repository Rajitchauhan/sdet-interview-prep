from playwright.sync_api import Page, expect

from pages.cart_page import CartPage


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self._heading = page.get_by_role("heading", name="Products")
        self.cart_badge = page.get_by_test_id("cart-count")
        self._cart_button = page.get_by_role("button", name="View Cart")
        self._cards = page.get_by_test_id("product")

    def wait_until_loaded(self):
        expect(self._heading).to_be_visible()

    def add_to_cart(self, product_name: str):
        self._cards.filter(has_text=product_name).get_by_role("button", name="Add to cart").click()

    def open_cart(self) -> CartPage:
        self._cart_button.click()
        cart = CartPage(self.page)
        cart.wait_until_loaded()
        return cart
