from playwright.sync_api import sync_playwright


def test_browser_context_isolation():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        # Two isolated browser contexts
        context = browser.new_context()
    

        # One page inside each context
        page1 = context.new_page()
        page2 = context.new_page()

        # Both visit the same website
        page1.goto("https://example.com")
        page2.goto("https://example.com")

        # Store something only in Context 1
        page1.evaluate(
            "localStorage.setItem('username', 'Nithin')"
        )

        # Read it from both contexts
        value1 = page1.evaluate(
            "localStorage.getItem('username')"
        )

        value2 = page2.evaluate(
            "localStorage.getItem('username')"
        )

        print("Context", value1)
    

        context.close()
        browser.close()


def test_new_tab(page):

    page.goto("https://the-internet.herokuapp.com/windows")

    with page.context.expect_page() as new_page_info:
        page.get_by_text("Click Here").click()

    new_page = new_page_info.value

    print("Original page:", page.title())
    print("New page:", new_page.title())