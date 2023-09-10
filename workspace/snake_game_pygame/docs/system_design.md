## Implementation approach
We will use the Pygame library, an open-source module for Python, to create the snake game. Pygame provides functionalities for game development such as handling events, rendering graphics, and managing game states. The game will be designed as a single-player game where the player controls a snake to eat food that randomly appears on the screen. The snake grows longer each time it eats food. The game ends when the snake hits the screen border or its own body.

## Python package name
```python
"snake_game_pygame"
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
        +bool game_over
        +int score
        +start_game()
        +end_game()
        +pause_game()
        +resume_game()
        +update_score()
    }
    class Snake{
        +list body
        +str direction
        +move()
        +grow()
        +check_collision()
    }
    class Food{
        +tuple position
        +generate()
    }
    Game "1" -- "1" Snake: controls
    Game "1" -- "1" Food: generates
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant S as Snake
    participant F as Food
    M->>G: start_game()
    loop Game is not over
        G->>S: move()
        G->>S: check_collision()
        G->>F: generate()
        G->>G: update_score()
    end
    G->>M: end_game()
```

## Anything UNCLEAR
The requirement is clear to me. We will proceed with the implementation using Pygame library for Python.