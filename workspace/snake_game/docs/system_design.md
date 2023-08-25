## Implementation approach
We will use Pygame, a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the Python language. Pygame is highly portable and runs on almost every platform and operating system. 

The difficult points of the requirements are the game logic, the user interface, and the score tracking. Pygame provides tools to handle these aspects. The game logic will be implemented in a Game class, the user interface will be drawn using Pygame's drawing functions, and the score will be tracked in the Game class and displayed using Pygame's font module.

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
        +int score
        +bool game_over
        +Snake snake
        +Food food
        +ScoreBoard scoreboard
        +__init__(self)
        +run(self)
        +reset(self)
    }
    class Snake{
        +list body
        +str direction
        +__init__(self)
        +move(self)
        +grow(self)
        +collides_with(self, other)
    }
    class Food{
        +tuple position
        +__init__(self)
        +reposition(self)
    }
    class ScoreBoard{
        +int score
        +int high_score
        +__init__(self)
        +update(self, score)
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
    M->>G: create game
    G->>S: create snake
    G->>F: create food
    G->>SB: create scoreboard
    loop game loop
        G->>S: move snake
        G->>S: check if snake collides with food
        alt snake collides with food
            S->>S: grow snake
            G->>F: reposition food
            G->>SB: update score
        else snake does not collide with food
            G->>S: check if snake collides with self
            alt snake collides with self
                G->>G: end game
            end
        end
    end
```

## Anything UNCLEAR
The requirement is clear to me.