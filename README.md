The core classes, functions, and methods necessary for the game are:

1. `Point`: A class to represent a point in the grid. It will have two attributes, `x` and `y`, to represent the coordinates of the point.

2. `Snake`: A class to represent the snake. It will have the following attributes and methods:
   - `body`: A list of `Point` objects to represent the body of the snake.
   - `direction`: A `Point` object to represent the direction in which the snake is moving.
   - `get_head_position`: A method to get the position of the snake's head.
   - `turn_left`, `turn_right`, `turn_up`, `turn_down`: Methods to change the direction of the snake.
   - `move`: A method to move the snake in the current direction.
   - `grow`: A method to grow the snake by adding a new segment at the end of its body.
   - `collides_with_self`: A method to check if the snake has collided with itself.

3. `Game`: A class to represent the game. It will have the following attributes and methods:
   - `snake`: A `Snake` object to represent the snake.
   - `apple`: A `Point` object to represent the position of the apple.
   - `score`: An integer to represent the score.
   - `is_over`: A boolean to represent whether the game is over.
   - `reset`: A method to reset the game.
   - `place_apple`: A method to place a new apple in a random position in the grid.
   - `update`: A method to update the game state.
   - `draw`: A method to draw the game state.

4. `main`: A function to start the game. It will create a `Game` object and enter a game loop where it reads user input, updates the game state, and draws the game state.

Now, let's write the code for each of these classes, functions, and methods.

snake_game.py
