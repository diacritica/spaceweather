#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import collections
import datetime

import json
import os, sys
import django

delta1day = datetime.timedelta(days=1)

filetime = datetime.date.today() #- delta1day

baseurl = "http://www.spaceweather.com/images"
filetimestring = filetime.strftime("%Y/%d%b%y/sunspot_labels.txt").lower()
url = baseurl + filetimestring

r = requests.get(url)
rlines = r.text.split("\n")

"""
2492 N14W78   146  0010 Axx  00   01 Alpha
2494 S14W96   164  0010 Axx  01   01 Alpha
2497 N13W19   087  0250 Eac  13   20 Beta-Gamma-Delta
2498 N18E15   053  0010 Axx  01   01 Alpha
2499 N11E38   030  0010 Axx  01   01 Alpha

"id": 1,
        "date": "2015-12-14",
        "region": 2463,
        "numberofsunspots": 2,
        "magneticclass": "β",
        "size": 10,
        "spotclass": "Cro",
        "location": "S09W62",
        "bogus": false,

"""

proj_path = "/srv/spaceweather/git/spaceweather/src/spaceweather/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

django.setup()

from core.models import *

#today = (datetime.date.today() - delta1day).isoformat()
today = datetime.date.today().isoformat()
magneticclassdict = {"Alpha":"α","Beta":"β","Gamma":"γ","Beta-Gamma":"β-γ","Delta":"δ","Beta-Delta":"β-δ","Beta-Gamma-Delta":"β-γ-δ","Gamma-Delta":"γ-δ"}

for line in rlines:
    values = line.strip().split()
    if len(values) == 8:
        region,location,dummy1,size,spotclass,numberofsunspots,dummy2,magneticclass = values
        magneticclass = magneticclassdict[magneticclass]
        try:
            Sunspotregion.objects.get(region=region,date=today)
            print("Data for {} at {} already there!".format(region,today))
        except:
            ssr = Sunspotregion(date=today,region=region,location=location,size=size,spotclass=spotclass,numberofsunspots=int(numberofsunspots),magneticclass=magneticclass,bogus=False)
            print("Data for {} at {} inserted!".format(region,today))
            ssr.save()
