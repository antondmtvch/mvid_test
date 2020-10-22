FROM tiangolo/uwsgi-nginx-flask

RUN apk --update add bash nano

WORKDIR /var/www/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt