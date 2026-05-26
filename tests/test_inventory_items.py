from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_inventory_items(page:Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user")
    all_items = page.locator(".inventory_item")
    #print(len(all_items))
    expect(all_items).to_have_count(6)