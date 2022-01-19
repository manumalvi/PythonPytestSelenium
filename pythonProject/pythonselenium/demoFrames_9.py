from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# develpoer uses frame for this page iframe,framset,frame
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(3)
# Q  not able to find with this locator
#driver.find_element_by_css_selector("#tinymce").clear()
# so first switch to frame , then give either frame id , frmae name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("my name is manu")

# this will fail bcoz your driver will still serch in frame only
#driver.find_element_by_tag_name("h3").text
# so come back to html
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)




