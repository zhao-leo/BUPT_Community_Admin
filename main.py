from nicegui import app,ui
from source.login import loginui
from source.pim import pimui
from source.suggestion.suggestion_untreated import suggestionui
from source.suggestion.suggestion_template import suggestion_num
from source.complaint.complaint_untreated import complaintui
from source.complaint.complaint_template import complaint_num
from source.limit import limitui

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
    ui.navigate.to('/home')
ui.run(port=5000)