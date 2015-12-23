import os
import time, datetime

import PIL
from PIL import Image

newwidth = 512
newheight = 512
quality_val = 70

now = datetime.datetime.utcnow().isoformat()
channels = ['171','193','211','304']

for c in channels:
    filename = "{}-{}.jpg".format(c,now)
    os.system("wget http://umbra.nascom.nasa.gov/images/latest_aia_{}.gif -O {}".format(c,filename))
    time.sleep(1)
    downloadedimage = Image.open(filename).convert('RGB')
    downloadedimage = downloadedimage.resize((newwidth, newheight), PIL.Image.ANTIALIAS)
    downloadedimage.save(filename)
