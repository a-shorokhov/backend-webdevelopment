from fastapi import APIRouter, Depends, HTTPException

from schemas.tasks import TaskIn, TaskUpdate
from services.tasks import TaskService


router = APIRouter(tags=["tasks"])


@router.post("/tasks", status_code=201)
def post_tasks(raw_task: TaskIn, service: TaskService = Depends()):
    return service.create_task(raw_task)


@router.get("/tasks", status_code=200)
def get_tasks(service: TaskService = Depends()):

    tasks = service.get_all_tasks()
    return tasks


@router.get("/tasks/{task_id}", status_code=200)
def get_task(task_id: int, service: TaskService = Depends()):
    task = service.get_task_by_id(task_id)

    if task["success"]:
        return task
    else:
        raise HTTPException(status_code=404, detail=task["message"])


@router.patch("/tasks/{task_id}", status_code=200)
def update_task(
    task_id: int,
    upd_data: TaskUpdate,
    service: TaskService = Depends(),
):
    task = service.edit_task(task_id, upd_data)

    if task["success"]:
        return task
    else:
        raise HTTPException(status_code=404, detail=task["message"])


@router.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id: int, service: TaskService = Depends()):
    delete_result = service.delete_task(task_id)

    if delete_result["success"]:
        return delete_result
    else:
        raise HTTPException(
            status_code=404,
            detail=delete_result["message"],
        )