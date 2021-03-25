# Advanced parsing get requests

import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

json_response = json.loads(response.text)

# lets find out the email of the first student: the 1st value in the list located in the "data" key of our json response

email_1 = jsonpath.jsonpath(json_response, 'data[0].email') # As the jsonpath.jsonpath(..) will always produce a list
                                                            # with a single value we need to use a [0] zero index

print(email_1[0])       # michael.lawson@reqres.in
# or we can put it as follows: email_1 = jsonpath.jsonpath(json_response, 'data[0].email')[0]

number_of_students = len(json_response['data'])
print(number_of_students)       # 6

# Now that we know all number of all the students in our list, let's fetch and print out all students' emails.

students_data = jsonpath.jsonpath(json_response, 'data')[0] # jsonpath.jsonpath(..) always produces a list
print(students_data)

#print out all the emails
for index in range(0, len(students_data)):
    email = students_data[index]['email']
    print(email)

# also there is a jsonpath way to do so
for index in range(0, 6):
    email = jsonpath.jsonpath(json_response, f'data[{index}].email')[0]
    first_name = jsonpath.jsonpath(json_response, f'data[{index}].first_name')[0]
    last_name = jsonpath.jsonpath(json_response, f'data[{index}].last_name')[0]
    print('{:<30}{:<10}{:<10}'.format(email, first_name, last_name))
# michael.lawson@reqres.in      Michael   Lawson
# lindsay.ferguson@reqres.in    Lindsay   Ferguson
# tobias.funke@reqres.in        Tobias    Funke
# byron.fields@reqres.in        Byron     Fields
# george.edwards@reqres.in      George    Edwards
# rachel.howell@reqres.in       Rachel    Howell


# Now we will code a little assert test.
def assert_success(text="Assert success"):
    print(text)
    return True

name = jsonpath.jsonpath(json_response, f'data[0].first_name')[0]
assert name == 'Michael' and assert_success(), 'Wrong fiirst name'
# Assert success