from playwright.sync_api import Locator, Page, expect


class OrderDetailsModal:
    def __init__(self, page: Page):
        self.root: Locator = page.get_by_role("dialog", name="Order details")
        self.title: Locator = self.root.get_by_role("heading")
        self._close_button = self.root.get_by_role("button", name="Close")

    def wait_until_open(self):
        expect(self.root).to_be_visible()
        return self

    def close(self):
        self._close_button.click()
