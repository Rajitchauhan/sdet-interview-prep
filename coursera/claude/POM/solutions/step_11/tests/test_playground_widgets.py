from playwright.sync_api import expect


def test_payment_form_inside_iframe(playground):
    playground.payment.pay("4242424242424242")
    expect(playground.payment.message).to_have_text("Payment accepted")


def test_rating_widget_inside_shadow_dom(playground):
    playground.rating.rate(4)
    expect(playground.rating.value).to_have_text("Rating: 4")


def test_help_opens_in_new_tab(playground):
    help_page = playground.open_help()
    expect(help_page.loaded_locator).to_be_visible()
    assert help_page.page is not playground.page      # alag tab


def test_delete_account_confirmed(playground):
    playground.delete_account(confirm=True)
    expect(playground.account_status).to_have_text("Account deleted")


def test_delete_account_cancelled(playground):
    playground.delete_account(confirm=False)
    expect(playground.account_status).to_have_text("")
