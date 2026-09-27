from playwright.sync_api import Page, expect
from pages.checkout_page import CheckoutPage
class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def get_cart_item_by_name(self, item_name: str):
        return self.page.locator(".cart_item").filter(has_text=item_name)   

    def get_cart_item_price(self, item_name: str):
        cart_item = self.get_cart_item_by_name(item_name)
        return cart_item.locator(".inventory_item_price")

    def go_to_checkout(self):
        self.page.get_by_role("button" , name="Checkout").click()
        return CheckoutPage(self.page) 

   

