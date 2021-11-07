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
$ python -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ cd fituska
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py creategroups
$ python manage.py shell < db_import.py
$ python manage.py runserver
```

## Nový import dat do databaze

```shell
$ python manage.py loaddata db.json
```
