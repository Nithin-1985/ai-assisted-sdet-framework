from config.logger import setup_logger
logger = setup_logger(__name__)
from playwright.sync_api import Page
import allure


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button   = page.get_by_role("button",name = "Login")
    
    @allure.step("Open login page")
    def open(self):
        logger.info("Opening login page")
        self.page.goto("https://the-internet.herokuapp.com/login")
        self.username_input.wait_for(state="visible")
        logger.info("Login page opened successfully")

    @allure.step("Login as user: {username}")
    def login(self, username: str, password: str):
        allure.dynamic.parameter(
            "password",
            password,
            mode=allure.parameter_mode.MASKED
        )

        logger.info(f"Attempting login for user: {username}")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()