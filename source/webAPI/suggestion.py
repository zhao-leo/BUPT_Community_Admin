# -*- coding: utf-8 -*-
from source.webAPI.request import Request

# 获取投诉列表
def get_suggestion(url):
    return Request('GET',url,{})

# 回复投诉
def reply_suggestion(url,sugg_id,pim_id,content,way,name,tel,status=True):
    data = {
        "sugg_status": status,
        "sugg_content": content,
        "sugg_staff_name": name,
        "sugg_staff_tele": tel,
        "sugg_way": way,
        "sugg_handle_id": pim_id
    }
    return Request('PUT',f'{url}{sugg_id}/',data)

# 获取单个投诉
def suggestion_single(url,id):
    return Request('GET',f'{url}{id}/',{})
