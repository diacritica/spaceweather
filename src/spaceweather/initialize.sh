#!/bin/bash

# A basic script for initialize the initial production like
# database without games.

python manage.py flush
echo "Database flushed"
python manage.py migrate --noinput
echo "Database migrated to new model if necessary"
echo "Adding auth credentials"
python manage.py loaddata auth
echo "Added auth credentials"
echo "Adding Protontype fixtures..."
python manage.py loaddata ptype
echo "Added Protontype fixtures..."
echo "Adding Electrontype fixtures..."
python manage.py loaddata etype
echo "Added Electrontype fixtures..."
echo "Adding Xraytype fixtures..."
python manage.py loaddata xtype
echo "Added Xraytype fixtures..."
echo "Adding Protonflux fixtures..."
python manage.py loaddata protonflux
echo "Added Protonflux fixtures..."
echo "Adding Electronflux fixtures..."
python manage.py loaddata electronflux
echo "Added Electronflux fixtures..."
echo "Adding Xrayflux fixtures..."
python manage.py loaddata xrayflux
echo "Added Xrayflux fixtures..."
echo "Adding Alerttype fixtures..."
python manage.py loaddata alerttype
echo "Added Alerttype fixtures..."
echo "Adding Alert fixtures..."
python manage.py loaddata alert
echo "Added Alert fixtures..."
echo "Adding Sunspottype fixtures..."
python manage.py loaddata sunspottype
echo "Added Sunspottype fixtures..."
echo "Adding Sunspot fixtures..."
python manage.py loaddata sunspot
echo "Added Sunspot fixtures..."
echo "Adding Sunspotregion fixtures..."
python manage.py loaddata sunspotregion
echo "Added Sunspotregion fixtures..."
