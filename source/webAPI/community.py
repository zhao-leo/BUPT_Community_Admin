import requests
from source.webAPI.login import getToken

def get_hotline(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res=response.json()
    return res

def update_hotline(url,id,name,phone):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    data = {
        "hotline_who":name,
        "hotline_tel":phone
    }
    response = requests.put(url+str(id)+'/', headers=headers, json=data)