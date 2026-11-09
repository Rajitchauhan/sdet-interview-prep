from playwright.sync_api import Page, expect


class OrderCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Thank you for your order!")

    def wait_until_loaded(self):
        expect(self.heading).to_be_visible()
