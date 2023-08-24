## Implementation approach
We will use the Pygame library, an open-source Python library designed for making video games. It includes computer graphics and sound libraries. Pygame is highly portable and runs on almost every platform and operating system. 

The game will be divided into three main parts: 
1. Game Initialization: This is where we will initialize the Pygame library, define game variables, and create the game window.
2. Game Loop: This is the main loop where all the action happens. It includes event handling (like checking for key presses), updating the game state (like moving the snake and checking for collisions), and rendering the game state to the screen.
3. Game Over: This is where we will handle the end of the game, display the final score, and provide an option to restart the game.

The game will be developed in an object-oriented manner, with separate classes for the Snake, Food, and Game.

## Python package name
```python
"snake_game"
```

## File list
```python
[
    "main.py",
    "snake.py",
    "food.py",
    "game.py"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Snake{
        +list body
        +str direction
        +move()
        +grow()
    }
    class Food{
        +tuple position
        +respawn()
    }
    class Game{
        +Snake snake
        +Food food
        +int score
        +bool game_over
        +start_game()
        +end_game()
        +update_game_state()
        +render_game_state()
    }
    Game "1" -- "1" Snake: has
    Game "1" -- "1" Food: has
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant S as Snake
    participant F as Food
    M->>G: start_game()
    loop Game Loop
        G->>S: move()
        G->>G: update_game_state()
        G->>G: render_game_state()
        Note over G: Check for game over
    end
    G->>M: end_game()
```

## Anything UNCLEAR
The requirement is clear to me.