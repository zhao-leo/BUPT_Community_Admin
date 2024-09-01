# A python admin based on NiceGUI

这是与一个django后端匹配的内容管理后台，主要负责处理反馈事项，与前端微信小程序共同构成一个整体。

webAPI中定义了所有的接口函数

文件树如下：

```
COMMUNITYADMIN\SRC
│  API.py
│  main.py
│
├─icon
│      favicon.ico
│
└─source
    │  community.py
    │  login.py
    │  pim.py
    │
    ├─complaint
    │      complaint_template.py
    │      complaint_treat.py
    │      complaint_treated_template.py
    │      complaint_untreated.py
    │
    ├─layout
    │      footer.py
    │      head.py
    │      page_layout.py
    │      sidebar.py
    │
    ├─suggestion
    │      suggestion_template.py
    │      suggestion_treat.py
    │      suggestion_treated_template.py
    │      suggestion_untreated.py
    │
    └─webAPI
            community.py
            complaint.py
            excel.py
            login.py
            pim.py
            request.py
            suggestion.py
```

其中main.py是主程序入口，API.py包含所有接口

Recommend:
```python
# style debug tools
from niceguiToolkit.layout import inject_layout_tool
inject_layout_tool()
```
