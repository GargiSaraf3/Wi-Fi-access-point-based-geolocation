import json
from config import CONSIDERIP

import requests

class Geolocator:
	def __init__(self, api_key, accessPoints):
		self.api_key = api_key
		self.accessPoints = accessPoints
		self.listOfLoc = []
		
		
	def locateAP(self):
		"""
	    	Task performed in this function:
	    	1. Calling _extractor function to modify and create payload for all the apscans.
	    	2. Create URL using the API_KEY provided
	    	3. Create POST APIs for all the individual apscans
	    	2. For all the individual apscan it returns the output simultaneously
	    	
		"""
		
		for accessPoint in self.accessPoints:
			payload = self._extractor(accessPoint)
			headers = {"content-Type": "application/json"}
			url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + str(self.api_key)
		
			# Create POST API
			response1 = requests.post(url, headers= headers, data= json.dumps(payload))
			
			
			# To print the result simultaneously on the screen use yield
			yield response1.text
			
			
			# Alternate approach:
			# Adding the response of individual API to a list and returning the list
			# Uncomment line 39 and 40 and comment out line 33 to unable this
 			# self.listOfLoc.append(response1.text)
		# return self.listOfLoc
		
	
	
	def _extractor(self, accessPoint):
	    """ 
	    Task performed in this function:
	    1. Modify the payload for each apscan to represent the payload specified in document: 
	       https://developers.google.com/maps/documentation/geolocation/overview
	    1. Create payload for all the scans which belongs to a apscan
	    """
	    
	    # Structure for WiFi access point object
	    payload = {
	    	"considerIp": CONSIDERIP,
	    	"wifiAccessPoints": []
	    }
	    
	    # Parsing and adding individual scans in main apscan
	    for ap in accessPoint['apscan_data']:
	        wifiAP = {
	            "macAddress": ap["bssid"],
	            "signalStrength": ap["rssi"],
	            "channel": ap["channel"]
	        }
	        payload["wifiAccessPoints"].append(wifiAP)
	    return payload