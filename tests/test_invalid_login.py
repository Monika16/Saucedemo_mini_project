from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_invalid_login(page:Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("user")
    page.wait_for_timeout(2000)
    error_msg=page.locator(".error-message-container h3")
    #print(error_msg.inner_text())
    expect(error_msg).to_contain_text("Username and password do not match")