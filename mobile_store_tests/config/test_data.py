# All the data your tests will use
class TestData:
    # Login credentials (provided by testathon)
    USERNAME = "testuser"
    PASSWORD = "testpass"
    
    # Address for checkout
    VALID_ADDRESS = {
        "first_name": "John",
        "last_name": "Doe", 
        "address": "123 Main St",
        "state": "CA",
        "zip_code": "94105"
    }
    
    # Vendor names for filtering
    VENDORS = ["Apple", "Samsung", "Google", "OnePlus"]