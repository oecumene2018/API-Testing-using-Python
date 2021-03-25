# GETTING USER CUSTOMISED HEADERS
import requests


# API URL

url = 'https://httpbin.org/get'

response = requests.get(url)
# print(response.text)

# Execute the file in Terminal type: python Requests/07GetHeaders.py
# Below are default headers
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.25.1",
#     "X-Amzn-Trace-Id": "Root=1-604924a7-7c278ca16e60321a52d0defc"
#   }

# We want to add a customised header like so: "T1": "First_Header", "T2": "Second_Header"
# Let's send our customised headers

header_data = {"T1": "First_Header", "T2": "Second_Header"}
response2 = requests.get(url, headers=header_data)
print(response2.text)
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "T1": "First_Header",
#     "T2": "Second_Header",
#     "User-Agent": "python-requests/2.25.1",
#     "X-Amzn-Trace-Id": "Root=1-6049279f-3b2fcf290e662ea513be35b1"
#   },
#   "origin": "176.37.154.33",
#   "url": "https://httpbin.org/get"
# }