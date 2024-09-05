# -*- coding: utf-8 -*-
from nicegui import ui,app
from source.webAPI.excel import get_excel
from source.webAPI.pim import get_deal
from API import excel,handlenumber
from datetime import datetime
from pyecharts.charts import Pie
import json

from source.layout.page_layout import PageLayout

class PimPage(PageLayout):
    def __init__(self):
        super().__init__('欢迎-{}')
        self.label = ['未处理','已处理']
        res = get_deal(handlenumber())
        if res.get('code') == 200:
            data = res.get('data')
            self.complaint = [data.get('comp_todo'),data.get('comp_done')]
            self.suggestion =[data.get('sugg_todo'),data.get('sugg_done')]
        else:
            ui.notify(res.get('message'), type='warning',position='top')
    def content(self):
        with ui.card().style("width:100%;height:100%"):
            ui.label('欢迎您: {}'.format(app.storage.user.get('NAME'))).style('font-size:1.1rem')
            ui.separator()
            with ui.row().style('width:100%'):
                with ui.card().style('height:350px;width:18%'):
                    ui.label('以下是您的个人信息:').style('font-size:1.1rem')
                    ui.separator()
                    ui.label('身份: {}'.format(app.storage.user.get('ROLE'))).style('font-size:1.1rem')
                    ui.label('电话: {}'.format(app.storage.user.get('PHONE'))).style('font-size:1.1rem')
                    ui.label('账号: {}'.format(app.storage.user.get('ACCOUNT'))).style('font-size:1.1rem')

                with ui.card().style('height:350px;width:30%'):
                    ui.label('建议处理情况').style('font-size:1.5rem')
                    ui.echart.from_pyecharts(Pie().add("",list(zip(self.label,self.suggestion))))
                with ui.card().style('height:350px;width:30%'):
                    ui.label('诉求处理情况').style('font-size:1.5rem')
                    ui.echart.from_pyecharts(Pie().add("",list(zip(self.label,self.complaint))))

                with ui.card().style('height:350px;width:18%'):
                    ui.label('获取Excel表格').style('font-size:1.5rem')
                    with ui.input('开始日期') as date1:
                        with ui.menu().props('no-parent-event') as menu:
                            with ui.date().bind_value(date1):
                                with ui.row().classes('justify-end'):
                                    ui.button('关闭', on_click=menu.close).props('flat')
                        with date1.add_slot('append'):
                            ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
                    with ui.input('结束日期') as date2:
                        with ui.menu() as menu:
                            with ui.date().bind_value(date2).props(f''':options="date => date >= '{date1.value}'"'''):
                                with ui.row().classes('justify-end'):
                                    ui.button('关闭', on_click=menu.close).props('flat')
                        with date2.add_slot('append'):
                            ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
                    def download_excel(date1: ui.input,date2: ui.input):
                        if date1.value=='' or date2.value=='':
                            ui.notify('日期不能为空',position='top',type='warning')
                        elif datetime.strptime(date2.value,'%Y-%m-%d')<datetime.strptime(date1.value,'%Y-%m-%d'):
                            ui.notify('结束日期不能小于开始日期',position='top',type='warning')
                        else:
                            response = get_excel(excel(),date1.value,date2.value)
                            if response.status_code == 200:
                                ui.download(response.content,'{}-{}社区投诉和建议表.xlsx'.format(date1.value,date2.value))
                            else:
                                res = json.loads(response.text)
                                ui.notify(res.get('message'),position='top',type='warning',close_button="关闭")

                    ui.button('点击下载', on_click=lambda: download_excel(date1,date2)).style('margin-top:1rem')

def pim_ui():
    PimPage().show_layout()