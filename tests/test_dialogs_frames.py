from playwright.sync_api import Page, expect 


def test_alert_dialog(page: Page):

    def handle_dialog(dialog):
        print(dialog.message)
        dialog.accept()

    page.on("dialog", handle_dialog)

    page.set_content("""
        <button onclick="alert('Hello from Playwright!')">
            Show Alert
        </button>
    """)

    page.get_by_role("button", name="Show Alert").click()




def test_confirm_dialog_cancel(page: Page):

    def handle_dialog(dialog):
        print(dialog.message)
        dialog.dismiss()

    page.on("dialog", handle_dialog)

    page.set_content("""
        <button onclick="
            document.getElementById('result').innerText =
                confirm('Do you want to continue?')
                ? 'You clicked: Ok'
                : 'You clicked: Cancel'
        ">
            Continue
        </button>

        <p id="result"></p>
    """)

    page.get_by_role(
        "button",
        name="Continue"
    ).click()

    expect(
        page.locator("#result")
    ).to_have_text("You clicked: Cancel")


def test_confirm_dialog_accept(page: Page):

    def handle_dialog(dialog):
        print(dialog.message)
        dialog.accept()

    page.on("dialog", handle_dialog)

    page.set_content("""
        <button onclick="
            document.getElementById('result').innerText =
                confirm('Do you want to continue?')
                ? 'You clicked: Ok'
                : 'You clicked: Cancel'
        ">
            Continue
        </button>

        <p id="result"></p>
    """)

    page.get_by_role(
        "button",
        name="Continue"
    ).click()

    expect(
        page.locator("#result")
    ).to_have_text("You clicked: Ok")


def test_prompt_dialog(page: Page):

    def handle_dialog(dialog):
        print(dialog.message)
        dialog.accept("Nithin")

    page.on("dialog", handle_dialog)

    page.set_content("""
        <button onclick="
            document.getElementById('result').innerText =
                'You entered: ' + prompt('Please enter your name')
        ">
            Enter Name
        </button>

        <p id="result"></p>
    """)

    page.get_by_role(
        "button",
        name="Enter Name"
    ).click()

    expect(
        page.locator("#result")
    ).to_have_text("You entered: Nithin")



def test_interactive_iframe(page: Page):

    page.goto(
        "https://playground.qajourney.net/iframes/"
    )

    iframe = page.frame_locator(
        '[data-testid="form-iframe"]'
    )


    input_field = iframe.locator(
    '[data-testid="iframe-input"]'
    )

    input_field.fill("Hello from Playwright")

    expect(input_field).to_have_value(
        "Hello from Playwright"
    )