import pymongo
from  FnCreateUser import CreateUser


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ApiDataBase"]
#mycol = mydb["Users"]

#mydict = { "name": "John", "Age": "33", "address": "Highway 37" }

#x = mycol.insert_one("Users")

#print(myclient.list_database_names())

CreateUser()