#import libraries
import gps
import detection
import requests


# Global Variables
server_link = 'https://amsa.glitch.me/addPothole'
server_data = {}

def start():    
    while(1):
        # Wait Pothole to be detected
        detection.waitDetectedPothle()

        # Get GPS Position
        pos = gps.getPosition()
 
        if pos is not None :
            server_data = {"Lat": pos["lat"] , "Lng": pos["lng"]}
            resp = requests.post(server_link, json = server_data)
            print(resp)
        else :
            print("Can't Get GPS Position: indoor buildings")
    
    