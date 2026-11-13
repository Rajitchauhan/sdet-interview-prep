from playwright.sync_api import Page, expect

from pages.order_complete_page import OrderCompletePage


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self._heading = page.get_by_role("heading", name="Your Cart")
        self._checkout_button = page.get_by_role("button", name="Checkout")

    def wait_until_loaded(self):
        expect(self._heading).to_be_visible()

    def checkout(self) -> OrderCompletePage:
        self._checkout_button.click()
        done = OrderCompletePage(self.page)
        done.wait_until_loaded()
        return done
