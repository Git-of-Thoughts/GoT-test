from todolist import TodoList

def main():
    todo_list = TodoList()

    while True:
        print("1. Add task")
        print("2. Delete task")
        print("3. Edit task")
        print("4. Mark task as complete")
        print("5. List tasks")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == 2:
            title = input("Enter task title to delete: ")
            todo_list.delete_task(title)
        elif choice == 3:
            old_title = input("Enter task title to edit: ")
            new_title = input("Enter new task title: ")
            new_description = input("Enter new task description: ")
            todo_list.edit_task(old_title, new_title, new_description)
        elif choice == 4:
            title = input("Enter task title to mark as complete: ")
            todo_list.mark_task_as_complete(title)
        elif choice == 5:
            todo_list.list_tasks()
        elif choice == 6:
            break

if __name__ == "__main__":
    main()
