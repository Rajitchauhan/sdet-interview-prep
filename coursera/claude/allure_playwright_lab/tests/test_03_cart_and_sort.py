import allure
import pytest
from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.allure_helpers import attach_screenshot


@pytest.fixture
def inventory(page: Page, base_url) -> InventoryPage:
    login = LoginPage(page, base_url)
    login.open()
    login.login("standard_user", "secret_sauce")
    inv = InventoryPage(page)
    inv.expect_loaded()
    return inv


@allure.epic("ShopDemo")
@allure.feature("Cart")
class TestCart:

    @allure.story("Add to cart")
    @allure.title("Ek product add karne par cart count 1 hota hai")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_add_one_item(self, page: Page, inventory: InventoryPage):
        inventory.add_to_cart("Backpack")
        expect(inventory.cart_count).to_have_text("1")
        attach_screenshot(page, "cart-after-add")

    @allure.story("Cart contents")
    @allure.title("Cart me wahi items dikhte hain jo add kiye")
    @pytest.mark.regression
    def test_cart_contents(self, page: Page, inventory: InventoryPage):
        inventory.add_to_cart("Backpack")
        inventory.add_to_cart("Onesie")
        inventory.open_cart()
        CartPage(page).expect_items(["Backpack", "Onesie"])


@allure.epic("ShopDemo")
@allure.feature("Sorting")
@pytest.mark.regression
@pytest.mark.parametrize(
    "label, expected_names",
    [
        ("Name (A to Z)", ["Backpack", "Bike Light", "Onesie"]),
        ("Name (Z to A)", ["Onesie", "Bike Light", "Backpack"]),
        ("Price (low to high)", ["Onesie", "Bike Light", "Backpack"]),
        ("Price (high to low)", ["Backpack", "Bike Light", "Onesie"]),
    ],
)
def test_sorting(inventory: InventoryPage, label, expected_names):
    allure.dynamic.title(f"Sorting: {label}")
    inventory.sort_by(label)
    expect(inventory.names).to_have_text(expected_names)
