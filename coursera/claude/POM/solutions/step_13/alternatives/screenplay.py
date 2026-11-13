from playwright.sync_api import Locator, Page


class Actor:
    """Screenplay-lite: Actor TASKS karta hai aur QUESTIONS puchta hai."""

    def __init__(self, name: str, page: Page):
        self.name = name
        self.page = page

    def attempts_to(self, *tasks) -> None:
        for task in tasks:
            task.perform_as(self)

    def sees(self, question) -> Locator:
        return question.answered_by(self)


class Login:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    def perform_as(self, actor: Actor) -> None:
        page = actor.page
        page.goto("/")
        page.get_by_placeholder("Username").fill(self._username)
        page.get_by_placeholder("Password").fill(self._password)
        page.get_by_role("button", name="Login").click()


class AddToCart:
    def __init__(self, product_name: str):
        self._product_name = product_name

    def perform_as(self, actor: Actor) -> None:
        card = actor.page.get_by_test_id("product").filter(has_text=self._product_name)
        card.get_by_role("button", name="Add to cart").click()


class CartBadge:
    def answered_by(self, actor: Actor) -> Locator:
        return actor.page.get_by_test_id("cart-count")
