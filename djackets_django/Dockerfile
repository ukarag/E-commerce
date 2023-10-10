# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./djackets_django/requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./djackets_django/manage.py /code/ 
COPY ./djackets_django /code/