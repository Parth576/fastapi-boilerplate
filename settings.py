import os
from os.path import join, dirname
from dotenv import load_dotenv
import pymongo
import urllib

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

dbUsername = os.environ.get("DBUSERNAME")
dbPassword = os.environ.get("DBPASSWORD")

mongodb_uri = "mongodb+srv://"+ urllib.parse.quote_plus(dbUsername) + ":" + urllib.parse.quote_plus(dbPassword) + "@cluster0.1ufkz.mongodb.net/proctoring?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongodb_uri)
