from todolist import TodoList

def main():
    todo_list = TodoList()

    while True:
        print("1. Add todo")
        print("2. List todos")
        print("3. Mark todo as completed")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter the task: ")
            todo_list.add_todo(task)
        elif choice == 2:
            todos = todo_list.get_all_todos()
            for todo in todos:
                status = "Completed" if todo.completed else "Not completed"
                print(f"{todo.id}. {todo.task} - {status}")
        elif choice == 3:
            id = int(input("Enter the id of the todo to mark as completed: "))
            todo_list.mark_as_completed(id)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
