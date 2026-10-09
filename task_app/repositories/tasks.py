tasks = {}

class TaskRepository:
    def create_task(self, title, priority, completed):
        task_id = len(tasks) + 1

        tasks[task_id] = {
            "id": task_id,
            "title": title,
            "priority": priority,
            "completed": completed,
        }

        return tasks[task_id]

    def get_all_tasks(self):
        return tasks

    def get_task_by_id(self, task_id: int):
        task = tasks.get(task_id, None)

        return task

    def update_task(self, task_id: int, upd_data: dict):
        tasks[task_id].update(**upd_data)

        return tasks[task_id]

    def delete_task(self, task_id: int):
        return tasks.pop(task_id)