
#****************************************************
# Import Package
#****************************************************

import sys
import socket
import time
import http.client, urllib.parse
sys.path.append('/home/pi/rpi/code/Package')

#****************************************************
# Set ThingSpeak Key
#****************************************************

thingSpeakApiKey = "ANE05QHZMPE9TBDI"

#****************************************************
# Set ThingSpeak Connection
#****************************************************

def post_to_thingspeak(payload):
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    not_connected = 1
    while (not_connected):
        try:
            conn = http.client.HTTPConnection("api.thingspeak.com:80")
            conn.connect()
            not_connected = 0
        except (http.client.HTTPException, socket.error) as ex:
            print("Error: %s" %(ex))
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/update", payload, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

#****************************************************
# Post ThingSpeak
#****************************************************

def main():

    Depth = 0.3

    #****************************************************
    # upload spm result to cloud
    #****************************************************

    print("depth = %.02f cm"%(Depth))
    params = urllib.parse.urlencode({'field1': Depth, 'key': thingSpeakApiKey})
    post_to_thingspeak(params)

if __name__ == '__main__':
    main()
