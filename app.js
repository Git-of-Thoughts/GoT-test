document.addEventListener('DOMContentLoaded', function() {
    var todoForm = document.getElementById('todo-form');
    var todoList = document.getElementById('todo-list');
    var todoInput = document.getElementById('todo-input');

    todoForm.addEventListener('submit', function(event) {
        event.preventDefault();
        var newTodo = todoInput.value;
        if (newTodo) {
            var newListItem = document.createElement('li');
            newListItem.textContent = newTodo;
            newListItem.className = 'todo-item';
            var deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            deleteButton.addEventListener('click', function() {
                todoList.removeChild(newListItem);
            });
            newListItem.appendChild(deleteButton);
            todoList.appendChild(newListItem);
            todoInput.value = '';
        }
    });
});
