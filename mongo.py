from pymongo import MongoClient
class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient("mongodb+srv://isoham:isoham@cluster0.4x3lf.mongodb.net/StudentDatabase?retryWrites=true&w=majority")

connection = Connect.get_connection()
db = connection.test
db = connection.student
db.inventory.insert_one(
    {"item": ["canvas"],
     "qty": 100,
     "tags": ["cotton"],
     "size": {"h": 28, "w": 35.5, "uom": "cm"}})

# dict = {"CSE":[[1,"SS",["A","B","C"]],[2,"SD",["A","B","C"]]]}