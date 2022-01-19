from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#To enter any value in BOX
driver.find_element_by_name("name").send_keys("hello")  # it will enter in box
#To enter any value in BOX by css
driver.find_element_by_css_selector("input[name='email']").send_keys("manu_prince2005")
#To select any check box
driver.find_element_by_id("exampleCheck1").click()

# 2 types of drop down first is static which is having select class in inspect another is dynamic like flight source list
# select class provide method to handle the option in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# Or   dropdown.select_by_index(0)  or dropdown.select_by_value("male")  when tagnem is select is there as class then only this work

#To click in button
driver.find_element_by_xpath("//input[@value='Submit']").click()

#customizes CSS Syntex
# tagname[attribute='value']
#input[name='name']
#to chekc how many place it hit on site 1 or more go to inspact next tab console
# $("input[name='name']")
# so selenium start scan from top left and first box it match will fill the value

#customizes Xpath Syntex
# //tagname[@attribute='value']
#to chekc how many place it hit on site 1 or more go to inspact next tab console
# $x("//input[@value='Submit']")
# cropath will generate xpath and css but its a plugin in chrome
# To get what is being display as Test
# Regular Expression : we can match with CSS also but reguler exp if clas name is too big [class*='alert-success']
# Regular Exp : for Xpath //*[contain(@class,'alert-success')]
message = driver.find_element_by_class_name("alert-success").text

# assert alwasy expect true
assert "Success!" in message

driver.close()