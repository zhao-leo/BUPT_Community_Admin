from nicegui import ui
from source.webAPI.complaint import get_complaint
from source.webAPI.pim import getInf
from API import complaintAll

from source.layout.sidebar import sidebar
from source.layout.head import header


# from niceguiToolkit.layout import inject_layout_tool
# inject_layout_tool()
def complaintui():
    ui.page_title('建议列表-{}'.format(getInf()['NAME']))
    res=get_complaint(complaintAll())
    if res["code"]==200:
        with ui.column().style("font-size:1.5rem;width:100%;height:auto"):
            header()
            with ui.row().style("display:flex;height:100%;width:100%"):
                sidebar()
                with ui.column().style('flex:1'):
                    columns = [
                        {'name': 'id', 'label': 'ID', 'field': 'id','align': 'left'},
                        {'name': 'name', 'label': '建议人', 'field': 'name','align': 'left'},
                        {'name': 'content', 'label': '诉求内容', 'field': 'content','align': 'left'},
                        {'name': 'site', 'label': '诉求地点', 'field': 'site','align': 'left'},
                        {'name': 'time', 'label': '提交时间', 'field': 'time','align': 'left'},
                        {'name': 'link', 'label': '回复', 'field': 'link','align': 'left'}
                    ]
                    rows = [{'id':i['id'],'name':i['comp_name'],'content':i['comp_text'],'site':i['comp_site'],'time':i['comp_sub_time'].split('T')[0],'link':'/complaint/untreated/{}'.format(i['id'])} for i in res['data']]
                    table=ui.table(columns=columns, rows=rows, row_key='id',pagination=15).style("width:100%")
                    table.add_slot('body-cell-link', '''
                        <q-td :props="props">
                            <q-badge :color="blue">
                                <a :href="props.value">点击前往</a>
                            </q-badge>

                        </q-td>
                    ''')


    else:
        ui.notify(res["message"],position='top',type='warning')
        ui.navigate.to('/')