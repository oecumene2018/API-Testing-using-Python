# Test creation of a new user
import pytest
import requests
import json



# API URL
url = 'https://reqres.in/api/users'
file_path = '/Users/admin/Documents/Python API/API Testing using Python/new_user.json'


def success(text='Assert Success'):
    print(text)
    return True


def test_create_new_user_positive_status():
    file = open(file_path, 'r')
    data_input = file.read()
    json_data = json.loads(data_input)
    response = requests.post(url, json_data)
    assert response.status_code == 201 and success(), 'Wrong response code, should be: 201'


@pytest.mark.xfail
def test_create_new_user_negative_status():
    file = open(file_path, 'r')
    data_input = file.read()
    json_data = json.loads(data_input)
    response = requests.post(url, json_data)
    assert response.status_code == 200 and success(), 'Wrong response code, should be: 201'
