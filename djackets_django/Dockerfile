FROM python:3
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code
RUN python setup.py
EXPOSE 8000
#COPY ./docker-entrypoint.sh /docker-entrypoint.sh
#RUN chmod +x /docker-entrypoint.sh
#ENTRYPOINT ["/docker-entrypoint.sh"]