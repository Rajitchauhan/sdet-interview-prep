from playwright.sync_api import Locator, Page

from components.orders_table import OrdersTable
from components.payment_frame import PaymentFrame
from components.rating_widget import RatingWidget
from core.base_page import BasePage


class PlaygroundPage(BasePage):
    path = "/playground.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self._heading = page.get_by_role("heading", name="Playground")
        self.orders = OrdersTable(page)
        self.payment = PaymentFrame(page)
        self.rating = RatingWidget(page)

    @property
    def loaded_locator(self) -> Locator:
        return self._heading
