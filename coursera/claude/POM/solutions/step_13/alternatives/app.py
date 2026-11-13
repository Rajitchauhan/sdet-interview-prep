from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class ShopApp:
    """Facade: ek object se saare pages. Pages wahi, bas milne ka tareeka alag."""

    def __init__(self, page: Page):
        self._page = page

    @property
    def login(self) -> LoginPage:
        return LoginPage(self._page)

    @property
    def inventory(self) -> InventoryPage:
        return InventoryPage(self._page)

    @property
    def cart(self) -> CartPage:
        return CartPage(self._page)
