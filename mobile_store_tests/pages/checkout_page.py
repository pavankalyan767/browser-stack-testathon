# Handles checkout form and submission
class CheckoutPage(BasePage):
    def fill_shipping_address(self, address): pass # Fill all address fields
    def submit_order(self): pass             # Click submit button
    def is_order_confirmed(self): pass       # Check if order succeeded