import requests
import json
from nicegui import app



def Request(method: str,url: str, data: dict) -> dict:
    headers = {'Content-type': 'application/json','Authorization': app.storage.user.get('TOKEN')}
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, data=json.dumps(data), headers=headers)
        elif method == 'PUT':
            response = requests.put(url, data=json.dumps(data), headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        try:
            res = response.json()
        except:
            res = {"message":"未知错误","code":0}
        return res
    except:
        return {"message":"网络错误","code":0}

def GetExcel(url:str, data: dict) -> requests.Response:
    headers = {'Content-type': 'application/json','Authorization': app.storage.user.get('TOKEN')}
    response = requests.post(url, headers=headers, json=data)
    return response

def FileUpload(url:str, data: dict) -> dict:
    headers = {'Authorization': app.storage.user.get('TOKEN')}
    response = requests.post(url, headers=headers, files=data)
    try:
        res = response.json()
    except:
        res = {"message":"未知错误","code":0}
    return res