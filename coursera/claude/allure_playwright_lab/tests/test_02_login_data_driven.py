import allure
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage

# Data ek jagah. Test ke parameters me sirf SCENARIO ka naam jayega,
# taaki password Allure ke parameters/test name me leak na ho.
LOGIN_CASES = {
    "locked-user": ("locked_user", "secret_sauce", "Sorry, this user has been locked out."),
    "wrong-password": ("standard_user", "wrong_pass", "Username and password do not match"),
    "unknown-user": ("nobody", "secret_sauce", "Username and password do not match"),
}


@allure.epic("ShopDemo")
@allure.feature("Login")
@allure.story("Invalid login")
@pytest.mark.regression
@pytest.mark.parametrize("scenario", list(LOGIN_CASES))
def test_invalid_login(page: Page, base_url, scenario):
    username, password, message = LOGIN_CASES[scenario]
    allure.dynamic.title(f"Invalid login: {scenario}")
    login = LoginPage(page, base_url)
    login.open()
    login.login(username, password)
    login.expect_error(message)
