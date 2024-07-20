# -*- coding: utf-8 -*-
from nicegui import ui,app
from source.login import login_ui
from source.pim import pim_ui

from source.suggestion.suggestion_untreated import suggestion_ui
from source.suggestion.suggestion_template import suggestion_num_ui

from source.complaint.complaint_untreated import complaint_ui
from source.complaint.complaint_template import complaint_num_ui
from source.community import community_ui

TOKEN = ""
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

@ui.page('/complaint')
def index():
    ui.navigate.to('/complaint/untreated')

@ui.page('/complaint/untreated')
def index():
    complaint_ui()

@ui.page('/complaint/untreated/{id}')
def index(id: int):
    complaint_num_ui(id)

@ui.page('/community')
def index():
    community_ui()

@ui.page('/{other}')
def index(other: str):
    ui.navigate.to('/')
ui.run(host='0.0.0.0',port=2156,language='zh-CN',storage_secret='your_complex_secret_here')
# app.native.window_args['resizable'] = True
# app.native.start_args['debug'] = False
# app.native.settings['ALLOW_DOWNLOADS'] = True

# ui.run(native=True, window_size=(800, 600), fullscreen=False,storage_secret='your_complex_secret_here')