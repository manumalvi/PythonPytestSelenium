# Any pytest file should start with test_ keyword or end with _test
# for pytest stander you need to write in function only , any code should be wrapped in method
# pytest method name should start with test keyword
# shift + f10 to run
# Run all the test in package by below command
# C:\Users\mmalvi\PycharmProjects\pythonProject\pytest_usage>py.test -v -s

# run specific file
# C:\Users\mmalvi\PycharmProjects\pythonProject\pytest_usage>py.test test_Demo2.py -v -s

# keyword specific rum like in entire dir only creditcard test case name will run
# C:\Users\mmalvi\PycharmProjects\pythonProject\pytest_usage>py.test -k creditcard -v -s

# method name should have sense
# -k stand for method name executions
# -s logs in output
# -v more information meta data
# you can run specific file py.test <filename>
# you can mark (tag) tests and then run with -m
#pytest.mark.xfail to run but skip in result
# fisture are for setup and tesr down, conftest file to generelize fixture
# data driven and perametrization can be done with return statement in list format
# when you define fixture scope to class only it will run only once class is initiated and at end
# first install plugin for pytest html
# C:\Users\mmalvi\PycharmProjects\pythonProject\pytest_usage>py.test --html=report.html
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_first_func():
    print("Hello")

def test_greet():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)