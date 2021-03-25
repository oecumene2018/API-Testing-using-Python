# Conditional test case execution and fixtures.

# We can can consitionally execute test cases inseveral different ways:
# 1. grouping tests with pytest's marks like .mark.skip or .mark.skipif(<condition>)
# 2. command prompt/terminal commands applying -k argument like:
#   - pytest -k test_my_test_case_name Test_Case_Folder (to run a certain test case located somewhere in the test folder)
#   - pytest -k test_my_test Test_Case_Folder (to run all test cases in the folder if their names contain "test_my_test ")


# fixtures are pieces of code that are supposed to be executed before or after the tests are executed

# let's post some data to the server and test the response code again

import pytest
import requests
import json
import jsonpath


def success(text='Assert Success'):
    print(text)
    return True


x = 10


@pytest.fixture(scope='session')
def setup():
    global file, url, posted_data, json_data, response
    url = 'https://reqres.in/api/users'
    filepath = '/Users/admin/Documents/Python API/API Testing using Python/new_user.json'
    file = open(filepath, 'r')
    posted_data = file.read()
    json_data = json.loads(posted_data)
    response = requests.post(url, json_data)


@pytest.mark.skipif(x >= 10, reason='Condition is met')
def test_response_body_first_name(setup):
    response_body = json.loads(response.text)
    first_name = jsonpath.jsonpath(response_body, 'first_name')[0]
    assert first_name == 'Test1234' and success(), 'Wrong first name, should be: Test1234'


def test_response_response_code(setup):
    response_code = response.status_code
    assert response_code == 201 and success(), 'Wrong response code, should be 201'


def test_response_header_date(setup):
    response_headers = response.headers  # no need to use json.loads (converts from str to dict) as response.headers are dict
    date = response_headers['Date']
    assert date.find('Mar 2021') != -1 and success(), "Wrong date header, date should contain 13 Mar 2021"
