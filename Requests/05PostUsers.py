import requests
import json
import jsonpath

# API URL

url = 'https://reqres.in/api/users'

# Import and read json file from the same directory
file = open('user.json', 'r')
input_data = file.read()
post_json = json.loads(input_data) # convert the read data to json

# Make POST request with json-data as body
response = requests.post(url, data=post_json)       # note that the rersponse is a string, not JSON
print(response.text)
# {"avatar":"https://reqres.in/img/faces/11-image.jpg","email":"test@e-mail.safe",
# "first_name":"Test123","last_name":"Test456","job":"Student","id":"540",
# "createdAt":"2021-03-10T15:55:10.162Z"}


# Validating that response code equals 201
def assert_success(text='Assert success'):
    print(text)
    return True


assert response.status_code == 201 and assert_success(), "Wrong response code, should be 201: 'Created'"

# Fetch all headers from response
headers = response.headers
# print(headers)
#{'Date': 'Wed, 10 Mar 2021 15:33:59 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '51', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d688dd4abd48143f320ffcb77361d98171615390439; expires=Fri, 09-Apr-21 15:33:59 GMT; path=/; domain=.reqres.in; HttpOnly; SameSite=Lax; Secure', 'X-Powered-By': 'Express', 'Access-Control-Allow-Origin': '*', 'Etag': 'W/"33-n/Do8pcGZcpG0tAPRPUg3r94sMU"', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'cf-request-id': '08be5f0f0100002debbc01d000000001', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report?s=g%2FARgEzPqz6ZcbjWPUdWBeTaxaDUGV6ShJk0k%2FWJE9FlLYliDJ8ZmtjA1eQtmhOz2uJd6AndT0L7tgxujXZLUye89NRgd0QxoAQ%3D"}],"max_age":604800,"group":"cf-nel"}', 'NEL': '{"report_to":"cf-nel","max_age":604800}', 'Server': 'cloudflare', 'CF-RAY': '62dd9ac4cf792deb-KBP'}

# Fetch only a specific header, for instance the 'Content-Type'
print(response.headers['Content-Type'])     # application/json; charset=utf-8
print(response.headers['Content-Length'])   # 51

# In order to parse the response body we need to convert it to json. We will use the json module for that
response_json = json.loads(response.text)

# Now, we want to fetch the auto created is from the response.  We will have to use the jsonpath for that
id = jsonpath.jsonpath(response_json, 'id')[0]
print(id)       # 825