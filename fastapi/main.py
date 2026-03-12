from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int

students = {}

@app.post("/students")
def create_student(student: Student):
    students[student.id] = student
    return {"message": "Student added"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students.get(student_id)

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    students[student_id] = student
    return {"message": "Student updated"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    students.pop(student_id)
    return {"message": "Student deleted"}