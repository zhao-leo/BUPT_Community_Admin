# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.pim import Frequency
from API import frequency

def footer():
    with ui.footer(bordered=True).style('height: 50px;').style('background-color: white;'):
        with ui.row().classes('w-full justify-center items-center'):
            ui.link('京ICP-000000000000000', 'https://help.aliyun.com/zh/icp-filing/support/website-to-add-the-record-number-faq').style('font-size:1rem; margin-right: 2rem; font-color: black;')
            ui.label('用户访问量：{}'.format(Frequency(frequency()).get('data'))).style('font-size:1rem; color: black;')
