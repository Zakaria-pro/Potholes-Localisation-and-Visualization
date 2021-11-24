#import libraries
import gps
import requests

# Global Variables
server_link = 'https://amsa.glitch.me/addPothole'
server_data = {}

def start():    
    while(1):
        # Wait Pothole to be detected
        #waitDetectedPothle()

        # Get GPS Position
        pos = gps.getPosition()
        #print(type(pos))
        print(pos)
        if pos is not None :
            server_data = {"Lat": pos["lat"] , "Lng": pos["lng"]}
            print("server data : ", server_data)
            # Send Request to Server
            resp = requests.post(server_link, json = server_data)
        else :
            print("i cant work indoor buildings")
    
    