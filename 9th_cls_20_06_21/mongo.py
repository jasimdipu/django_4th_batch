import pymongo

mydb = pymongo.MongoClient("mongodb://localhost:27017")

db = mydb['mydatabase']
print(mydb)

