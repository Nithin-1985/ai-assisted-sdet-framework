import pytest
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


@pytest.fixture(scope="session")
def api_client():
    return APIClient(BASE_URL)





