FROM python:3.6-alpine

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install -r test-requirements.txt

