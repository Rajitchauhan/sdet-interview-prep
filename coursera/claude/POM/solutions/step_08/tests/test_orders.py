from playwright.sync_api import expect

from pages.playground_page import PlaygroundPage


def test_orders_table_shows_four_orders(page):
    playground = PlaygroundPage(page).open()
    expect(playground.orders.rows).to_have_count(4)


def test_pending_order_can_be_cancelled(page):
    playground = PlaygroundPage(page).open()
    row = playground.orders.row_for("1002")

    expect(row.status).to_have_text("Pending")
    row.cancel()

    expect(row.status).to_have_text("Cancelled")
    expect(row.cancel_button).to_have_count(0)


def test_order_details_modal_opens_and_closes(page):
    playground = PlaygroundPage(page).open()

    modal = playground.orders.row_for("1001").open_details()
    expect(modal.title).to_have_text("Order #1001")

    modal.close()
    expect(modal.root).to_be_hidden()
