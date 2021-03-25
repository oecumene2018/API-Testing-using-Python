import pytest
from selenium import webdriver


# in order to perform any test in Pytest we should write test functions
# pytest will recognize a function and run it ONLY if the function's name starts with word "test"

# if you want to execute only one test case, e.g. test_registration_valid_data2,
# print "pytest -k test_registration_valid_data2" in the terminal or add "-k test_registration_valid_data2"
# to the additional arguments in the file run configuration settings.

# function to validate registration would be writen like this:
def test_registration_valid_data():
    try:
        browser = webdriver.Chrome()
        browser.get('https://www.thetestworld.com/testings')
        browser.maximize_window()
    except Exception as error:
        print(f'Something went wrong. Traceback: {error}')
    finally:
        browser.implicitly_wait(4)
        browser.quit()


condition = 100


@pytest.mark.skipif(condition >= 100, reason="Will not be executed on the current build")
def test_registration_valid_data2():
    try:
        browser = webdriver.Chrome()
        browser.get('https://www.thetestworld.com/testings')
        browser.maximize_window()
    except Exception as error:
        print(f'Something went wrong. Traceback: {error}')
    finally:
        browser.implicitly_wait(4)
        browser.quit()

# if we want to run a group of test cases, for example all that have "registration" word in their names
# for that we can either create a pytest.ini file and register the "registration" marker
# or use a -k key and a work in the test case's name to run such test cases


def test_invalid_data3():
    try:
        browser = webdriver.Chrome()
        browser.get('https://www.thetestworld.com/testings')
        browser.maximize_window()
    except Exception as error:
        print(f'Something went wrong. Traceback: {error}')
    finally:
        browser.implicitly_wait(4)
        browser.quit()
