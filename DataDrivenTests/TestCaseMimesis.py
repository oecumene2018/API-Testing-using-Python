# Mimesis test case

import random
from .LibraryM import CommonM


def test_post_multiple_student_data():
    post_api_url = 'http://thetestingworldapi.com/api/studentsDetails'
    for i in range(0, random.randint(3, 7)):        # generating from 3 to 7 number of student data dicts
        student = CommonM()
        response = student.post_personal_data(post_api_url) # posting data as json
        code = response.status_code
        assert code == 201 and student.assert_success(), 'Wrong status code, should be 201'

# {"id":109323,"first_name":"Landon","middle_name":"Yer","last_name":"Floyd","date_of_birth":"12/26/2003"}
# 201
#
# Assert successful
# {"id":109324,"first_name":"Torrie","middle_name":"Leo","last_name":"Alford","date_of_birth":"12/21/2014"}
# 201
#
# Assert successful
# {"id":109325,"first_name":"Garry","middle_name":"Joslyn","last_name":"York","date_of_birth":"05/17/2019"}
# 201
#
# Assert successful
# PASSED