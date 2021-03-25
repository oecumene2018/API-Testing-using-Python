# FIXTURES are the auxiliary code that is required to be run BEFORE or AFTER you run your test cases
# for instance you may need to open a browser, connect to a server, quit the browser at the end of a session etc.
#
# import pytest
# from selenium import webdriver
#
# url1 = 'https://www.wikipedia.org'
# url2 = 'https://www.google.com.ua'
# url3 = 'https://www.youtube.com'
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print('Starting tests')
#     browser = webdriver.Chrome()
#     browser.maximize_window()
#     yield browser
#     browser.implicitly_wait(4)
#     print('Quitting tests')
#     browser.quit()
#
#
# def test_browser_open_page_wiki(browser):
#     browser.get(url1)
#
#
# def test_browser_open_page_google(browser):
#     browser.get(url2)
#
#
# def test_browser_open_page_youtube(browser):
#     browser.get(url3)



# for the purposes of this lesson, we can achieve exact same thing by a shorter pytest code, which is the best practice

import time
import pytest
from selenium import webdriver
#
urls = ['https://www.wikipedia.org',
        'https://www.google.com.ua',
        'https://www.youtube.com']


# service function for printing out a successful assert message
def assert_successful(text='Assert success!'):
    print(text)
    return True

# Fixture to initialise a browser session and quit it aftewards
@pytest.fixture(scope='session')
def web_driver():
    print('Starting webdriver')
    browser = webdriver.Chrome()
    yield browser
    browser.implicitly_wait(5)
    print('Quitting webdriver')
    browser.quit()


@pytest.mark.parametrize("url", urls)
def test_open_url(web_driver, url):
    web_driver.get(url)
    assert web_driver.current_url.startswith(url) and assert_successful(), 'Wrong url open'



