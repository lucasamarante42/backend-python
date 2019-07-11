FROM python:3.6-jessie

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN apt-get update && \ 
    apt-get install -y libssl-dev mysql-client libmysqld-dev libffi-dev
RUN pip install -r requirements.txt
ADD . /code/

EXPOSE 8000

CMD gunicorn --workers 4 --access-logfile=- --bind 0.0.0.0:8000 sysestoque.wsgi