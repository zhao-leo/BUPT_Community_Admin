# -*- coding: utf-8 -*-
from nicegui import ui,app
from source.webAPI.login import update_password,add_admin
from source.webAPI.pim import update_pim
from API import pimapi,addadmin

# 定义logout函数,用于清除token
def logout():
    app.storage.user['TOKEN'] = None
    app.storage.user['NAME'] = None
    app.storage.user['ACCOUNT'] = None
    app.storage.user['PHONE'] = None
    app.storage.user['ROLE'] = None
    ui.notify('已退出', close_button='确定')
    ui.navigate.to('/')

def header():
# --------------------------------- dialog for update password --------------------------------- #
    with ui.dialog() as dialog1,ui.card(): # 修改密码

        def handlepassword(url,code,recode):
            res=update_password(url,code,recode)
            if res["code"]==200: # 如果返回的code为200,表示修改成功,关闭弹窗并跳转到首页
                ui.notify(res["message"],position='top',type='info')
                dialog1.close()
                ui.navigate.to('/home')
            else: # 否则提示错误信息
                ui.notify(res["message"],position='top',type='warning',close_button='确定')

        code1 = ui.input(label='新密码', password=True,password_toggle_button=True)
        recode = ui.input(label='确认密码', password=True,password_toggle_button=True)
        
        with ui.row():
            ui.button('取消',on_click=dialog1.close)
            ui.button('提交', on_click=lambda:handlepassword(pimapi(),code1.value,recode.value))

# --------------------------- dialog for update personal information --------------------------- #
    with ui.dialog() as dialog2,ui.card(): # 修改个人信息

        def handlepim(url,account,name,phone):
            res=update_pim(url,account,name,phone)
            if res['code']==200: # 如果返回的code为200,表示修改成功,关闭弹窗并跳转到首页
                ui.notify(res["message"],position='top',type='info')
                dialog1.close()
                ui.navigate.to('/home')
            else: # 否则提示错误信息
                ui.notify(res["message"],position='top',type='warning',close_button='确定')

        with ui.row():
            NAME=app.storage.user.get('NAME')
            ACCOUNT=app.storage.user.get('ACCOUNT')
            PHONE=app.storage.user.get('PHONE')
            account1 = ui.input(label='账号')
            account1.value=ACCOUNT
            name = ui.input(label='姓名')
            name.value=NAME
        phone = ui.input(label='电话',validation={'请正确填写电话号码': lambda value: value is not None and len(value) == 11 and value.isdigit()})
        phone.value=PHONE

        with ui.row():
            ui.button('取消',on_click=dialog2.close)
            ui.button('提交', on_click=lambda:handlepim(pimapi(),account1.value,name.value,phone.value))

# ---------------------------------- dialog for add manager ---------------------------------- #
    with ui.dialog() as dialog3,ui.card(): # 添加管理员

        def handleNewUser(url,account,code):
            res=add_admin(url,account,code)
            if res['code']==200: # 如果返回的code为200,表示修改成功,关闭弹窗并跳转到首页
                ui.notify(res["message"],position='top',type='info')
                dialog1.close()
                ui.navigate.to('/home')
            else: # 否则提示错误信息
                ui.notify(res["message"],position='top',type='warning',close_button='确定')

        account = ui.input(label='登录名')
        code = ui.input(label='密码', password=True,password_toggle_button=True)

        with ui.row():
            ui.button('取消',on_click=dialog3.close)
            ui.button('提交', on_click=lambda:handleNewUser(addadmin(),account.value,code.value))

# ------------------------------------- logout function ------------------------------------- #
    with ui.header(elevated=True).classes('items-center justify-between').style('background-color: white;'):
        ui.label('社区反馈管理系统').style('font-size:1.5rem;font-weight:bold;color:black')
        with ui.button(text='账户设置',icon='menu'):
            with ui.menu():
                ui.menu_item('修改个人信息', on_click=dialog2.open)
                ui.menu_item('修改密码', on_click=dialog1.open)
                ui.menu_item('退出当前账户', on_click=logout)
                if app.storage.user.get('ROLE')=='超级管理员': # 如果是超级管理员,则显示用户管理
                    ui.separator()
                    ui.menu_item('添加用户', on_click=dialog3.open)
