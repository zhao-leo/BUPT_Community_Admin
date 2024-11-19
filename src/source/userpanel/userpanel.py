# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.userpanel import get_full_usr,delete_user,rst_user
from API import manager_list,pimapi,manager_rst

from source.layout.page_layout import PageLayout

class ManagerPanel(PageLayout):
    def __init__(self):
        super().__init__('管理员列表-{}')
        self.pagenum = 1
        self.res=get_full_usr(manager_list(),{'pagenum':self.pagenum,'pagesize':8})
        self.status = self.res.get('code')

    def content(self):
        with ui.card().style('width:100%;height:auto'):
            with ui.row().style('width:100%;height:auto'):
                ui.label('编号').style('width:2%;height:auto')
                ui.label('人员姓名').style('width:24%;height:auto')
                ui.label('人员电话').style('width:24%;height:auto')
                ui.label('登录名').style('width:24%;height:auto')
                ui.label('操作').style('width:20%;height:auto')
        
        def Delete_user(id):
            res = delete_user(pimapi(),id)
            if res.get('code') == 200:
                ui.notify(res.get('message'),type='info',position='top')
                list_ui.refresh()
            else:
                ui.notify(res.get('message'),type='warning',position='top')

        def Reset_user(id):
            res =  rst_user(manager_rst(),id)
            if res.get('code') == 200:
                ui.notify(res.get('message'),type='info',position='top')
                list_ui.refresh()
            else:
                ui.notify(res.get('message'),type='warning',position='top')
        @ui.refreshable
        def list_ui():
            self.res=get_full_usr(manager_list(),{'pagenum':self.pagenum,'pagesize':8})
            if self.res.get('data'):
                with ui.row().style('width:100%;height:auto'):
                    for i in self.res.get('data'):
                        with ui.card().style('width:100%;height:auto'):
                                with ui.row().style('width:100%;height:auto'):
                                    ui.label(i.get("id")).style('width:2%;height:auto')
                                    ui.label(i.get("manager_name") or "未设置").style('width:24%;height:auto')
                                    ui.label(i.get("manager_tele") or "未设置").style('width:24%;height:auto')
                                    ui.label(i.get('manager_account')).style('width:24%;height:auto')
                                    ui.button("删除",on_click=lambda i=i:Delete_user(i.get("id")),color='red').style('width:8%;')
                                    ui.button("重置",on_click=lambda i=i:Reset_user(i.get("id"))).style('width:8%;')
            else:
                with ui.column().style('width:100%'):
                    ui.label('暂无数据').style('font-size: 40px;').style('width:100%').style('text-align: center;')
        list_ui()
        @ui.refreshable
        def tab_ui():
            with ui.row().style('width:100%;height:auto;display:flex;justify-content:center;'):
                if self.pagenum != 1:
                    def former_page():
                        self.pagenum = self.pagenum - 1
                        list_ui.refresh()
                        tab_ui.refresh()
                    ui.button("上一页",on_click=lambda:former_page())
                ui.button(self.pagenum)
                if self.pagenum != self.res.get("total_pages"):
                    def next_page():
                        self.pagenum = self.pagenum + 1
                        list_ui.refresh()
                        tab_ui.refresh()
                    ui.button('下一页',on_click=lambda:next_page())
        if self.status == 200:
            tab_ui()
def userpanel_ui():
    ManagerPanel().show_layout()