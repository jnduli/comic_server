# Comic Server

This code repository contains the code that runs the comic site found at
[jnduli comics](https://comics.jnduli.co.ke).

The project is a django project. I've also included a sample ansible
script that one can use to set up the project.

## Setup
To set up the project

```
python -m venv .env
source ./.env/bin/activate
pip install -r requirements.txt
```

To run tests:

```
cd comicsite
python manage.py migrate
python manage.py test
```

If you had a backup that you want to replicate locally:

```
# ensure you have postgres set up properly locally
DJANGO_DATABASE=server python manage.py migrate
DJANGO_DATABASE=server python manage.py dbrestore --uncompress --input-path full_path_to_db_backup
DJANGO_DATABASE=server python manage.py mediarestore --input-path full_path_to_media_backup
DJANGO_DATABASE=server python manage.py runserver
```

