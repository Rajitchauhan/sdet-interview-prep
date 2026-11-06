from pathlib import Path

import allure
import pytest
from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def inventory(page: Page, base_url) -> InventoryPage:
    login = LoginPage(page, base_url)
    login.open()
    login.login("standard_user", "secret_sauce")
    inv = InventoryPage(page)
    inv.expect_loaded()
    return inv


@allure.epic("ShopDemo")
@allure.feature("Screenshot techniques")
class TestScreenshotTechniques:

    @allure.title("A) bytes se seedha attach (disk par file nahi)")
    def test_attach_bytes(self, page: Page, inventory):
        allure.attach(page.screenshot(), name="page-bytes",
                      attachment_type=allure.attachment_type.PNG)

    @allure.title("B) file save karke attach.file")
    def test_attach_file(self, page: Page, inventory, tmp_path: Path):
        path = tmp_path / "inventory.png"
        page.screenshot(path=str(path))
        allure.attach.file(str(path), name="page-file",
                           attachment_type=allure.attachment_type.PNG)

    @allure.title("C) sirf ek element ka screenshot")
    def test_element(self, page: Page, inventory):
        card = page.locator("[data-testid=product]").first
        allure.attach(card.screenshot(), name="first-product-card",
                      attachment_type=allure.attachment_type.PNG)

    @allure.title("D) full page screenshot")
    def test_full_page(self, page: Page, inventory):
        allure.attach(page.screenshot(full_page=True), name="full-page",
                      attachment_type=allure.attachment_type.PNG)

    @allure.title("E) sensitive/dynamic hissa mask karna")
    def test_mask(self, page: Page, inventory):
        allure.attach(page.screenshot(mask=[inventory.sort]), name="sort-masked",
                      attachment_type=allure.attachment_type.PNG)

    @allure.title("F) JPEG (chhoti file size)")
    def test_jpeg(self, page: Page, inventory):
        allure.attach(page.screenshot(type="jpeg", quality=60), name="page-jpeg",
                      attachment_type=allure.attachment_type.JPG)
