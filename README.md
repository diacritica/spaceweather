# spaceweather
Space Weather online resource web

## How to install ##

Install PostgreSQL 9.4 or higher

In Arch

```bash
pacman -S postgresql
sudo passwd postgres
sudo su - postgres
initdb --locale es_ES.UTF-8 -E UTF8 -D '/var/lib/postgres/data'
systemctl start postgresql
systemctl enable postgresql
createuser spaceweather --pwprompt
createdb -E UTF-8 -O spaceweather spaceweather
```

In Debian

```bash
sudo apt-get install postgresql-9.4 postgresql-client-9.4 postgresql-contrib-9.4
sudo passwd postgres
sudo su - postgres
sudo service postgresql start
createuser spaceweather --pwprompt
createdb -E UTF-8 -O spaceweather spaceweather
psql
GRANT ALL PRIVILEGES ON DATABASE  spaceweather to "spaceweather";
```

As a normal user, create a virtualenv environment for Python 3.3+

```bash
mkvirtualenv -p /usr/bin/python3 SW
cd $YOUR_SPACEWEATHER_REPO/
pip install -r requirements.txt --upgrade
```

### How to crate the database schema ###

First, user edit settings.py under src/spaceweather/spaceweather

and find this section

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'spaceweather',
        "USER": "spaceweather",
        "PASSWORD": "spaceweather",
        "HOST": "localhost",
        "PORT": "",

    }
}
```

and change PASSWORD with the password you chose earlier.

Then under src/spaceweather run

```bash
python manage.py makemigrations
python manage.py migrate
```

### How to install fixtures ###

```bash
. initialize.sh
```

answering yes to the question about deleting the databse content

user: admin, pass: 123456

### Run in development mode ###

```bash
cd src/spaceweather
python manage.py runserver
```

and go to http://127.0.0.1:8000/api/


### API examples ###

Remember that the defaul admin user is

user: admin, pass: 123456

Protonflux

http://127.0.0.1:8000/api/protonflux/?date_min=2015-12-06&date_max=2015-12-07&ptype=1&bogus=False

will yield all protonflux valid values for 2015-12-06 of energy type 1 (P>10MeV)

```
{
    "count": 251,
    "next": "http://127.0.0.1:8000/api/protonflux/?bogus=False&date_max=2015-12-07&date_min=2015-12-06&page=2&ptype=1",
    "previous": null,
    "results": [
        {
            "id": 268,
            "date": "2015-12-06T00:00:00Z",
            "ptype": 1,
            "value": 0.138,
            "units": "Protons/cm2-s-sr",
            "bogus": false,
            "links": {
                "self": "http://127.0.0.1:8000/api/protonflux/268/"
            }
        },
        {
            "id": 269,
            "date": "2015-12-06T00:05:00Z",
            "ptype": 1,
            "value": 0.109,
            "units": "Protons/cm2-s-sr",
            "bogus": false,
            "links": {
                "self": "http://127.0.0.1:8000/api/protonflux/269/"
            }
        },
        ...
]
