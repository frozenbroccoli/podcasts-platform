# Documentation of the APIs

## Search API

### What does it return?

The top `200` paginated results of an itunes
podcasts search, the page size being `20`.

### How to call it?

Make a GET request to the endpoint `{{base_url}}/podcasts/search/?query={{query}}&page={{page}}`.

### How to run the development server?

Clone the repo and run it locally.

```commandline
git clone https://github.com/frozenbroccoli/podcasts-platform

cd podcasts-platform
```

Paste the `.env` file (yes) here. Then run the server.

```commandline
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver
```

The server should be up and running at `127.0.0.1:8000/` or `localhost:8000/`.

### Next order of business

1. Sort/filter the search results based on dates published.
2. Sort/filter based on rating.
