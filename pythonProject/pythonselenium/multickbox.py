import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
'''
# Find generic locator and then itrate through it
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

# to select all check box
# for checkbox in checkboxes:
#     checkbox.click()
#     assert checkbox.is_selected()

# to seect any specific check box
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
'''
# Radio button we can select all , can only select one at a time
radiobuttons = driver.find_elements_by_xpath("//input[@type='radio']")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()
