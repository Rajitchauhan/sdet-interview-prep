import allure
import pytest
from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.allure_helpers import step_shot


@allure.epic("ShopDemo")
@allure.feature("Checkout")
@allure.story("Happy path")
@allure.title("Login se order complete tak poora flow")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_full_checkout(page: Page, base_url):
    login = LoginPage(page, base_url)
    inv = InventoryPage(page)
    cart = CartPage(page)

    with step_shot(page, "1. Login page kholo"):
        login.open()

    with step_shot(page, "2. Valid user se login karo"):
        login.login("standard_user", "secret_sauce")
        inv.expect_loaded()

    with step_shot(page, "3. Bike Light cart me daalo"):
        inv.add_to_cart("Bike Light")
        expect(inv.cart_count).to_have_text("1")

    with step_shot(page, "4. Cart check karo"):
        inv.open_cart()
        cart.expect_items(["Bike Light"])

    with step_shot(page, "5. Checkout karo"):
        cart.checkout()
