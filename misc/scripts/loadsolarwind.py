from core.models import *
import json

myfile = open("/home/diacritica/GIT/spaceweather/misc/research/SW/plasma-7-day.json","r")
j=json.load(myfile)


for i in j[1:]:
    if i[0][-4] == '0':
        if None in i:
            asw = Solarwind(date=i[0],density=0,radialspeed=0,temperature=0,bogus=True)
        else:
            asw = Solarwind(date=i[0],density=i[1],radialspeed=i[2],temperature=i[3])
        asw.save()
