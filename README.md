This service accepts Wi-Fi access points and return latitude, longitude 
and accuracy of the location at which the AP scan was performed.

This service accepts a json file or a zip file as input, creates REST API and
displays the output for a single batch of AP scan result simultaneously.
Alternatively the script can also be modified to return a list of all the AP scans. 

REQUIREMENTS:

To run the script successfully install the following libraries:
1. json library
2. requests library
3. zipfile library


RUNING THE SERVICE:

1. Modify the config.py file to specify the location of input file (SCANFILE)
2. Provide/Modify the APIKEY in config.py file
3. Run wifiAP.py using command:
      python wifiAPI.py