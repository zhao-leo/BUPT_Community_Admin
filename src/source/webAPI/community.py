# -*- coding: utf-8 -*-
from .request import Request,FileUpload

# 获取热线电话
def get_hotline(url):
    return Request('GET',url,{})

# 修改热线电话
def update_hotline(url,id,name,phone):
    data = {
        "hotline_who":name,
        "hotline_tele":phone
    }
    return Request('PUT',url+str(id)+'/',data)

# 添加热线电话
def add_hotline(url,name,phone):
    data = {
        "hotline_who":name,
        "hotline_tele":phone
    }
    return Request('POST',url,data)

# 删除热线电话
def remove_hotline(url,id):
    return Request('DELETE',url+str(id)+'/',{})

# 获取温馨提示
def get_warmtext(url):
    return Request('GET',url,{})

# 修改温馨提示
def update_warmtext(url,text):
    data = {
        "warn_text":text
    }
    return Request('POST',url,data)

# 获取图片
def get_picture(url):
    return Request('GET',url,{})

# 上传图片
def upload_pic(url,file:bytes):
    files = {"cover_file":file}
    return FileUpload(url,files)

# 删除图片
def delete_pic(url,id):
    return Request('DELETE',url+str(id)+'/',{})

# 上传背景
def upload_bkground(url,file):
    files = {"back_file":file}
    return FileUpload(url,files)