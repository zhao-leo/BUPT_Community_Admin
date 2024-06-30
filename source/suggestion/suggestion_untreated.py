from nicegui import ui
from source.webAPI.suggestion import get_suggestion,reply_suggestion
from API import suggestionAll,replysuggestion

from source.layout.sidebar import sidebar
from source.layout.head import header

def suggestionui():
    res=get_suggestion(suggestionAll())
    if res["code"]==200:
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
                        
                            with ui.dialog() as dialog,ui.card().style('width:80%'):
                                with ui.column():
                                    with ui.row():
                                        ui.label('建议人')
                                        ui.label('{}'.format(i['sugg_name']))
                                    with ui.row():
                                        ui.label('建议地点')
                                        ui.label('{}'.format(i['sugg_site']))
                                    with ui.row():
                                        ui.label('联系电话')
                                        ui.label('{}'.format(i['sugg_user_tele']))
                                    with ui.row():
                                        ui.label('提交时间')
                                        formatted_date = i["sugg_sub_time"].split('T')[0]
                                        ui.label(f'{formatted_date}')
                                    with ui.row():
                                        ui.label('联系内容')
                                        ui.label('{}'.format(i['sugg_text']))
                                with ui.row():
                                    name=ui.input(label='回复人',placeholder='请输入回复人姓名')
                                    tele=ui.input(label='联系电话',placeholder='请输入联系电话')
                                    way=ui.input(label='解决方式',placeholder='请输入解决方式')
                                content=ui.textarea(label='回复内容',placeholder='请输入回复内容').style('width:550px')
                                # def handle_reply():
                                #     res = reply_suggestion(replysuggestion(),i['id'],content.value,way.value,name.value,tele.value)
                                #     if res['code']==200:
                                #         ui.notify(res['msg'],position='top',type='info')
                                #     else:
                                #         ui.notify(res['msg'],position='top',type='warning')
                                #     dialog.close()
                                with ui.row():
                                    #ui.button('提交',on_click=handle_reply)
                                    ui.button('取消',on_click=dialog.close)
                            
                            ui.label('{}'.format(i["id"])).style('width:5%;font-size:1.1rem')
                            ui.label('{}'.format(i['sugg_name'])).style('width:20%;font-size:1.1rem')
                            ui.label('{}'.format(i['sugg_text'])).style('width:28%;font-size:1.1rem')
                            ui.label('{}'.format(i['sugg_site'])).style('width:20%;font-size:1.1rem')
                            formatted_date = i["sugg_sub_time"].split('T')[0]
                            ui.label(f'{formatted_date}').style('width:12%;font-size:1.1rem')
                            ui.button('处理',on_click=dialog.open).style('width:5%')
    else:
        ui.notify(res["message"],position='top',type='warning')
        ui.navigate.to('/')

        #         {
        #     "id": 3,
        #     "suggestionmedia_set": [],
        #     "sugg_sub_time": "2024-05-22T15:15:17.547136+08:00",
        #     "sugg_status": false,
        #     "sugg_content": "",
        #     "sugg_staff_name": "",
        #     "sugg_way": "",
        #     "sugg_handle_time": "2024-05-22T15:15:17.549277+08:00",
        #     "sugg_staff_tele": "",
        #     "sugg_feedback": null,
        #     "sugg_sub_id": 1,
        #     "sugg_handle_id": null
        # },

