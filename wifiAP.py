## import library ##
import json
from config import APIKEY, SCANFILE
from zipfile import ZipFile 
from geolocator import Geolocator


## 
def main():
    print("Starting the WIFI access point based geolocator")
    print("Locating current location")
    
    # If the input file is a zip file
    if SCANFILE.endswith('.zip'):
    	with ZipFile(SCANFILE, 'r') as zipf:
    		for filenames in zipf.namelist():
    			with zipf.open(filenames) as z:
    			    data1 = z.read()
    			    fileContent = json.loads(data1.decode("utf-8"))
    
    # If the input file is a json file	
    elif SCANFILE.endswith('.json'):
    	with open(SCANFILE) as jf:
        	fileContent = json.loads(jf.read())	

    # Calling Geolocation class from geolocator file
    geolocator = Geolocator(APIKEY, fileContent)
    
    # Print output simultaneously using yield statement
    wifi_access_points = geolocator.locateAP()
    for wifi_access_point in wifi_access_points:
    	print(wifi_access_point, sep= '\n')    
    
    # Alternate approach:
    # Printing the output from list 
    # Uncomment line 37 and line 38 and comment out line 31 and line 32 to unable this
    # wifi_access_point = geolocator.locate()
    # print(*wifi_access_point, sep = '\n')
        
if __name__ == "__main__":
    main()