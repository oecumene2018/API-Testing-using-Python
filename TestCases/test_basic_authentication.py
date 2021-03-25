# BASIC AUTHENTICATION
# Authontication using login and password

import requests
import json
from requests.auth import HTTPBasicAuth


def success(text='\nAssert success'):
    print(text)
    return True


def test_url_no_login_pass():
    url = 'https://api.github.com/user'
    response = requests.get(url)
    msg = json.loads(response.text)['message']
    assert msg == 'Requires authentication' and success("\nMessage is 'Requires authentication'"), \
        'Wrong authentication message, should be: Requires authentication'


def test_url_with_loging_pass():
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth (username='oecumene2018', password='1984mznxbcv'))
    print(response)
