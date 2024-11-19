# -*- coding: utf-8 -*-
from .request import Request,FileUpload

# 获取投诉列表
def get_complaint(url,pageinf:dict):
    return Request('GET',url,pageinf)

# 回复投诉
def reply_complaint(url,comp_id,pim_id,content,way,name,tel,status=True):
    data = {
        "comp_status": status,
        "comp_content": content,
        "comp_staff_name": name,
        "comp_staff_tele": tel,
        "comp_way": way,
        "comp_handle_id": pim_id
    }
    return Request('PUT',f'{url}{comp_id}/',data)

# 获取单个投诉
def complaint_single(url,id):
    return Request('GET',f'{url}{id}/',{})

def handle_complaint_treat(url,id,summary):
    data = {
        "comp_treat": 2,
        "comp_summary": summary
    }
    return Request('PUT',f'{url}{id}/',data)

def upload_pic(url,file:bytes,extension_name):
    files = {"comp_media":("comp_media.{}".format(extension_name),file,"image/{}".format(extension_name))}
    return FileUpload(url,files)