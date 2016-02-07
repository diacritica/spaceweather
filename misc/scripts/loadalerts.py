
import json
import os, sys
import django

def getFieldsFromAlert(jsonalert):

    SWMC = jsonalert["message"].split("\n")[0].split(":")[1].strip()
    serialnumber = int(jsonalert["message"].split("\n")[1].split(":")[1].strip())
    alerttype = jsonalert["message"].split("\n")[4].split(":")[0].strip()
    message = jsonalert["message"].split("\n")[4].split(":")[1].strip()
    payload = "".join(jsonalert["message"].split("\n")[5:])

    return SWMC,serialnumber,alerttype,message,payload

os.system("wget http://services.swpc.noaa.gov/products/alerts.json -O output/alerts.json")
myfile = open("output/alerts.json","r")
j=json.load(myfile)

proj_path = "/home/elfo/GIT/spaceweather/src/spaceweather/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spaceweather.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

from core.models import *

for i in j:
    try:
        Alert.objects.get(issuetime=i["issue_datetime"])
        print("Data for {} already there!".format(i["issue_datetime"]))
    except:

        SWMC, serialnumber, alerttype, message, payload = getFieldsFromAlert(i)
        alerttypeid = Alerttype.objects.get(name=alerttype)

        alert = Alert(issuetime=i["issue_datetime"],SWMC=SWMC, serialnumber=serialnumber, alerttype=alerttypeid, message=message, payload=payload)
        print("Data for {} inserted!".format(i["issue_datetime"]))
        alert.save()
