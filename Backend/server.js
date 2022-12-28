// import necessary modules
const express = require("express");
const path = require("path");
const Datastore = require("nedb");
const bodyParser = require("body-parser");
const { MongoClient } = require("mongodb");

const uri =
  "mongodb+srv://zedDB:dAQZaszOuSSmsW0D@cluster0.dh0zyjw.mongodb.net/?retryWrites=true&w=majority";

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

const cors = require("cors");
const app = express();
app.use(cors());
const PORT = 3000;
app.use(bodyParser.json({ limit: "5mb" }));

const client = new MongoClient(uri);

/*****   Start MongoDB & NodeJS Server  *****/

async function startServers() {
  database = client.db("PotholesDB");
  potholesCollection = database.collection("potholesdb");
  console.log(database.databaseName, "is running ..");
  app.listen(PORT, () => console.log("Server is running on localhost:3000"));
}
startServers().catch(console.dir);

/*********   Getting Potholes positions    **********/

app.get("/", async (req, res) => {
  // res.status(200).sendFile(path.join(__dirname, "./../Frontend/map.html"));
  try {
    const data = await potholesCollection.findOne();
    res.status(200).send(data);
  } catch (error) {
    res.status(400).send("error : ", error);
  }
});

// POST

/*********   Adding Pothole    **********/
app.post("/addPosPothole", function (req, res) {
  var newPosPothole = req.body;
  console.log(newPosPothole);
  // Verify the validity of data

  if (newPosPothole.latitude != "" || newPosPothole.longitude != "") {
    addNewPosPothole(newPosPothole);
  }

  res.end();
});

/*********   Adding New Pothole position    **********/
function addNewPosPothole(posPothole) {
  const currentDate = new Date().valueOf();
  var posDocument = { date: currentDate, ...posPothole };
  potholesCollection.insertOne(posDocument);
}

/*********   Getting Last Pothole position    **********/
app.get("/getLastPosPothole", function (req, res) {});
