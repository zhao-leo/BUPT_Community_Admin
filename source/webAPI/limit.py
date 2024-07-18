# -*- coding: utf-8 -*-
from source.webAPI.request import Request

# 获取车辆限行信息
def get_limit(url):
    return Request('GET',url)

# 更新车辆限行信息
def update_limit(url,start,end,mon='未填写',tue='未填写',wed='未填写',thr='未填写',fri='未填写'):
    data={
        "start_time":start,
        "finish_time":end,
        "mon":mon,
        "tue":tue,
        "wed":wed,
        "thu":thr,
        "fri":fri
    }
    return Request('POST',url,data)
