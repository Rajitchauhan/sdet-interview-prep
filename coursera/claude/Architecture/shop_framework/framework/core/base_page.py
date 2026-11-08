"""CORE layer: har Page Object ka base class."""
from playwright.sync_api import Locator, Page, expect


class BasePage:
    """Yahan sirf wo cheezein jo SAB pages ko chahiye."""

    path = "/"   # child page apna path override karta hai

    def __init__(self, page: Page):
        self.page = page

    @property
    def loaded_locator(self) -> Locator:
        """Wo element jo dikhe to maanenge ki page load ho gaya."""
        raise NotImplementedError("Child page 'loaded_locator' define kare")

    def wait_until_loaded(self):
        expect(self.loaded_locator).to_be_visible()
        return self

    def open(self, query: str = ""):
        self.page.goto(self.path + query)
        return self.wait_until_loaded()
