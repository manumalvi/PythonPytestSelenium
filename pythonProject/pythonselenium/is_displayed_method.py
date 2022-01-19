from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print(driver.find_element_by_id("displayed-text").is_displayed())
assert driver.find_element_by_id("displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()

print(driver.find_element_by_id("displayed-text").is_displayed())

assert not driver.find_element_by_id("displayed-text").is_displayed()