# REQUEST CHAINING
# Request chaining is a process whereby we fetch data in one request
# and use it as an input data for another request.

# This time we will use a user id from a post request and use it as a param in a get request

import requests
import json
import jsonpath


def success(text='Assert success'):
    print(text)
    return True


global post_id


def test_post_student_data():
    global post_id
    post_api = 'http://thetestingworldapi.com/api/studentsDetails'
    file = open('../request_json.json')
    post_data = file.read()
    post_json = json.loads(post_data)
    response = requests.post(post_api, json=post_json)
    assert response.status_code == 201 and success('\nPosted 201'), 'Wrong status code, should be 201'
    post_id = jsonpath.jsonpath(json.loads(response.text), 'id')[0]


def test_get_student_data():
    get_api = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(post_id)
    response = requests.get(get_api)
    assert response.status_code == 200 and success('\nGET request 200'), 'Wrong status code, should be 200'
