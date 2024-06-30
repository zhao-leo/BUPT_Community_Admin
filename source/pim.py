from nicegui import ui
from source.webAPI.pim import get_pim,getInf
from API import pimapi

from source.layout.sidebar import sidebar
from source.layout.head import header

# from niceguiToolkit.layout import inject_layout_tool
# inject_layout_tool()


def __get__pim():
    url = pimapi()
    return get_pim(url)

def __identify_id(id):
    if id<=3:
        return '超级管理员'
    else:
        return '普通管理员'

def pimui():
    res=__get__pim()
    if res["code"]==149 or res["code"]==0:
        ui.notify(res["msg"],position='top',type='warning')
        ui.timer(1, lambda: ui.navigate.to('/'))
    elif res["code"]==200:
        person=getInf()
        with ui.column().style("font-size:1.5rem;width:100%;height:auto"):
            header()
            with ui.row().style("width:100%;height:100%"):
                sidebar()
                with ui.column().style("width:auto;flex-direction:column;align-self:flex-start;height:auto"):
                    ui.label('欢迎您: {}'.format(person['NAME']))
                    with ui.card().style("width:auto;font-size:1.0rem;align-self:flex-start;height:auto"):
                        ui.label('以下是您的个人信息:')
                        ui.label('身份: {}'.format(__identify_id(person['ID'])))
                        ui.label('电话: {}'.format(person['PHONE']))
                        ui.label('账号: {}'.format(person['ACCOUNT']))
                        with ui.row():
                            ui.button('修改个人信息')
                            ui.button('修改密码')