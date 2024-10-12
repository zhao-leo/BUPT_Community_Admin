'''
Author: zhao-leo 18055219130@163.com
Date: 2024-10-12 17:44:01
LastEditTime: 2024-10-12 18:06:44
'''
# -*- coding: utf-8 -*-
from nicegui import ui
from source.login import login_ui
from source.pim import pim_ui
from API import BASE_URL,Icon
from hashlib import md5

from source.suggestion.suggestion_untreated import suggestion_ui
from source.suggestion.suggestion_template import suggestion_num_ui
from source.suggestion.suggestion_treat import suggestion_treat_ui
from source.suggestion.suggestion_treated_template import suggestion_num_treat_ui
from source.suggestion.suggestion_finished import suggestion_finished_ui
from source.suggestion.suggestion_finished_template import suggestion_num_finished_ui

from source.complaint.complaint_untreated import complaint_ui
from source.complaint.complaint_template import complaint_num_ui
from source.complaint.complaint_treat import complaint_treat_ui
from source.complaint.complaint_treated_template import complaint_num_treat_ui
from source.complaint.complaint_finished import complaint_finished_ui
from source.complaint.complaint_finished_template import complaint_num_finished_ui

from source.community import community_ui

import random

string = random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 15)
string = md5(''.join(string).encode()).hexdigest()

print(BASE_URL)
@ui.page('/')
def index():
    login_ui()

@ui.page('/home')
def index():
    pim_ui()

@ui.page('/suggestion')
def index():
    ui.navigate.to('/suggestion/untreated')

@ui.page('/suggestion/untreated')
def index():
    suggestion_ui()

@ui.page('/suggestion/untreated/{id}')
def index(id: int):
    suggestion_num_ui(id)

@ui.page('/suggestion/treated')
def index():
    suggestion_treat_ui()

@ui.page('/suggestion/treated/{id}')
def index(id: int):
    suggestion_num_treat_ui(id)

@ui.page('/complaint')
def index():
    ui.navigate.to('/complaint/untreated')

@ui.page('/complaint/untreated')
def index():
    complaint_ui()

@ui.page('/complaint/treated')
def index():
    complaint_treat_ui()

@ui.page('/complaint/untreated/{id}')
def index(id: int):
    complaint_num_ui(id)

@ui.page('/complaint/treated/{id}')
def index(id: int):
    complaint_num_treat_ui(id)

@ui.page('/complaint/finished')
def index():
    complaint_finished_ui()

@ui.page('/complaint/finished/{id}')
def index(id: int):
    complaint_num_finished_ui(id)

@ui.page('/suggestion/finished')
def index():
    suggestion_finished_ui()

@ui.page('/suggestion/finished/{id}')
def index(id: int):
    suggestion_num_finished_ui(id)

@ui.page('/community')
def index():
    community_ui()

ui.run(port=9000,language='zh-CN',show_welcome_message=False,storage_secret=string,favicon=Icon(),title="您访问了一个不存在的页面")