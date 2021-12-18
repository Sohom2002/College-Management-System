from pymongo import MongoClient
class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient("mongodb+srv://isoham:isoham@cluster0.4x3lf.mongodb.net/FacultyDatabase?retryWrites=true&w=majority")

connection = Connect.get_connection()
db = connection.Faculty

Faculty,myDict= [],{}

Maths, opt1 = [],0
print("Faculty of Maths Dept")
while(opt1!=-1):
    l1= []
    emp_id = int(input("Enter employee id : "))
    name = input("Enter name : ")
    l1.append(emp_id)
    l1.append(name)
    dept = input("Enter Depts : ")
    dept = dept.split()
    l1.append(dept)
    Maths.append(l1)
    opt1 = int(input("Enter 1 to continue -1 to exit : "))

myDict["Maths"] = Maths

Computer, opt1 = [],0
print("Faculty of Computer Dept")
while(opt1!=-1):
    l1= []
    emp_id = int(input("Enter employee id : "))
    name = input("Enter name : ")
    l1.append(emp_id)
    l1.append(name)
    dept = input("Enter Depts : ")
    dept = dept.split()
    l1.append(dept)
    Computer.append(l1)
    opt1 = int(input("Enter 1 to continue -1 to exit : "))

myDict["Comp"] = Computer

English, opt1 = [],0
print("Faculty of English Dept")
while(opt1!=-1):
    l1= []
    emp_id = int(input("Enter employee id : "))
    name = input("Enter name : ")
    l1.append(emp_id)
    l1.append(name)
    dept = input("Enter Depts : ")
    dept = dept.split()
    l1.append(dept)
    English.append(l1)
    opt1 = int(input("Enter 1 to continue -1 to exit : "))

myDict["English"] = English

Faculty.append(myDict)
last = {}
last["Faculty"] = Faculty

db.Teachers.insert_one(myDict)

#print(Faculty)
