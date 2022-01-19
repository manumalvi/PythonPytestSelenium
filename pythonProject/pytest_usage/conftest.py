# problem : pytest fixture need to be put in all files
# put fixture in one file conftest and call the function in which ever test is needed .
# if you want to run setup and tear down only ocnce after class so in conftest make scope=class
#@pytest.fixture(scope="class")
import pytest


@pytest.fixture()
#@pytest.fixture(scope="class")
def setup():
    print("I will print First")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("I will print First")
    return ["manu","malvi"]

@pytest.fixture(params=["chrome","Firefox"])
# @pytest.fixture(params=[("chrome","rahul","shetty"),"Firefox"]) # can pass multiple data for chrome   # perametrization in fixture class
def crossBrowser(request):
    return request.param

