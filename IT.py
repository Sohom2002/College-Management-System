from pymongo import MongoClient
class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient("mongodb+srv://isoham:isoham@cluster0.4x3lf.mongodb.net/StudentDatabase?retryWrites=true&w=majority")

connection = Connect.get_connection()
db = connection.student

IT = []

Firstyr, opt, subj = [],0,["Computer","Maths","English"]
print("Student entry for 1st year IT\n")
while(opt!=-1):
    l = []
    roll = int(input("Enter Roll No : "))
    name = input("Enter name : ")
    l.append(roll)
    l.append(name)
    l.append(subj)
    Firstyr.append(l)
    opt = int(input("Enter 1 to continue -1 to exit : "))

print("Student entry for 2nd year IT\n")
Secondyr, opt, subj = [],0,["Computer","Maths","English"]
while(opt!=-1):
    l = []
    roll = int(input("Enter Roll No : "))
    name = input("Enter name : ")
    l.append(roll)
    l.append(name)
    l.append(subj)
    Secondyr.append(l)
    opt = int(input("Enter 1 to continue -1 to exit : "))

IT.append(Firstyr)
IT.append(Secondyr)

myDict = {}
myDict["Information Tech"] = IT

db.IT.insert_one(myDict)


#print(IT)
