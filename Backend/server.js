// import necessary modules
const express = require("express");
const path = require("path");
const Datastore = require("nedb");
const bodyParser = require("body-parser");

/*********   Global variables   **********/

const db = new Datastore({
  filename: "./potholeCoordinates.db",
  autoload: true,
  corruptAlertThreshold: 1,
});

const lastDataDB = new Datastore({
  filename: "./lastCoordinates.db",
  autoload: true,
  corruptAlertThreshold: 1,
});

var lastPosPothole = { latitude: "", longitude: "", image: "" };

/*********   Start server   **********/

const app = express();
const PORT = 3000;
app.use(bodyParser.json({ limit: "5mb" }));
app.listen(PORT, () => console.log("Server is running!!"));

/*********   Serving HTML page to client    **********/

app.get("/", function (req, res) {
  res.status(200).sendFile(path.join(__dirname, "map.html"));
});

// POST

/*********   Adding Pothole    **********/
app.post("/addPosPothole", function (req, res) {
  var newPosPothole = req.body;
  //console.log(newPosPothole.latitude)
  console.log("pos added");
  // Verify the validity of data
  if (
    "latitude" in newPosPothole &&
    "longitude" in newPosPothole &&
    "image" in newPosPothole
  ) {
    if (newPosPothole.latitude != "" || newPosPothole.longitude != "") {
      // insert data to database
      addNewPosPothole(newPosPothole);
    }
  }
  res.end();
});

/*********   Adding New Pothole position    **********/
function addNewPosPothole(posPothole) {
  const currentDate = new Date().valueOf();
  var insertedData = { date: currentDate, ...posPothole };

  // if data contain image, it will be added to requests with images
  if (posPothole.image !== "") {
    console.log("insertion with image");

    db.insert(insertedData, function (err, doc) {
      if (err) throw err;
    });
  }

  console.log("inserted", insertedData.latitude, insertedData.longitude);

  // add received data, after erasing the whole database
  lastDataDB.remove({}, { multi: true }, function (err, numDeleted) {
    lastDataDB.loadDatabase(function (err) {});
  });

  lastDataDB.insert(insertedData, function (err, doc) {
    //console.log(insertedData)
    if (err) throw err;
  });
}

// GET

/*********   Getting Last Pothole position    **********/
app.get("/getLastPosPothole", function (req, res) {
  lastDataDB
    .find({})
    .sort({ date: -1 })
    .limit(1)
    .exec((err, results) => {
      if (err) console.log(err);

      if (results[0] != undefined) {
        /*if (
        lastPosPothole.latitude != results[0].latitude ||
        lastPosPothole.longitude != results[0].longitude
      ) {*/
        //console.log(lastPosPothole.latitude, lastPosPothole.longitude);
        lastPosPothole = results[0];

        console.log(
          "requested",
          lastPosPothole.latitude,
          lastPosPothole.longitude
        );

        res.json(lastPosPothole);

        return;
        //}
      }

      res.json({});
    });
});

/*********   Getting Potholes positions    **********/
app.get("/getInit", function (req, res) {
  //res.json(lastPosPothole);

  db.find({}, function (err, results) {
    if (err) console.log(err);
    console.log(results);
    res.json(results);
  });
});
