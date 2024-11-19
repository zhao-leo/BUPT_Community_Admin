# -*- coding: utf-8 -*-
from .request import Request

# 获取登录信息
def login(url,user,password):
    data = {'manager_account': user, 'manager_code': password}
    return Request('POST',url,data)

# 修改管理员密码
def update_password(url,code,recode):
    data = {'manager_code': code, 'manager_recode': recode}
    return Request('PUT',url,data)

# 添加管理员
def add_admin(url,account,code,super):
    data = {'manager_account': account, 'manager_code': code,'manager_role':super}
    return Request('POST',url,data)
