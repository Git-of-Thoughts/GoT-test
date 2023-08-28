## Implementation approach
We will use the Pygame library, which is a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in Python. Pygame is highly portable and runs on almost every platform and operating system.
The game logic will be implemented in a Game class, which will handle the game loop, user input, and game state. The Snake and Food classes will be used to represent the snake and the food respectively. The ScoreBoard class will be used to track and display the current and high scores.

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
    "scoreboard.py"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Game{
        +bool game_over
        +Snake snake
        +Food food
        +ScoreBoard scoreboard
        +start()
        +update()
        +draw()
    }
    class Snake{
        +List[Tuple[int, int]] body
        +Tuple[int, int] direction
        +move()
        +grow()
        +check_collision()
    }
    class Food{
        +Tuple[int, int] position
        +generate()
    }
    class ScoreBoard{
        +int score
        +int high_score
        +update()
        +reset()
        +draw()
    }
    Game "1" -- "1" Snake: has
    Game "1" -- "1" Food: has
    Game "1" -- "1" ScoreBoard: has
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant S as Snake
    participant F as Food
    participant SB as ScoreBoard
    M->>G: start game
    loop game loop
        G->>S: move snake
        G->>S: check collision
        alt if snake eats food
            G->>S: grow snake
            G->>F: generate new food
            G->>SB: update score
        end
        alt if snake hits wall or itself
            G->>SB: update high score if necessary
            G->>G: end game
        end
    end
```

## Anything UNCLEAR
The requirement is clear to me.