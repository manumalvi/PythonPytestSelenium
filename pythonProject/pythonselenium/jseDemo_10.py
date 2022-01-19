# Java script JS DOM Document object model can access any elemt on web page just like how selenium does
# selenium have a method to execute javascript code in it
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello")

# this below wont work because we have entered this after page loaded so there are other methods to do this in selenium
# when browser loads we can only get the data of that by text
print(driver.find_element_by_name("name").text)

# Fisrt method
print(driver.find_element_by_name("name").get_attribute("value"))

# second method to acive it by purly by java script
# execute script method is for java script
# go to inspect console and write java script command eg : document.getElementsByName("name")[0]
#selinum is giving control to execute script menthod
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# if this is not working some how not able to click then use js
shopButton = driver.find_element_by_css_selector("a[href='/angularpractice/shop']")
driver.execute_script("arguments[0].click();",shopButton)

# to scroll down its not possibel by selium hece using js
# Q seleium dont have java script we can do 
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")