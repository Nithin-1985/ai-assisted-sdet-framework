from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_form(page:Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()


def test_login_with_invalid_password(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("tomsmith", "wrongpassword")

    expect(page.get_by_text("Your password is invalid!")).to_be_visible()