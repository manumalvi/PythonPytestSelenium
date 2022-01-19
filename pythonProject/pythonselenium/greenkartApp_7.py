import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()

driver.find_element_by_css_selector("input[class='search-keyword']").send_keys("ber")
time.sleep(3)

count = len(driver.find_elements_by_xpath("//div[@class='product']"))
assert count == 3
products = []
vegitables = driver.find_elements_by_xpath("//h4[@class='product-name']")
for veg in vegitables:
    products.append(veg.text)
print(products)

addItem = driver.find_elements_by_xpath("//div[@class='product-action']/button")
newlst = []
for item in addItem:
    #we can traverse back word to parent with xpath like below  commmented
    newlst.append(item.find_element_by_xpath("parent::div/parent::div/h4").text)
    item.click()
    print(item)
print(newlst)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)

products_nxtpg = driver.find_elements_by_xpath("//p[@class='product-name']")
finallst = []
for pronxt in products_nxtpg:
    finallst.append(pronxt.text)
print(finallst)
assert products == finallst

# Q : Can you traverse back to parent with CSS no only xpath we can do that