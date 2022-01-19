import pytest

# @pytest.fixture()
# def setup():
#     print("I will print First")
#     yield
#     print("I will be executed last")

# def test_fixture_Demo(setup):
#     print("I will execute steps in fixturedemo method")
# problem : if n number of test are there so you need to write setup in all test args
# sol : write it under one class and and inside class medentory peram is self in method
# class shoudl als be Test

# if you want to run setup and tear down only ocnce after class so in conftest make scope=class

@pytest.mark.usefixtures("setup")
class TestExapmle:

    def test_fixture_Demo1(self):
        print("I will execute steps in fixturedemo method")

    def test_fixture_Demo2(self):
        print("I will execute steps in fixturedemo method")
