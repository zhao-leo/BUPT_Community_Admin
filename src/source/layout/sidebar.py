# -*- coding: utf-8 -*-
from nicegui import ui
import json
from datetime import datetime
from source.webAPI.excel import get_excel
from API import excel

def sidebar():
    with ui.dialog() as dialog,ui.card():
        #ui.label("请选择导出数据的日期范围").style('font-size:1.5rem')
        ui.separator()
        result = ui.date().props("range").props(''':options="date => date <= '{}'"'''.format(datetime.now().strftime(r"%Y/%m/%d")))
        def download_excel(date: dict):
            # date = json.loads(date)
            date1 = date.get("from")
            date2 = date.get("to")
            # print(date)
            if date1=='' or date2=='':
                ui.notify('日期不能为空',position='top',type='warning')
            elif datetime.strptime(date2,r'%Y-%m-%d')<datetime.strptime(date1,r'%Y-%m-%d'):
                ui.notify('结束日期不能小于开始日期',position='top',type='warning')
            else:
                response = get_excel(excel(),date1.replace("/","-"),date2.replace("/","-"))
                if response.status_code == 200:
                    ui.download(response.content,'{}-{}社区投诉和建议表.xlsx'.format(date1,date2))
                else:
                    res = json.loads(response.text)
                    ui.notify(res.get('message'),position='top',type='warning',close_button="关闭")

        with ui.row():
            ui.button('取消',on_click=dialog.close)
            ui.button('点击下载', on_click=lambda:download_excel(result.value))

    
    with ui.left_drawer(bordered=True,fixed=False).props('width=170 bordered'):
        with ui.column().style("height:100%;width:auto;font-size:1.0rem"):
            ui.item('欢迎',on_click=lambda: ui.navigate.to('/home'))

            with ui.expansion('社区建议'):
                ui.item('待处理', on_click=lambda: ui.navigate.to('/suggestion/untreated'))
                ui.item('待回访', on_click=lambda: ui.navigate.to('/suggestion/treated'))
            
            with ui.expansion('社区诉求'):
                ui.item('待处理', on_click=lambda: ui.navigate.to('/complaint/untreated'))
                ui.item('待回访', on_click=lambda: ui.navigate.to('/complaint/treated'))

            # if app.storage.user.get('ROLE')=='超级管理员':
            #     ui.item('社区管理',on_click=lambda: ui.navigate.to('/community'))
            ui.item('社区管理',on_click=lambda: ui.navigate.to('/community'))
            ui.item('导出数据',on_click=lambda: dialog.open())