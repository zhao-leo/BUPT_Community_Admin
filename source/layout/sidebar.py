from nicegui import ui
# from niceguiToolkit.layout import inject_layout_tool
# inject_layout_tool()
def sidebar():
    with ui.column().style("height:100vh;width:auto;font-size:1.0rem"):
        ui.item('欢迎',on_click=lambda: ui.navigate.to('/home'))

        with ui.expansion('社区建议'):
            ui.item('待处理', on_click=lambda: ui.navigate.to('/suggestion/untreated'))
            ui.item('待回访', on_click=lambda: ui.notify('/suggestion/treated'))