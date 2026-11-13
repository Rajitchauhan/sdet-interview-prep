from playwright.sync_api import Locator, Page

from pages.inventory_page import InventoryPage


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")
        self.error: Locator = page.get_by_role("alert")

    def open(self):
        self.page.goto("/")

    def attempt_login(self, username: str, password: str) -> "LoginPage":
        """Login try karo. Kya hoga pata nahi (success ya error), isliye wahi page lautao."""
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()
        return self

    def login_as(self, username: str, password: str) -> InventoryPage:
        """Login jo SUCCESS hona chahiye. Agla page (inventory) lautao."""
        self.attempt_login(username, password)
        inventory = InventoryPage(self.page)
        inventory.wait_until_loaded()
        return inventory
