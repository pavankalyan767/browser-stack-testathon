# mobile_store_tests/pages/checkout_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    """Page Object for the Checkout Page."""

    # --- Locators for Shipping Form ---
    FIRST_NAME_INPUT = (By.ID, "firstNameInput")
    LAST_NAME_INPUT = (By.ID, "lastNameInput")
    ADDRESS_INPUT = (By.ID, "addressLine1Input")
    STATE_INPUT = (By.ID, "provinceInput")
    POSTAL_CODE_INPUT = (By.ID, "postCodeInput")
    SUBMIT_BUTTON = (By.ID, "checkout-shipping-continue")

    # --- NEW: Locators for Confirmation and Error States ---
    CONFIRMATION_HEADER = (By.CLASS_NAME, "optimizedCheckout-headingPrimary")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, ".continueButtonContainer button")
    # This locator assumes an error message element appears when validation fails.
    # It looks for a div that gets a specific class when an error is present.
    FORM_FIELD_ERROR = (By.CSS_SELECTOR, "div.form-field--error")


    # --- Initializer ---
    def __init__(self, driver):
        super().__init__(driver)

    # --- Page Actions ---
    def fill_shipping_and_submit(self, first_name, last_name, address, state, postal_code):
        """
        Fills in the entire shipping information form and clicks submit.
        """
        self.do_send_keys(self.FIRST_NAME_INPUT, first_name)
        self.do_send_keys(self.LAST_NAME_INPUT, last_name)
        self.do_send_keys(self.ADDRESS_INPUT, address)
        self.do_send_keys(self.STATE_INPUT, state)
        self.do_send_keys(self.POSTAL_CODE_INPUT, postal_code)
        self.do_click(self.SUBMIT_BUTTON)

    def get_confirmation_header(self):
        """
        Waits for the confirmation header to be visible and returns its text.
        """
        # Increased robustness by waiting for the element to be visible
        return self.get_element_text(self.CONFIRMATION_HEADER)

    def click_continue_shopping(self):
        """Clicks the 'Continue Shopping' button after a successful order."""
        self.do_click(self.CONTINUE_SHOPPING_BUTTON)

    def is_form_error_visible(self) -> bool:
        """
        Checks if a validation error message is visible on the form.
        Returns True if an error is found, False otherwise.
        """
        return self.is_element_visible(self.FORM_FIELD_ERROR)