from playwright.sync_api import Page, expect
import allure
import pytest
from test_data.data_loader import load_json

pytestmark = pytest.mark.ui

def load_invalid_users():
    data = load_json("login_data.json")
    return data["invalid_users"]

@pytest.mark.smoke
@allure.feature("Authentication")
@allure.story("Login")
@allure.title("Login with valid credentials")
def test_login_form(login_page, login_data):
    login_page.open()
    username = login_data["valid_user"]["username"]
    password = login_data["valid_user"]["password"]
    login_page.login(username, password)

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
@pytest.mark.parametrize("invalid_user", load_invalid_users(),
    ids=[
        "wrong_password",
        "wrong_username",
        "wrong_username_and_password"
    ])
def test_login_with_invalid_password(page: Page, login_page, invalid_user):

    login_page.open()
    login_page.login(
        invalid_user["username"],
        invalid_user["password"]
    )

    expect(
    page.get_by_text(invalid_user["expected_message"])
    ).to_be_visible()

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


