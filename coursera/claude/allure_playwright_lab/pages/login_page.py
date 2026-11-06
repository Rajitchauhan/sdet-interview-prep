import allure
from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error = page.get_by_role("alert")

    def open(self, query: str = ""):
        with allure.step("Login page kholo"):
            self.page.goto(self.base_url + query)

    def login(self, username: str, password: str):
        # NOTE: context manager use kiya, decorator nahi: password step ke parameters me nahi jaata
        with allure.step(f"Login karo: user = {username}"):
            self.username.fill(username)
            self.password.fill(password)
            self.login_button.click()

    def expect_error(self, message: str):
        with allure.step(f"Error message dikhna chahiye: {message}"):
            expect(self.error).to_have_text(message)
