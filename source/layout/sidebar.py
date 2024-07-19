# -*- coding: utf-8 -*-
from nicegui import ui

def sidebar():
    with ui.left_drawer(bordered=True,fixed=False).props('width=170 bordered'):
        with ui.column().style("height:100%;width:auto;font-size:1.0rem"):
            ui.item('欢迎',on_click=lambda: ui.navigate.to('/home'))

            with ui.expansion('社区建议'):
                ui.item('待处理', on_click=lambda: ui.navigate.to('/suggestion/untreated'))
                ui.item('待回访', on_click=lambda: ui.notify('/suggestion/treated'))
            
            with ui.expansion('社区诉求'):
                ui.item('待处理', on_click=lambda: ui.navigate.to('/complaint/untreated'))
                ui.item('待回访', on_click=lambda: ui.notify('/complaint/treated'))
            
            ui.item('限行',on_click=lambda: ui.navigate.to('/carlimit'))

            ui.item('社区管理',on_click=lambda: ui.navigate.to('/community'))