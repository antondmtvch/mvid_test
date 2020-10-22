FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /var/www/mvid

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app app
COPY config.py config.py
COPY main.py main.py
COPY uwsgi.ini uwsgi.ini