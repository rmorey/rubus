import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

stop = "hilln"
route = "rexb"

url = "http://webservices.nextbus.com/service/publicXMLFeed" \
      "?a=rutgers&command=predictions&r="+route+"&s="+stop

root = ET.fromstring(requests.get(url).text)

for p in root[0][0]:
    t = datetime.now()+timedelta(seconds=int(p.get('seconds')))
    print(p.get('minutes')+" minutes at " + str(t.strftime("%I:%M:%S %p")))
