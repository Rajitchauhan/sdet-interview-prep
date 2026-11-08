"""PAGE: products list page."""
import allure
from playwright.sync_api import Locator, Page

from framework.components.header import Header
from framework.components.product_list import ProductList
from framework.core.base_page import BasePage


class InventoryPage(BasePage):
    path = "/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.header = Header(page)
        self.products = ProductList(page)
        self._heading = page.get_by_role("heading", name="Products")
        self._sort = page.get_by_test_id("sort")

    @property
    def loaded_locator(self) -> Locator:
        return self._heading

    def sort_by(self, label: str):
        with allure.step(f"Sort karo: {label}"):
            self._sort.select_option(label=label)
