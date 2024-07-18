# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.pim import Frequency
from API import frequency

def footer():
    with ui.footer(elevated=True).style('height: 40px;').style('background-color: white;'):
        with ui.row().classes('w-full justify-center items-center'):
            ui.link('社区反馈管理系统', 'https://help.aliyun.com/zh/icp-filing/support/website-to-add-the-record-number-faq').style('font-size:1rem; margin-right: 2rem; font-color: black;')
            ui.label('用户访问量：{}'.format(Frequency(frequency()))).style('font-size:1rem; font-color: black;')
