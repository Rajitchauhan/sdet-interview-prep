from playwright.sync_api import Locator, Page, expect


class BasePage:
    path = "/"

    def __init__(self, page: Page):
        self.page = page

    @property
    def loaded_locator(self) -> Locator:
        raise NotImplementedError("Child page 'loaded_locator' define kare")

    def wait_until_loaded(self):
        expect(self.loaded_locator).to_be_visible()
        return self

    def open(self):
        self.page.goto(self.path)
        return self.wait_until_loaded()
