from fastapi import APIRouter
from schemas.tasks import TaskIn, TaskUpdate

router = APIRouter(tags=["tasks"])
tasks = []


@router.post("/tasks", status_code=201)
def post_tasks(task: TaskIn):
    task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "priority": task.priority,
        "completed": task.completed,
    }
    tasks.append(task)

    return task

@router.get("/tasks", status_code=200)
def get_tasks():
    return tasks


@router.get("/tasks/{task_id}", status_code=200)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task


@router.patch("/tasks/{task_id}", status_code=200)
def update_task(task_id: int, updated_task: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["priority"] = updated_task.priority
            task["completed"] = updated_task.completed

            return task


@router.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            return task