#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import collections
import datetime

import json
import os, sys
import django


urlwithfile = "ftp://ftp.swpc.noaa.gov/pub/lists/xray/Gp_xr_5m.txt"

with urllib.request.urlopen(urlwithfile) as response:
    r = str(response.read())

rlines = r.split("\\n")

proj_path = "/srv/spaceweather/git/spaceweather/src/spaceweather/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

django.setup()

from core.models import *

for line in rlines:
    values = line.strip().split()
    if len(values) == 9 and "-1.00e+05" not in values:
        YR,MO,DA,HHMM,GDay,GSec,S,L,R = values
        particledatetime = datetime.datetime(int(YR),int(MO), \
                                                 int(DA),int(HHMM[:2]), \
                                                 int(HHMM[2:])).isoformat()

        try:
            Xrayflux.objects.get(xtype=1,date=particledatetime)
            print("Data for {} at {} already there!".format("1",particledatetime))
        except:
            axtype = Xtype.objects.get(id=1)
            xshort = Xrayflux(date=particledatetime,xtype=axtype,value=float(S),units="Watts/m2",bogus=False)
            print("Data for {} at {} inserted!".format(axtype,particledatetime))
            xshort.save()


        try:
            Xrayflux.objects.get(xtype=2,date=particledatetime)
            print("Data for {} at {} already there!".format("2",particledatetime))
        except:
            axtype = Xtype.objects.get(id=2)
            xlong = Xrayflux(date=particledatetime,xtype=axtype,value=float(L),units="Watts/m2",bogus=False)
            print("Data for {} at {} inserted!".format(axtype,particledatetime))
            xlong.save()
