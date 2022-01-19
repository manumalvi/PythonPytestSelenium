# On each page what ever obejct are ther to keep then in one class for better readability
# we call it Page object design pettern
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"a[href='/angularpractice/shop']")
    name = (By.NAME,"name")
    email = (By.CSS_SELECTOR,"input[name='email']")
    ckbox = (By.ID,"exampleCheck1")
    sheet = (By.ID,"exampleFormControlSelect1")
    submitbtn = (By.XPATH,"//input[@value='Submit']")
    alertmsg = (By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']")
    #self.driver.find_element_by_class_name("alert-success")

    #dropdown = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))

    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)

    def nameObj(self):
        return self.driver.find_element(*HomePage.name)

    def userEmail(self):
        return self.driver.find_element(*HomePage.email)

    def selectedCkbox(self):
        return self.driver.find_element(*HomePage.ckbox)

    def sheetbox(self):
        return self.driver.find_element(*HomePage.sheet)

    def submitbtm(self):
        return self.driver.find_element(*HomePage.submitbtn)

    def successalert(self):
        return self.driver.find_element(*HomePage.alertmsg)

