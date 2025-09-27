


# This file tells BrowserStack how to run your tests

import os 
from dotenv import load_dotenv


BROWSERSTACK_USERNAME = os.getenv('USER_NAME')
BROWSERSTACK_ACCESS_KEY = os.getenv('ACCESS_KEY')

def get_browserstack_capabilities(test_name):
    return {
        'browserName': 'Chrome',                  # Which browser to use
        'os': 'Windows',                          # Which operating system
        'projectName': 'Mobile Store Testathon',  # Project name in BS dashboard
        'sessionName': test_name,                 # Test name in BS dashboard
    }