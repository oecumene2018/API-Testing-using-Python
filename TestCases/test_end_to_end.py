# in this file we are writing a test in which we are going to
# 1. post a student's data
# 2. post a student's tech skills data
# 3. post student's addresses
# 4. get all final student's details

import requests
import json
import jsonpath


def success(text='Assert success'):
    print(text)
    return True


# 1. post a student's data
def test_post_student_data():
    post_api_url = 'http://thetestingworldapi.com/api/studentsDetails'
    file = open('../request_json.json', 'r')
    json_data = json.loads(file.read())
    response = requests.post(post_api_url, json=json_data)  # json command converts our 'json_data' dict to json format
    # for uploading
    response_json: dict = json.loads(response.text)
    post_id: int = jsonpath.jsonpath(response_json, 'id')[0]
    print(post_id)
    assert response.status_code == 201 and success('Response code is 201: created'), \
        'Wrong response code, should be 201'

    # 2. post a student's tech skills data.  Note that we should update id(int) and st_id: str
    post_skills_api = 'http://thetestingworldapi.com/api/technicalskills'
    skills_file = open('../tech_skills.json', 'r')
    skills_data = skills_file.read()
    json_data2: dict = json.loads(skills_data)
    json_data2['id'], json_data2['st_id'] = post_id, str(post_id)
    print(json_data2['id'])
    skills_response = requests.post(post_skills_api, json=json_data2)
    assert skills_response.status_code == 200 and success('Response code is 200: Ok'), \
        'Wrong response code, should be 200'

    # 3. post student's addresses. Note that we should set stId which is string
    post_address_api = 'http://thetestingworldapi.com/api/addresses'
    address_file = open('../address.json', 'r')
    address_data = address_file.read()
    json_data3: dict = json.loads(address_data)
    json_data3['stId'] = str(post_id)
    address_response = requests.post(post_address_api, json=json_data3)
    assert address_response.status_code == 200 and success('Address post code is 200: Ok'), \
        'Wrong response code, should be 200'

    # 4. get all final student's details We want to use GET method for this
    final_api = f'http://thetestingworldapi.com/api/FinalStudentDetails/{post_id}'
    final_response = requests.get(final_api)
    get_st_id: str = jsonpath.jsonpath(final_response.json(), 'data.TechnicalDetails')[0][0]['st_id']
    get_stid: str = jsonpath.jsonpath(final_response.json(), 'data.Address')[0][0]['stId']
    assert all(id == str(post_id) for id in [get_st_id, get_stid]) and success('All final ids match'), "Ids do not match"





