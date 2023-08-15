The core classes, functions, and methods necessary for the snake game are:

1. Class `Game`: This class will handle the game logic.
    - Method `__init__`: Initializes the game.
    - Method `reset`: Resets the game to its initial state.
    - Method `draw`: Draws the game board.
    - Method `move`: Moves the snake.
    - Method `check_collision`: Checks if the snake has collided with the wall or itself.
    - Method `check_food`: Checks if the snake has eaten food.
    - Method `run`: Runs the game loop.

2. Class `Snake`: This class will represent the snake.
    - Method `__init__`: Initializes the snake.
    - Method `move`: Moves the snake.
    - Method `grow`: Grows the snake.

3. Class `Food`: This class will represent the food.
    - Method `__init__`: Initializes the food.
    - Method `reset`: Resets the food to a random location.

4. Function `main`: This function will start the game.

Now, let's write the code for each class and function.

snake.py
