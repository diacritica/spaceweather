
import json
import os, sys
import django

os.system("wget http://services.swpc.noaa.gov/experimental/products/solar-wind/plasma-2-hour.json -O output/plasma-2-hour.json")
myfile = open("output/plasma-2-hour.json","r")
j=json.load(myfile)

proj_path = "/srv/spaceweather/git/spaceweather/src/spaceweather/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

from core.models import *

for i in j[1:]:
    if i[0][-4] == '0':
        try:
            Solarwind.objects.get(date=i[0])
            print("Data for {} already there!".format(i[0]))
        except:
            if None in i:
                asw = Solarwind(date=i[0],density=0,radialspeed=0,temperature=0,bogus=True)
            else:
                asw = Solarwind(date=i[0],density=i[1],radialspeed=i[2],temperature=i[3])
            print("Data for {} inserted!".format(i[0]))
            asw.save()
