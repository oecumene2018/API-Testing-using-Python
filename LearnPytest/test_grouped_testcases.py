# in order to run group of tests we need to group them
# for example in some cases (like smoke testing) we need to run only test intended for smoke testing.
# for sanity tasting we will need to run only corresponding tests
# so, we can do that by marking tests to our liking
# note that marking tests in pytest is basically tagging them for some conditional usage
# when our tests have been marked we can use -m key and add the mark to run the related tests

import pytest
from selenium import webdriver

url1 = 'https://www.wikipedia.org'
url2 = 'https://www.google.com.ua'
url3 = 'https://www.youtube.com'
browser = webdriver.Chrome()


@pytest.mark.foo
def test_browser_valid_open_google():
    try:
        browser.get(url2)
    except Exception as error:
        print(f'Something went wrong. Traceback: {error}')
    # finally:
    #     browser.implicitly_wait(4)
    #     browser.quit()
    # this part is commented to avoid MaxRetryError caused by quitting browser for each test
    #probably, we will have to use webdriver fixture @pytest.fixture(scope="session")


@pytest.mark.bar(scope='session')
def test_browser_valid_open_wiki():
    try:
        browser.get(url1)
    except Exception as error:
        print(f'Something went wrong. Traceback: {error}')
    # finally:
    #     browser.implicitly_wait(4)
    #     browser.quit()
    # this part is commented to avoid MaxRetryError caused by quitting browser for each test
    #probably, we will have to use webdriver fixture @pytest.fixture(scope="session")


@pytest.mark.bar(scope='session')
def test_browser_valid_open_tube():
    try:
        browser.get(url3)
    except Exception as error:
        print(f'Something went wrong. Traceback: {error}')
    # finally:
    #     browser.implicitly_wait(4)
    #     browser.quit()
    # this part is commented to avoid MaxRetryError caused by quitting browser for each test
    #probably, we will have to use webdriver fixture @pytest.fixture(scope="session")