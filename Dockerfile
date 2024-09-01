FROM python:3.11-slim

ENV BASE_URL=http://49.232.6.217:8001

ENV ICP_URL=https://help.aliyun.com/zh/icp-filing/support/website-to-add-the-record-number-faq

ENV ICP_CODE=000000000000000

ENV PYTHONDONTWRITEBYTECODE=1

COPY . /app/

WORKDIR /app

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone

RUN pip install --no-cache-dir -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 9000

CMD ["python3", "main.py"]
