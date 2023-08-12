from typing import List
from todo import Todo

class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, task: str):
        id = len(self.todos) + 1
        todo = Todo(id, task)
        self.todos.append(todo)

    def get_all_todos(self) -> List[Todo]:
        return self.todos

    def mark_as_completed(self, id: int):
        for todo in self.todos:
            if todo.id == id:
                todo.completed = True
                break
