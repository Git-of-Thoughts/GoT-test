class TodoList {
    constructor() {
        this.tasks = [];
    }

    addTask(task) {
        this.tasks.push(task);
        this.updateTaskList();
    }

    listTasks() {
        return this.tasks;
    }

    searchTasks(query) {
        return this.tasks.filter(task => task.includes(query));
    }

    clearTasks() {
        this.tasks = [];
        this.updateTaskList();
    }

    updateTaskList() {
        const taskListElement = document.getElementById('taskList');
        taskListElement.innerHTML = '';
        this.tasks.forEach(task => {
            const listItem = document.createElement('li');
            listItem.textContent = task;
            taskListElement.appendChild(listItem);
        });
    }
}

const todoList = new TodoList();

function addTask() {
    const taskInput = document.getElementById('taskInput');
    todoList.addTask(taskInput.value);
    taskInput.value = '';
}

function searchTasks() {
    const searchInput = document.getElementById('searchInput');
    const searchResults = todoList.searchTasks(searchInput.value);
    const taskListElement = document.getElementById('taskList');
    taskListElement.innerHTML = '';
    searchResults.forEach(task => {
        const listItem = document.createElement('li');
        listItem.textContent = task;
        taskListElement.appendChild(listItem);
    });
}

function clearTasks() {
    todoList.clearTasks();
}
