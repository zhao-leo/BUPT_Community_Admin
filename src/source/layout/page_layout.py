from source.layout.head import header
from source.layout.footer import footer
from source.layout.sidebar import sidebar
from nicegui import ui,app
from source.webAPI.pim import get_pim
from API import pimapi

class PageLayout():
    def __init__(self, title: str):
        self.title = title
        self.__token = app.storage.user.get('TOKEN') # 获取token
        # 如果没有token，则跳转到登录页面
        if not self.__token:
            ui.notify('请先登录', type='error',position='top',close_button='确定')
            ui.navigate.to('/')
        # 如果有token，验证token有效期，则获取管理员信息
        else:
            data=get_pim(pimapi()) # 获取管理员信息
            if data['code'] == 200: # 如果返回的code为200,表示获取成功,写入缓存
                app.storage.user['NAME'] = data['data']['manager_name']
                app.storage.user['ACCOUNT'] = data['data']['manager_account']
                app.storage.user['PHONE'] = data['data']['manager_tele']
                app.storage.user['ID'] = data['data']['id']
                if data['data']['id'] <= 3:
                    app.storage.user['ROLE'] = '超级管理员'
                else:
                    app.storage.user['ROLE'] = '管理员'
            else: # 否则提示错误信息，并跳转到登录页面
                ui.notify('获取管理员信息失败', type='error',position='top',close_button='确定')
                ui.navigate.to('/')
    
    def content(self): # 内容区域
        #ui.label('Write your CONTENT here')
        pass
    
    def show_layout(self):
            ui.page_title(self.title.format(app.storage.user.get('NAME'))) # 页面标题
            header() # 头部
            sidebar() # 侧边栏
            self.content() # 内容区域
            footer() # 底部

