import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element_by_css_selector("input[class='search-keyword']").send_keys("ber")
time.sleep(3)

addItem = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for item in addItem:
    item.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)
# Method 1 make list then set
# price_list = []
# prices = driver.find_elements_by_xpath("//p[@class='amount']")
# for price in prices:
#     price_list.append(price.text)
# print(price_list)
# print(set(price_list))

# Method 2 find exact xpath
sum = 0
prices = driver.find_elements_by_xpath("//tr/td[5]/p")
for price in prices:
    sum = sum + int(price.text)
print(sum)

totalamt = driver.find_element_by_css_selector("span[class='totAmt']").text
print(totalamt)
assert sum == int(totalamt)


# beforeDiscount = driver.find_element_by_css_selector("span[class='discountAmt']").text
# print(type(beforeDiscount))
#
# driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
# driver.find_element_by_css_selector("button[class='promoBtn']").click()
#
# applied = driver.find_element_by_css_selector("span[class='promoInfo']").text
# assert applied == "Code applied ..!"
# afterDiscount = driver.find_element_by_css_selector("span[class='discountAmt']").text
# print(afterDiscount)
# assert float(beforeDiscount) > float(afterDiscount)