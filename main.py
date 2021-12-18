from typing import List, Optional

from fastapi import FastAPI

from pymongo import MongoClient

app = FastAPI()

class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient("mongodb+srv://isoham:isoham@cluster0.4x3lf.mongodb.net/StudentDatabase?retryWrites=true&w=majority")

connection = Connect.get_connection()
student = connection.student

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

"""CSE Student Input"""
@app.post("/student/cse/{stud_id}")
def post_item(stud_id: int, name: str , sub: str):
    student.CSE.insert_one(
    {"Student_id": stud_id,
     "Name": name,
     "Subject_Comb": sub.split()})
    return 201

"""IT Student Input"""
@app.post("/student/it/{stud_id}")
def post_item(stud_id: int, name: str , sub: str):
    student.IT.insert_one(
    {"Student_id": stud_id,
     "Name": name,
     "Subject_Comb": sub.split()})
    return 201

"""Faculty Input"""
@app.post("/faculty/teachers/{stud_id}")
def post_item(emp_id: int, name: str , dept_in_charge: str):
    student.IT.insert_one(
    {"Employee_id": emp_id,
     "Name": name,
     "Teaching Depts": dept_in_charge.split()})
    return 201

#uvicorn main:app --reload
#http://127.0.0.1:8000/docs#/