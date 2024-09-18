# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.suggestion import get_suggestion
from API import suggestionHistory

from source.layout.page_layout import PageLayout

class SuggestionReplyPage(PageLayout):
    def __init__(self):
        super().__init__('诉求列表-历史记录-{}')
        self.res=get_suggestion(suggestionHistory())
        if self.res.get('code') == 200 and self.res.get('data'):
            # ui.notify(self.res.get('message'), type='info',position='top')
            pass
        else:
            # ui.notify(self.res.get('message'), type='warning',position='top')
            pass

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
                rows = [{'id':i.get('id'),'name':i.get('sugg_name'),'content':i.get('sugg_title'),'site':i.get('sugg_site'),'time':i.get('sugg_sub_time').split('T')[0],'link':'/suggestion/finished/{}'.format(i.get('id'))} for i in self.res.get('data')]
                table=ui.table(columns=columns, rows=rows, row_key='id',pagination={'rowsPerPage': 12, 'sortBy': 'id'}).style("width:100%")
                table.add_slot('body-cell-link', '''
                    <q-td :props="props">
                        <q-badge :color="blue">
                            <a :href="props.value">点击前往</a>
                        </q-badge>
                    </q-td>
                ''')
        else:
            with ui.column().style('width:100%'):
                ui.label('暂无未处理表单').style('font-size: 40px;').style('width:100%').style('text-align: center;')
def suggestion_finished_ui():
    SuggestionReplyPage().show_layout()