import requests
import xml.etree.ElementTree as ET

url = "http://webservices.nextbus.com/service/publicXMLFeed" \
      "?a=rutgers&command=predictions&r=rexb&s=hilln"

nbstring = requests.get(url).text
root = ET.fromstring(nbstring)

for p in root[0][0]:
    print(p.get('minutes'))
