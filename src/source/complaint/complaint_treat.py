# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.complaint import get_complaint
from API import complainttreat

from source.layout.page_layout import PageLayout

class ComplaintReplyPage(PageLayout):
    def __init__(self):
        super().__init__('诉求列表-待回访-{}')
        self.res=get_complaint(complainttreat())
        if self.res.get('code') == 200 and self.res.get('data'):
            ui.notify(self.res.get('message'), type='info',position='top')
        else:
            ui.notify(self.res.get('message'), type='warning',position='top')

    def content(self):
        if self.res.get('data'):
            with ui.column().style('width:100%'):
                columns = [
                    {'name': 'id', 'label': 'ID', 'field': 'id','align': 'left','sortable': True,':sort': '(a,b,rowA,rowB) => b - a'},
                    {'name': 'name', 'label': '建议人', 'field': 'name','align': 'left'},
                    {'name': 'content', 'label': '诉求内容', 'field': 'content','align': 'left'},
                    {'name': 'site', 'label': '诉求地点', 'field': 'site','align': 'left'},
                    {'name': 'time', 'label': '提交时间', 'field': 'time','align': 'left'},
                    {'name': 'link', 'label': '回复', 'field': 'link','align': 'left'}
                ]
                rows = [{'id':i.get('id'),'name':i.get('comp_name'),'content':i.get('comp_title'),'site':i.get('comp_site'),'time':i.get('comp_sub_time').split('T')[0],'link':'/complaint/treated/{}'.format(i.get('id'))} for i in self.res.get('data')]
                table=ui.table(columns=columns, rows=rows, row_key='id',pagination={'rowsPerPage': 12, 'sortBy': 'id'}).style("width:100%")
                table.add_slot('body-cell-link', '''
                    <q-td :props="props">
                        <q-badge :color="blue">
                            <a :href="props.value">点击前往</a>
                        </q-badge>
                    </q-td>
                ''')

def complaint_treat_ui():
    ComplaintReplyPage().show_layout()