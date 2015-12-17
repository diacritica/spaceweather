http://sdo.gsfc.nasa.gov/mission/spaceweather.php

Solarwind (plasma) http://www.solarmonitor.org/ace_pop.php?date=20151216&type=aceplasma

http://www.swpc.noaa.gov/products/wsa-enlil-solar-wind-prediction

http://www.spaceweatherlive.com/en/help/the-classification-of-sunspots-after-malde
http://www.spaceweatherlive.com/en/solar-activity/sunspot-regions
http://www.dartmouth.edu/~physics/labs/descriptions/solar.observing/solar2015.writeup.pdf
http://www.spaceweather.com/images2015/08dec15/sunspot_labels.txt
http://www.spaceweather.com/
https://www.ngdc.noaa.gov/stp/iono/sunspot.html
http://www.sws.bom.gov.au/Solar/1/6
http://sunspotwatch.com/
http://www.srl.caltech.edu/ACE/

http://jsoc.stanford.edu/data/hmi/images/latest/

EIT, LASCO

EIT images are taken twice a day while LASCO/SDO are taken much more frequently

LASCO images are taken every 12 minutes
SDO images are taken every 30 minutes

jsoc.stanford.edu/cgi-bin/hmiimage.pl?Year=2010&Month=05&Day=01&Hour=00&Minute=00&Kind=_Ic_flat_&resolution=1k

http://sdowww.lmsal.com/sdomedia/SunInTime/webgl_tool/sv3/?date=20151213

http://www.solarmonitor.org/

http://umbra.nascom.nasa.gov/images/

from django.core.files import File

ct=Channeltype.objects.all()[3]
>>> ic.image.save('0.gif',File(open('/home/diacritica/0.gif','rb')))
>>> ic.save()
>>> ic=Imagechannel(date="2015-12-15 00:10", channeltype=ct, originaldate="2015-12-15 00:07", bogus=False,)
>>> ic.image.save('0.gif',File(open('/home/diacritica/0.gif','rb')))
>>> ic.image.save('0.gif',File(open('/home/diacritica/0.gif','rb')))
>>> ic.save()
>>> ic=Imagechannel(date="2015-12-15 00:10", channeltype=ct, originaldate="2015-12-15 00:07", bogus=False,)
>>> ic.image.save('0.gif',File(open('/home/diacritica/0.gif','rb')))


ffmpeg -framerate 30 -pattern_type glob -i '304-1*.jpg' -c:v libx264 out.mp4
