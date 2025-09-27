import os 
from dotenv import load_dotenv

load_dotenv()
BROWSERSTACK_USERNAME = "pranavsrinivas_EvYlkc"
BROWSERSTACK_ACCESS_KEY = "nzxbAX2DZJPYsAHysRMS"
BROWSERSTACK_URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub.browserstack.com/wd/hub"

print(f"here inside the config , loading the environment variables {BROWSERSTACK_USERNAME} and {BROWSERSTACK_ACCESS_KEY}")

def get_browserstack_capabilities(test_name):
    return {
        'browserName': 'Chrome',                  # Which browser to use
        'os': 'Windows',                          # Which operating system
        'projectName': 'Mobile Store Testathon',  # Project name in BS dashboard
        'sessionName': test_name,                 # Test name in BS dashboard
    }