from __future__ import print_function
import pylab as pl
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

pl.rc('font', size=15)

#MTA_KEY = "d3ccd72f-edb3-433f-8935-1ec3de863290"

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='\
+sys.argv[1]+'&VehicleMonitoringDetailLevel=calls&LineRef='+sys.argv[2]

#url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTAAPIKEY + \
#"VehicleMonitoringDetailLevel=calls&LineRef=B52"
#print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
busx=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
busx

counter = 0 
#import pprint //##see structure of the tuple
for i in busx:
    counter+=1
    print('Bus', str(counter), 'is at latitude:',i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],\
          'Longitude',i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])