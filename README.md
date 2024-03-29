# Comic Server

Code for website: [jnduli comics](https://comics.jnduli.co.ke).


## How To Restore Backups
Uses django-dbbackup to set up backups and restore, but there's a
problem with restore
(https://github.com/django-dbbackup/django-dbbackup/issues/245).

To restore a back up:
- create users in original db (postgres and comic_db_user)
- modify the backup file to remove the lines that DROP constraints
  (until drop schema public)
- Run:
  `DB_USER=postgres DB_PASSWORD=password python manage.py dbrestore --uncompress --input-path path_to_dbbackup`    

## TODO: Clean up The Lines Below

## Running in a server
TODO: working on these ansible instructions, will add problems with
docker and move to vagrant
Have ansible instructions here and disable CI CD at the moment.

## Moving to Docker
- how to run the docker-compose on the server?
- dealing with certificates on the server?
- how to link up static files on the server?
- how to manage release process for the project?
- server organization??


what things do I need on a server to get everything up and ready?
- docker
- certbot
- nginx set up

# To run this:
This command will also update with local changes in the code base:
    docker-compose build && docker-compose up -d
To run migrations:
    docker-compose exec comic_server python manage.py migrate
To do a backup:
t

## TODO: Clean up The Lines Below

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


# migration to sqlite

Plan to migrate to sqlite:

1. Change ansible playbook to deploy an sqlite configuration for the website and
   system:
   - change branch
   - change folder project sits on
   - change the ip and port we follow
   - TODO: look for other alternatives
   - TODO: ensure we have backups and dump.json has run
2. Log into the main server and run dump.json
3. Run and deploy the new sqlite version, change the folder we checkout to and
   the ip port we listen on
4. Run load_data on the sqlite version
5. Manually change nginx to point to the new sqlite version
6. Merge changes to main
7. Clean up ansible play books and re-run everything from scratch to see how it
   would work
8. Clean up the old docker-compose files
9. Document everything in blog post
   

Run this command:

1. docker-compose exec comic_server bash -c "python manage.py dumpdata > /var/backups/comic_server/json_dump.json"
 
