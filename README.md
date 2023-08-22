Assumptions:
1. The game board will be a 20x20 grid.
2. The snake will start at a speed of 1 block per second.
3. The snake will grow by 1 block each time it eats food.
4. The game will end when the snake hits the border or itself.
5. The score will be calculated based on the number of food items eaten.
6. The game will be text-based, with the snake represented by 'S', food by 'F', and empty spaces by '.'.
7. There will be no special items or power-ups.
8. There will be no high score system.

Core Classes, Functions, and Methods:
1. `Game`: This class will represent the game itself. It will contain methods to start the game, handle user input, update the game state, and check for game over conditions.
2. `Snake`: This class will represent the snake. It will contain methods to move the snake, grow the snake, and check if the snake has collided with itself.
3. `Food`: This class will represent the food. It will contain a method to place the food at a random location on the board.
4. `Board`: This class will represent the game board. It will contain methods to initialize the board, update the board, and display the board.

Now, let's write the code for each of these classes.

snake.py
