The core classes, functions, and methods necessary for the snake game are:

1. `Point`: A class to represent a point in the grid. It will have two attributes, `x` and `y`, to represent the coordinates of the point.

2. `Snake`: A class to represent the snake. It will have the following methods:
   - `__init__`: To initialize the snake with a given length and direction.
   - `move`: To move the snake in the current direction.
   - `change_direction`: To change the direction of the snake.
   - `grow`: To increase the length of the snake.
   - `collides_with_self`: To check if the snake has collided with itself.
   - `collides_with_wall`: To check if the snake has collided with the wall.

3. `Game`: A class to represent the game. It will have the following methods:
   - `__init__`: To initialize the game with a given grid size and initial snake length.
   - `play`: To start the game.
   - `draw`: To draw the game state.
   - `handle_input`: To handle user input.
   - `update`: To update the game state.
   - `check_collision`: To check if the snake has collided with the wall or itself.
   - `spawn_apple`: To spawn an apple at a random location in the grid.

4. `main`: A function to start the game.

Now, let's write the code for each of these components.

snake_game.py
