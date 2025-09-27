# mobile_store_tests/pages/signin_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class SignInPage(BasePage):
    """Page Object for the Sign In page."""

    # --- Locators ---
    USERNAME_DROPDOWN = (By.ID, "username")
    PASSWORD_DROPDOWN = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")

    # --- NEW: Specific locators for each input field ---
    # This finds the input only within the username dropdown component
    USERNAME_INPUT = (By.CSS_SELECTOR, "div#username input[id^='react-select-']")
    # This finds the input only within the password dropdown component
    PASSWORD_INPUT = (By.CSS_SELECTOR, "div#password input[id^='react-select-']")

    # --- Initializer ---
    def __init__(self, driver):
        super().__init__(driver)

    # --- Page Actions ---
    def login(self, username, password):
        """
        Performs the complete login action using the custom dropdowns.
        """
        # Handle username
        self.do_click(self.USERNAME_DROPDOWN)
        # Use the NEW specific locator for the username input
        self.do_send_keys(self.USERNAME_INPUT, username + Keys.ENTER)

        # Handle password
        self.do_click(self.PASSWORD_DROPDOWN)
        # Use the NEW specific locator for the password input
        self.do_send_keys(self.PASSWORD_INPUT, password + Keys.ENTER)

        # Click login button
        self.do_click(self.LOGIN_BUTTON)