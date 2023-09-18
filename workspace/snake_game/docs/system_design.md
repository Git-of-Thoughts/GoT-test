## Implementation approach
We will use the Pygame library, an open-source module for Python, to develop the game. Pygame provides functionalities for game development like handling events, rendering graphics, and playing sounds which will be useful for our project. 

The game will be divided into two main parts: the game logic and the user interface. The game logic will handle the movement of the snake, the generation of food items, and the scoring system. The user interface will handle the rendering of the game, the display of the score, and user inputs.

The game will be developed in an object-oriented manner with classes for the game, the snake, and the food items. This will make the code more modular, easier to understand, and easier to maintain.

## Python package name
```python
"snake_game"
```

## File list
```python
[
    "main.py",
    "game.py",
    "snake.py",
    "food.py",
    "constants.py"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Game{
        +int score
        +bool game_over
        +start_game()
        +end_game()
        +pause_game()
        +resume_game()
    }
    class Snake{
        +list body
        +str direction
        +move()
        +grow()
    }
    class Food{
        +tuple position
        +generate()
    }
    Game "1" -- "*" Snake: has
    Game "1" -- "*" Food: has
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as main
    participant G as Game
    participant S as Snake
    participant F as Food
    M->>G: create game
    G->>S: create snake
    G->>F: create food
    M->>G: start game
    loop game loop
        G->>S: move snake
        G->>F: check if food eaten
        G->>S: check if snake hit self or wall
    end
    G->>M: end game
```

## Anything UNCLEAR
The requirement is clear to me.