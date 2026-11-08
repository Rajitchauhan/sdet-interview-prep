import allure
import pytest
from playwright.sync_api import expect

from framework.data.products import BACKPACK
from framework.pages.inventory_page import InventoryPage

pytestmark = pytest.mark.demo_failure   # ye test JAAN-BOOJH ke fail hota hai


@allure.feature("Failure evidence")
def test_cart_badge_in_bug_mode(authenticated_page, shop_api):
    shop_api.add_to_cart(BACKPACK.id)                                  # setup API se (fast)
    inventory = InventoryPage(authenticated_page).open(query="?bug=1") # app ka BUG mode
    expect(inventory.header.cart_badge).to_have_text("1", timeout=2000)
