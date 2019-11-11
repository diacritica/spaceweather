#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import collections
import datetime

import json
import os, sys
import django


urlwithfile = "ftp://ftp.swpc.noaa.gov/pub/lists/particle/Gp_part_5m.txt"

with urllib.request.urlopen(urlwithfile) as response:
    r = str(response.read())

rlines = r.split("\\n")
print(rlines)

proj_path = "/srv/spaceweather/git/spaceweather/src/spaceweather/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

django.setup()

from core.models import *

for line in rlines:
    values = line.strip().split()[:-1] #we skip latest E>4.0 MeV
    if len(values) == 14 and "-1.00e+05" not in values:
        YR,MO,DA,HHMM,GDay,GSec,P1,P5,P10,P30,P50,P100,E08,E20 = values
        particledatetime = datetime.datetime(int(YR),int(MO), \
                                                 int(DA),int(HHMM[:2]), \
                                                 int(HHMM[2:])).isoformat()

        try:
            Protonflux.objects.get(ptype=1,date=particledatetime)
            print("Data for {} at {} already there!".format("1",particledatetime))
        except:
            aptype = Ptype.objects.get(id=1)
            pf10 = Protonflux(date=particledatetime,ptype=aptype,value=float(P10),units="Protons/cm2-s-sr",bogus=False)
            print("Data for {} at {} inserted!".format(aptype,particledatetime))
            pf10.save()

        try:
            Protonflux.objects.get(ptype=3,date=particledatetime)
            print("Data for {} at {} already there!".format("3",particledatetime))
        except:
            aptype = Ptype.objects.get(id=3)
            pf100 = Protonflux(date=particledatetime,ptype=aptype,value=float(P100),units="Protons/cm2-s-sr",bogus=False)
            print("Data for {} at {} inserted!".format(aptype,particledatetime))
            pf100.save()

        try:
            Electronflux.objects.get(etype=2,date=particledatetime)
            print("Data for {} at {} already there!".format("2",particledatetime))
        except:
            aetype = Etype.objects.get(id=2)
            ef08 = Electronflux(date=particledatetime,etype=aetype,value=float(E08),units="Electrons/cm2-s-sr",bogus=False)
            print("Data for {} at {} inserted!".format(aetype,particledatetime))
            ef08.save()

        try:
            Electronflux.objects.get(etype=1,date=particledatetime)
            print("Data for {} at {} already there!".format("1",particledatetime))
        except:
            aetype = Etype.objects.get(id=1)
            ef20 = Electronflux(date=particledatetime,etype=aetype,value=float(E20),units="Electrons/cm2-s-sr",bogus=False)
            print("Data for {} at {} inserted!".format(aetype,particledatetime))
            ef20.save()
