# -*- coding: utf-8 -*-
from nicegui import ui,app
from fastapi import Response
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

@app.get("/favicon.ico")
async def get_image():
    with open("icon/favicon.ico", "rb") as image_file:
        image_data = image_file.read()
    return Response(content=image_data, media_type="image/ico")

ui.run(port=9000,language='zh-CN',storage_secret='e48d1469c529a31f67b8293e82cb604929759dab9cb8f83199b23bff89f739d1',favicon='./icon/favicon.ico')