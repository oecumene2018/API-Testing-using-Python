# UPDATING EXISTING DATA ON THE SERVER

import requests
import json
import jsonpath

# API URL


url = "https://reqres.in/api/users/2"


# Read from json file located in the project folder
file = open('user_update.json', 'r')
input = file.read()
json_data = json.loads(input)

response = requests.put(url, json_data)
print(response.text)
# {"email":"update_test@e-mail.safe","first_name":"update_Test123","last_name":"update_Test456",
# "job":"update_Student","updatedAt":"2021-03-10T17:55:29.519Z"}

def success_assert(text='Assert success'):
    print(text)
    return True

assert response.status_code == 200 and success_assert(), 'Wrong response code, should be 200: OK'
# Assert success

# Parse response content
response_body = json.loads(response.text)

assert jsonpath.jsonpath(response_body, 'first_name')[0] == 'update_Test123' and \
       success_assert('First name is "update_Test123"'), 'Wrong first name, it should be equal to "update_Test123"'
#First name is "update_Test123"