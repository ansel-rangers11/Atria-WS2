## Overview

This project is the backend REST API of the Atria Volunteer Platform. 

## Project Setup

Prerequisites:
- [Python 3.6](https://www.python.org/downloads/)
- [Pipenv](https://docs.pipenv.org/)

After checking out the repo, Install required packages:

    $ cd Atria-WS
    $ pipenv install

Enter the pipenv shell:

    $ pipenv shell

Initialize database:

    $ python manage.py migrate

Create a superuser, if you want:

    $ python manage.py createsuperuser

Then run the dev server

    $ python manage.py runserver

Dev server runs by default on port 8000, so go to `localhost:8000` or `127.0.0.1:8000` in your browser to view the API autodocs.
