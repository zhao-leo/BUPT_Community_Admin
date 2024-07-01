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
        "hotline_tele":phone
    }
    response = requests.put(url+str(id)+'/', headers=headers, json=data)
    if response.json()['code'] == 200:
        return response.json()['message']
    else:
        return '修改失败'

def add_hotline(url,name,phone):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    data = {
        "hotline_who":name,
        "hotline_tele":phone
    }
    response = requests.post(url, headers=headers, json=data)
    if response.json()['code'] == 200:
        return response.json()['message']
    else:
        return '添加失败'

def remove_hotline(url,id):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.delete(url+str(id)+'/', headers=headers)
    if response.json()['code'] == 200:
        return response.json()['meaasge']

def get_warmtext(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res=response.json()
    return res['data']["warn_text"]

def update_warmtext(url,text):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    data = {
        "warn_text":text
    }
    response = requests.post(url, headers=headers, json=data)
    if response.json()['code'] == 200:
        return response.json()['message']
    else:
        return '修改失败'