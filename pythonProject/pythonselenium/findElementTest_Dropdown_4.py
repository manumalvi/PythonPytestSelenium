# Auto Suggestion Concept , suggestion comes based on you input
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)

# if you type any thing and then inspect and it disapper then put some value and go to htat value and then do inspect
# observe here its Find elements
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

for county in countries:
    if county.text == "India":
        county.click()
        break
# after updating the text in page text method will not get it bcoz selenium gets only when page refresh
# so get_attribute will work

assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"

#driver.close()