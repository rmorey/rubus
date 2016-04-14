import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

AGENCY = 'rutgers'
API_URL = "http://webservices.nextbus.com/service/publicXMLFeed?a="+AGENCY+"&command={c}"

def get_predictions(route,stop):
    url = API_URL.format(c="predictions") + "&r={}&s={}".format(route,stop)
    root = ET.fromstring(requests.get(url).text)
    for p in root[0][0]:
        t = datetime.now()+timedelta(seconds=int(p.get('seconds')))
        print(p.get('minutes')+" minutes at " + str(t.strftime("%I:%M %p")))

def list_routes():
    url = API_URL.format(c="routeList")
    root = ET.fromstring(requests.get(url).text)
    print root
