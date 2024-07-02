# -*- coding: utf-8 -*-
import requests
from source.webAPI.login import getToken
def get_limit(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def update(url,start,end,mon='未填写',tue='未填写',wed='未填写',thr='未填写',fri='未填写'):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    data={
        "start_time":start,
        "finish_time":end,
        "mon":mon,
        "tue":tue,
        "wed":wed,
        "thu":thr,
        "fri":fri
    }
    response = requests.post(url, headers=headers,json=data)
    res = response.json()
    return res
