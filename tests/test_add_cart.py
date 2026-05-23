from playwright.sync_api import Page, expect


def test_add_cart(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    page.wait_for_timeout(2000)
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#shopping_cart_container").click()
    items = page.locator(".cart_item")
    expect(items).to_have_count(1)