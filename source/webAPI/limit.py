import requests
from source.webAPI.login import getToken
def get_limit(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res
