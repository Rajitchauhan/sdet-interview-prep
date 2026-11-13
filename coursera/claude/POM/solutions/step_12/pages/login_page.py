from playwright.sync_api import Locator, Page

from core.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    path = "/"

    def __init__(self, page: Page):
        super().__init__(page)
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")
        self.error: Locator = page.get_by_role("alert")

    @property
    def loaded_locator(self) -> Locator:
        return self._login_button

    def attempt_login(self, username: str, password: str) -> "LoginPage":
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()
        return self

    def login_as(self, username: str, password: str) -> InventoryPage:
        self.attempt_login(username, password)
        return InventoryPage(self.page).wait_until_loaded()
