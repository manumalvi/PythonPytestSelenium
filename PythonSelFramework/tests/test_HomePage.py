import time

import pytest
from selenium.webdriver.support.select import Select

from TestData.TestDataHomePage import TestData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_HomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.nameObj().send_keys(getData["firstname"])
        log.info("This is the Fist name" + getData["firstname"])
        homepage.userEmail().send_keys(getData["lastname"])
        homepage.selectedCkbox().click()
        dropdown = Select(homepage.sheetbox())
        dropdown.select_by_visible_text(getData["gender"])
        dropdown.select_by_index(1)

        homepage.submitbtm().click()

        message = homepage.successalert().text

        assert "Success!" in message
        time.sleep(5)
        self.driver.refresh()
    # Method 1
    # list only used when we pass data with idex eg getData[0]
    #@pytest.fixture(params=[("manu","malvi","Male"),("honey","malviya","Female")])
    # Method 2
    #@pytest.fixture(params=[{"firstname" : "manu","lastname" : "malvi","gender" : "Male"}, {"firstname" : "honey","lastname" : "malviya","gender" : "Female"}])
    # method 3
    @pytest.fixture(params=TestData.test_Homepage_Data)
    #@pytest.fixture(params=TestData.getTestDataExcel("Testcase2"))
    def getData(self,request):
        return request.param

