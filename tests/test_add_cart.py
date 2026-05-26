from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_add_cart(page:Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user")
    page.wait_for_timeout(2000)
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#shopping_cart_container").click()
    items = page.locator(".cart_item")
    expect(items).to_have_count(1)