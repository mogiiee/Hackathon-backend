from . import exporter
import pymongo


#stores all sorts of database information

cluster = pymongo.MongoClient(exporter.realcluster)

db = cluster[exporter.db_name]

user_collection = db[exporter.collection]

hackathon_collection = db[exporter.hackathon_collection]

submission_collection = db[exporter.submission_collection]

firebaseConfig = {
    "apiKey": exporter.firebaseApiKey,
    "authDomain": "ai-planet.firebaseapp.com",
    "projectId": "ai-planet",
    "storageBucket": "ai-planet.appspot.com",
    "messagingSenderId": "53765739711",
    "appId": exporter.firebaseAppID,
    "measurementId": "G-KZXF5H2WN7",
    "databaseURL": "https://ai-planet-default-rtdb.firebaseio.com/",
    "serviceAccount": "ai-planet-firebase-adminsdk-g7a8x-65b9193f00.json",
    "databaseURL": exporter.databaseURL,
}
