import pymongo;

url = 'mongodb://localhost:27028'
client = pymongo.MongoClient(url)

db = client['proyecto']

