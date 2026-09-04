from playwright.sync_api import Page, expect


def test_playwright_homepage(page: Page):
    page.goto("https://playwright.dev/")

    expect(page).to_have_title(
        "Fast and reliable end-to-end testing for modern web apps | Playwright"
    )

def test_get_started_navigation(page: Page):
    page.goto("https://playwright.dev/")

    page.get_by_role("link", name="Get started").click()

    expect(page).to_have_url("https://playwright.dev/docs/intro")

    expect(page.get_by_role("heading", name="Installing Playwright")).to_be_visible()


def test_playwright_home_using_fixture(playwright_home: Page):

    expect(playwright_home).to_have_title(
        "Fast and reliable end-to-end testing for modern web apps | Playwright"
    )

    playwright_home.get_by_role("link", name="Get started").click()

    expect(
        playwright_home.get_by_role(
            "heading",
            name="Installing Playwright"
        )
    ).to_be_visible()