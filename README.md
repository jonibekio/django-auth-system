# Django Authentication and Profile Demo

![Python](https://img.shields.io/badge/Python-Django%20project-3776AB?logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-templates-092E20?logo=django&logoColor=white) ![Database](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite&logoColor=white)

## Overview

A small server-rendered Django learning project for account registration, sign-in/sign-out, and profile viewing/editing. It is a teaching exercise rather than a production authentication service.

## Features

- Registration, login, and logout pages.
- Profile display and profile editing.
- Django session authentication and SQLite development database.

## Screenshots

No application screenshots are tracked in this repository.

## Technology stack and architecture

Python, Django, Django templates, HTML/CSS, and SQLite. The project uses a conventional Django project with an `accounts` app and a `config` package.

```text
accounts/     User model, forms, views, URLs, migrations
config/       Django settings, root URLs, WSGI/ASGI
templates/    Server-rendered pages
manage.py
db.sqlite3    Local development database (should not be committed)
```

## Installation

The repository does not include a dependency manifest. In a clean Python environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install Django
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. The default development database is SQLite. Use a fresh local database rather than relying on the committed database file.

## Configuration

There is no documented environment-variable contract. Django settings currently contain development defaults. Do not deploy with those settings; define a unique secret key, `DEBUG=False`, and explicit `ALLOWED_HOSTS` before any hosted use.

## Routes and API

This project is a server-rendered website and does not expose a REST API. Registration, login, logout, and profile routes are defined in `accounts/urls.py`.

## Database

The account model and Django migrations are under `accounts/`. SQLite is used for local development. No production database setup is included.

## Testing and deployment

The repository has no substantive test suite, CI workflow, or deployment configuration. Run locally with Django's development server only. Add auth and permission tests before extending the project.

## Security notes

- Signup contains a username validation error: the cleaner treats the submitted username string like a model manager. Registration may fail until corrected.
- The project has insecure Django development settings. Do not expose it to the internet as-is.
- Remove database and Python cache artifacts from version control as a separately reviewed cleanup; this README does not alter them.

## Future improvements

- Fix and test registration and profile ownership checks.
- Add dependency pinning, `.gitignore`, production settings, and a CI workflow.
- Add a REST API only if the project scope is intentionally expanded.
