FROM docker.anyhub.us.kg/library/python:3.11

ENV BASE_URL=172.22.0.2:8000

WORKDIR /app

COPY . /app

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 8080

CMD ["python3", "main.py"]