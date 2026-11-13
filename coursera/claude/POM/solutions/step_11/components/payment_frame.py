from playwright.sync_api import Locator, Page


class PaymentFrame:
    """Page ke andar ek iframe ka form."""

    def __init__(self, page: Page):
        frame = page.frame_locator("iframe[title='Payment']")
        self._card_number = frame.get_by_label("Card number")
        self._pay_button = frame.get_by_role("button", name="Pay now")
        self.message: Locator = frame.locator("#msg")

    def pay(self, card_number: str):
        self._card_number.fill(card_number)
        self._pay_button.click()
