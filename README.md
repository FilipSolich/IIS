# IIS - Knihovní systém

## Požadavky

 - Python 3.8+

## Spuštění

```shell
$ git clone git@github.com:FilipSolich/IIS.git
$ cd IIS 
$ python -m venv .env
$ source .env/bin/activate
$ pip install -r requiremets.txt
$ cd is_library 
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py creategroups
$ python manage.py runserver
```
