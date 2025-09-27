# mobile_store_tests/pages/home_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.test_data import TestData
# Make sure this import is at the top of the file
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    """Page Object for the Home Page."""

    # --- Locators ---
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "shelf-item__buy-btn")
    CART_ICON_QUANTITY = (By.CLASS_NAME, "bag__quantity")
    CART_ICON = (By.CLASS_NAME, "float-cart")

    # --- Initializer ---
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # --- Page Actions ---

    #
    # === REPLACE THIS METHOD ===
    #
    def add_first_item_to_cart(self):
        """
        Finds the first 'Add to cart' button, clicks it, and crucially,
        waits for the cart count on the icon to update.
        """
        self.do_click(self.ADD_TO_CART_BUTTON)

        # NEW: Wait for the cart count to appear and become '1'
        self.wait.until(
            EC.text_to_be_present_in_element(self.CART_ICON_QUANTITY, "1"),
            "Cart count did not update to 1 after adding an item."
        )
    #
    # === END OF REPLACEMENT ===
    #

    def get_cart_item_count(self):
        """Returns the number displayed on the cart icon."""
        if self.is_element_visible(self.CART_ICON_QUANTITY):
            return int(self.get_element_text(self.CART_ICON_QUANTITY))
        return 0

    def open_cart(self):
        """Clicks the cart icon to open the cart view."""
        self.do_click(self.CART_ICON)