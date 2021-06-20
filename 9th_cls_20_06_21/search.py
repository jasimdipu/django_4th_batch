import pymongo

mydb = pymongo.MongoClient("mongodb://localhost:27017")

db = mydb['mydatabase']

usercol = db['users']

jahid = usercol.find_one({'name': "Jahid Hasan"})

print(jahid)

mydb.close()
