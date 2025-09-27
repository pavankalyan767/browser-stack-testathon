import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage

class TestCartManagement:
    def test_add_remove_items(self, browser):
        """Test adding and removing items from cart"""
        home_page = HomePage(browser)
        cart_page = CartPage(browser)
        
        # 1. Add item
        home_page.add_first_product_to_cart()
        assert home_page.get_cart_count() == "1", "Item not added to cart"
        
        # 2. Go to cart and remove item
        home_page.go_to_cart()
        initial_count = cart_page.get_item_count()
        cart_page.remove_first_item()
        
        # 3. Verify cart is empty
        home_page.go_to_cart()  # Refresh cart view
        final_count = cart_page.get_item_count()
        assert final_count < initial_count, "Item not removed from cart"
        
        print("✅ Cart management test PASSED - Add/remove working")