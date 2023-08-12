from todolist import ToDoList

def main():
    """The entry point function."""
    todo_list = ToDoList()

    while True:
        print('1. Add task')
        print('2. View tasks')
        print('3. Mark task as completed')
        print('4. Exit')
        choice = input('Choose an option: ')

        if choice == '1':
            description = input('Enter task description: ')
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input('Enter task number: '))
            todo_list.mark_task_as_completed(task_number)
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
