import requests
import json
from source.webAPI.login import getToken
from source.webAPI.pim import getInf
def get_suggestion(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res=response.json()
    return res

def reply_suggestion(url,getid,content,way,name,tel):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    data = {
       "sugg_content": content,
       "sugg_staff_name": name,
       "sugg_staff_tele": tel,
       "sugg_way": way,
       "sugg_handle_id": getInf()['ID']
    }
    response = requests.put(url+f'{getid}/', headers=headers, json=json.dumps(data))
    return {"msg":response.json()['message'],'code':response.json()['code']}

if __name__ == "__main__":
  res=get_suggestion("http://127.0.0.1:8000/user/SuggestionAll/")
  print(res)