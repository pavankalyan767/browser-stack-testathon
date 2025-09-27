import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.test_data import TestData

class TestCheckoutFlow:
    def test_happy_path_single_item(self, browser):
        """Happy Path: Add 1 item → Checkout → Success"""
        home_page = HomePage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)
        
        # 1. Add item to cart
        assert home_page.add_first_product_to_cart(), "Failed to add product to cart"
        
        # 2. Verify cart count
        cart_count = home_page.get_cart_count()
        assert cart_count == "1", f"Expected cart count 1, got {cart_count}"
        
        # 3. Go to cart and checkout
        home_page.go_to_cart()
        cart_page.proceed_to_checkout()
        
        # 4. Fill and submit checkout form
        checkout_page.fill_address_form(TestData.VALID_ADDRESS)
        checkout_page.submit_order()
        
        # 5. Verify success
        assert checkout_page.is_order_successful(), "Order confirmation not shown"
        print("✅ Happy path test PASSED - Single item checkout successful")
    
    def test_happy_path_multiple_items(self, browser):
        """Happy Path: Add 2 items from different vendors → Checkout"""
        home_page = HomePage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)
        
        # 1. Add first item
        assert home_page.add_first_product_to_cart(), "Failed to add first product"
        
        # 2. Add second item from different vendor
        assert home_page.add_product_by_vendor("Samsung"), "Failed to add Samsung product"
        
        # 3. Verify cart has 2 items
        cart_count = home_page.get_cart_count()
        assert cart_count == "2", f"Expected cart count 2, got {cart_count}"
        
        # 4. Complete checkout
        home_page.go_to_cart()
        cart_page.proceed_to_checkout()
        checkout_page.fill_address_form(TestData.VALID_ADDRESS)
        checkout_page.submit_order()
        
        assert checkout_page.is_order_successful(), "Multi-item order failed"
        print("✅ Happy path test PASSED - Multi-item checkout successful")
    
    def test_sad_path_empty_fields(self, browser):
        """Sad Path: Try checkout with empty required fields"""
        home_page = HomePage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)
        
        # 1. Add item and go to checkout
        home_page.add_first_product_to_cart()
        home_page.go_to_cart()
        cart_page.proceed_to_checkout()
        
        # 2. Try to submit without filling form
        checkout_page.submit_order()
        
        # 3. Verify error message
        error_message = checkout_page.get_error_message()
        assert error_message is not None, "Expected error message for empty form"
        print("✅ Sad path test PASSED - Form validation working")