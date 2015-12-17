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
echo "Adding Channeltype fixtures..."
python manage.py loaddata channeltype
echo "Added Channeltype fixtures..."
echo "Adding Imagechanell fixtures..."
python manage.py loaddata imagechannel
echo "Added Imagechannel fixtures..."
echo "Adding Solarradiationtype fixtures..."
python manage.py loaddata solarradiationtype
echo "Added Solarradiationtype fixtures..."
echo "Adding Solarradiation fixtures..."
python manage.py loaddata solarradiation
echo "Added Solarradiation fixtures..."
echo "Adding Radioblackouttype fixtures..."
python manage.py loaddata radioblackouttype
echo "Added Radioblackouttype fixtures..."
echo "Adding Radioblackout fixtures..."
python manage.py loaddata radioblackout
echo "Added Radioblackout fixtures..."
echo "Adding Geomagactivity fixtures..."
python manage.py loaddata geomagactivity
echo "Added Geomagactivity fixtures..."
echo "Adding Forecastrationalie fixtures..."
python manage.py loaddata forecastrationale
echo "Added Forecastrationale fixtures..."
echo "Adding Solarwind fixtures..."
python manage.py loaddata solarwind
echo "Added Solarwind fixtures..."
