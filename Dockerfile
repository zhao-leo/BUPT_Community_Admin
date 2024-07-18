FROM docker.anyhub.us.kg/library/python:3.11-slim

ENV BASE_URL=http://10.21.235.116:8000

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY . /app

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone

RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt

EXPOSE 8080:9000

CMD ["python3", "main.py"]