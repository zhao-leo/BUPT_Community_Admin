# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.suggestion import get_suggestion
from API import suggestionAll

from source.layout.page_layout import PageLayout

class SuggestionPage(PageLayout):
    def __init__(self):
        super().__init__('建议列表-{}')
        self.res=get_suggestion(suggestionAll())
        if self.res.get('code') == 200 and self.res.get('data'):
            ui.notify(self.res.get('message'), type='info',position='top')
        else:
            ui.notify(self.res.get('message'), type='warning',position='top')

            ui.navigate.to('/home')

    def content(self):
        if self.res.get('data'):
            with ui.column().style('width:100%'):
                columns = [
                    {'name': 'id', 'label': 'ID', 'field': 'id','align': 'left','sortable': True,':sort': '(a,b,rowA,rowB) => b - a'},
                    {'name': 'name', 'label': '建议人', 'field': 'name','align': 'left'},
                    {'name': 'content', 'label': '建议内容', 'field': 'content','align': 'left'},
                    {'name': 'site', 'label': '建议地点', 'field': 'site','align': 'left'},
                    {'name': 'time', 'label': '提交时间', 'field': 'time','align': 'left'},
                    {'name': 'link', 'label': '回复', 'field': 'link','align': 'left'}
                ]
                rows = [{'id':i.get('id'),'name':i.get('sugg_name'),'content':i.get('sugg_text'),'site':i.get('sugg_site'),'time':i.get('sugg_sub_time').split('T')[0],'link':'/suggestion/untreated/{}'.format(i.get('id'))} for i in self.res.get('data')]
                table=ui.table(columns=columns, rows=rows, row_key='id',pagination={'rowsPerPage': 12, 'sortBy': 'id'}).style("width:100%")
                table.add_slot('body-cell-link', '''
                    <q-td :props="props">
                        <q-badge :color="blue">
                            <a :href="props.value">点击前往</a>
                        </q-badge>
                    </q-td>
                ''')

def suggestion_ui():
    SuggestionPage().show_layout()