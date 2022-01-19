from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe") # can give other broser also like gekodriver for firefox
driver.maximize_window() # it will maximi the window

driver.get("https://rahulshettyacademy.com/")  # get menthod to hit url on browser

print(driver.title)  # to get the title

print(driver.current_url) #to get the curent url so that we can say its not the other site

driver.close() # it will close only current window but quit will close all windows if opend

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window() # it will minimize the window
driver.back()  # to come to back page
driver.refresh() # to refreseh the screen



