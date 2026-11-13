from playwright.sync_api import expect


def test_payment_form_inside_iframe(playground):
    playground.payment.pay("4242424242424242")
    expect(playground.payment.message).to_have_text("Payment accepted")


def test_rating_widget_inside_shadow_dom(playground):
    playground.rating.rate(4)
    expect(playground.rating.value).to_have_text("Rating: 4")
