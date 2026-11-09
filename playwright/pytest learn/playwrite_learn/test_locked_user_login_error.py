

def test_locked_user_login_error(page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("locked_out_user")
    page.locator("#password").fill("secret_sauce") 
    
    page.locator("#login-button").click()

    # Step 4: Extract text from error container
    error_msg = page.locator("[data-test='error']").text_content()

    # Step 5: Verify the exact locked out message
    assert "Sorry, this user has been locked out." in error_msg

