# Reports Connect 🍃

A simple reports management application build for Heavy Connect challenge.

## Preview

|                                          |                                                 |                                            |
| :--------------------------------------- | :---------------------------------------------: | :----------------------------------------: |
| ![Home](./screenshots/screenshot_01.png) | ![User filter](./screenshots/screenshot_02.png) | ![Mobile](./screenshots/screenshot_03.png) |
|                                          |                                                 |                                            |

## Getting Started

Install the dependencies (needed [Pipenv](https://github.com/pypa/pipenv)):

```sh
pipenv install

```

Optionally use _pipenv shell_ or _pipenv run_.

Initialize the database and load the fixtures:

```sh
python manage.py migrate

# load fixtures
python manage.py loaddata fixtures/users.json --app users.User
python manage.py loaddata fixtures/reports.json --app reports.Report
python manage.py loaddata fixtures/report_responses.json --app reports.ReportResponse
```

Generate the static files:

```sh
python manage.py collectstatic
python manage.py compress
```

Now, just run the server:

```sh
python manage.py runserver
```

http://127.0.0.1:8000/
