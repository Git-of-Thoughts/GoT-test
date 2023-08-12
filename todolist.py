from task import Task

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def edit_task(self, old_title, new_title, new_description):
        for task in self.tasks:
            if task.title == old_title:
                task.title = new_title
                task.description = new_description

    def mark_task_as_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_complete()

    def list_tasks(self):
        for task in self.tasks:
            print(f"Title: {task.title}, Description: {task.description}, Completed: {task.is_completed}")
