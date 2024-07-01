# -*- coding: utf-8 -*-
from API import replysuggestion
from nicegui import ui
from source.layout.head import header
from source.layout.sidebar import sidebar
from source.webAPI.suggestion import suggestion_single,reply_suggestion
from source.webAPI.pim import getInf

def __handle_reply(getid,content,way,name,tel,status):
    url = replysuggestion()
    res = reply_suggestion(url,getid,content,way,name,tel,status)
    if res['code']==200:
        ui.notify(res['msg'],position='top',type='info')
        ui.timer(1.0,lambda:ui.navigate.to('/suggestion/untreated'))
    else:
        ui.notify(res['msg'],position='top',type='warning')

def suggestion_num(id):
    ui.page_title('建议-{}-{}'.format(id,getInf()['NAME']))
    try:
        res = suggestion_single(replysuggestion(),id)
    except:
        ui.notify('网络错误',position='top',type='warning')
        ui.navigate.to('/suggestion/untreated')
    with ui.column().style("font-size:1.5rem;width:100%;height:auto"):
        header()
        with ui.row().style("height:100%;width:100%"):
            if res['code']==200 and res['data'][0]['sugg_status']==False:
                columns = [
                    {'name': 'name', 'label': '类型', 'field': 'name', 'required': True, 'align': 'left'},
                    {'name': 'inf', 'label': '信息', 'field': 'inf','align': 'left'},
                ]
                rows = [
                    {'name': '建议人：', 'inf': res['data'][0]['sugg_name']},
                    {'name': '建议地点：', 'inf': res['data'][0]['sugg_site']},
                    {'name': '联系电话：', 'inf': res['data'][0]['sugg_user_tele']},
                    {'name': '提交时间：', 'inf': res['data'][0]["sugg_sub_time"].split('T')[0]},
                    {'name': '建议内容：', 'inf': res['data'][0]['sugg_text']},
                ]
                sidebar()
                with ui.card().style('flex:1'):
                    with ui.column().style("width:100%;flex-direction:column;align-self:flex-start;height:100vh"):
                        ui.table(columns=columns, rows=rows, row_key='name').style('width:100%')
                        if res['data'][0]["suggestionmedia_set"]:
                            ui.label('附件图片：')
                            with ui.row():
                                for i in res['data'][0]["suggestionmedia_set"]:
                                    ui.image(i["sugg_media"]).style('weight:auto;height:200px').classes('object-fit:cover;')
                        with ui.row():
                            name=ui.input(label='回复人',validation={'人名不能为空': lambda value: len(value) >= 0})
                            tele=ui.input(label='联系电话',validation={'请正确填写电话号码': lambda value: len(value) == 11 and value.isdigit()})
                            way=ui.input(label='解决方式',validation={'解决方式不能为空': lambda value: len(value) >= 0})
                        switch = ui.switch('是否解决', value=True)
                        content=ui.textarea(label='回复内容',validation={'回复内容不能为空': lambda value: len(value) >= 0}).style('width:100%')
                        ui.button('提交',on_click=lambda: __handle_reply(id,content.value,way.value,name.value,tele.value,switch.value))
            else:
                ui.notify(res['message'],position='top',type='warning')
                ui.navigate.to('/suggestion/untreated')