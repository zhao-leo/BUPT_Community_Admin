# -*- coding: utf-8 -*-
from API import replycomplaint,BASE_URL,complainthandle,compPicupload
from nicegui import ui,events
from source.webAPI.complaint import complaint_single,handle_complaint_treat,upload_pic

from source.layout.page_layout import PageLayout

class ComplaintPage(PageLayout):
    def __init__(self,id):
        super().__init__(f'待回访诉求-{id}-'+'{}')
        self.id = id
        self.res=complaint_single(replycomplaint(),id)
        if self.res.get('code') == 200 and self.res.get('data'):
            ui.notify(self.res.get('message'), type='info',position='top')
        else:
            ui.notify(self.res.get('message'), type='warning',position='top')
            ui.navigate.to('/complaint/untreated')

    def content(self):
        if self.res.get('data'):
            def preview(res: list):
                with ui.dialog() as dialog,ui.card().style('width:80vh;height:auto;'):
                    if res!=None:
                        with ui.carousel(animated=True, arrows=True, navigation=True).style('width: 60%;height:auto;align-self:center'):
                            for i in res:
                                with ui.carousel_slide().classes('p-0'):
                                    ui.image(BASE_URL[:-1]+i['comp_media'])
                        ui.button('关闭').on_click(lambda:dialog.close())
                dialog.open()
            def preview2(res: list):
                with ui.dialog() as dialog,ui.card().style('width:80vh;height:auto;'):
                    if res!=None:
                        with ui.carousel(animated=True, arrows=True, navigation=True).style('width: 60%;height:auto;align-self:center'):
                            for i in res:
                                with ui.carousel_slide().classes('p-0'):
                                    ui.image(BASE_URL[:-1]+i['comp_handle_media'])
                        ui.button('关闭').on_click(lambda:dialog.close())
                dialog.open()
            def __handle_reply(doc_id,summary):
                if summary == '':
                    summary = '无'
                res=handle_complaint_treat(complainthandle(),doc_id,summary)
                if res.get('code') == 200:
                    ui.notify(res.get('message'), type='info',position='top')
                    ui.navigate.to('/complaint/treated')
                else:
                    ui.notify(res.get('message'), type='warning',position='top')
            columns = [
                {'name': 'name', 'label': '类型', 'field': 'name', 'required': True, 'align': 'left'},
                {'name': 'inf', 'label': '信息', 'field': 'inf','align': 'left'},
            ]
            rows = [
                {'name': '提出人：', 'inf': self.res['data'][0]['comp_name']},
                {'name': '提出地点：', 'inf': self.res['data'][0]['comp_site']},
                {'name': '联系电话：', 'inf': self.res['data'][0]['comp_user_tele']},
                {'name': '提交时间：', 'inf': self.res['data'][0]["comp_sub_time"].split('T')[0]},
                {'name': '建议内容：', 'inf': self.res['data'][0]['comp_text']},
                {'name': '处理状态：', 'inf': '需要回访' if self.res['data'][0]['comp_treat'] else '不需要回访','slot': 'row_5'},
            ]
            row2 = [
                {'name': '回复人：', 'inf':  self.res['data'][0]['comp_staff_name']},
                {'name': '回复电话：', 'inf': self.res['data'][0]['comp_staff_tele']},
                {'name': '回复时间：', 'inf': self.res['data'][0]['comp_handle_time'][:10]},
                {'name': '回复内容：', 'inf': self.res['data'][0]['comp_content']},
            ]
            with ui.card().style('width:100%'):
                with ui.column().style("width:100%;flex-direction:column;align-self:flex-start;height:100%"):
                    table=ui.table(columns=columns, rows=rows, row_key='name').style('width:100%').style('font-size: 1.0rem;')
                    table.add_slot('body-cell-inf', '''
                    <q-td key="row_5" :props="props">
                        <q-badge :color="props.value == '需要回访' ? 'red' : (props.value == '不需要回访' ? 'green' : 'transparent')" style="font-size: 0.9rem; color: black;">
                            {{ props.value }}
                        </q-badge>
                    </q-td>''')
                    with ui.row():
                        if self.res['data'][0]["complaintmedia_set"]:
                            ui.label('附件图片：').style('font-size:1.4rem;height:30px;')
                            ui.button("点击查看",on_click=lambda:preview(self.res['data'][0]["complaintmedia_set"])).style('width:100px;')
                        if self.res['data'][0]["complainthandlemedia_set"]:
                            ui.label('回访图片：').style('font-size:1.4rem;height:30px;')
                            ui.button("点击查看",on_click=lambda:preview2(self.res['data'][0]["complainthandlemedia_set"])).style('width:100px;')
                    ui.table(columns=columns,rows=row2,row_key='name').style('width:100%').style('font-size: 1.0rem;')
                    # def handle_upload(e:events.UploadEventArguments):
                    #     file = e.content.read()
                    #     extension_name = e.name
                    #     #print(e.name)
                    #     res = upload_pic(compPicupload()+str(self.id)+'/',file,extension_name=extension_name)
                    #     if res.get('code') == 200:
                    #         ui.notify(res.get('message'),type='info',position='top')
                    #     else:
                    #         ui.notify(res.get('message'),type='warning',position='top')
                    # ui.upload(label='上传图片',multiple=True,max_file_size=1024 * 1024 * 5,on_rejected=lambda :ui.notify('上传失败'),on_upload=handle_upload,auto_upload=True).props('accept=.png,.jpg,.jpeg')
                    x=ui.input("回访总结（可选）").style('margin-top:10px;').style('width:100%')
                    ui.button('提交',on_click=lambda: __handle_reply(self.id,x.value)).style('margin-top:10px;')

def complaint_num_treat_ui(id):
    ComplaintPage(id).show_layout()