import urllib2
import json
import sys
import csv

#take arguments from command line
if __name__ == '__main__':    
	if len(sys.argv) != 4 :
		sys.exit("This script takes exactly 3 arguments, no more, no less.")
	url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + str(sys.argv[1]) + '&OperatorRef=MTA+NYCT&LineRef='+str(sys.argv[2])
	
	#handling the http get request
	response = urllib2.urlopen(url)
	data = response.read()
	json_data = json.loads(data)

	#digging into json
	buses = json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']


	with open(sys.argv[3], 'wb') as f:
	        csvwriter = csv.writer(f)

	        # Add the header
	        csvwriter.writerow(["Latitude", "Longitude", "Stop Name", "Stop Status"])

	        for bus in buses:
	            bus = bus['MonitoredVehicleJourney']

	            # Handle N/A's
	            data_present = bus['OnwardCalls']['OnwardCall'][0] if len(bus['OnwardCalls']) else None

	            #Output
	            csvwriter.writerow([
	                bus['VehicleLocation']['Latitude'],
	                bus['VehicleLocation']['Longitude'],
	                data_present['StopPointName'] if data_present else "N/A",
	                data_present['Extensions']['Distances']['PresentableDistance'] if data_present else "N/A"
	            ])