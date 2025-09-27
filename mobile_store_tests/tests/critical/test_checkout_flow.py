# mobile_store_tests/tests/critical/test_checkout_flow.py

import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.signin import SignInPage
from pages.checkout_page import CheckoutPage
from config.test_data import TestData

@pytest.mark.usefixtures("driver")
class TestCheckoutFlow:

    def test_happy_path_checkout(self):
        """
        Tests the full checkout flow: Add item -> Go to cart -> Login -> Fill shipping.
        """
        # 1. Add an item to the cart from the home page
        home_page = HomePage(self.driver)
        home_page.add_first_item_to_cart()
        home_page.open_cart()

        # 2. Click checkout from the cart view
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()

        # 3. On the Sign In page, log in with a valid user
        signin_page = SignInPage(self.driver)
        signin_page.login(TestData.VALID_USER, TestData.VALID_PASSWORD)

        # 4. On the Checkout page, fill shipping info and submit
        checkout_page = CheckoutPage(self.driver)
        assert "checkout" in self.driver.current_url, "Did not redirect to checkout after login"
        
        checkout_page.fill_shipping_and_submit(
            TestData.SHIPPING_FIRST_NAME,
            TestData.SHIPPING_LAST_NAME,
            TestData.SHIPPING_ADDRESS,
            TestData.SHIPPING_STATE,
            TestData.SHIPPING_POSTAL_CODE
        )

        # 5. Assert that the order was successful
        # This final step depends on your site's confirmation page.
        # This example checks for a confirmation heading.
        confirmation_message = checkout_page.get_confirmation_header()
        assert "Thank you" in confirmation_message, "Order confirmation message not found."