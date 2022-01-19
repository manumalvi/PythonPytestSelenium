from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    media_heading = (By.CSS_SELECTOR,"h4[class='media-heading']")

    ckbtn = (By.CSS_SELECTOR,"button[class='btn btn-success']")

    cntry = (By.ID,"country")

    ind = (By.LINK_TEXT,"India")

    primary_ckbox = (By.CSS_SELECTOR,"div[class='checkbox checkbox-primary")

    smt = (By.CSS_SELECTOR,"input[type='submit']")

    suc_msg = (By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible")

    def media(self):
        return self.driver.find_element(*ConfirmPage.media_heading)

    def ckoutbtn(self):
        return self.driver.find_element(*ConfirmPage.ckbtn)

    def country(self):
        return self.driver.find_element(*ConfirmPage.cntry)

    def india(self):
        return self.driver.find_element(*ConfirmPage.ind)

    def primary_checkbox(self):
        return self.driver.find_element(*ConfirmPage.primary_ckbox)

    def submit_btn(self):
        return self.driver.find_element(*ConfirmPage.smt)

    def success_msg(self):
        return self.driver.find_element(*ConfirmPage.suc_msg)
