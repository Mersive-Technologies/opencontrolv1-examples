#Solstice API Demo Script!
#This script pulls the current screen key for a known IP address so an admin can use browser look-in remotely
#This script prints formatted results to console.

#import necessary packages:
from __future__ import print_function
import sys
from sys import version
import time
import datetime
import requests

#set value relationships required to properly read all the Boolean results:
true=1
false=0


#Enter target device URL
myurl = "http://192.168.128.50"

print("Target Device:", myurl)
myconfigurl = myurl+'/api/config'

#Create the two target URLs for the device with supplied admin password (change the password to the real value)
#admin_password = "Pa$$w0rd"
#mystatsurl = myurl+'/api/stats?password='+admin_password
#myconfigurl = myurl+'/api/config?password='+admin_password

rc=requests.get(myconfigurl)

#The GET returns a string that we want to use as a dictionary of key:value pairs, so convert results using eval()

rconfig=eval(rc.text)


#sessionKey: shows current 4-character key needed to access host
#Returns string of 4 characters
print("Screen Key:", rconfig.get('m_authenticationCuration',{}).get('sessionKey'))


#Shut it down (on your own terms, if running the program directly) 
end = input("Press any key to exit")


