import allure
from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Products")
        self.cart_count = page.get_by_test_id("cart-count")
        self.sort = page.get_by_test_id("sort")
        self.names = page.locator("[data-testid=product] .name")
        self.prices = page.locator("[data-testid=product] .price")

    def expect_loaded(self):
        with allure.step("Inventory page load honi chahiye"):
            expect(self.heading).to_be_visible()

    def add_to_cart(self, product_name: str):
        with allure.step(f"Cart me add karo: {product_name}"):
            card = self.page.locator("[data-testid=product]").filter(has_text=product_name)
            card.get_by_role("button", name="Add to cart").click()

    def sort_by(self, label: str):
        with allure.step(f"Sort karo: {label}"):
            self.sort.select_option(label=label)

    def open_cart(self):
        with allure.step("Cart kholo"):
            self.page.get_by_role("button", name="View Cart").click()
