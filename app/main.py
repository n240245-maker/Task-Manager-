from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Task Manager API",
    summary="Hey there..! you can  manage your tasks here..",
    description="This is a Task Manger API build for managing your daily tasks by FastAPI..! "
)

class Task(BaseModel):
    title : str
    completed : bool = False
    

@app.get("/")
def home():
    return {
        "message":"Welcome to TaskManager API",
        "status":"success"
    }

@app.post("/tasks",status_code=201)
def create_tasks(task : Task):
    return {
    "message":"Task created... Betee",
    "task":task
    }