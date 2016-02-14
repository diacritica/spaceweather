import os, sys
import time, datetime

import PIL
from PIL import Image

proj_path = "/srv/spaceweather/git/spaceweather/src/spaceweather/"
output_path = "/srv/spaceweather/git/spaceweather/misc/scripts/output/"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)


newwidth = 512
newheight = 512
quality_val = 70

now = datetime.datetime.utcnow()
isonow = now.isoformat()
channels = ['171','193','211','304']

for c in channels:
    filename = "{}-{}.jpg".format(c,isonow)
    os.system("wget http://umbra.nascom.nasa.gov/images/latest_aia_{}.gif -O output/{}/{}".format(c,c,filename))
    time.sleep(1)
    downloadedimage = Image.open("output/{}/{}".format(c,filename)).convert('RGB')
    downloadedimage = downloadedimage.resize((newwidth, newheight), PIL.Image.ANTIALIAS)
    downloadedimage.save("output/{}/{}".format(c,filename))

#HMI
basenow = now.replace(minute=0, second=0, microsecond=0)
minutes = now.minute
loopminutes = minutes//15 +1
delta15min = datetime.timedelta(minutes=15)
delta1hour = datetime.timedelta(hours=1)
for l in range(loopminutes):
    filetime = basenow - delta1hour + delta15min*l
    print("filetime",filetime)
    filetimestring = filetime.strftime("%Y/%m/%d/%Y%m%d_%H%M%S_Ic_512.jpg")
    filetimestringout = filetime.strftime("%Y%m%d_%H%M%S_Ic_512.jpg")

    os.system("wget http://jsoc.stanford.edu/data/hmi/images/{} -O output/{}".format(filetimestring,filetimestringout))

os.chdir(proj_path)
from core.models import *
from django.core.files import File

os.chdir(output_path)

for c in channels:
    entry = "{}/{}-{}.jpg".format(c,c,isonow)
    entryb = "{}-{}.jpg".format(c,isonow)
    ct = Channeltype.objects.get(name__contains=c)
    ic = Imagechannel(date=isonow,originaldate=isonow,bogus=False,channeltype=ct)
    ic.image.save(entryb,File(open(entry,'rb')))
    ic.save()

for l in range(loopminutes):
    filetime = basenow - delta1hour + delta15min*l
    filetimestring = filetime.strftime("%Y%m%d_%H%M%S_Ic_512.jpg")
    ct = Channeltype.objects.get(name__contains="HMI")
    try:
        Imagechannel.objects.get(date=filetime)
        print("Data for {} already there!".format(filetime))
    except:
        ic = Imagechannel(date=filetime,originaldate=filetime,bogus=False,channeltype=ct)
        ic.image.save(filetimestring,File(open(filetimestring,'rb')))
        ic.save()
        print("Data for {} inserted!".format(filetime))
        