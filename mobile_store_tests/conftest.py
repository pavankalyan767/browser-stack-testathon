# mobile_store_tests/conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from config.test_data import TestData

@pytest.fixture(scope="class")
def driver(request):
    """
    Fixture to initialize and quit the WebDriver instance.
    This fixture has a 'class' scope, meaning it will be created once per test class.
    """
    browser_name = TestData.BROWSER.lower()
    print(f"--- Setting up driver for {browser_name} ---")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported.")

    driver.maximize_window()
    driver.implicitly_wait(2) # Implicit wait

    # Set the driver instance to the test class that calls this fixture
    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    print("--- Tearing down driver ---")
    driver.quit()