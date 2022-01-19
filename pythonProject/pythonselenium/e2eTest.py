from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href='/angularpractice/shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()
driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()

assert driver.find_element_by_css_selector("h4[class='media-heading']").text == productName

driver.find_element_by_css_selector("button[class='btn btn-success']").click()

driver.find_element_by_id("country").send_keys("Ind")

wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element_by_link_text("India").click()

driver.find_element_by_css_selector("div[class='checkbox checkbox-primary").click()

driver.find_element_by_css_selector("input[type='submit']").click()

success_str = driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible").text

assert "Success! Thank you!" in success_str

driver.get_screenshot_as_file("screen.png")

