from nicegui import ui
from source.webAPI.suggestion import get_suggestion,reply_suggestion
from API import suggestionAll,replysuggestion

from source.layout.sidebar import sidebar
from source.layout.head import header

# from niceguiToolkit.layout import inject_layout_tool
# inject_layout_tool()

def suggestionui():
    res=get_suggestion(suggestionAll())
    if res["code"]==200:
        with ui.dialog() as dialog,ui.card():
            ui.label('处理建议')
            ui.label('x')
            ui.label('y')
            ui.button('取消',on_click=dialog.close)
        with ui.column().style("font-size:1.5rem;width:100%;height:auto"):
            header()
            with ui.row().classes('w-full items-center').style("width:100%"):
                sidebar()
                with ui.column().style("width:90%;flex-direction:column;align-self:flex-start;height:auto"):
                    ui.label('未处理建议:')
                    with ui.row().classes('w-full items-center').style("width:100%"):
                        ui.label('ID').style('width:5%')
                        ui.label('建议人').style('width:20%;')
                        ui.label('联系内容').style('width:28%')
                        ui.label('建议地点').style('width:20%')
                        ui.label('提交时间').style('width:12%')
                        ui.label('处理').style('width:5%')
                    for i in res["data"]:
                        with ui.row().classes('w-full items-center').style("width:100%"):
                            ui.label('{}'.format(res["data"].index(i))).style('width:5%;font-size:1.2rem')
                            ui.label('{}'.format(i['sugg_name'])).style('width:20%;font-size:1.2rem')
                            ui.label('{}'.format(i['sugg_text'])).style('width:28%;font-size:1.2rem')
                            ui.label('{}'.format(i['sugg_site'])).style('width:20%;font-size:1.2rem')
                            formatted_date = i["sugg_sub_time"].split('T')[0]
                            ui.label(f'{formatted_date}').style('width:12%;font-size:1.2rem')
                            ui.button('处理',on_click=dialog.open).style('width:5%')
    else:
        ui.notify(res["message"],position='top',type='warning')
        ui.timer(1, lambda: ui.navigate.to('/'))