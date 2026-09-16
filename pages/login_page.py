from config.logger import setup_logger
logger = setup_logger(__name__)
from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button   = page.get_by_role("button",name = "Login")

    def open(self):
        logger.info("Opening login page")
        self.page.goto("https://the-internet.herokuapp.com/login")
        logger.info("Login page opened successfully")

    def login(self, username: str, password: str):
        logger.info(f"Attempting login for user: {username}")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()