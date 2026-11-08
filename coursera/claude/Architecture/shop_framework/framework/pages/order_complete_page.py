"""PAGE: order complete (thank you) page."""
from playwright.sync_api import Locator, Page

from framework.core.base_page import BasePage


class OrderCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="Thank you for your order!")
        self._order_id = page.get_by_test_id("order-id")

    @property
    def loaded_locator(self) -> Locator:
        return self.heading

    def order_id(self) -> int:
        """'Order #1001' me se number nikalta hai."""
        return int(self._order_id.inner_text().replace("Order #", ""))
