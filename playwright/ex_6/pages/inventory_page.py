from playwright.sync_api import Page
from .cart_page import CartPage

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

    def get_product_card(self, product_name: str):
        product_card = self.page.locator(".inventory_item").filter(has_text=product_name)
        return product_card

    def get_product_name(self, product_name: str):
        return self.get_product_card(product_name).locator(".inventory_item_name")

    def get_product_price(self, product_name: str):
        return self.get_product_card(product_name).locator(".inventory_item_price")

    def add_product_to_cart(self, product_name: str):
        self.get_product_card(product_name).get_by_role("button", name="Add to cart").click()       

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()
        return CartPage(self.page)
    