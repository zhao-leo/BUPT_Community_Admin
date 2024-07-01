# -*- coding: utf-8 -*-
import requests
from source.webAPI.login import getToken
from source.webAPI.pim import getInf
def get_suggestion(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res=response.json()
    return res

def reply_suggestion(url,getid,content,way,name,tel,status=True):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    data = {
        "sugg_status": status,
        "sugg_content": content,
        "sugg_staff_name": name,
        "sugg_staff_tele": tel,
        "sugg_way": way,
        "sugg_handle_id": getInf()['ID']
    }
    response = requests.put(f'{url}{getid}/', headers=headers, json=data)
    return {"msg":response.json()['message'],'code':response.json()['code']}

def suggestion_single(url,id):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(f'{url}{id}/', headers=headers)
    res=response.json()
    return res
