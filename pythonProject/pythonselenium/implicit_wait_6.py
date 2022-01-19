# Synchronization explicit wait , implicit wait
# implicit wait
# explicit wait

# pause te test for few seconds suing time class
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)  # no need to add every where it will work with driver objct
# wait until 5 second if object is not displayed
# Global wait , its intelligent enough if it get obj in 2 sec it will move to next step wont wiat till 5 sec
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()

driver.find_element_by_css_selector("input[class='search-keyword']").send_keys("ber")
time.sleep(3)

count = len(driver.find_elements_by_xpath("//div[@class='product']"))
assert count == 3
addItem = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for item in addItem:
    item.click()
    print(item)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button[class='promoBtn']").click()
print(driver.find_element_by_css_selector("span[class='promoInfo']").text)