from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_students(request: Request):
    db: Session = SessionLocal()
    students = db.query(models.Student).all()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "students": students}
    )


@app.post("/add")
def add_student(name: str = Form(...), age: int = Form(...)):
    db: Session = SessionLocal()

    student = models.Student(name=name, age=age)

    db.add(student)
    db.commit()

    return RedirectResponse(url="/", status_code=303)


@app.get("/delete/{student_id}")
def delete_student(student_id: int):
    db: Session = SessionLocal()

    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    db.delete(student)
    db.commit()

    return RedirectResponse(url="/", status_code=303)


@app.get("/edit/{student_id}", response_class=HTMLResponse)
def edit_student(request: Request, student_id: int):
    db: Session = SessionLocal()

    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    return templates.TemplateResponse(
        "edit.html",
        {"request": request, "student": student}
    )


@app.post("/update/{student_id}")
def update_student(student_id: int, name: str = Form(...), age: int = Form(...)):
    db: Session = SessionLocal()

    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    student.name = name
    student.age = age

    db.commit()

    return RedirectResponse(url="/", status_code=303)