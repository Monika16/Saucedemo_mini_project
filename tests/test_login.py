import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.parametrize("username",
        ["standard_user","problem_user","performance_glitch_user","error_user","visual_user"])
def test_login(page:Page, username:str):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(username)
    # page.goto("https://www.saucedemo.com/")
    # page.locator("#user-name").fill(username)
    # page.locator("#password").fill("secret_sauce")
    # page.locator("#login-button").click()
    expect(page.locator(".app_logo")).to_contain_text("Swag Labs")
    page.wait_for_timeout(2000)