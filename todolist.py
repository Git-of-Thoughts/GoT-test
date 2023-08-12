class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)

    def remove(self, title):
        self.todos = [todo for todo in self.todos if todo.title != title]

    def list_all(self):
        return self.todos
