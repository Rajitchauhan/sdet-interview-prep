from playwright.sync_api import Locator, Page

from core.base_page import BasePage


class HelpPage(BasePage):
    path = "/help.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self._heading = page.get_by_role("heading", name="Help Center")

    @property
    def loaded_locator(self) -> Locator:
        return self._heading
