# A python admin Based NiceGUI

这是与一个django后端匹配的内容管理后台，主要负责处理反馈事项，与前端微信小程序共同构成一个整体。

webAPI中定义了所有的接口函数

文件树如下：

```
COMMUNITY-ADMIN
│  .gitignore
│  API.py
│  main.py
│  readme.md
│  style.debug
│  tree.txt
└─source
    │  community.py
    │  limit.py
    │  login.py
    │  pim.py
    │  
    ├─complaint
    │     complaint_template.py
    │     complaint_untreated.py
    │       
    ├─layout
    │      head.py
    │      sidebar.py
    │      
    ├─suggestion
    │      suggestion_template.py
    │      suggestion_untreated.py
    │      
    └─webAPI
            community.py
            complaint.py
            limit.py
            login.py
            pim.py
            suggestion.py
```

其中main.py是主程序入口，API.py包含所有接口，webAPI文件夹包含获取数据和存储数据两部分，没有启用Cookies，关闭即登出

source中其他的文件都是页面文件，在main.py文件中注册