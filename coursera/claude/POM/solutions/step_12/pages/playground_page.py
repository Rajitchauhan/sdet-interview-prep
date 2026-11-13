from playwright.sync_api import Locator, Page

from components.orders_table import OrdersTable
from components.payment_frame import PaymentFrame
from components.rating_widget import RatingWidget
from core.base_page import BasePage
from pages.help_page import HelpPage


class PlaygroundPage(BasePage):
    path = "/playground.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self._heading = page.get_by_role("heading", name="Playground")
        self._open_help_button = page.get_by_role("button", name="Open help (new tab)")
        self._delete_account_button = page.get_by_role("button", name="Delete account")
        self.account_status: Locator = page.get_by_test_id("account-status")
        self.orders = OrdersTable(page)
        self.payment = PaymentFrame(page)
        self.rating = RatingWidget(page)

    @property
    def loaded_locator(self) -> Locator:
        return self._heading

    def open_help(self) -> HelpPage:
        """Naya tab khulta hai. Us naye tab ka page object lautao."""
        with self.page.expect_popup() as popup_info:
            self._open_help_button.click()
        return HelpPage(popup_info.value).wait_until_loaded()

    def delete_account(self, confirm: bool = True):
        """Browser ka confirm() dialog aata hai. Dialog ko accept ya dismiss karo."""
        self.page.once("dialog", lambda dialog: dialog.accept() if confirm else dialog.dismiss())
        self._delete_account_button.click()
