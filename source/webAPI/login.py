import requests
import json
TOKEN = ""
def login(url,user,password):
    data = {'manager_account': user, 'manager_code': password}
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    res=response.json()
    if len(res)==2:
        return {"msg":"用户名或密码错误","code":2}
    elif len(res)==3:
        global TOKEN
        TOKEN = res["token"]
        return {"msg":"登录成功","code":1}
    else:
        return {"msg":"未知错误","code":0}

def getToken():
    return TOKEN

def logout():
    global TOKEN
    TOKEN = ""

def update_password(url,code,recode):
    data = {'manager_code': code, 'manager_recode': recode}
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.put(url, data=json.dumps(data), headers=headers)
    res=response.json()
    if res["code"]==200:
        return {"msg":"修改成功","code":1}
    else:
        return {"msg":"修改失败","code":0}
