import os
import datetime
import glob
from core.models import *
from django.core.files import File

origdir = "/home/diacritica/GIT/spaceweather/misc/scripts/"
desdir = "/home/diacritica/GIT/spaceweather/src/spaceweather/"

os.chdir(origdir)

#channels = ['171','193','211','304']
channels = ['171','193','211','304']


for c in channels:
    print(c)
    os.chdir(origdir)
    k = glob.glob("{}-*-*.jpg".format(c))
    k.sort()
    for entry in k:
        print(entry)
        os.chdir(origdir)
        entrydate = "".join(entry.split(".")[0].split("-")[1:])
        entrydate = "{}-{}-{} {}".format(entrydate[0:4],entrydate[4:6],entrydate[6:8],entrydate[9:18])
        ct = Channeltype.objects.get(name__contains=c)
        ic = Imagechannel(date=entrydate,originaldate=entrydate,bogus=False,channeltype=ct)
        os.chdir(desdir)
        ic.image.save(entry,File(open(origdir+entry,'rb')))
        ic.save()

