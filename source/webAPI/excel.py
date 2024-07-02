# -*- coding: utf-8 -*-
import requests
from source.webAPI.login import getToken
def get_excel(url,start_time,finish_time):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    data = {
        'start_time': start_time,
        'finish_time': finish_time
    }
    response = requests.post(url, headers=headers, json=data)
    res =response.content
    return res

