import serial
import time
import string
import pynmea2

try:
    port = "/dev/serial0"
    ser = serial.Serial(port, baudrate=9600, timeout=1)
except Exception as e:
    print(e)
    exit(0)

def getPosition():
    data = ser.readline() 
    newdata = data.decode('utf-8')
    
    if newdata[0:6] == "$GNGLL":
        try:
            msg = pynmea2.parse(newdata)
            lat = msg.latitude
            lng = msg.longitude
        except:
            lat = 0
            lng = 0
        
        gps = {"lat": int(lat),"lng": int(lng)}
        
        if (gps['lat'] == 0 and gps['lng'] == 0):
            return None
        else:
            #print("gps : ", gps)
            return gps


