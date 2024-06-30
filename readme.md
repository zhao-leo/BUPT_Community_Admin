A python admin Based NiceGUI

# from niceguiToolkit.layout import inject_layout_tool
# inject_layout_tool()

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
        with ui.column():
            name=ui.input(label='回复人',validation={'人名不能为空': lambda value: len(value) >= 0})
            content=ui.textarea(label='回复内容',validation={'回复内容不能为空': lambda value: len(value) >= 0})
        with ui.column():
            tele=ui.input(label='联系电话',validation={'请正确填写电话号码': lambda value: len(value) == 11 and value.isdigit()})
            way=ui.input(label='解决方式',validation={'解决方式不能为空': lambda value: len(value) >= 0})
            with ui.row():
                ui.button('提交',on_click=create_on_click_handler(int(i['id']),content.value,way.value,name.value,tele.value))
                ui.button('取消',on_click=ui.notify(content.value))

def __handle_reply(getid,content,way,name,tel):
    url = replysuggestion()
    res = reply_suggestion(url,getid,content,way,name,tel)
    if res['code']==200:
        ui.notify(res['msg'],position='top',type='info')
    else:
        ui.notify(res['msg'],position='top',type='warning')

def create_on_click_handler(sugg_id, content, way, name, tele):
    return lambda: __handle_reply(sugg_id, content, way, name, tele)