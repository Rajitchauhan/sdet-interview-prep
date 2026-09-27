from playwright.sync_api import Page, expect
import pytest
from pages.login_page import LoginPage

@pytest.fixture
def auth_page(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    return page 

