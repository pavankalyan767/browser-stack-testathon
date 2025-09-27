# Handles cart page actions
class CartPage(BasePage):
    def get_cart_items(self): pass           # List all items in cart
    def update_quantity(self, item, qty): pass # Change item quantity
    def remove_item(self, item): pass        # Remove item from cart
    def proceed_to_checkout(self): pass      # Click checkout button