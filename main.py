# -*- coding: utf-8 -*-
from nicegui import ui
from source.login import loginui
from source.pim import pimui
from source.suggestion.suggestion_untreated import suggestionui
from source.suggestion.suggestion_template import suggestion_num
from source.complaint.complaint_untreated import complaintui
from source.complaint.complaint_template import complaint_num
from source.limit import limitui
from source.community import communityui

TOKEN = ""
@ui.page('/')
def index():
    loginui()

@ui.page('/home')
def index():
    pimui()

@ui.page('/suggestion')
def index():
    ui.navigate.to('/suggestion/untreated')

@ui.page('/suggestion/untreated')
def index():
    suggestionui()

@ui.page('/suggestion/untreated/{id}')
def index(id: int):
    suggestion_num(id)

@ui.page('/complaint')
def index():
    ui.navigate.to('/complaint/untreated')

@ui.page('/complaint/untreated')
def index():
    complaintui()

@ui.page('/complaint/untreated/{id}')
def index(id: int):
    complaint_num(id)

@ui.page('/carlimit')
def index():
    limitui()

@ui.page('/community')
def index():
    communityui()

@ui.page('/{other}')
def index(other: str):
    ui.navigate.to('/')
ui.run(host='0.0.0.0',port=2156,language='zh-CN',storage_secret='your_complex_secret_here')