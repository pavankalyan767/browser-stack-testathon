# mobile_store_tests/config/test_data.py

class TestData:
    """Holds constant data for the test suite."""
    BASE_URL = "https://bugbash.online/"
    BROWSER = "chrome"

    # --- Login Credentials ---
    VALID_USER = "demouser"
    VALID_PASSWORD = "testingisfun99"

    # --- Sample Shipping Info ---
    SHIPPING_FIRST_NAME = "Test"
    SHIPPING_LAST_NAME = "User"
    SHIPPING_ADDRESS = "123 Automation Lane"
    SHIPPING_STATE = "Test State"
    SHIPPING_POSTAL_CODE = "12345"