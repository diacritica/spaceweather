#!/bin/bash

# A basic script for initialize the initial production like
# database without games.

python manage.py flush
python manage.py migrate --noinput
python manage.py loaddata auth
python manage.py loaddata ptype
python manage.py loaddata etype
python manage.py loaddata xtype
python manage.py loaddata protonflux
python manage.py loaddata electronflux
python manage.py loaddata xrayflux
python manage.py loaddata alerttype
python manage.py loaddata alert

