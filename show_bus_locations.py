

import urllib2
import json
import sys

#take arguments from c.l.
if __name__ == '__main__': 
	if len(sys.argv) != 3 :
		sys.exit("This script takes exactly 2 arguments, no more, no less.")  

	url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + str(sys.argv[1]) + '&OperatorRef=MTA+NYCT&LineRef='+str(sys.argv[2])
	
	#handling the http get request
	response = urllib2.urlopen(url)
	data = response.read()
	json_data = json.loads(data)

	#digging into json
	buses = json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

	#iterate over buses
	x=0
	d={}
	for bus in buses:
	    d[x]= bus['MonitoredVehicleJourney']['VehicleLocation']
	    x+=1

	#output
	print "Bus Line: " + str(sys.argv[2])
	print "Number of Active Buses : %s" %x
	for i in range(0,x):
	    print "Bus",i,"is at latitude",d[i]['Latitude'], "and longitude",d[i]['Longitude']