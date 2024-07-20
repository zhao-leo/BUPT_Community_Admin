# -*- coding: utf-8 -*-
from nicegui import ui,events
from source.webAPI.community import get_hotline,update_hotline,add_hotline,remove_hotline,\
get_warmtext,update_warmtext,get_picture,upload_pic,delete_pic,upload_bkground
from API import hotline,hotlinedetail,warmnotice,picture,picDetail,background,BASE_URL

from source.layout.page_layout import PageLayout

class CommunityPage(PageLayout):
    def __init__(self):
        super().__init__("社区管理-{}")

    def content(self):
        with ui.column().style('width:100%'):
            @ui.refreshable
            def WarnUI():
                with ui.card().style('width:100%'):
                    ui.label('温馨提示').style('font-size:1.5rem')
                    warntext=ui.textarea('社区热线管理，可添加、修改、删除社区热线').style('width:100%;height:100%;font-size:1.2rem')
                    warntext.value=get_warmtext(warmnotice()).get('data').get('warn_text')
                    def update_warn(url,text):
                        res = update_warmtext(url,text)
                        if res.get('code') == 200:
                            ui.notify(res.get('message'),type='info',position='top')
                            WarnUI.refresh()
                    ui.button('修改',on_click=lambda:update_warn(warmnotice(),warntext.value))
            
            @ui.refreshable
            def hotlineUI():
                with ui.card().style('width:100%'):
                    with ui.row():
                    
                        def Add_hotline(url: str) -> None:
                            with ui.dialog() as dialog,ui.card().style('width:20%'):
                                ui.label('添加热线').style('font-size:1.2rem')
                                names=ui.input('联系人').style('width:100%')
                                teles=ui.input('联系电话',validation={'请输入正确的手机号码':lambda value: len(value) == 11 and value.isdigit()}).style('width:100%')
                                def upload():
                                    res=add_hotline(url,names.value,teles.value)
                                    if res.get('code') == 200:
                                        ui.notify(res.get('message'),type='info',position='top')
                                        dialog.close()
                                        return True
                                    else:
                                        ui.notify(res.get('message'),type='warning',position='top')
                                        return False
                                with ui.row():
                                    ui.button('添加').on_click(lambda: hotlineUI.refresh() if upload() else None)
                                    ui.button('取消').on_click(lambda:dialog.close())
                                dialog.open()
                        
                        def hotlineUpdate(url: str,id: int,name: str,phone: str) -> None:
                            with ui.dialog() as dialog,ui.card().style('width:20%'):
                                ui.label('修改热线').style('font-size:1.2rem')
                                names=ui.input('联系人').style('width:100%')
                                teles=ui.input('联系电话',validation={'请输入正确的手机号码':lambda value: len(value) == 11 and value.isdigit()}).style('width:100%')
                                names.value=name
                                teles.value=phone
                                def update():
                                    res=update_hotline(url,id,names.value,teles.value)
                                    if res.get('code') == 200:
                                        ui.notify(res.get('message'),type='info',position='top')
                                        dialog.close()
                                        return True
                                    else:
                                        ui.notify(res.get('message'),type='warning',position='top')
                                        return False
                                with ui.row():
                                    ui.button('确定').on_click(lambda: hotlineUI.refresh() if update() else None)
                                    ui.button('取消').on_click(lambda:dialog.close())
                                dialog.open()
                        
                        def RemoveHotline(url: str,id: int) -> None:
                            with ui.dialog() as dialog,ui.card():
                                ui.label('是否删除该热线').style('font-size:1.2rem')
                                def remove():
                                    res=remove_hotline(url,id)
                                    if res.get('code') == 200:
                                        ui.notify(res.get('message'),type='info',position='top')
                                        dialog.close()
                                        return True
                                    else:
                                        ui.notify(res.get('message'),type='warning',position='top')
                                        return False
                                with ui.row().style('width:100%').classes('justify-content: center'):
                                    ui.button('确定',color='red').on_click(lambda: hotlineUI.refresh() if remove() else None)
                                    ui.button('取消').on_click(lambda:dialog.close())
                                dialog.open()

                        ui.label('热线管理').style('font-size:1.5rem')
                        ui.button('添加',on_click=lambda:Add_hotline(hotline()))
                    with ui.row().style('width:100%;height:auto'):
                        ui.label('联系人').style('width:32%;font-size:1.2rem')
                        ui.label('联系电话').style('width:37%;font-size:1.2rem')
                        ui.label('操作').style('width:24%;font-size:1.2rem')
                    hotlineInf = get_hotline(hotline()).get('data')
                    if hotlineInf!=None:
                        for i in hotlineInf:
                            with ui.row().style('width:100%;height:auto'):
                                with ui.column().style('width:100%;height:auto'):
                                    with ui.row().style('width:100%;height:auto'):
                                        ui.label(i.get('hotline_who')).style('width:32%')
                                        ui.label(i.get('hotline_tele')).style('width:37%')
                                        ui.button('修改').on_click(lambda i=i:hotlineUpdate(hotlinedetail(),i.get('id'),i.get('hotline_who'),i.get('hotline_tele')))
                                        ui.button('删除',color='red').on_click(lambda i=i:RemoveHotline(hotlinedetail(),i.get('id')))
            @ui.refreshable
            def coverUI():
                
                def handle_upload(e:events.UploadEventArguments):
                    file = e.content.read()
                    res = upload_pic(picture(),file)
                    if res.get('code') == 200:
                        ui.notify(res.get('message'),type='info',position='top')
                        coverUI.refresh()
                    else:
                        ui.notify(res.get('message'),type='warning',position='top')
                
                def del_cover(id):
                    res = delete_pic(picDetail(),id)
                    if res.get('code') == 200:
                        ui.notify(res.get('message'),type='info',position='top')
                        coverUI.refresh()
                    else:
                        ui.notify(res.get('message'),type='warning',position='top')

                with ui.card().style('width:100%'):
                    ui.label('轮播图').style('font-size:1.5rem')
                    ui.upload(label='上传轮播图',max_files=1,max_file_size=1024 * 1024 * 5,on_rejected=lambda :ui.notify('上传失败'),on_upload=handle_upload,auto_upload=True).props('accept=.png,.jpg,.jpeg').classes('max-w-full').style('width:50%;height:auto;')

                    res = get_picture(picture())
                    if res.get('data')!=None:
                        with ui.carousel(animated=True, arrows=True, navigation=True).style('width: 60%;height:auto;align-self:center'):
                            for i in res.get('data'):
                                with ui.carousel_slide().classes('p-0'):
                                    ui.button(text='删除当前图片',color='red').on_click(lambda i=i:del_cover(i['id'])).style('justify-content:flex-end;')
                                    ui.image(BASE_URL[:-1]+i['cover_file'])

            @ui.refreshable
            def backgroundUI():
                def handle_upload(e:events.UploadEventArguments):
                    file = e.content.read()
                    res = upload_bkground(background(),file)
                    if res.get('code') == 200:
                        ui.notify(res.get('message'),type='info',position='top')
                        backgroundUI.refresh()
                    else:
                        ui.notify(res.get('message'),type='warning',position='top')

                with ui.card().style('width:100%'):
                    ui.label('背景图').style('font-size:1.5rem')
                    r = get_picture(background()).get('data')
                    ui.upload(label='上传背景图',max_files=1,max_file_size=1024 * 1024 * 5,on_rejected=lambda :ui.notify('上传失败'),on_upload=handle_upload,auto_upload=True).props('accept=.png,.jpg,.jpeg,.ico').classes('max-w-full').style('width:50%;height:auto;')
                    if r!=None:
                        ui.image(BASE_URL[:-1]+r[0].get('back_file')).style('width:100%;height:auto;')
            WarnUI()
            hotlineUI()
            coverUI()
            backgroundUI()

def community_ui():
    CommunityPage().show_layout()