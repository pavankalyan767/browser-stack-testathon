# mobile_store_tests/pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    The base page class which all other page objects will inherit from.
    Contains common methods for interacting with web elements.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def do_click(self, locator):
        """Waits for an element to be clickable and then clicks it."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def do_send_keys(self, locator, text):
        """Waits for an element to be visible and then sends keys to it."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        """Waits for an element to be visible and returns its text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_element_visible(self, locator):
        """Checks if an element is visible on the page."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def get_title(self):
        """Returns the title of the current page."""
        return self.driver.title