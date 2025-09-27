from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://bugbash.online")

# Grab by ID
ids = [el.get_attribute("id") for el in driver.find_elements(By.XPATH, "//*[@id]")]

# Grab by name
names = [el.get_attribute("name") for el in driver.find_elements(By.XPATH, "//*[@name]")]

# Grab by class
classes = [el.get_attribute("class") for el in driver.find_elements(By.XPATH, "//*[@class]")]

# Grab all links (with hrefs)
links = [el.get_attribute("href") for el in driver.find_elements(By.TAG_NAME, "a")]

# Grab all buttons
buttons = [el.text for el in driver.find_elements(By.TAG_NAME, "button")]

print("IDs:", ids)
print("Names:", names)
print("Classes:", classes)
print("Links:", links)
print("Buttons:", buttons)
