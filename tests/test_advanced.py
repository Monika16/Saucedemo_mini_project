from playwright.sync_api import Page, expect, Playwright


def test_alert(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()
    result = page.locator("#result")
    page.wait_for_timeout(2000)
    expect(result).to_contain_text("successfully")

def test_frame(page:Page):
    page.goto("https://practice-automation.com/iframes/")
    page.wait_for_timeout(2000)
    target_frame= page.frame(name="top-iframe")
    target_frame.get_by_role("button", name="Search (Command+K)").click()
    search_box = target_frame.get_by_role("searchbox", name="Search")
    search_box.fill("dialogs")
    target_frame.wait_for_timeout(2000)
    search_box.press("Enter")
    target_frame.wait_for_timeout(4000)
    header=target_frame.locator(".theme-doc-markdown header h1").inner_text()
    assert "Dialogs" in header

def test_multiple_windows(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    first_page = context.new_page()

    first_page.goto("https://the-internet.herokuapp.com/windows")
    first_page.on("popup",lambda page:page.wait_for_load_state())
    first_page.get_by_role("link", name="Click Here").click()
    first_page.wait_for_timeout(3000)

    all_pages = context.pages
    assert len(all_pages) == 2
    assert all_pages[1].title() == "New Window"


