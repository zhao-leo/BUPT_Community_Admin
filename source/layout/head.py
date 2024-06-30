from nicegui import ui
from source.webAPI.login import logout

def log_out():
    logout()
    ui.navigate.to('/')

def header():
    with ui.row().classes('w-full items-center').style("width:100%"):
        ui.label('社区反馈管理系统').classes('mr-auto')
        with ui.button(icon='menu'):
            with ui.menu():
                ui.menu_item('登出', on_click=log_out)
    