from contextlib import contextmanager

import allure
from playwright.sync_api import Page


def attach_screenshot(page: Page, name: str, full_page: bool = False) -> None:
    """Page ka screenshot memory se seedha Allure me attach karo."""
    allure.attach(
        page.screenshot(full_page=full_page),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


@contextmanager
def step_shot(page: Page, title: str):
    """Ek Allure step banao aur step KHATAM hone par (pass ya fail dono me) screenshot attach karo.
    Screenshot step ke ANDAR attach hota hai, isliye report me wahi step ke neeche dikhta hai."""
    with allure.step(title):
        try:
            yield
        finally:
            try:
                attach_screenshot(page, f"after: {title}")
            except Exception:
                pass   # screenshot fail hone se asli error mat chhupao
