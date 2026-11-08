import allure
import pytest
from playwright.sync_api import expect

from framework.data.products import ALL_PRODUCTS, BACKPACK, ONESIE

# Expected order DATA se nikalta hai (copy-paste list nahi)
SORT_RULES = {
    "Name (A to Z)": lambda ps: sorted(ps, key=lambda p: p.name),
    "Name (Z to A)": lambda ps: sorted(ps, key=lambda p: p.name, reverse=True),
    "Price (low to high)": lambda ps: sorted(ps, key=lambda p: p.price),
    "Price (high to low)": lambda ps: sorted(ps, key=lambda p: p.price, reverse=True),
}


@allure.feature("Inventory")
@pytest.mark.regression
@pytest.mark.parametrize("label", SORT_RULES)
def test_sorting(inventory_page, label):
    expected_names = [p.name for p in SORT_RULES[label](ALL_PRODUCTS)]
    inventory_page.sort_by(label)
    expect(inventory_page.products.names).to_have_text(expected_names)


@allure.feature("Inventory")
@pytest.mark.smoke
def test_add_and_remove_updates_badge(inventory_page):
    badge = inventory_page.header.cart_badge
    expect(badge).to_have_text("0")

    inventory_page.products.add(BACKPACK.name)
    expect(badge).to_have_text("1")

    inventory_page.products.add(ONESIE.name)
    expect(badge).to_have_text("2")

    inventory_page.products.remove(BACKPACK.name)
    expect(badge).to_have_text("1")
