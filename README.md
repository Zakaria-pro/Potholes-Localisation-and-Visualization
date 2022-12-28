# SafeRoad

an IoT Systems that allows localisation and visualization of potholes to monitor the quality of roads.

![Web Application](./assets/amsa6-pothole-detection.jpg)

# IoT System Architecture

![IoT System Architecture](./assets/iot-app-architecture.jpg)
we can break the system into 5 componenets :

## Data Generation

- Smart things: Raspberry Pi 4 + Camera + GPS + Huawei 4G Dongle (E3372h-153)
- **pynmea2** library used for parsing GPS data
- **requests** library used to send post request to the server

## Server

- NodeJS ExpressJS
- Mongodb
- 🚧 Change Streams (Web Sockets) 


## Data Map Ploting

- Fetch API
- Leaflet
- 🚧 WebSocket to have a realtime communication with the server (each time a new pothole is sent to the backend)

# Demonstration Video

## [Demo Video](https://drive.google.com/file/d/1cuEcpcOaUutxG1opQEddCqUB-Nxv5CWZ/view?usp=sharing)

# Used Technologies

### hardware :

- Raspberry pi 4
- Modem 4G Orange (huawei E3372h-153)
- Camera PI
- GPS b220
- PowerBank

### software :

- Python
- NodeJS
- Mongodb
- Leaflet
- 🚧 Socket.io
