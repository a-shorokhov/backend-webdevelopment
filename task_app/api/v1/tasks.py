from fastapi import APIRouter, Depends
from repositories.tasks import TaskRepository
from schemas.tasks import TaskIn, TaskUpdate

router = APIRouter(tags=["tasks"])


@router.post("/tasks", status_code=201)
def post_tasks(task: TaskIn, repository: TaskRepository = Depends()):
    return repository.create_task(
        task.title,
        task.priority,
        task.completed,
    )


@router.get("/tasks", status_code=200)
def get_tasks(repository: TaskRepository = Depends()):
    return repository.get_all_tasks()


@router.get("/tasks/{task_id}", status_code=200)
def get_task(task_id: int, repository: TaskRepository = Depends()):
    return repository.get_task_by_id(task_id)


@router.patch("/tasks/{task_id}", status_code=200)
def update_task(
    task_id: int,
    updated_task: TaskUpdate,
    repository: TaskRepository = Depends(),
):
    return repository.update_task(
        task_id,
        updated_task.model_dump(),
    )


@router.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id: int, repository: TaskRepository = Depends()):
    return repository.delete_task(task_id)