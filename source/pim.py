# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.pim import get_pim,getInf
from API import pimapi

from source.layout.sidebar import sidebar
from source.layout.head import header

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
                    with ui.column().style("width:100%;flex-direction:column;align-self:flex-start;height:100%"):
                        ui.label('欢迎您: {}'.format(person['NAME']))
                        ui.label('以下是您的个人信息:').style('font-size:1.1rem')
                        with ui.card():
                            ui.label('身份: {}'.format(__identify_id(person['ID']))).style('font-size:1.1rem')
                            ui.label('电话: {}'.format(person['PHONE'])).style('font-size:1.1rem')
                            ui.label('账号: {}'.format(person['ACCOUNT'])).style('font-size:1.1rem')