#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os, sys
import django

def getFieldsFromProton(protonitem):

    particledatetime = protonitem["time_tag"]
    energy = protonitem["energy"]
    ptype = 0
    if energy == ">=10 MeV":
        ptype = 1
    if energy == ">=100 MeV":
        ptype = 3
    value = protonitem["flux"]
    return particledatetime,ptype,value


os.system("wget https://services.swpc.noaa.gov/json/goes/primary/integral-protons-6-hour.json -O output/integral-protons-6-hour.json")
myfile = open("output/integral-protons-6-hour.json","r")
j=json.load(myfile)
proj_path = "/srv/spaceweather/git/spaceweather/src/spaceweather/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
django.setup()

from core.models import *
for i in j[-24:]:
    particledatetime,ptype,value = getFieldsFromProton(i)
    if ptype !=0:
        try:
            Protonflux.objects.get(ptype=ptype,date=particledatetime)
            print("Data for {} at {} already there!".format(ptype,particledatetime))
        except:
            ptype = Ptype.objects.get(id=ptype)
            p = Protonflux(date=particledatetime,ptype=ptype,value=value,units="Protons/cm2-s-sr",bogus=False)
            p.save()

