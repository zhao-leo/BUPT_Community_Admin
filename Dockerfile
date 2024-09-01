FROM python:3.11-slim

ENV BASE_URL=http://49.232.6.217:8001

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY /src /app

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9000

CMD ["python3", "main.py"]
