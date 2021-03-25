# Adding students data to students management system
# We will use this api service to create students data: http://thetestingworldapi.com/Help
# At first, we wnt to use the studentsDetails section of the API
# and the first operation will be posting, getting, updating anddeleting data for which we should use
# various api endpoints found at the address above .
# In this file we are going to create a pytest test cases file

import requests
import json
import jsonpath
import pytest


def success(text='Assert success'):
    print(text)
    return True


# lets write the post test case
def test_post_student_data():
    global post_id  # post id is made global to us it in other test cases as a global variable
    API_POST_URL = 'http://thetestingworldapi.com/api/studentsDetails'
    file = open('../request_json.json')
    post_data = json.loads(file.read())
    response = requests.post(API_POST_URL, data=post_data)
    json_response = json.loads(response.text) # we get a dictionary here
    post_id = json_response['id'] # that is how we'll get an autogenerated user id in consol
    assert response.status_code == 201 and success(), 'Wrong response code, should be 201'


# now, lets get the student data we have just posted
def test_get_student_data():
    API_GET_URL = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(post_id)
    response = requests.get(API_GET_URL)
    json_response = json.loads(response.text)
    get_id = jsonpath.jsonpath(json_response, 'data.id')[0]
    print(get_id)
    assert get_id == post_id and success(), f"Wrong id, should be {post_id}"


# let's send a put request
def test_put_student_data():
    API_PUT_URL = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(post_id)
    file = open('../request_json_upd.json', 'r')
    put_data = json.loads(file.read())
    put_data['id'] = post_id
    response = requests.put(API_PUT_URL, put_data)
    assert response.status_code == 200 and success('Status code is 200'), 'Wrong status_code, should be 200'


# now we should check that our put request has chanhed the data as expected
def test_check_put_results_get_data():
    API_GET_URL = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(post_id)
    response = requests.get(API_GET_URL)
    json_response = json.loads(response.text)
    get_id = jsonpath.jsonpath(json_response, 'data.id')[0]
    last_name = jsonpath.jsonpath(json_response, 'data.last_name')[0]
    assert get_id == post_id and success(f'id is {post_id}'), f'Wrong id, should be {post_id}, actually - {get_id}'
    assert last_name.startswith('Update') and success(f'Last name updated'), 'Last name is not updated'


#now let's delete the student data that we have created.
def test_delete_student_data():
    API_DELETE_URL = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(post_id)
    response = requests.delete(API_DELETE_URL)
    json_response = json.loads(response.text)
    assert json_response['msg'] == 'Delete  data success' and success('Ok data deleted'), 'Data was not deleted properly'


# now, lets get double-check that the data actually has been deleted
def test_validate_student_data_deleted():
    API_GET_URL = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(post_id)
    response = requests.get(API_GET_URL)
    json_response = json.loads(response.text)
    assert json_response['msg'] == 'No data Found' and success(
        'Ok No data found'), 'Data was not deleted properly'


