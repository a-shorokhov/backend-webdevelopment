from fastapi import Depends
from sqlalchemy.orm import Session

from core.database import get_db
from models.tasks import Task


class TaskRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_task(self, title, priority, completed):
        task = Task(
            title=title,
            priority=priority,
            completed=completed,
        )

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return task

    def get_all_tasks(self):
        return self.db.query(Task).all()

    def get_task_by_id(self, task_id: int):
        return self.db.get(Task, task_id)

    def update_task(self, task_id: int, upd_data: dict):
        task = self.get_task_by_id(task_id)

        task.title = upd_data["title"]
        task.priority = upd_data["priority"]
        task.completed = upd_data["completed"]

        self.db.commit()
        self.db.refresh(task)

        return task

    def delete_task(self, task_id: int):
        task = self.get_task_by_id(task_id)

        self.db.delete(task)
        self.db.commit()