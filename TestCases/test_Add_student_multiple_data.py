# DATA DRIVEN TESTING

# Data driven testing is testing when you use multiple data variations set automatically (not manual data input)
# Firstly we would want to create a standard test with posting a new students data from json file
# loaded from our system
# We will use


import requests
import json
import jsonpath
import openpyxl



def success(text='\nAssert success'):
    print(text)
    return True


def test_add_one_student_data():
    post_api_url = 'http://thetestingworldapi.com/api/studentsDetails'
    file = open('../request_json.json', 'r')
    json_data = json.loads(file.read())
    response = requests.post(post_api_url, json=json_data)
    assert response.status_code == 201 and success(), 'Wrong status code, should be 201'


def test_add_multiple_student_data():
    post_api_url = 'http://thetestingworldapi.com/api/studentsDetails'

# load and parse excel file
    book = openpyxl.load_workbook('../students.xlsx')   # load excel file from the project folder
    sheet = book['students']                            # select a sheet
    students = list(sheet.values)[1:]                   # creating a list of tuples except column headers
    titles = tuple(sheet.values)[0]                     # creating a tuple of including column headers

# creating a dict for earch student, converting it to json and posing to database
# followed by looping through and posing each student's data to the endpoint

    for student in students:                            # take each table row (tuple) except column headers
        dic = {}                                        # creating a temp dict for converting to json
        for i in range(0, len(titles)):               # find number of columns
            dic[titles[i]] = student[i]                 # add a key (header) and value cell value to dict
        response = requests.post(post_api_url, json=dic) # posting dict as json to api endpoint
        print(response.text)                            # printing result for reference
        assert response.status_code == 201 and \
               success(), 'Wrong status code, should be 201' # assert successful post


# {"id":109145,"first_name":"John","middle_name":"K","last_name":"Ranolds","date_of_birth":"March 11, 1994"}
#
# Assert success
# {"id":109146,"first_name":"Jessica","middle_name":"J","last_name":"Jenning","date_of_birth":"April 11, 1996"}
#
# Assert success
# {"id":109147,"first_name":"Marry","middle_name":"Adeline","last_name":"Taylore","date_of_birth":"December 11, 1995"}
#
# Assert success
# {"id":109148,"first_name":"David","middle_name":"George","last_name":"Sott","date_of_birth":"June 11, 1994"}
#
# Assert success
# {"id":109149,"first_name":"Kevin","middle_name":"L","last_name":"Liberman","date_of_birth":"January 11, 1995"}
#
# Assert success
# {"id":109150,"first_name":"Olaf","middle_name":"H","last_name":"Libhert","date_of_birth":"August 11, 1993"}