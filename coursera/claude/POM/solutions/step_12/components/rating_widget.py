from playwright.sync_api import Locator, Page


class RatingWidget:
    """Custom element <rating-widget> (open shadow DOM ke andar)."""

    def __init__(self, page: Page):
        self._root = page.locator("rating-widget")
        self.value: Locator = self._root.get_by_text("Rating:")

    def rate(self, stars: int):
        self._root.get_by_role("button", name=f"Rate {stars}").click()
