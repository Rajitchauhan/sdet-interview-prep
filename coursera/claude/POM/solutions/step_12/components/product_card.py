from playwright.sync_api import Locator


class ProductCard:
    """Ek product card. Page se nahi, apne 'root' locator se bana hai."""

    def __init__(self, root: Locator):
        self._root = root
        self.name: Locator = root.locator(".name")
        self.price: Locator = root.locator(".price")
        self.action_button: Locator = root.get_by_role("button")

    def add_to_cart(self):
        self._root.get_by_role("button", name="Add to cart").click()

    def remove_from_cart(self):
        self._root.get_by_role("button", name="Remove").click()
