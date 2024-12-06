from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))
username = os.getenv('MONGO_USER') 
password = os.getenv('MONGO_PASS')
host = os.getenv('MONGO_HOST')
query_param = 'ssl=false'
port = os.getenv('MONGO_PORT')
uri = f"mongodb://{username}:{password}@{host}:{port}/?{query_param}"
dbname = 'realthon'
client = MongoClient(uri)[dbname]
client.command('ping')