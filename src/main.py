# -*- coding: utf-8 -*-
from nicegui import ui
from source.login import login_ui
from source.pim import pim_ui
from API import BASE_URL

from source.suggestion.suggestion_untreated import suggestion_ui
from source.suggestion.suggestion_template import suggestion_num_ui
from source.suggestion.suggestion_treat import suggestion_treat_ui
from source.suggestion.suggestion_treated_template import suggestion_num_treat_ui

from source.complaint.complaint_untreated import complaint_ui
from source.complaint.complaint_template import complaint_num_ui
from source.complaint.complaint_treat import complaint_treat_ui
from source.complaint.complaint_treated_template import complaint_num_treat_ui

from source.community import community_ui

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

@ui.page('/community')
def index():
    community_ui()

ui.run(port=9000,language='zh-CN',show_welcome_message=False,storage_secret='e48d1469c529a31f67b8293e82cb604929759dab9cb8f83199b23bff89f739d1',favicon=r'src\icon\favicon.ico')