import pytest
from playwright.sync_api import Page


@pytest.fixture
def playwright_home(page: Page):
    print("\nSETUP: Opening Playwright homepage")

    page.goto("https://playwright.dev/")

    yield page

    print("\nTEARDOWN: Test has finished")