# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.suggestion import get_suggestion
from source.webAPI.pim import getInf
from API import suggestionAll

from source.layout.sidebar import sidebar
from source.layout.head import header
from source.layout.footer import footer

def suggestionui():
    ui.page_title('建议列表-{}'.format(getInf()['NAME']))
    res=get_suggestion(suggestionAll())
    if res["code"]==200:
        with ui.column().style("font-size:1.5rem;width:100%;height:auto"):
            header()
            with ui.row().style("display:flex;height:100%;width:100%"):
                sidebar()
                with ui.column().style('flex:1'):
                    columns = [
                        {'name': 'id', 'label': 'ID', 'field': 'id','align': 'left'},
                        {'name': 'name', 'label': '建议人', 'field': 'name','align': 'left'},
                        {'name': 'content', 'label': '建议内容', 'field': 'content','align': 'left'},
                        {'name': 'site', 'label': '建议地点', 'field': 'site','align': 'left'},
                        {'name': 'time', 'label': '提交时间', 'field': 'time','align': 'left','sortable': True},
                        {'name': 'link', 'label': '回复', 'field': 'link','align': 'left'}
                    ]
                    rows = [{'id':i['id'],'name':i['sugg_name'],'content':i['sugg_text'],'site':i['sugg_site'],'time':i['sugg_sub_time'].split('T')[0],'link':'/suggestion/untreated/{}'.format(i['id'])} for i in res['data']]
                    table=ui.table(columns=columns, rows=rows, row_key='id',pagination=15).style("width:100%")
                    table.add_slot('body-cell-link', '''
                        <q-td :props="props">
                            <q-badge :color="blue">
                                <a :href="props.value">点击前往</a>
                            </q-badge>

                        </q-td>
                    ''')
            footer()
    else:
        ui.notify(res["message"],position='top',type='warning')
        ui.navigate.to('/home')