#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os, sys
import django

def getFieldsFromElectron(electronitem):

    particledatetime = electronitem["time_tag"]
    energy = electronitem["energy"]
    etype = 0
    if energy == ">=2 MeV":
        etype = 1
    value = electronitem["flux"]
    return particledatetime,etype,value


os.system("wget https://services.swpc.noaa.gov/json/goes/primary/integral-electrons-6-hour.json -O output/integral-electrons-6-hour.json")
myfile = open("output/integral-electrons-6-hour.json","r")
j=json.load(myfile)
proj_path = "/srv/spaceweather/git/spaceweather/src/spaceweather/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
django.setup()

from core.models import *
for i in j[-3:]:
    particledatetime,etype,value = getFieldsFromElectron(i)
    if etype !=0:
        try:
            Electronflux.objects.get(etype=etype,date=particledatetime)
            print("Data for {} at {} already there!".format(etype,particledatetime))
        except:
            etype = Etype.objects.get(id=etype)
            e = Electronflux(date=particledatetime,etype=etype,value=value,units="Electrons/cm2-s-sr",bogus=False)
            e.save()

