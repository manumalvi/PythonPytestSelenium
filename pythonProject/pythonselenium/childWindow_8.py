from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_xpath("//a[text()='Click Here']").click()
# all window ID will store in list with window_handles method
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close() # it will close child window
parentwindow = driver.window_handles[0]
driver.switch_to.window(parentwindow)
assert "Opening a new window" ==  driver.find_element_by_tag_name("h3").text