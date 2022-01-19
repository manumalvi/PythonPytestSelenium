# Any pytest file should start with test_ keyword or end with _test
# for pytest stander you need to write in function only , any code should be wrapped in method
# pytest method name should start with test keyword
# shift + f10 to run

#make a mark for specific run like smoke regression etc
# C:\Users\mmalvi\PycharmProjects\pythonProject\pytest_usage>py.test -m smoke -v -s

# if you have to skip any test like you know its already a bug whixh is not fixed sos use @pytest.mark.skip
#C:\Users\mmalvi\PycharmProjects\pythonProject\pytest_usage>py.test -v -s  it will skip this markrd and run all

#if you have some operation on test on which other test are dependent so you can run but not report in result by foooling mark
#C:\Users\mmalvi\PycharmProjects\pythonProject\pytest_usage>py.test -v -s  it will run the xfail but wont report it in results

import pytest

def test_first_func():
    msg = "Hello"
    assert msg == "hi" , "Hi test Failed not matched "

@pytest.mark.smoke
def test_sec_func():
    msg = "Hello"
    assert msg == "Hello" , "Hi test Failed not matched "

@pytest.mark.xfail
def test_creditcard():
    msg = "credit"
    assert msg == "credit" , "Hi test credit matched "

