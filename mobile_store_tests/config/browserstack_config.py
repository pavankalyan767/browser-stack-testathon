


# This file tells BrowserStack how to run your tests

import os 
from dotenv import load_dotenv

load_dotenv()
BROWSERSTACK_USERNAME = os.getenv('USER_NAME')
BROWSERSTACK_ACCESS_KEY = os.getenv('ACCESS_KEY')
print(f"here inside the config , loading the environment variables {BROWSERSTACK_USERNAME} and {BROWSERSTACK_ACCESS_KEY}")

def get_browserstack_capabilities(test_name):
    return {
        'browserName': 'Chrome',                  # Which browser to use
        'os': 'Windows',                          # Which operating system
        'projectName': 'Mobile Store Testathon',  # Project name in BS dashboard
        'sessionName': test_name,                 # Test name in BS dashboard
    }