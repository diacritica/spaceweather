import datetime, json
from core.models import *

now = datetime.datetime.now()
delta5 = datetime.timedelta(minutes=5)

afile = open("solarelectron08flux.txt",'r')
ajsonfile = json.load(afile)

data = ajsonfile['data']['y']

atype = Etype.objects.filter(name="E>0.8MeV")[0]

count = 0

for value in data:
    e = Electronflux(date=now+delta5*count,etype=atype,
    value=value,units="Electrons/cm2-s-sr",bogus=False)
    count += 1
    e.save()
