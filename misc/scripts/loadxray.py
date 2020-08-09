#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os, sys
import django

def getFieldsFromXRAY(xrayitem):

    particledatetime = xrayitem["time_tag"]
    length = xrayitem["energy"]
    if length == "0.05-0.4nm":
        xraytype = 1
    else:
        xraytype = 2
    value = xrayitem["flux"]
    return particledatetime,xraytype,value


os.system("wget https://services.swpc.noaa.gov/json/goes/primary/xrays-6-hour.json -O output/xrays-6-hour.json")
myfile = open("output/xrays-6-hour.json","r")
j=json.load(myfile)
proj_path = "/srv/spaceweather/git/spaceweather/src/spaceweather/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
django.setup()

from core.models import *
for i in j[-2:]:
    particledatetime,xraytype,value = getFieldsFromXRAY(i)
    try:
        Xrayflux.objects.get(xtype=xraytype,date=particledatetime)
        print("Data for {} at {} already there!".format(xraytype,particledatetime))
    except:
        axtype = Xtype.objects.get(id=xraytype)
        xray = Xrayflux(date=particledatetime,xtype=axtype,value=value,units="Watts/m2",bogus=False)
        xray.save()

