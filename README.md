The game will be implemented in a single Python file named `snake_game.py`. The game will be structured using object-oriented programming principles, with a `Game` class to manage the game state and a `Snake` class to manage the snake's state.

The `Game` class will have the following methods:
- `__init__`: Initializes the game state.
- `reset`: Resets the game state.
- `draw_board`: Draws the current state of the game board.
- `place_apple`: Places an apple at a random location on the board.
- `game_over`: Checks if the game is over.
- `run`: Runs the game loop.

The `Snake` class will have the following methods:
- `__init__`: Initializes the snake's state.
- `move`: Moves the snake in the current direction.
- `grow`: Grows the snake by one unit.
- `change_direction`: Changes the direction of the snake.
- `get_head`: Returns the position of the snake's head.
- `get_body`: Returns the positions of the snake's body.

The `snake_game.py` file will also contain a `main` function that creates a `Game` object and starts the game.

Here is the complete code for the `snake_game.py` file:

snake_game.py
