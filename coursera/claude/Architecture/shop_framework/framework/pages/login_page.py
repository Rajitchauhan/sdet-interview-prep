"""PAGE: login page."""
from playwright.sync_api import Locator, Page

from framework.core.base_page import BasePage
from framework.core.steps import step


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

    @step("Login form bharke submit karo")
    def login(self, username: str, password: str):
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()
