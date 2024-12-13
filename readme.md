# A python admin based on NiceGUI

这是与一个django后端匹配的内容管理后台，主要负责处理反馈事项，与前端微信小程序共同构成一个整体。
包括`Dashbroad`,`complaint`,`suggestion`界面和一个导出历史数据的按钮。

在[WebAPI](https://github.com/zhao-leo/communityAdmin/tree/main/src/source/webAPI)中定义了所有的接口函数，在[API.py](https://github.com/zhao-leo/communityAdmin/blob/main/src/API.py)中定义了所有API路径。

本项目仅在python3.12下测试！
推荐使用poetry作为包管理工具，但是也提供`requirements.txt`作为备选项。

其中main.py是主程序入口，直接运行main.py即可

本项目同时提供docker镜像:
```
docker pull registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:latest
```
docker 中需要的环境变量 
```
BASE_URL = "https://api.example.com
ICP_URL = 京ICP备-XXXXXXXX号
```
同时，内部网页服务的端口号是9000，记得根据需要自行映射

PS：
修改404界面需要对NiceGUI包进行修改！
```
~/.venv/Lib/site-packages/nicegui/error.py
```

build.bat
```bat
docker build -t registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:$version -f Dockerfile src/
docker tag registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:$version registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:latest
docker login --username=aliyun4438435934 registry.cn-hangzhou.aliyuncs.com

docker push registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:$version
docker push registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:latest
```