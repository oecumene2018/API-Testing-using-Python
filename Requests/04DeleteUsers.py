import requests

# API URL

url = 'https://reqres.in/api/users/2'

# According to the documentation we should get a 204 response
response = requests.delete(url)

# Fetch response
print(response.status_code)     # 204

def assert_success(text='Assert success'):
    print(text)
    return True

assert response.status_code == 204 and assert_success(), 'Wrong http response code, should be 204'

