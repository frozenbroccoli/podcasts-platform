# Podcasts Platform

## How to run the development server?

Clone the repo and run it locally.

```commandline
git clone https://github.com/frozenbroccoli/podcasts-platform

cd podcasts-platform

git checkout development
```

Paste the `.env` file (yes) here. Then run the server.

```commandline
python3 manage.py migrate

python3 manage.py runserver
```

The server should be up and running at `127.0.0.1:8000/` or `localhost:8000/`.

