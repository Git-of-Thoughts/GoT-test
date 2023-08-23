Assumptions:
1. The game window size is 800x600 pixels.
2. The initial speed of the snake is moderate and increases as the game progresses.
3. The snake dies when it hits the border or crosses itself.
4. The score is displayed and increases when the snake eats food.
5. The controls for the snake's movement are the arrow keys.
6. There are no special items or power-ups in the game.
7. There are no sound effects or background music.

Core Classes, Functions, and Methods:
1. `Snake`: This class represents the snake. It has methods for moving the snake, growing the snake, and checking if the snake has collided with itself.
2. `Food`: This class represents the food. It has a method for placing the food at a random location.
3. `Game`: This class represents the game. It has methods for starting the game, ending the game, and updating the game state.
4. `draw`: This function draws the game state on the screen.
5. `main`: This function is the entry point of the program. It initializes the game and enters the game loop.

Now, let's write the code for each file.

snake.py
