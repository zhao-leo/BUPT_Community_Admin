'''
Author: zhao-leo 18055219130@163.com
Date: 2024-10-12 17:44:01
LastEditTime: 2024-10-12 17:47:59
'''
# -*- coding: utf-8 -*-
from nicegui import ui
from source.webAPI.pim import Frequency
from API import frequency
from os import getenv

def footer():
    with ui.footer(bordered=True).style('height: 50px;').style('background-color: white;'):
        with ui.row().classes('w-full justify-center items-center'):
            ui.link(getenv('ICP_CODE'), "https://beian.miit.gov.cn/").style('font-size:1rem; margin-right: 2rem; font-color: black;')
            ui.label('用户访问量：{}'.format(Frequency(frequency()).get('data'))).style('font-size:1rem; color: black;')
