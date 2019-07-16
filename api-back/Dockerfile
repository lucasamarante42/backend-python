FROM python:3.6-jessie

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN apt-get update && \ 
    apt-get install -y libssl-dev mysql-client libmysqld-dev libffi-dev fontconfig xfonts-75dpi \
    xfonts-base libpng12-0 nano vim telnet libxrender1 libfontconfig1 libx11-dev libjpeg62 libxtst6
RUN pip install -r requirements.txt
RUN wget "https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.jessie_amd64.deb" && \
	dpkg -i wkhtmltox_0.12.5-1.jessie_amd64.deb && \
	apt-get -f install

ADD . /code/

EXPOSE 8000

CMD gunicorn --workers 4 --access-logfile=- --bind 0.0.0.0:8000 sysestoque.wsgi