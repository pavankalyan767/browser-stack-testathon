from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    # Locators - UPDATE THESE SELECTORS based on actual website
    PRODUCT_CARD = (By.CLASS_NAME, "product-card")  # Change to actual class
    ADD_TO_CART_BTN = (By.XPATH, ".//button[contains(text(),'Add to Cart')]")
    VENDOR_FILTER = (By.XPATH, f"//button[contains(text(),'{{}}')]")  # Template
    CART_COUNT = (By.ID, "cart-count")  # Change to actual ID
    CART_ICON = (By.ID, "cart-icon")    # Change to actual ID
    
    def add_first_product_to_cart(self):
        """Add the first product on the page to cart"""
        products = self.driver.find_elements(*self.PRODUCT_CARD)
        if products:
            add_button = products[0].find_element(*self.ADD_TO_CART_BTN)
            add_button.click()
            return True
        return False
    
    def add_product_by_vendor(self, vendor_name):
        """Add a product from a specific vendor"""
        # Click vendor filter
        vendor_locator = (self.VENDOR_FILTER[0], self.VENDOR_FILTER[1].format(vendor_name))
        self.click(vendor_locator)
        
        # Add first product
        return self.add_first_product_to_cart()
    
    def get_cart_count(self):
        """Get the number displayed on cart icon"""
        return self.get_text(self.CART_COUNT)
    
    def go_to_cart(self):
        """Click cart icon to go to cart page"""
        self.click(self.CART_ICON)