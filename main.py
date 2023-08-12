from todo import Todo
from todolist import TodoList

def main():
    todo_list = TodoList()

    while True:
        print("1. Add a new To-Do")
        print("2. Remove a To-Do")
        print("3. List all To-Dos")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the To-Do: ")
            description = input("Enter the description of the To-Do: ")
            status = input("Enter the status of the To-Do: ")

            todo = Todo(title, description, status)
            todo_list.add(todo)

        elif choice == "2":
            title = input("Enter the title of the To-Do to remove: ")
            todo_list.remove(title)

        elif choice == "3":
            todos = todo_list.list_all()

            for todo in todos:
                print(f"Title: {todo.title}, Description: {todo.description}, Status: {todo.status}")

        elif choice == "4":
            break

if __name__ == "__main__":
    main()
