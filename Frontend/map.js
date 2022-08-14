const apiKey =
  "pk.eyJ1IjoiYmVuZXR0YWxlYiIsImEiOiJja2w3NWV1dnMyZXp4MnZsYjB1ZW9qcDVjIn0.fSUhZIwlPmxnd95ioh7e-Q";

// Map Creation
const map = L.map("map").setView([40.770116, -73.967909], 13);

L.tileLayer(
  "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
  {
    maxZoom: 18,
    id: "mapbox/streets-v11",
    tileSize: 512,
    zoomOffset: -1,
    accessToken: apiKey,
  }
).addTo(map);

var orangeIcon = new L.Icon({
  iconUrl:
    "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-orange.png",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

const marker = L.marker([0, 0], [0.001, 0.0001]).addTo(map);

/*********   First Initialisation get All saved data   **********/

/*async function getInit() {
const response = await fetch("/getInit");
if (response) {
  try {
    const data = await response.json();

    if ("latitude" in data && "longitude" in data && "image" in data) {
      const latitude = data.latitude;
      const longitude = data.longitude;

      const image = new Image();
      image.src = "data:image/png;base64," + data.image;

      let template =
        `
            <h3>Pothole Image</h3>
            <div style="text-align:center">
                <img id = "myImg" width="150" height="150" src="` +
        image.src +
        `"/>
            </div>
            `;

      marker.bindPopup(template);

      marker.setLatLng([latitude, longitude]);
      map.setView([latitude, longitude], 16);
    }
  } catch (error) {
    console.log(error);
  }
}
}

getInit();*/

/*********   Requesting last position   **********/

// variable to store last valid response
var lastPos = { latitude: "", longitude: "" };

// set the location of the marker to the new valid position obtained
async function getCurrLoc() {
  const response = await fetch("/getLastPosPothole");
  if (response) {
    try {
      const data = await response.json();

      if ("latitude" in data && "longitude" in data && "image" in data) {
        const latitude = data.longitude;
        const longitude = data.latitude;

        if (
          lastPos.latitude !== data.latitude ||
          lastPos.longitude !== data.longitude
        ) {
          console.log("New Coordinates Received");

          lastPos = data;

          //  Set just GPS Position if no image received
          if (data.image === "") {
            console.log("gps data without image:", latitude, longitude);
            marker.setLatLng([latitude, longitude]);
            map.setView([latitude, longitude], 20);
          }

          // Create new marker for data containing image
          else {
            const image = new Image();
            image.src = "data:image/png;base64," + data.image;

            let template =
              `
            <h3>Pothole Image</h3>
            <div style="text-align:center">
                <img id = "myImg" width="150" height="150" src="` +
              image.src +
              `"/>
            </div>
            `;

            const newMarker = new L.Marker([latitude, longitude], {
              icon: orangeIcon,
            }).addTo(map);
            newMarker.bindPopup(template);
            //map.setView([latitude, longitude], 12);
          }
        }
      }
    } catch (error) {
      console.log(error);
    }
  }
}
setInterval(getCurrLoc, 2000);
