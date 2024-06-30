# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.login import login
from API import loginapi

def __login(username, password):
    url = loginapi()
    res=login(url,username, password)
    if res["code"]==1:
        ui.notify(res["msg"],position='top',type='info')
        ui.navigate.to('/home')
    else:
        ui.notify(res["msg"],position='top',type='warning')

def loginui():
    with ui.column(align_items='center').style("height:100vh;width:100%;flex-direction:column").classes('w-full h-full flex justify-center items-center'):
        ui.label('欢迎使用社区反馈管理系统').style("width:auto;height:auto;align-self:center").style("font-size:2.0rem")
        with ui.card():
            ui.label('登录')
            username=ui.input(label='用户名',validation={'用户名不能为空': lambda value: len(value) >= 0})
            password=ui.input(label='密码', password=True,password_toggle_button=True, validation={'密码不得少于6位': lambda value: len(value) >= 6})
            ui.button('登录', on_click=lambda: __login(username.value, password.value))