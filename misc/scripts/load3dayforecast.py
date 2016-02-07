"""
:Product: three_day_forecast.txt
:Issued: 2012 Dec 12 1235 UTC
# Prepared by the U.S. Dept. of Commerce, NOAA, Space Weather Prediction
Center
#
A. NOAA Geomagnetic Activity Observation and Forecast

The greatest observed 3 hr Kp over the past 24 hours was 1 (below NOAA
Scale levels).
The greatest expected 3 hr Kp for Dec 12-Dec 14 2012 is 3 (below NOAA
Scale levels).

NOAA Kp index breakdown Dec 12-Dec 14 2012

            Dec 12     Dec 13     Dec 14
00-03UT        0          2          2
03-06UT        0          1          2
06-09UT        1          1          0
09-12UT        0          1          1
12-15UT        1          1          1
15-18UT        1          1          1
18-21UT        2          3          2
21-00UT        2          3          2

Rationale: Expecting predominately quiet conditions throughout the
forecast period. A chance for unsettled conditions exists late on 13 Dec
as a negative polarity coronal hole/high speed stream becomes
geoeffective.  No NOAA scale G1 or greater storms expected.

B. NOAA Solar Radiation Activity Observation and Forecast

Solar radiation, as observed by NOAA GOES-13 over the past 24 hours, was
below S-scale storm level thresholds.

Solar Radiation Storm Forecast for Dec 12-Dec 14 2012

              Dec 12  Dec 13  Dec 14
S1 or greater    1%      1%      1%

Rationale: No NOAA scale S1 or greater storms are expected.

C. NOAA Radio Blackout Activity and Forecast

No radio blackouts were observed over the past 24 hours.

Radio Blackout Forecast for Dec 12-Dec 14 2012

              Dec 12        Dec 13        Dec 14
R1-R2            1%            1%            1%
R3 or greater    1%            1%            1%

Rationale:  No NOAA scale R1 or greater storms are expected.
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import collections
import datetime

import json
import os, sys
import django


urlwithfile = "http://services.swpc.noaa.gov/text/3-day-forecast.txt"

r = requests.get(urlwithfile)
rlines = r.text.split("\n")
adate=rlines[1].split(":")[2].strip()
referencedatetime = datetime.datetime.strptime(adate, '%Y %b %d %I%M %Z')
basedate = datetime.datetime(year=referencedatetime.year,month=referencedatetime.month,day=referencedatetime.day,hour=0,minute=0)
delta3h = datetime.timedelta(hours=3)
delta1d = datetime.timedelta(days=1)



ARationalestart = r.text.find("Rationale",0)
ARationaleend = r.text.find("B",ARationalestart)

BRationalestart = r.text.find("Rationale",ARationaleend)
BRationaleend = r.text.find("C",BRationalestart)

CRationalestart = r.text.find("Rationale",BRationaleend)
CRationaleend = -1

proj_path = "/srv/spaceweather/git/spaceweather/src/spaceweather/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

from core.models import *

# GEOMAGNETIC ACTIVITY

geomagneticdaytimes = []
for line in rlines:
    if line.find("UT ") > -1:
        geomagneticdaytimes.append(line)


"""
00-03UT        2          4          4
03-06UT        1          4          3
06-09UT        1          3          2
09-12UT        2          3          4
12-15UT        3          3          4
15-18UT        3          3          3
18-21UT        3          3          3
21-00UT        4          4          3
"""

deltanumber = 0
for line in geomagneticdaytimes:
    values = line.split()[1:]
    for day in range(3):
        dt = basedate+(delta1d*day)+(delta3h*deltanumber)
        try:
            Geomagactivity.objects.get(date=dt)
            print("Data for {} already there!".format(dt))
        except:
            value = values[day]
            g = Geomagactivity(date=dt,value=value,bogus=False)
            g.save()
            print("Data for {} inserted!".format(dt))
    deltanumber+=1

geomagrationale = r.text[ARationalestart:ARationaleend]

# SOLAR RADIATION

basedate = datetime.date(year=referencedatetime.year,month=referencedatetime.month,day=referencedatetime.day)

# R1-R2

solarradiation = ""

for line in rlines:
    if line.find("S1 or greater") > -1:
        solarradiation = line
        break
values = solarradiation.split()[3:]

for day in range(3):
    dt = basedate+(delta1d*day)
    try:
        Solarradiation.objects.get(date=dt)
        print("Data for {} already there!".format(dt))
    except:
        srt = Solarradiationtype.objects.get(name="S1 or greater")
        value = int(values[day][:-1])
        s = Solarradiation(date=dt, value=value, solarradiationtype=srt, bogus=False)
        s.save()
        print("Data for {} inserted!".format(dt))

solarradiationrationale = r.text[BRationalestart:BRationaleend]

# RADIO BLACKOUT


basedate = datetime.date(year=referencedatetime.year,month=referencedatetime.month,day=referencedatetime.day)

radioblackout = ""

for line in rlines:
    if line.find("R1-R2") > -1:
        radioblackout = line
        break

if len(radioblackout) > 0:

    values = radioblackout.split()[1:]

    for day in range(3):
        dt = basedate+(delta1d*day)
        try:
            Radioblackout.objects.get(date=dt)
            print("Data for {} already there!".format(dt))
        except:
            rbt = Radioblackouttype.objects.get(name="R1-R2")
            value = int(values[day][:-1])
            rb = Radioblackout(date=dt, value=value, radioblackouttype=rbt, bogus=False)
            rb.save()
            print("Data for {} inserted!".format(dt))


radioblackout = ""

for line in rlines:
    if line.find("R3 or greater") > -1:
        radioblackout = line
        break
if len(radioblackout) > 0:

    values = radioblackout.split()[1:]

    for day in range(3):
        dt = basedate+(delta1d*day)
        try:
            Radioblackout.objects.get(date=dt)
            print("Data for {} already there!".format(dt))
        except:
            rbt = Radioblackouttype.objects.get(name="R3 or greater")
            value = int(values[day][:-1])
            rb = Radioblackout(date=dt, value=value, radioblackouttype=rbt, bogus=False)
            rb.save()
            print("Data for {} inserted!".format(dt))


radioblackoutrationale = r.text[CRationalestart:CRationaleend]

# FORECAST RATIONALE

basedate = datetime.datetime(year=referencedatetime.year,month=referencedatetime.month,day=referencedatetime.day,hour=0,minute=0)

try:
    Forecastrationale.objects.get(date=basedate)
    print("Data for {} already there!".format(basedate))
except:
    fr = Forecastrationale(date=basedate, radioblackout=radioblackoutrationale, solarradiation=solarradiationrationale, geomagactivity=geomagrationale)
    fr.save()
    print("Data for {} inserted!".format(dt))
