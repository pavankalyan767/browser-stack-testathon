# mobile_store_tests/pages/cart_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page Object for the Cart view."""

    # --- Locators ---
    CHECKOUT_BUTTON = (By.CLASS_NAME, "buy-btn")
    SUBTOTAL_VALUE = (By.CLASS_NAME, "sub-price__val")
    EMPTY_CART_MESSAGE = (By.CLASS_NAME, "shelf-empty")

    # --- Initializer ---
    def __init__(self, driver):
        super().__init__(driver)

    # --- Page Actions ---
    def get_subtotal(self) -> float:
        """Returns the cart subtotal as a float."""
        text = self.get_element_text(self.SUBTOTAL_VALUE)
        # Assuming the text is something like "$ 10.90", remove non-numeric characters
        return float(''.join(c for c in text if c.isdigit() or c == '.'))

    def is_cart_empty(self) -> bool:
        """Checks if the 'cart is empty' message is visible."""
        return self.is_element_visible(self.EMPTY_CART_MESSAGE)

    def click_checkout(self):
        """Clicks the checkout button."""
        self.do_click(self.CHECKOUT_BUTTON)