from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

tasks = {}
task_counter = 1


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskStatusUpdate(BaseModel):
    status: str


@app.post("/tasks")
def create_task(task: TaskCreate):
    global task_counter

    new_task = {
        "task_id": task_counter,
        "title": task.title,
        "description": task.description,
        "status": "pending",
        "created_at": datetime.now()
    }

    tasks[task_counter] = new_task
    task_counter += 1

    return new_task


@app.get("/tasks")
def get_all_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks[task_id]


@app.put("/tasks/{task_id}")
def update_task(task_id: int, update: TaskStatusUpdate):

    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks[task_id]["status"] = update.status

    return tasks[task_id]


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = tasks.pop(task_id)

    return {"message": "Task deleted", "task": deleted_task}