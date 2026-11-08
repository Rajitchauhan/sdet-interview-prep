import allure
import pytest
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.epic("ShopDemo")
@allure.feature("Login")
@allure.story("Valid login")
@allure.title("Valid user login karke products page dekh sakta hai")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_valid_login(page: Page, base_url):
    login = LoginPage(page, base_url)
    login.open()
    login.login("standard_user", "secret_sauce")
    InventoryPage(page).expect_loaded()
