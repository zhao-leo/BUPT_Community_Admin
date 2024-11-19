from source.layout.head import header
from source.layout.footer import footer
from source.layout.sidebar import sidebar
from source.webAPI.pim import update_pim
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
                app.storage.user['role'] = data['data']['role']
                app.storage.user['ID'] = data['data']['id']
                #print(app.storage.user['ID'])
                if data['data']['manager_name']==None:
                    ui.notify('请先完善个人信息', type='warning')
                    # --------------------------------- dialog for update personal information --------------------------------- #
                    with ui.dialog() as dialog1,ui.card(): # 修改个人信息

                        def handlepim(url,account,name,phone):
                            res=update_pim(url,account,name,phone)
                            if res['code']==200: # 如果返回的code为200,表示修改成功,关闭弹窗并跳转到首页
                                ui.notify(res["message"],position='top',type='info')
                                dialog1.close()
                                ui.navigate.to('/home')
                            else: # 否则提示错误信息
                                ui.notify(res["message"],position='top',type='warning',close_button='确定')

                        with ui.row():
                            NAME=data['data']['manager_name']
                            ACCOUNT=data['data']['manager_account']
                            PHONE=data['data']['manager_tele']
                            account1 = ui.input(label='账号')
                            account1.value=ACCOUNT
                            name = ui.input(label='姓名')
                            name.value=NAME
                        phone = ui.input(label='电话',validation={'请正确填写电话号码': lambda value: value is not None and len(value) == 11 and value.isdigit()})
                        phone.value=PHONE

                        with ui.row():
                            ui.button('提交', on_click=lambda:handlepim(pimapi(),account1.value,name.value,phone.value))
                    dialog1.open()
                if data['data']['role'] ==  True:
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

