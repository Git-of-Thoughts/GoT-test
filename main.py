from task import Task

def add_task(task_list, task_description):
    """
    Adds a new task to the task list.
    """
    task = Task(task_description)
    task_list.append(task)

def main():
    """
    The main function of the application.
    """
    task_list = []
    while True:
        task_description = input("Enter a task (or 'quit' to stop): ")
        if task_description.lower() == 'quit':
            break
        add_task(task_list, task_description)
    print("Here are your tasks:")
    for task in task_list:
        print(task)

if __name__ == "__main__":
    main()
