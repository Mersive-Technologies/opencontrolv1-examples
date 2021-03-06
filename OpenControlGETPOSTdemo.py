#Solstice API Demo Script
#This version changes the display name of your Pod using the /config api URL
#The "before" and "after" versions are printed to the console. 

#import necessary packages:
from __future__ import print_function
import sys
import requests
import random
from random import choice

#set value relationships required to properly read all the Boolean results:
true=1
false=0

#To change your pod name to a chosen value, uncomment the line below, comment out the random pod list lines below, and change "New Name" below to your desired name. 
#newname = "New Name"

#To set your pod name to a random name, leave the two following lines active:
namelist = ("Claude" , "Maude", "Todd", "Pernod", "Melrod", "Anthro")
newname = random.choice(namelist)+" the Pod"

#Say Hello
print("##########################################")
print("#  Solstice API Name Change Demo Script  #")
print("##########################################")
	
#Get the Solstice Device's URL.  For example, http://192.168.3.127 
#myurl = raw_input("Enter Target Device URL in http://xxx format: ")

#If you're testing this code against the same device over and over, enter the URL here, uncomment the line, and comment out the "input" line above.
myurl = "http://192.168.128.71"

#If you're supplying an Admin password, type it in here and uncomment the URLs that use passwords.  Otherwise, leave it blank as "" 
admin_password = ""

print("Target Device:", myurl)
print(".............")

#Create the two target URLs for the device
mystatsurl = myurl+'/api/stats'
myconfigurl = myurl+'/api/config'

#Create the two target URLs for the device with supplied admin password

#mystatsurl = myurl+'/api/stats?password='+admin_password
#myconfigurl = myurl+'/api/config?password='+admin_password

#GET the stats url
rs=requests.get(mystatsurl)

#GET the config url
rc=requests.get(myconfigurl)

#The GET returns a JSON object that we'll convert to a dictionary with the json() function from requests
rstats=rs.json()
rconfig=rc.json()

#m_displayName: current device display name from the /api/stats URL
#Returns string
print("Current Display Name from Stats:", rstats.get('m_displayInformation',{}).get('m_displayName'))

#m_displayName: current device display name from the /api/config URL 
#Returns string
print("Current Display Name from Config:", rconfig.get('m_displayInformation',{}).get('m_displayName'))
print(".............")

# Create a dictionary that contains the key value pairs to send to the server
new_config = {
    'password': admin_password,
    'm_displayInformation':
        {
            'm_displayName': newname
        }
}



#POST the new display name to the /api/config URL 
r=requests.post(myconfigurl, json=new_config)
print("Changing Name to: ",newname)
print(".............")
 
#Repeat the GET and formatting seen above
rs=requests.get(mystatsurl)
rc=requests.get(myconfigurl)
rstats=rs.json()
rconfig=rc.json()

#Display the new display name, as read from both /api/stats and /api/config
print("New Display Name from Stats:", rstats.get('m_displayInformation',{}).get('m_displayName'))
print("New Display Name from Config:", rconfig.get('m_displayInformation',{}).get('m_displayName'))
if (rstats.get('m_displayInformation',{}).get('m_displayName')==rconfig.get('m_displayInformation',{}).get('m_displayName') == newname):
    print("Name Change Success!")
else:
    print("Name Change Failure")
print(".............")

sys.exit(0)
