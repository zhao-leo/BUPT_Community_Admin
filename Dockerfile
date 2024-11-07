FROM python:3.11-slim

ENV BASE_URL=http://api.example.com

ENV ICP_CODE=京ICP备XXXXXXXX号

ENV PYTHONDONTWRITEBYTECODE=1

COPY . /app/

WORKDIR /app

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone

RUN pip install --no-cache-dir -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 9000

CMD ["python3", "main.py"]
