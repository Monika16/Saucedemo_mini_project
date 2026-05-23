from playwright.sync_api import Page, expect


def test_inventory_items(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    page.wait_for_timeout(2000)
    all_items = page.locator(".inventory_item")
    #print(len(all_items))
    expect(all_items).to_have_count(6)