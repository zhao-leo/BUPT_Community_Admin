# -*- coding: utf-8 -*-
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

def get_picture(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res=response.json()
    return res['data']

def upload_pic(url,fileb64):
    headers = {'Authorization':getToken()}
    files = {"cover_file":fileb64}
    response = requests.post(url, headers=headers, files=files)
    return response.json()

def delete_pic(url,id):
    headers = {'Authorization':getToken()}
    response = requests.delete(f"{url}{id}/", headers=headers)
    return response.json()