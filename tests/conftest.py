import pytest
from playwright.sync_api import Page


@pytest.fixture
def playwright_home(page: Page):
    page.goto("https://playwright.dev/")
    return page