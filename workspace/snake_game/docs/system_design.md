## Implementation approach
We will use the Pygame library, which is an open-source module for Python designed for game development. It includes computer graphics and sound libraries. The main challenges will be implementing the game logic, handling user input, and managing the game state. We will start by creating a basic version of the game, then add additional features like pausing the game and tracking high scores.

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
    class Main{
        +start_game()
        +end_game()
    }
    class Game{
        +int score
        +bool game_over
        +start()
        +pause()
        +resume()
        +end()
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
    class Scoreboard{
        +int high_score
        +update_score(int)
        +reset_score()
    }
    Main "1" -- "1" Game: controls
    Game "1" -- "1" Snake: has
    Game "1" -- "1" Food: has
    Game "1" -- "1" Scoreboard: has
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant S as Snake
    participant F as Food
    participant SB as Scoreboard
    M->>G: start()
    G->>S: move()
    G->>F: generate()
    G->>SB: update_score(G.score)
    G->>M: end_game()
```

## Anything UNCLEAR
The requirement is clear to me.