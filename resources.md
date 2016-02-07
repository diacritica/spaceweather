##Useful resources

### On Space Weather in general

http://sdo.gsfc.nasa.gov/mission/spaceweather.php


### On EIT/EUV filters

http://umbra.nascom.nasa.gov/newsite/images.html

There is an alternate source from the same team

http://sdowww.lmsal.com/suntoday/

Updates every 30 min.

We use this information to populate ImageChannel

Also interesting is: http://jsoc.stanford.edu/data/aia/images/

### On LASCO

http://sohowww.nascom.nasa.gov/data/REPROCESSING/Completed/

Updated every 12 minutes

### On HMI

http://jsoc.stanford.edu/data/hmi/images/2015/12/18/

We use continuum like this

http://jsoc.stanford.edu/data/hmi/images/2015/12/18/20151218_000000_Ic_512.jpg

Update every 15 min

### On Sunspot Regions

A url such as this

http://www.spaceweather.com/images2015/18dec15/sunspot_labels.txt

will give us all the relevant info.

Also interesting: http://www.spaceweatherlive.com/en/solar-activity/sunspot-regions
http://www.spaceweatherlive.com/en/help/the-classification-of-sunspots-after-malde

Updated every 24h

### On Solarcycle

Past observed and smoothed values

http://legacy-www.swpc.noaa.gov/ftpdir/weekly/RecentIndices.txt

Predicted values

http://legacy-www.swpc.noaa.gov/ftpdir/weekly/Predict.txt

Updated every month

### On GOES data (particles, electrons, x-ray)

Particules (5min)

http://legacy-www.swpc.noaa.gov/ftpdir/lists/particle/Gp_part_5m.txt

Updated every 5 min. Contains last 2h

Electrons (5min)

http://legacy-www.swpc.noaa.gov/ftpdir/lists/particle/Gp_part_5m.txt

Updated every 5 min. Contains last 2h

X-ray (5min)

"http://legacy-www.swpc.noaa.gov/ftpdir/lists/xray/%s_Gp_xr_5m.txt"%(today.strftime("%Y%m%d"))

Updated every 5 min

###On Solar wind (plasma)

http://services.swpc.noaa.gov/experimental/products/solar-wind/plasma-7-day.json

updated every minute. We resample it to every 10 min.

Also, useful for a "visual"

http://www.solarmonitor.org/ace_pop.php?date=20151216&type=aceplasma

Great for the future

http://www.swpc.noaa.gov/products/wsa-enlil-solar-wind-prediction

### On Alerts

http://legacy-www.swpc.noaa.gov/alerts/archive/current_month.html

http://services.swpc.noaa.gov/products/alerts.json

Updated every month

### On 3-day forecastrationale

http://services.swpc.noaa.gov/text/3-day-forecast.txt

Upated twice every day

### Other useful resources

http://www.srl.caltech.edu/ACE/

jsoc.stanford.edu/cgi-bin/hmiimage.pl?Year=2010&Month=05&Day=01&Hour=00&Minute=00&Kind=_Ic_flat_&resolution=1k

http://sdowww.lmsal.com/sdomedia/SunInTime/webgl_tool/sv3/?date=20151213

http://www.solarmonitor.org/

http://umbra.nascom.nasa.gov/images/

ffmpeg -framerate 30 -pattern_type glob -i '304-1*.jpg' -c:v libx264 out.mp4
