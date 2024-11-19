# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.suggestion import get_suggestion
from API import suggestionAll

from source.layout.page_layout import PageLayout

class SuggestionPage(PageLayout):
    def __init__(self):
        super().__init__('建议列表-{}')
        self.pagenum = 1
        self.res=get_suggestion(suggestionAll(),{'pagenum':self.pagenum,'pagesize':8})
        self.status = self.res.get('code')

    def content(self):
        @ui.refreshable
        def list_ui():
            self.res=get_suggestion(suggestionAll(),{'pagenum':self.pagenum,'pagesize':8})
            if self.res.get('data'):
                with ui.row().style('width:100%;height:auto'):
                    for i in self.res.get('data'):
                        with ui.card().style('width:100%;height:auto'):
                                with ui.row().style('width:100%;height:auto'):
                                    ui.label(i.get("id")).style('width:2%;height:auto')
                                    ui.label(i.get("sugg_name")).style('width:12%;height:auto')
                                    ui.label(i.get("sugg_title")).style('width:24%;height:auto')
                                    ui.label(i.get('sugg_site')).style('width:24%;height:auto')
                                    ui.label(i.get('sugg_sub_time').split('T')[0]).style('width:20%;height:auto')
                                    ui.button("点击前往",on_click=lambda i=i :ui.navigate.to('/suggestion/untreated/{}'.format(i.get('id')),new_tab=True)).style('width:8%;')
            else:
                with ui.column().style('width:100%'):
                    ui.label('暂无未处理表单').style('font-size: 40px;').style('width:100%').style('text-align: center;')
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

def suggestion_ui():
    SuggestionPage().show_layout()