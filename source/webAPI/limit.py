# -*- coding: utf-8 -*-
import requests
from source.webAPI.login import getToken
def get_limit(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def update(url,start,end,mon,tue,wed,thr,fri):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    data={
        "start":start,
        "end":end,
        "mon":mon,
        "tue":tue,
        "wed":wed,
        "thr":thr,
        "fri":fri
    }
    response = requests.post(url, headers=headers,json=data)
    res = response.json()
    return res
