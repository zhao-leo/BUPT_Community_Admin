# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.pim import get_pim,getInf
from source.webAPI.excel import get_excel
from API import pimapi,excel

from source.layout.sidebar import sidebar
from source.layout.head import header
from source.layout.footer import footer

def __get__pim():
    url = pimapi()
    return get_pim(url)

def __identify_id(id):
    if id<=3:
        return '超级管理员'
    else:
        return '普通管理员'

def pimui():
    res=__get__pim()
    if res["code"]==149 or res["code"]==0:
        ui.notify(res["msg"],position='top',type='warning')
        ui.timer(1, lambda: ui.navigate.to('/'))
    elif res["code"]==200:
        person=getInf()
        ui.page_title('欢迎-{}'.format(person['NAME']))
        with ui.column().style("font-size:1.5rem;width:100%;height:auto"):
            header()
            with ui.row().style("width:100%;height:auto"):
                sidebar()
                with ui.card().style("flex:1"):
                    with ui.row().style("width:100%;height:100%"):
                        with ui.card():
                            with ui.card().style("flex:1"):
                                ui.label('欢迎您: {}'.format(person['NAME']))
                                ui.label('以下是您的个人信息:').style('font-size:1.1rem')
                            with ui.card().style("flex:1"):
                                ui.label('身份: {}'.format(__identify_id(person['ID']))).style('font-size:1.1rem')
                                ui.label('电话: {}'.format(person['PHONE'])).style('font-size:1.1rem')
                                ui.label('账号: {}'.format(person['ACCOUNT'])).style('font-size:1.1rem')
                        with ui.card():
                            ui.label('获取Excel表格').style('font-size:1.5rem')
                            with ui.input('开始日期') as date1:
                                with ui.menu() as menu:
                                    with ui.date().bind_value(date1) as startdate:
                                        with ui.row().classes('justify-end'):
                                            ui.button('关闭', on_click=menu.close).props('flat')
                                with date1.add_slot('append'):
                                    ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

                            with ui.input('结束日期') as date2:
                                with ui.menu() as menu:
                                    with ui.date().bind_value(date2) as enddate:
                                        with ui.row().classes('justify-end'):
                                            ui.button('关闭', on_click=menu.close).props('flat')
                                with date2.add_slot('append'):
                                    ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
                            ui.button('点击下载', on_click=lambda: ui.download(get_excel(excel(),startdate.value,enddate.value),'{}-{}XX社区投诉和建议表.xlsx'.format(startdate.value,enddate.value))).style('margin-top:1rem')
                        
            footer()