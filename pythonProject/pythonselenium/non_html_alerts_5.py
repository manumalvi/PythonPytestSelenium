
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element_by_css_selector("#name").send_keys("manu")
driver.find_element_by_id("alertbtn").click()

alert = driver.switch_to.alert

print(alert.text)
assert "manu" in alert.text
alert.accept()

# for clancel box
# alrt.dismiss()

