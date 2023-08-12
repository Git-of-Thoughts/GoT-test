from typing import List
from task import Task

class ToDoList:
    """A class to manage the list of tasks."""
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, description: str):
        """Add a new task to the list."""
        self.tasks.append(Task(description))

    def view_tasks(self):
        """Print all tasks."""
        for i, task in enumerate(self.tasks, start=1):
            status = 'Done' if task.is_completed else 'Not Done'
            print(f'{i}. {task.description} - {status}')

    def mark_task_as_completed(self, task_number: int):
        """Mark a task as completed."""
        self.tasks[task_number - 1].is_completed = True
