from fastapi import Depends, HTTPException

from repositories.tasks import TaskRepository
from schemas.tasks import TaskIn, TaskUpdate

class TaskService:
    def __init__(self, repository: TaskRepository = Depends()):
        self.repository = repository

    def create_task(self, raw_task: TaskIn):
        task = self.repository.create_task(
            raw_task.title,
            raw_task.priority,
            raw_task.completed,
        )

        return {"success": True, **task}

    def get_all_tasks(self):
        tasks = self.repository.get_all_tasks()

        return tasks

    def get_task_by_id(self, task_id: int):
        task = self.repository.get_task_by_id(task_id)

        if task:
            return {"success": True, **task}
        else:
            return {"success": False, "message": "Task not found."}

    def edit_task(self, task_id: int, upd_data: TaskUpdate):
        if not self.repository.get_task_by_id(task_id):
            return {"success": False, "message": "Task not found."}
        else:
            upd_data = upd_data.model_dump()
            task = self.repository.update_task(task_id, upd_data)

            return {"success": True, **task}

    def delete_task(self, task_id: int):
        if not self.repository.get_task_by_id(task_id):
            return {"success": False, "message": "Task not found."}
        else:
            self.repository.delete_task(task_id)

            return {
                "success": True,
                "message": "Task was deleted.",
            }