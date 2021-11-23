# IIS - FITUŠKA

## Požadavky

 - Python 3.8+

## Verze knihoven

 - Django 3.2.7
 - Pillow 8.3.2
 - Bootstrap 5.0.2

## Spuštění

```shell
$ git clone git@github.com:FilipSolich/IIS.git
$ cd IIS
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py creategroups
$ python manage.py runserver
```

## Import dat do DB

```shell
$ python manage.py loaddata db.json
```
