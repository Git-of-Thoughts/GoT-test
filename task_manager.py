class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        id = len(self.tasks) + 1
        task = Task(id, description)
        self.tasks.append(task)

    def delete_task(self, id):
        task = self.get_task_by_id(id)
        if task:
            self.tasks.remove(task)

    def mark_task_as_completed(self, id):
        task = self.get_task_by_id(id)
        if task:
            task.completed = True

    def get_all_tasks(self):
        return self.tasks

    def get_task_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None
