from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("Zip/Postal Code").fill(postal_code)

    def continue_to_overview(self):
        self.page.get_by_role("button", name="Continue").click()

    def finish_checkout(self):
        self.page.get_by_role("button", name="Finish").click()

    def get_checkout_complete_message(self):
        return self.page.get_by_text("THANK YOU FOR YOUR ORDER")