import gps
#import libraries
import gps
import requests

# Global Variables
server_link = 'https://amsa.glitch.me/addPothole'
server_data = {}

while(1):
    # Wait Pothole to be detected
    waitDetectedPothle()

    # Get GPS Position
    pos = gps.getPosition()
    server_data = {"Lat": pos["lat"] , "Lng": pos["lng"]}
    print(server_data)

    # Send Request to Server
    #resp = requests.post(server, json = server_data)
