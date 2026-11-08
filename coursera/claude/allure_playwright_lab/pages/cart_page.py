import allure
from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator("#cart-items li")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def expect_items(self, names: list[str]):
        with allure.step(f"Cart me ye items hone chahiye: {names}"):
            expect(self.items).to_have_text(names)

    def checkout(self):
        with allure.step("Checkout karo"):
            self.checkout_button.click()
            expect(self.page.get_by_role("heading", name="Thank you for your order!")).to_be_visible()
