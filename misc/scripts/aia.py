import os, sys
import time, datetime

import PIL
from PIL import Image

proj_path = "/home/elfo/GIT/spaceweather/src/spaceweather/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)


newwidth = 512
newheight = 512
quality_val = 70

now = datetime.datetime.utcnow().isoformat()
channels = ['171','193','211','304']

for c in channels:
    filename = "{}-{}.jpg".format(c,now)
    os.system("wget http://umbra.nascom.nasa.gov/images/latest_aia_{}.gif -O output/{}/{}".format(c,c,filename))
    time.sleep(1)
    downloadedimage = Image.open("output/{}/{}".format(c,filename)).convert('RGB')
    downloadedimage = downloadedimage.resize((newwidth, newheight), PIL.Image.ANTIALIAS)
    downloadedimage.save("output/{}/{}".format(c,filename))


os.chdir(proj_path)
from core.models import *
