from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#actions chains will do all mouse related oprations

action = ActionChains(driver)

menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()

childMenu = driver.find_element_by_link_text("Top")
#perform has to be there in last
action.move_to_element(childMenu).click().perform()