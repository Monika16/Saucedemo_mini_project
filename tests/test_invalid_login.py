from playwright.sync_api import Page, expect


def test_invalid_login(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    page.wait_for_timeout(2000)
    error_msg=page.locator(".error-message-container h3")
    #print(error_msg.inner_text())
    expect(error_msg).to_contain_text("Username and password do not match")