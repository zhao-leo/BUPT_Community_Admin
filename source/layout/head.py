# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.login import logout,update_password,add_admin
from source.webAPI.pim import update_pim,getInf
from API import pimapi,addadmin

def log_out():
    logout()
    ui.navigate.to('/')

def update_user_info():
    ui.notify('修改个人信息',position='top',type='info')

def header():
    with ui.dialog() as dialog1,ui.card():
        def handlepassword(url,code,recode):
            res=update_password(url,code,recode)
            if res["code"]==200:
                ui.notify(res["msg"],position='top',type='postive')
                ui.navigate.to('/home')
            else:
                ui.notify(res["msg"],position='top',type='warning')
        code = ui.input(label='新密码', password=True,password_toggle_button=True)
        recode = ui.input(label='确认密码', password=True)
        with ui.row():
            ui.button('取消',on_click=dialog1.close)
            ui.button('提交', on_click=lambda:handlepassword(pimapi(),code.value,recode.value))

    with ui.dialog() as dialog2,ui.card():
        def handlepim(url,account,name,phone):
            res=update_pim(url,account,name,phone)
            if res['code']==200:
                ui.notify(res['msg'],position='top',type='postive')
                ui.navigate.to('/home')
            else:
                ui.notify(res['msg'],position='top',type='warning')
        with ui.row():
            NAME=getInf()['NAME']
            ACCOUNT=getInf()['ACCOUNT']
            PHONE=getInf()['PHONE']
            account = ui.input(label='账号')
            account.value=ACCOUNT
            name = ui.input(label='姓名')
            name.value=NAME
        phone = ui.input(label='电话',validation={'请正确填写电话号码': lambda value: len(value) == 11 and value.isdigit()})
        phone.value=PHONE
        with ui.row():
            ui.button('取消',on_click=dialog2.close)
            ui.button('提交', on_click=lambda:handlepim(pimapi(),account.value,name.value,phone.value))

    with ui.dialog() as dialog3,ui.card():
        def handleNewUser(url,account,code):
            res=add_admin(url,account,code)
            if res["code"]==200:
                ui.notify(res["message"],position='top',type='postive')
                ui.navigate.to('/home')
            else:
                ui.notify(res["message"],position='top',type='warning')
        account = ui.input(label='登录名')
        code = ui.input(label='密码', password=True,password_toggle_button=True)
        with ui.row():
            ui.button('取消',on_click=dialog3.close)
            ui.button('提交', on_click=lambda:handleNewUser(addadmin(),account.value,code.value))
        

    with ui.card().style('width:100%; margin: auto;'):
        with ui.row().classes('w-full items-center').style("width:100%"):
            ui.label('社区反馈管理系统').classes('mr-auto')
            with ui.button(text='账户设置',icon='menu'):
                with ui.menu():
                    ui.menu_item('修改个人信息', on_click=dialog2.open)
                    ui.menu_item('修改密码', on_click=dialog1.open)
                    ui.menu_item('退出当前账户', on_click=log_out)
                    if getInf()['ID']<=3:
                        ui.menu_item('用户管理', on_click=dialog3.open)
