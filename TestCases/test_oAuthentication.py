# Advanced oAuth
# users use token to access API

import requests
import jsonpath


def success(text='\nAssert success'):
    print(text)
    return True


def test_o_authentication_no_token():
    url = "https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague"
    response = requests.get(url)
    message = jsonpath.jsonpath(response.json(), 'message')[0]
    assert response.status_code == 401 and success('Code 401: Unauthorized'), 'Wrong code, should be 401'
    assert message.startswith('Invalid API key.') and success(), 'Wrong message'

def test_o_authentication_with_token():
    url = "https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague"
    token = "f3d248a0a8msh83a9da772e99de2p1839b9jsn6b80f20da99a"
    host = "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
    query = {'matchday': 2}
    headers = {
        'x-rapidapi-key': f"{token}",
        'x-rapidapi-host': f"{host}"
    }
    response = requests.get(url, headers=headers, params=query)
    matches = jsonpath.jsonpath(response.json(), 'matches')[0]
    assert response.status_code == 200 and success('Code 200: Ok'), 'Wrong code, should be 200'
    assert len(matches) > 0 and success('Matches list not empty'), 'No matches data'

