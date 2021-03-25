# Parameters are text added after url and ? with a key-value pattern and separated by &

import requests


# API URL
url = 'https://httpbin.org/get'

# creating parameters
my_params = {'name': 'Kirill', 'task': 'testing', 'phrase': 'foo_bar'}
response = requests.get(url, params=my_params)
print(response.text)
# {
#   "args": {
#     "name": "Kirill",
#     "phrase": "foo_bar",
#     "task": "testing"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.25.1",
#     "X-Amzn-Trace-Id": "Root=1-6049302e-3af4cb2641c64bc729f7e88f"
#   },
#   "origin": "176.37.154.33",
#   "url": "https://httpbin.org/get?name=Kirill&task=testing&phrase=foo_bar" # NOTE THE URL WITH OUR PARAMS
# }
