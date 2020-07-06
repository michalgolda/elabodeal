FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/bin/app/

WORKDIR /usr/bin/app/

COPY requirements.txt /usr/bin/app/

RUN pip install -r requirements.txt

COPY . /usr/bin/app/

