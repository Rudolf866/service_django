FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/service_django

COPY requirements.txt ./

RUN pip install -r requirements.txt