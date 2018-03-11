## Overview

This project is the backend REST API of the Atria Volunteer Platform.

## Project Setup

Prerequisites:
- [Python 3.6](https://www.python.org/downloads/)
- [Pipenv](https://docs.pipenv.org/)

After checking out the repo, Install required packages:

    $ cd Atria-WS2
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


## Adding a new Model

Add a new class to api/models.py

    $ python manage.py makemigrations
    $ python manage.py migrate

Create a view in api/views

Register in api/admin.py

    $ python manage.py runserver

Run the admin console and verify the admin screens work

Add to api/urls.py

Run the api console and verify the api methods appear

Add test data to api/fixtures/one_npo.json

(Can extract data with python manage.py dumpdata api.<model>)

Create tests in api/tests/test<model>.py

Run the tests and verify that they pass

    $ python manage.py test
