# -*- coding: utf-8 -*-
from source.webAPI.request import Request

# 获取管理员信息
def get_pim(url):
    return Request('GET',url,{})

# 更新个人信息
def update_pim(url,account,name,phone):
    data = {'manager_name': name, 'manager_tele': phone, 'manager_account': account}
    return Request('PUT',url,data)

# 获取网站访问量
def Frequency(url):
    return Request('GET',url,{})