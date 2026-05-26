from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page:Page):
        self.page = page

    def load(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username:str):
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill("secret_sauce")
        self.page.locator("#login-button").click()