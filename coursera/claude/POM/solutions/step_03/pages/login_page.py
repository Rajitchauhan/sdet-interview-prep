from playwright.sync_api import Locator, Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")
        self.error: Locator = page.get_by_role("alert")

    def open(self):
        self.page.goto("/")

    def login(self, username: str, password: str):
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()
