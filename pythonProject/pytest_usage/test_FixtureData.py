import pytest

# Q : y u need argument here , bcoz you are returning some thing in conftest you have put return hence arg is needed
from pytest_usage.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editProfile(self,dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        #print(dataLoad)
        #print(dataLoad[1])
