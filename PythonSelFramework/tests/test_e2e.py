from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

#@pytest.mark.usefixtures("setup")
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        homepage = HomePage(self.driver)
        homepage.shopItem().click()

        checkout = CheckOutPage(self.driver)
        products = checkout.cardItem()

        confirmpage = ConfirmPage(self.driver)

        '''
        If you dont want multiple object so check the link button like shop button is link for next page so do like below
        
        def shopItem(self):
            self.driver.find_element(*HomePage.shop).click()
            checkout = CheckOutPage(self.driver)
            return checkout
        '''


        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            #productName = product.checkout.itemNames.text
            if productName == "Blackberry":
                product.find_element_by_xpath("div/button").click()

        checkout.ckoutbtn().click()

        assert confirmpage.media().text == productName

        confirmpage.ckoutbtn().click()

        confirmpage.country().send_keys("Ind")

        #wait = WebDriverWait(self.driver,7)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        # put this in base class utility
        self.verifyPresentLink("India")

        confirmpage.india().click()

        confirmpage.primary_checkbox().click()

        confirmpage.submit_btn().click()

        success_str = confirmpage.success_msg().text

        assert "Success! Thank you!" in success_str

        self.driver.get_screenshot_as_file("screen.png")

