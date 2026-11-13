from playwright.sync_api import Locator, Page

from components.order_details_modal import OrderDetailsModal


class OrderRow:
    def __init__(self, root: Locator, page: Page):
        self._page = page
        self.customer: Locator = root.get_by_test_id("customer")
        self.status: Locator = root.get_by_test_id("status")
        self.cancel_button: Locator = root.get_by_role("button", name="Cancel")
        self._details_button = root.get_by_role("button", name="Details")

    def cancel(self):
        self.cancel_button.click()

    def open_details(self) -> OrderDetailsModal:
        self._details_button.click()
        return OrderDetailsModal(self._page).wait_until_open()


class OrdersTable:
    def __init__(self, page: Page):
        self._page = page
        self.rows: Locator = page.get_by_test_id("order-row")

    def row_for(self, order_id: str) -> OrderRow:
        id_cell = self._page.get_by_test_id("order-id").get_by_text(order_id, exact=True)
        return OrderRow(self.rows.filter(has=id_cell), self._page)
