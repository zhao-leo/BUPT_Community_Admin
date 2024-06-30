from nicegui import app,ui
from source.login import loginui
from source.pim import pimui
from source.suggestion.suggestion_untreated import suggestionui
# from niceguiToolkit.layout import inject_layout_tool
# inject_layout_tool()
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

@ui.page('/suggestion/treated')
def index():
    ui.notify('已处理建议',position='top',type='info')

ui.run()