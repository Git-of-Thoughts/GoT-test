The core classes, functions, and methods necessary for this game are:

1. `Game` class: This class will handle the game logic.
   - `__init__`: Initializes the game.
   - `reset`: Resets the game.
   - `draw`: Draws the game board.
   - `move`: Moves the snake.
   - `collision_check`: Checks for collisions.
   - `food_check`: Checks if the snake has eaten food.
   - `run`: Runs the game.

2. `Snake` class: This class will represent the snake.
   - `__init__`: Initializes the snake.
   - `get_head_position`: Returns the position of the snake's head.
   - `turn`: Turns the snake.
   - `move`: Moves the snake.
   - `reset`: Resets the snake.
   - `add_cube`: Adds a cube to the snake.

3. `Cube` class: This class will represent a cube (a unit of the snake's body or a piece of food).
   - `__init__`: Initializes the cube.
   - `move`: Moves the cube.
   - `draw`: Draws the cube.

4. `draw_grid` function: This function will draw the grid on the game board.

5. `random_snack` function: This function will generate a piece of food at a random position on the game board.

6. `message_box` function: This function will display a message box.

7. `main` function: This function will run the game.

Now, let's write the code for each of these components.

snake.py
