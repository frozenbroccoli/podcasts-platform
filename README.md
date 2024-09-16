# Podcasts Platform

## Tech stack

This project is written in Python version 3.11.9 with
Django REST Framework.

## How to run the development server?

Clone the repo and run it locally.

```commandline
git clone https://github.com/frozenbroccoli/podcasts-platform

cd podcasts-platform
```

Paste the `.env` file (yes) here. The environmental variables
in the development mode are `SECRET_KEY` which is an
alphanumeric key and `ENV=DEVELOPMENT`.
Once the `.env` file is there, run the development server
with the following commands.

```commandline
python3 manage.py migrate

python3 manage.py runserver
```

The server should be up and running at `127.0.0.1:8000/` or `localhost:8000/`.

