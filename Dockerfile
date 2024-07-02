FROM docker.anyhub.us.kg/library/python:3.11

ENV BASE_URL=http://10.21.235.116:8000

WORKDIR /app

COPY . /app

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone

RUN pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt

EXPOSE 8080:9000

CMD ["python3", "main.py"]