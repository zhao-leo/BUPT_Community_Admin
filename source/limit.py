# -*- coding: utf-8 -*-
from source.webAPI.limit import get_limit
from source.webAPI.pim import getInf
from nicegui import ui
from API import carlimit
from source.layout.head import header
from source.layout.sidebar import sidebar
from source.layout.footer import footer

def limitui():
    ui.page_title('车辆限行-{}'.format(getInf()['NAME']))
    res=get_limit(carlimit())
    if res['code']==200:
      with ui.column().style("font-size:1.5rem;width:100%;height:auto"):
          header()
          with ui.row().style("height:100%;width:100%"):
              sidebar()
              with ui.card().style("flex:1"):
                  with ui.column().style("width:100%;"):
                      ui.label('本周车辆限行信息').style('font-size:1.5rem')
                      columns = [
                          {'name':'week', 'label': '工作周', 'field':'week','align': 'left'},
                          {'name': 'mon', 'label': '星期一', 'field': 'mon','align': 'left'},
                          {'name': 'tue', 'label': '星期二', 'field': 'tue','align': 'left'},
                          {'name': 'wed', 'label': '星期三', 'field': 'wed','align': 'left'},
                          {'name': 'thu', 'label': '星期四', 'field': 'thu','align': 'left'},
                          {'name': 'fri', 'label': '星期五', 'field': 'fri','align': 'left'},
                      ]
                      rows = [
                          {'week':'车牌尾号','mon': res['data']['limit_mon'],'tue': res['data']['limit_tue'],'wed':res['data']['limit_wed'],'thu': res['data']['limit_thu'],'fri': res['data']['limit_fri']}
                      ]
                      ui.table(columns=columns, rows=rows, row_key='week').style('width:100%')

                  with ui.column().style("width:100%;"):
                      ui.label('更新车辆限行信息').style('font-size:1.5rem')
                      with ui.row():
                          with ui.input('开始日期') as date1:
                              with ui.menu() as menu:
                                  with ui.date().bind_value(date1) as startdate:
                                      with ui.row().classes('justify-end'):
                                          ui.button('关闭', on_click=menu.close).props('flat')
                              with date1.add_slot('append'):
                                  ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

                          with ui.input('结束日期') as date2:
                              with ui.menu() as menu:
                                  with ui.date().bind_value(date2) as enddate:
                                      with ui.row().classes('justify-end'):
                                          ui.button('关闭', on_click=menu.close).props('flat')
                              with date2.add_slot('append'):
                                  ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
                      with ui.card():
                          ui.label("请直接输入限行尾号")
                          with ui.row():
                              mon=ui.input('星期一')
                              tue=ui.input('星期二')
                              wed=ui.input('星期三')
                              thu=ui.input('星期四')
                              fri=ui.input('星期五')
                      ui.button('提交更改')
              footer()

    else:
        ui.notify(res['message'],position='top',type='warning')
        ui.navigate.to('/home')