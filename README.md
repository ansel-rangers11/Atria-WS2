## Overview

This project is the backend REST API of the Atria Volunteer Platform. 

## Project Setup

Prerequisites:
- [Python 3.6](https://www.python.org/downloads/)
- [Pipenv](https://docs.pipenv.org/)

After checking out the repo, Install required packages:
```
$ cd Atria-WS
$ pipenv install
```

Enter the pipenv shell:
```
$ pipenv shell
```

Initialize database:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
