# -*- coding: utf-8 -*-
from nicegui import ui,app
from source.webAPI.pim import get_deal
from API import handlenumber
from pyecharts.charts import Pie

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
            ui.label('欢迎您: {}'.format(app.storage.user.get('NAME'))).style('font-size:1.2rem')
            ui.separator()
            with ui.row().style('width:100%'):
                with ui.card().style('height:350px;width:25%'):
                    ui.label('以下是您的个人信息:').style('font-size:1.2rem')
                    ui.separator()
                    ui.label('身份: {}'.format(app.storage.user.get('ROLE'))).style('font-size:1.2rem')
                    ui.label('电话: {}'.format(app.storage.user.get('PHONE'))).style('font-size:1.2rem')
                    ui.label('账号: {}'.format(app.storage.user.get('ACCOUNT'))).style('font-size:1.2rem')

                with ui.card().style('height:350px;width:35%'):
                    ui.label('建议处理情况').style('font-size:1.5rem')
                    ui.echart.from_pyecharts(Pie().add("",list(zip(self.label,self.suggestion))))
                with ui.card().style('height:350px;width:35%'):
                    ui.label('诉求处理情况').style('font-size:1.5rem')
                    ui.echart.from_pyecharts(Pie().add("",list(zip(self.label,self.complaint))))

def pim_ui():
    PimPage().show_layout()