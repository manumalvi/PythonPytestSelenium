from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform()
# contet click for right click
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
