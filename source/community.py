from nicegui import ui,events
from source.webAPI.community import get_hotline,update_hotline,add_hotline,remove_hotline,\
get_warmtext,update_warmtext,get_picture,upload_pic,delete_pic
from source.webAPI.pim import getInf
from API import hotline,hotlinedetail,warmnotice,picture,picDetail

from source.layout.sidebar import sidebar
from source.layout.head import header


# from niceguiToolkit.layout import inject_layout_tool
# inject_layout_tool()

def hotlineUpdate(url,id,name,phone):
    with ui.dialog() as dialog1,ui.card():
        ui.label('修改热线').style('font-size:1.5rem')
        names=ui.input('联系人')
        teles=ui.input('联系电话')
        names.value=name
        teles.value=phone
        def update():
            if update_hotline(url,id,names.value,teles.value):
                ui.notify(message='修改成功')
                ui.navigate.to('/community')
            else:
                ui.notify(message='修改失败')
        with ui.row():
          ui.button('确定').on_click(lambda:update())
          ui.button('取消').on_click(lambda:dialog1.close())
    dialog1.open()

def RemoveHotline(url,id):
    with ui.dialog() as dialog2,ui.card():
        ui.label('是否删除该热线').style('font-size:1.2rem')
        def remove():
            if remove_hotline(url,id):
                ui.notify(message='删除成功')
                ui.navigate.to('/community')
            else:
                ui.notify(message='删除失败')
        with ui.row().style('width:100%').classes('justify-content: center'):
          ui.button('确定',color='red').on_click(lambda:remove())
          ui.button('取消').on_click(lambda:dialog2.close())
    dialog2.open()

def Add_hotline(url):
    with ui.dialog() as dialog3,ui.card():
        ui.label('添加热线').style('font-size:1.5rem')
        names=ui.input('联系人')
        teles=ui.input('联系电话',validation={'请输入正确的手机号码':lambda value: len(value) == 11 and value.isdigit()})
        def upload():
            if add_hotline(url,names.value,teles.value):
                ui.notify(message='修改成功')
                ui.navigate.to('/community')
            else:
                ui.notify(message='修改失败')
        with ui.row():
          ui.button('确定').on_click(lambda:upload())
          ui.button('取消').on_click(lambda:dialog3.close())
    dialog3.open()

def warmText(url,text):
    res=update_warmtext(url,text)
    with ui.dialog() as dialog4,ui.card():
        ui.label(res).style('font-size:1.5rem')
        with ui.row():
          ui.button('确定').on_click(lambda:dialog4.close())
    dialog4.open()

def handle_upload(e: events.UploadEventArguments):
    fileb64=e.content.read()
    res=upload_pic(picture(),fileb64)
    if res['code']==200:
        ui.notify(message='上传成功')
        ui.timer(1.0,ui.navigate.to('/community'))
    else:
        ui.notify(message='上传失败')

def del_pic(id):
    res=delete_pic(picDetail(),id)
    if res['code']==200:
        ui.notify('删除成功')
        ui.navigate.to('/community')
    else:
        ui.notify('删除失败')
    

def communityui():
    ui.page_title('社区管理-{}'.format(getInf()['NAME']))
    hotlineInf=get_hotline(hotline())
    if hotlineInf["code"]==200:
        with ui.column().style("font-size:1.5rem;width:100%;height:auto"):
            header()
            with ui.row().style("width:100%;height:100%"):
                sidebar()
                with ui.column().style("flex:1"):
                    with ui.card().style("flex:1").style('width:100%'):
                        ui.label('温馨提示').style('font-size:1.5rem')
                        warntext=ui.textarea('社区热线管理，可添加、修改、删除社区热线').style('width:100%;height:100%;font-size:1.2rem')
                        warntext.value=get_warmtext(warmnotice())
                        ui.button('修改',on_click=lambda:warmText(warmnotice(),warntext.value))
                    with ui.card().style("flex:1;width:100%"):
                        with ui.row():
                            ui.label('热线管理').style('font-size:1.5rem')
                            ui.button('添加',on_click=lambda:Add_hotline(hotline()))
                        with ui.row().style("width:100%;height:auto"):
                            ui.label('联系人').style('width:32%;font-size:1.2rem')
                            ui.label('联系电话').style('width:37%;font-size:1.2rem')
                            ui.label('操作').style('width:24%;font-size:1.2rem')
                        for i in hotlineInf["data"]:
                            with ui.row().style("width:100%;height:auto"):
                                with ui.column().style("width:100%;height:auto"):
                                    with ui.row().style("width:100%;height:auto"):
                                        ui.label(i["hotline_who"]).style('width:32%')
                                        ui.label(i["hotline_tele"]).style('width:37%')
                                        ui.button("修改").on_click(lambda i=i:hotlineUpdate(hotlinedetail(),i["id"],i["hotline_who"],i["hotline_tele"])).style('width:12%')
                                        ui.button("删除",color='red').on_click(lambda i=i:RemoveHotline(hotlinedetail(),i["id"])).style('width:12%')
                    with ui.card().style("flex:1").style('width:100%'):
                        ui.label('轮播图').style('font-size:1.5rem')
                        ui.upload(label='上传轮播图',max_files=1,max_file_size=1024 * 1024 * 5,on_rejected=lambda :ui.notify('上传失败'),on_upload=handle_upload,auto_upload=True).props('accept=.png,.jpg,.jpeg').classes('max-w-full').style('width:50%;height:auto;')
                        res = get_picture(picture())
                        with ui.carousel(animated=True, arrows=True, navigation=True).style('width: 100%;height:auto;'):
                            for i in res:
                                with ui.carousel_slide().classes('p-0'):
                                    ui.button(text='删除当前图片',color='red').on_click(lambda i=i:del_pic(i['id'])).style('justify-content:flex-end;')
                                    ui.image(i['cover_file'])
    else:
        ui.notify(message='获取数据失败')
        ui.navigate.to('/home')