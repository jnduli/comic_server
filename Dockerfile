# To run this, look at the docker-compose.yaml file

FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y postgresql-client # required for backups and restore by django-dbbackup

COPY ./requirements.txt /
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir /comicsite
WORKDIR /comicsite
COPY ./comicsite/ /comicsite

EXPOSE 8000

ENV DJANGO_WSGI_MODULE comicsite.wsgi

CMD ["sh", "-c", "gunicorn ${DJANGO_WSGI_MODULE}:application --name comic_server --workers 3 --bind 0.0.0.0:8000 --log-level=debug --log-file=/var/comic_server_logs"]
# CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
# CMD ["sh", "-c", "python comicsite/manage.py migrate && python comicsite/manage.py runserver 0.0.0.0:8000"]
