from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    # Locators - UPDATE THESE
    CART_ITEMS = (By.CLASS_NAME, "cart-item")
    CHECKOUT_BTN = (By.XPATH, "//button[contains(text(),'Checkout')]")
    REMOVE_BTN = (By.CLASS_NAME, "remove-item")
    QUANTITY_INPUT = (By.NAME, "quantity")
    
    def get_item_count(self):
        """Get number of items in cart"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def proceed_to_checkout(self):
        """Click checkout button"""
        self.click(self.CHECKOUT_BTN)
    
    def remove_first_item(self):
        """Remove the first item from cart"""
        if self.get_item_count() > 0:
            remove_buttons = self.driver.find_elements(*self.REMOVE_BTN)
            remove_buttons[0].click()
            return True
        return False