# -*- coding: utf-8 -*-
from .request import Request,FileUpload

# 获取投诉列表
def get_suggestion(url,pageinf:dict):
    return Request('GET',url,pageinf)

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

def handle_suggestion_treat(url,id,summary):
    data = {
        "sugg_treat": 2,
        "sugg_summary": summary
    }
    return Request('PUT',f'{url}{id}/',data)

def upload_pic(url,file:bytes,extension_name):
    files = {"sugg_media":("sugg_media.{}".format(extension_name),file,"image/{}".format(extension_name))}
    return FileUpload(url,files)