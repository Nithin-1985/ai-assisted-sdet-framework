import pytest
import os
import allure

from config.settings import (
    BASE_URL,
    API_USERNAME,
    API_PASSWORD,
    BROWSER,
    ENVIRONMENT,
)

from playwright.sync_api import Page
from pages.login_page import LoginPage
from api.client import APIClient
from config.settings import BASE_URL


@pytest.fixture
def playwright_home(page: Page):
    print("\nSETUP: Opening Playwright homepage")

    page.goto("https://playwright.dev/")

    yield page

    print("\nTEARDOWN: Test has finished")

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def logged_in_page(login_page):
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    return login_page.page


@pytest.fixture(scope="session")
def api_client():
    return APIClient(BASE_URL)




@pytest.fixture(scope="session")
def config():
    return {
        "base_url": BASE_URL,
        "username": API_USERNAME,
        "password": API_PASSWORD,
        "browser": BROWSER,
    }

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    print(f"Test phase: {report.when} | Result: {report.outcome}")

    if report.when == "call" and report.failed:
        print("Test failed - screenshot needed")

        login_page = item.funcargs.get("login_page")
        page = item.funcargs.get("page")

        if login_page:
            page = login_page.page

        if page:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )


def pytest_sessionstart(session):
    os.makedirs("allure-results", exist_ok=True)

    with open("allure-results/environment.properties", "w") as file:
        file.write(
            f"Environment={ENVIRONMENT}\n"
            f"Browser={BROWSER}\n"
        )