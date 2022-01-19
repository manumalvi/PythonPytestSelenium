from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    card = (By.XPATH,"//div[@class='card h-100']")
    itemname = (By.XPATH,"div/h4/a")
    ckout = (By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']")

    # * is for to de serialize the touple
    def cardItem(self):
        return self.driver.find_elements(*CheckOutPage.card)

    def itemNames(self):
        return self.driver.find_element(*CheckOutPage.itemname)

    def ckoutbtn(self):
        return self.driver.find_element(*CheckOutPage.ckout)