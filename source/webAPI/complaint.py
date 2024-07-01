# -*- coding: utf-8 -*-
import requests
from source.webAPI.login import getToken
from source.webAPI.pim import getInf
def get_complaint(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res=response.json()
    return res

def reply_complaint(url,getid,content,way,name,tel,status=True):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    data = {
        "comp_status": status,
        "comp_content": content,
        "comp_staff_name": name,
        "comp_staff_tele": tel,
        "comp_way": way,
        "comp_handle_id": getInf()['ID']
    }
    response = requests.put(f'{url}{getid}/', headers=headers, json=data)
    return {"msg":response.json()['message'],'code':response.json()['code']}

def complaint_single(url,id):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(f'{url}{id}/', headers=headers)
    res=response.json()
    return res
