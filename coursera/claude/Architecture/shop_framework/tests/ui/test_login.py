from dataclasses import replace

import allure
import pytest
from playwright.sync_api import expect

from framework.data.users import get_user
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage

_STANDARD = get_user("standard")

# Parametrize me sirf scenario ka NAAM jaata hai (password report/test-name me leak nahi hota)
LOGIN_ERROR_CASES = {
    "locked-user": (get_user("locked"), "Sorry, this user has been locked out."),
    "wrong-password": (replace(_STANDARD, password="wrong-password"), "Username and password do not match"),
    "unknown-user": (replace(_STANDARD, username="nobody"), "Username and password do not match"),
}


@allure.feature("Login")
@pytest.mark.smoke
def test_valid_user_reaches_inventory(page, user):
    LoginPage(page).open().login(user.username, user.password)
    InventoryPage(page).wait_until_loaded()


@allure.feature("Login")
@pytest.mark.regression
@pytest.mark.parametrize("scenario", LOGIN_ERROR_CASES)
def test_login_errors(page, scenario):
    bad_user, message = LOGIN_ERROR_CASES[scenario]
    login = LoginPage(page).open()
    login.login(bad_user.username, bad_user.password)
    expect(login.error).to_have_text(message)
