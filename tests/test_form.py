from playwright.sync_api import Page, expect
import allure

@allure.feature("Authentication")
@allure.story("Login")
@allure.title("Login with valid credentials")
def test_login_form(login_page):
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    with allure.step("Verify login was successful"):
        expect(login_page.page).to_have_url(
            "https://the-internet.herokuapp.com/secure"
        )

        expect(
            login_page.page.get_by_text("You logged into a secure area!")
        ).to_be_visible()

@allure.feature("Authentication")
@allure.story("Login")
@allure.title("Login with invalid password")
def test_login_with_invalid_password(page: Page, login_page):

    login_page.open()
    login_page.login("tomsmith", "wrongpassword")

    expect(page.get_by_text("Your password is invalid!")).to_be_visible()

@allure.feature("Authentication")
@allure.story("Secure Area")
@allure.title("Verify secure page after login")
def test_secure_page(logged_in_page):

    expect(logged_in_page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )

    expect(
        logged_in_page.get_by_text("You logged into a secure area!")
    ).to_be_visible()

@allure.feature("Authentication")
@allure.story("Secure Area")
@allure.title("Verify logout button is visible")
def test_logout_button_visible(logged_in_page):
    expect(
        logged_in_page.get_by_role("link", name="Logout")
    ).to_be_visible()


