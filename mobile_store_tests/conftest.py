import pytest
import json
from selenium import webdriver
from config.browserstack_config import BROWSERSTACK_URL, get_browserstack_capabilities

@pytest.fixture(scope='function')
def browser(request):
    # Setup BrowserStack connection
    capabilities = get_browserstack_capabilities(request.node.name)
    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        desired_capabilities=capabilities
    )
    
    # Navigate to test website - UPDATE THIS URL
    driver.get("https://your-testathon-website.com")
    
    yield driver
    
    # Teardown
    driver.quit()