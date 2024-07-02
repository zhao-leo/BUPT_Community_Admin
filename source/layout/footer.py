# -*- coding: utf-8 -*-
from nicegui import ui

def footer():
    with ui.row().classes('w-full items-center').style("width:100%"):
        ui.link('社区反馈管理系统','https://help.aliyun.com/zh/icp-filing/support/website-to-add-the-record-number-faq').style('font-size:1rem').classes('text-center w-full')
