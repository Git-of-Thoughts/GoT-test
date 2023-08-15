class App:
    def __init__(self):
        self.task_manager = TaskManager()
        self.storage_manager = StorageManager('tasks.dat')

    def run(self):
        self.task_manager.tasks = self.storage_manager.load_tasks()
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            self.handle_choice(choice)

    def display_menu(self):
        print("1. Add task")
        print("2. Delete task")
        print("3. Mark task as completed")
        print("4. View tasks")
        print("5. Exit")

    def handle_choice(self, choice):
        if choice == '1':
            self.add_task()
        elif choice == '2':
            self.delete_task()
        elif choice == '3':
            self.mark_task_as_completed()
        elif choice == '4':
            self.view_tasks()
        elif choice == '5':
            self.storage_manager.save_tasks(self.task_manager.tasks)
            exit(0)
        else:
            print("Invalid choice. Please try again.")

    def add_task(self):
        description = input("Enter task description: ")
        self.task_manager.add_task(description)

    def delete_task(self):
        id = int(input("Enter task id: "))
        self.task_manager.delete_task(id)

    def mark_task_as_completed(self):
        id = int(input("Enter task id: "))
        self.task_manager.mark_task_as_completed(id)

    def view_tasks(self):
        tasks = self.task_manager.get_all_tasks()
        for task in tasks:
            print(f"ID: {task.id}, Description: {task.description}, Completed: {task.completed}")
