Assumptions:
1. The game board will be a 20x20 grid.
2. The snake will move in four directions: up, down, left, and right.
3. The snake will start at a speed of one grid per second and will increase its speed as it eats food.
4. The game will end when the snake hits the border or itself.
5. The snake will grow by one grid each time it eats food.
6. The game will be text-based with a simple console interface.
7. There will be no special features like power-ups or obstacles.
8. There will be no difficulty levels.

Core Classes, Functions, and Methods:
1. Class `Game`: This will be the main class that controls the game logic.
   - Method `__init__`: Initializes the game.
   - Method `start`: Starts the game.
   - Method `end`: Ends the game.
   - Method `draw_board`: Draws the game board.
   - Method `update`: Updates the game state.
2. Class `Snake`: This will represent the snake.
   - Method `__init__`: Initializes the snake.
   - Method `move`: Moves the snake.
   - Method `grow`: Grows the snake.
   - Method `check_collision`: Checks if the snake has collided with itself or the border.
3. Class `Food`: This will represent the food.
   - Method `__init__`: Initializes the food.
   - Method `generate`: Generates a new piece of food on the board.

Now, let's write the code for each class in separate files.

snake.py
