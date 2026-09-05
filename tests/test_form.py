from playwright.sync_api import Page, expect

def login(page: Page, username_value: str, password_value: str):
    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").fill(username_value)
    page.get_by_label("Password").fill(password_value)

    page.get_by_role("button", name="Login").click()



def test_login_form(page:Page):
    login(page,"tomsmith","SuperSecretPassword!")

    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()


def test_login_with_invalid_password(page: Page):
    login(page, "tomsmith", "wrongpassword")

    expect(page.get_by_text("Your password is invalid!")).to_be_visible()