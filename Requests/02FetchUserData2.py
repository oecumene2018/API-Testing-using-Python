# For parsing through response
# If we need to get only a part of the response, we would want to use jsonpath module
import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

# Send get request
response = requests.get(url)

#PARSE RESPONSE TO JSON FORMAT

json_response = json.loads(response.text)
print(json.dumps(json_response, indent=4))  # the whole json body will be printed out

# FETCH A VALUE USING JSON PATH
# to this end we will need to use our json-response and a corresponding key as arguments
# for example, let's see the "total_pages" key value.

pages = jsonpath.jsonpath(json_response, "total_pages") # this constructor will always produce a list
print(pages[0])        # 2

# Now let's write a small test and check if we gonna get the total number of students which should equal to 12.
total_students = jsonpath.jsonpath(json_response, "total")


# We need to write a function to see that our assert check has succeeded.
def success_func(message="Assert succeeded!"):
    print(message)
    return True


assert total_students[0] == 12 and success_func("Success, total = 12"), "Total value should equal 12"
# Success, total = 12
# If we put any wrong value in the assert clause - we are goint to get an error message:
# AssertionError: Total value should equal 12

studs = jsonpath.jsonpath(json_response, "data")[0]  # explanation: this construction will return a list with only 1 index
stud_1 = studs[0]                                    # but the "data" vlaue we are looking for also contains a list of dicts(students info)
st_email = stud_1["email"]                           # we want to find value of the "email" key for the first student (id_7)
print(st_email)  # michael.lawson@reqres.in

# there is a build-in method to fetch the required value in jsonpath - see the FetchUserData3.py
