# Synchronization explicit wait , implicit wait
# implicit wait
# explicit wait : it used to target only specific elemet, wait for few sec until some obj is display but implicit is applied to all

# pause te test for few seconds suing time class
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

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
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button[class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "promoInfo")))
print(driver.find_element_by_css_selector("span[class='promoInfo']").text)

# if you application is fast and lods quickly and SLA of like 2 sec from page to page then no point of using implicit wait
# use explicit wait for specific places like promo code etc