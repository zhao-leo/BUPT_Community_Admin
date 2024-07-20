# -*- coding: utf-8 -*-
from API import replysuggestion,BASE_URL
from nicegui import ui,app
from source.webAPI.suggestion import suggestion_single,reply_suggestion

from source.layout.page_layout import PageLayout

class SuggestionPage(PageLayout):
    def __init__(self,id):
        super().__init__(f'建议列表-{id}-'+'{}')
        self.id = id
        self.res=suggestion_single(replysuggestion(),id)
        if self.res.get('code') == 200 and self.res.get('data'):
            ui.notify(self.res.get('message'), type='info',position='top')
        else:
            ui.notify(self.res.get('message'), type='warning',position='top')
            ui.navigate.to('/suggestion/untreated')

    def content(self):
        if self.res.get('data'):
            def __handle_reply(doc_id,content,way,name,tele):
                    if not content or not way or not name or not tele:
                        ui.notify('请填写完整信息', type='warning',position='top')
                    else:
                        res=reply_suggestion(replysuggestion(),doc_id,app.storage.user.get('ID'),content,way,name,tele)
                        if res.get('code') == 200:
                            ui.notify(res.get('message'), type='info',position='top')
                            ui.navigate.to('/suggestion/untreated')
                        else:
                            ui.notify(res.get('message'), type='warning',position='top')
            columns = [
                {'name': 'name', 'label': '类型', 'field': 'name', 'required': True, 'align': 'left'},
                {'name': 'inf', 'label': '信息', 'field': 'inf','align': 'left'},
            ]
            rows = [
                {'name': '提出人：', 'inf': self.res['data'][0]['sugg_name']},
                {'name': '提出地点：', 'inf': self.res['data'][0]['sugg_site']},
                {'name': '联系电话：', 'inf': self.res['data'][0]['sugg_user_tele']},
                {'name': '提交时间：', 'inf': self.res['data'][0]["sugg_sub_time"].split('T')[0]},
                {'name': '建议内容：', 'inf': self.res['data'][0]['sugg_text']},
            ]
            with ui.card().style('width:100%'):
                with ui.column().style("width:100%;flex-direction:column;align-self:flex-start;height:100%"):
                    ui.table(columns=columns, rows=rows, row_key='name').style('width:100%')
                    if self.res['data'][0]["suggestionmedia_set"]:
                        ui.label('附件图片：')
                        with ui.row().style('flex-wrap:wrap'):
                            for i in self.res['data'][0]["suggestionmedia_set"]:
                                with ui.column().style('width:400px;height:auto;'):
                                    ui.image(BASE_URL[:-1]+i['comp_media']).style('object-fit:contain;') # .style('height:200px;width:auto;')
                    with ui.row():
                        name=ui.input(label='回复人',validation={'人名不能为空': lambda value: len(value) >= 0})
                        tele=ui.input(label='联系电话',validation={'请正确填写电话号码': lambda value: len(value) == 11 and value.isdigit()})
                        way=ui.input(label='解决方式',validation={'解决方式不能为空': lambda value: len(value) >= 0})
                    content=ui.textarea(label='回复内容',validation={'回复内容不能为空': lambda value: len(value) >= 0}).style('width:100%')
                    ui.button('提交',on_click=lambda: __handle_reply(self.id,content.value,way.value,name.value,tele.value))

def suggestion_num_ui(id):
    SuggestionPage(id).show_layout()