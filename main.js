document.getElementById('todo-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var todoInput = document.getElementById('todo-input');
    var todoText = todoInput.value.trim();

    if (todoText !== '') {
        addTodoItem(todoText);
        todoInput.value = '';
    }
});

function addTodoItem(text) {
    var todoList = document.getElementById('todo-list');

    var listItem = document.createElement('li');
    listItem.textContent = text;
    listItem.classList.add('todo-item');

    var deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.addEventListener('click', function() {
        todoList.removeChild(listItem);
    });

    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', function() {
        if (checkbox.checked) {
            listItem.classList.add('completed');
        } else {
            listItem.classList.remove('completed');
        }
    });

    listItem.appendChild(checkbox);
    listItem.appendChild(deleteButton);
    todoList.appendChild(listItem);
}
