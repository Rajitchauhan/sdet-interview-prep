"""COMPONENT: products ki list (cards)."""
import allure
from playwright.sync_api import Locator, Page


class ProductList:
    def __init__(self, page: Page):
        self._cards = page.get_by_test_id("product")
        self.names: Locator = self._cards.locator(".name")
        self.prices: Locator = self._cards.locator(".price")

    def _card(self, name: str) -> Locator:
        return self._cards.filter(has_text=name)

    def button_for(self, name: str) -> Locator:
        return self._card(name).get_by_role("button")

    def add(self, name: str):
        with allure.step(f"Cart me add karo: {name}"):
            self._card(name).get_by_role("button", name="Add to cart").click()

    def remove(self, name: str):
        with allure.step(f"Cart se hatao: {name}"):
            self._card(name).get_by_role("button", name="Remove").click()
