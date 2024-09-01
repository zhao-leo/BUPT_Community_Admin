# -*- coding: utf-8 -*-
from .request import GetExcel

# 获取excel文件
def get_excel(url,start_time,finish_time):
    data = {
        'start_time': start_time,
        'finish_time': finish_time
    }
    return GetExcel(url, data)
