import pymongo

mydb = pymongo.MongoClient("mongodb://localhost:27017")

db = mydb['mydatabase']

usercol = db['users']

user_list = db.list_collection_names()

data = {"name": "Saklain Hasan", "address": "Comilla"}
data2 = {"name": "Sakib Hasan", "address": "Khulna"}
data3 = {"name": "Tamim Hasan", "address": "Chitagong"}
data4 = {"name": "Tasin oskar", "address": "Dhaka"}
data5 = {"sec name": "another Tasin oskar", "address": "Dhaka"}

# x = usercol.insert_one(data5)

# print(x)

if "users" in user_list:
    for user in usercol.find():
        print(user)
else:
    print("NO users found")
