# -*- coding: utf-8 -*-
import requests
from source.webAPI.login import getToken
import json
ID,NAME,PHONE,ACCOUNT='','','',''
def get_pim(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res=response.json()
    if res["code"]==419:
        return {'msg':'请重新登录','code':149}
    elif res["code"]==200:
        global ID,NAME,PHONE,ACCOUNT
        ID=res["data"]["id"]
        NAME=res["data"]["manager_name"]
        PHONE=res["data"]["manager_tele"]
        ACCOUNT=res["data"]["manager_account"]
        return {'msg':'登录成功','code':200}
    else:
        return {'msg':'未知错误','code':0}

def getInf():
    return {'ID':ID,'NAME':NAME,'PHONE':PHONE,'ACCOUNT':ACCOUNT}

def update_pim(url,account,name,phone):
    data = {'manager_name': name, 'manager_tele': phone, 'manager_account': account}
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.put(url, data=json.dumps(data), headers=headers)
    res=response.json()
    if res["code"]==200:
        return {"msg":"修改成功","code":200}
    else:
        return {"msg":"修改失败","code":0}

def Frequency(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res=response.json()
    if res["code"]==200:
        return res['data']
    else:
        return {"msg":"未知错误","code":0}