# -*- coding: utf-8 -*-
from nicegui import ui,app
from source.webAPI.login import login
from API import loginapi
from source.layout.footer import footer

def __login(username, password):
    res=login(loginapi(),username, password)
    if res["code"]==200:
        app.storage.user['TOKEN']=res["token"]
        ui.notify(res["message"],position='top',type='info')
        ui.navigate.to('/home')
    else:
        ui.notify(res["message"],position='top',type='warning')


    #.style('''background-image: url("https://img.pptjia.com/image/20190311/23d36b57157ce994302d001124a0b562.jpg");''')
def login_ui():
    ui.page_title('登录')
    ui.query('body').style('''background-image: url("https://img.pptjia.com/image/20190311/23d36b57157ce994302d001124a0b562.jpg"); background-size: cover;''')
    with ui.card(align_items='center').classes('mx-auto').style("max-width: 500px; margin-top: 10%;").style('background-color: rgb(255 255 255 / 40%);'):
        ui.label('欢迎使用社区反馈管理系统').style("width:auto;height:auto;align-self:center").style("font-size:2.0rem")
        with ui.card().style('background-color: rgb(255 255 255 / 0%);'):
            ui.label('登录').style("font-size:1.5rem")
            username = ui.input(label='用户名', validation={'用户名不能为空': lambda value: len(value) >= 0}).style('font-size:1rem;width:100%;')
            password = ui.input(label='密码', password=True, password_toggle_button=True, validation={'密码不得少于6位': lambda value: len(value) >= 6}).style('font-size:1rem;width:100%;')
            ui.button('登录', on_click=lambda: __login(username.value, password.value))
    with ui.footer().style('height: 50px;').style('background-color: rgb(0 0 0 / 0%);'):
        with ui.row().classes('w-full justify-center items-center'):
            ui.link('京ICP-000000000000000', 'https://help.aliyun.com/zh/icp-filing/support/website-to-add-the-record-number-faq').style('font-size:1rem; margin-right: 2rem; font-color: black;')