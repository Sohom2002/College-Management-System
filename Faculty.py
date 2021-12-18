Faculty = []

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

Faculty.append(Maths)
Faculty.append(Computer)
Faculty.append(English)