from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    # Locators - UPDATE THESE
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ADDRESS = (By.ID, "address")
    STATE = (By.ID, "state")
    ZIP_CODE = (By.ID, "zip-code")
    SUBMIT_BTN = (By.ID, "submit-order")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "confirmation")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")
    
    def fill_address_form(self, address_data):
        """Fill the entire checkout form"""
        self.enter_text(self.FIRST_NAME, address_data["first_name"])
        self.enter_text(self.LAST_NAME, address_data["last_name"])
        self.enter_text(self.ADDRESS, address_data["address"])
        self.enter_text(self.STATE, address_data["state"])
        self.enter_text(self.ZIP_CODE, address_data["zip_code"])
    
    def submit_order(self):
        """Click submit order button"""
        self.click(self.SUBMIT_BTN)
    
    def is_order_successful(self):
        """Check if order confirmation appears"""
        return self.is_element_visible(self.SUCCESS_MESSAGE)
    
    def get_error_message(self):
        """Get validation error message if any"""
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return None