FROM python:3.9-alpine

COPY . /app
WORKDIR /app

RUN pip install -U setuptools pip
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["sh", "/app/entrypoint.sh"]