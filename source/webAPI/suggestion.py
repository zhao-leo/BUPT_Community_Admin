import requests
import json
from source.webAPI.login import getToken
def get_suggestion(url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    response = requests.get(url, headers=headers)
    res=response.json()
    return res

def reply_suggestion(content,way,name,tel,getid,replyid,url):
    headers = {'Content-type': 'application/json','Authorization':getToken()}
    data = {
       "sugg_content": content,
       "sugg_staff_name": name,
       "sugg_staff_tele": tel,
       "sugg_way": way,
       "sugg_handle_id": replyid
    }
    response = requests.put(url.join(f'{getid}/'), headers=headers, json=json.dumps(data))
    return response.json()['message']

if __name__ == "__main__":
  res=get_suggestion("http://127.0.0.1:8000/user/SuggestionAll/")
  print(res)