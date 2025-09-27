class TestData:
    # Since we're pre-logged in, just need address data
    VALID_ADDRESS = {
        "first_name": "Test",
        "last_name": "User",
        "address": "123 Main St", 
        "state": "California",
        "zip_code": "94105"
    }
    
    # Vendor names for filtering
    VENDORS = ["Apple", "Samsung", "Google", "OnePlus"]