FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /fampay

WORKDIR /fampay

ADD . /fampay/

RUN pip install -r requirements.txt
