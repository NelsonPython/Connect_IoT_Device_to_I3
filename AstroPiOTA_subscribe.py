﻿
#!/usr/bin/python

"""
Purpose:  subscribing to AstroPiOTA Weather Station data from I3 Consortium Data Marketplace at http://eclipse.usc.edu:8000
"""

import paho.mqtt.client as mqtt
import time
import json

def on_connect(client, userdata, flags, rc):
    """ reporting IoT device connection """

    try:
        m = "Connected flags " + str(flags) + "\nResult code " + str(rc) + "\nClient_id  " + str(client)
        print(m)
        print("\n")
    except e:
        print("Hmmm I couldn't report the IoT connection: ", e)


def on_message(client, userdata, msg):
    """ receiving data"""

    try:
        sensors = msg.payload
        sensors = json.loads(sensors.decode('utf-8'))
    except e:
        print("Check the message: ",e)

    # this format stores data in CSV format in AstroPiOTA.log
    print(str(sensors["timestamp"]),",",str(sensors["device_name"]),\
        str(sensors["device_owner"]),",",str(sensors["city"]),",",str(sensors["lng"]),\
        str(sensors["lat"]),",",str(sensors["temperature"]),",",str(sensors["humidity"]),\
        str(sensors["pressure"]),",",str(sensors["pitch"]),",",str(sensors["roll"]),\
        str(sensors["yaw"]),",",str(sensors["x"]),",",str(sensors["y"]),",",str(sensors["z"]),file=logfile)

    # this prints the AstroPiOTA data message
    print("\nTimestamp: ", str(sensors["timestamp"]))
    print("Device: ", sensors["device_name"])
    print("Device owner email: ", sensors["device_owner"])
    print("Device location: ", sensors["city"], " at longitude: ", sensors["lng"], " and latitude: ", sensors["lat"])

    print("Temperature: ", sensors["temperature"])
    print("Humidity: ", sensors["humidity"])
    print("Pressure: ", sensors["pressure"])

    print("Pitch: ", sensors["pitch"])
    print("Roll: ", sensors["roll"])
    print("Yaw: ", sensors["yaw"])

    print("Accelerometer x: ", sensors["x"])
    print("Accelerometer y: ", sensors["y"])
    print("Accelerometer z: ", sensors["z"])

def test_sub():
    '''
    Broker address: 18.217.227.236 (​ ec2-18-217-227-236.us-east-2.compute.amazonaws.com)
    Broker port: 1883
    account/pw:  username/password that you obtain from the marketplace
    topic: the name of the product that you purchased from the marketplace
    '''

    topic = "AstroPiOTA Weather Station"
    account = 'YourAccount'
    pw = 'yourpassword'

    sub_client = mqtt.Client(account)
    sub_client.on_connect = on_connect
    sub_client.on_message = on_message
    sub_client.username_pw_set(account, pw)
    sub_client.connect('18.217.227.236', 1883, 60) #connect to broker
    sub_client.subscribe(topic)

    # get data while the return code is zero
    rc = 0
    while rc == 0:
        rc = sub_client.loop()
        time.sleep(1)

if __name__ == '__main__':
    # subscribing to AstroPiOTA data
    global logfile
    logfile = open("AstroPiOTA.log", "a")
    try:
        test_sub()
    except KeyboardInterrupt:
        logfile.close()
        print("\nI'm stopping now")
