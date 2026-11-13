from playwright.sync_api import Locator, Page

from core.base_page import BasePage


class OrderCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="Thank you for your order!")

    @property
    def loaded_locator(self) -> Locator:
        return self.heading
