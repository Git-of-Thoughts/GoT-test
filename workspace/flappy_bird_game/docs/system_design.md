## Implementation approach
We will use Pygame, an open-source Python library for making video games. It is designed to be simple to use, yet powerful enough to allow for complex game development. Pygame provides modules for handling graphics, sound, input, and more, making it a good fit for our flapping bird game. 

The game will be designed as a single-player game where the player controls a bird trying to fly through gaps in incoming obstacles. The bird will be controlled by the space bar, which will make the bird flap and rise. The bird will automatically descend if the space bar is not pressed. 

The game will end if the bird touches an obstacle or the ground. The score will be determined by the number of obstacles the player successfully navigates through.

## Python package name
```python
"flappy_bird_game"
```

## File list
```python
[
    "main.py",
    "bird.py",
    "obstacle.py",
    "game.py",
    "constants.py",
    "scoreboard.py"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Bird{
        +int x
        +int y
        +int velocity
        +int gravity
        +int flap_power
        +bool is_alive
        +__init__(x: int, y: int, velocity: int, gravity: int, flap_power: int)
        +flap()
        +update()
    }
    class Obstacle{
        +int x
        +int y
        +int width
        +int gap_height
        +bool passed
        +__init__(x: int, y: int, width: int, gap_height: int)
        +update()
    }
    class Game{
        +Bird bird
        +list[Obstacle] obstacles
        +int score
        +bool game_over
        +__init__(bird: Bird)
        +start()
        +update()
        +end()
    }
    class Scoreboard{
        +int high_score
        +__init__()
        +update(score: int)
    }
    Bird "1" -- "1" Game: controls
    Obstacle "*" -- "1" Game: obstacles
    Game "1" -- "1" Scoreboard: updates
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant B as Bird
    participant O as Obstacle
    participant S as Scoreboard
    M->>G: create game
    G->>B: create bird
    G->>O: create obstacles
    G->>S: create scoreboard
    loop Game Loop
        M->>G: start game
        G->>B: bird.update()
        G->>O: obstacle.update()
        G->>S: scoreboard.update(score)
        G-->>M: game_over
    end
    M->>G: end game
```

## Anything UNCLEAR
The requirement is clear to me.