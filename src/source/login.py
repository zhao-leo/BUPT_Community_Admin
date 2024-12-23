# -*- coding: utf-8 -*-
from nicegui import ui,app
from source.webAPI.login import login
from source.webAPI.community import get_picture
from API import loginapi,background,BASE_URL
from os import getenv
import re

def loginui(username, password):
    res=login(loginapi(),username, password)
    if res["code"]==200:
        app.storage.user['TOKEN']=res["token"]
        ui.notify(res["message"],position='top',type='info')
        ui.navigate.to('/home')
    else:
        ui.notify(res["message"],position='top',type='warning')

def login_ui():
    ui.page_title('登录')
    try:
        r = get_picture(background()).get('data')[0].get('back_file')
    except:
        r = ''
    ui.query('body').style(f'''background-image: url("{BASE_URL[:-1]+r}"); background-size: cover;''').classes('no-shadow')
    with ui.card(align_items='center').classes('mx-auto').style("max-width: 500px; margin-top: 10%;").style('background-color: rgb(255 255 255 / 40%);'):
        with ui.card().style('background-color: rgb(255 255 255 / 0%);width:100%;').classes('no-shadow'):
            ui.label('欢迎使用社区反馈管理系统').style("width:auto;height:auto;align-self:center").style("font-size:2.0rem")
        ui.separator()
        with ui.card().style('background-color: rgb(255 255 255 / 0%);width:100%;').classes('no-shadow'):
            username = ui.input(label='用户名', validation={'用户名只能包含英文字母且不能为空': lambda value:( re.match(r'^[a-zA-Z]+$', value) is not None)}).style('font-size:1rem;width:100%;')
            password = ui.input(label='密码', password=True, password_toggle_button=True, validation={'密码不得少于6位': lambda value: len(value) >= 6}).style('font-size:1rem;width:100%;')
            ui.button('登录', on_click=lambda: loginui(username.value, password.value))
    with ui.footer().style('height: 50px;').style('background-color: rgb(0 0 0 / 0%);'):
        with ui.row().classes('w-full justify-center items-center'):
            ui.link(getenv('ICP_CODE'), "https://beian.miit.gov.cn/").style('font-size:1rem; margin-right: 2rem; font-color: black;')