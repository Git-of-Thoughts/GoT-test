## Implementation approach
We will use the Pygame open-source library to create the snake game. Pygame is a set of Python modules designed for writing video games and provides the functionality needed for our game such as handling events, drawing graphics, and updating the game state. The difficult points of the requirements include designing the game logic for snake movement and food consumption, creating a visually appealing and intuitive user interface, and implementing a system to keep track of high scores. We will tackle these challenges by dividing the tasks into smaller, manageable parts and developing them iteratively.

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
        +start_game()
        +pause_game()
        +resume_game()
        +end_game()
    }
    class Snake{
        +move()
        +eat(Food)
        +grow()
        +die()
    }
    class Food{
        +generate()
    }
    class ScoreBoard{
        +update_score(int)
        +reset_score()
        +get_high_score(): int
    }
    Game "1" -- "1" Snake: controls
    Game "1" -- "1" Food: controls
    Game "1" -- "1" ScoreBoard: controls
    Snake "1" -- "0..1" Food: eats
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant S as Snake
    participant F as Food
    participant SB as ScoreBoard
    M->>G: start_game()
    G->>S: move()
    G->>F: generate()
    S->>F: eat(F)
    alt if Snake eats Food
        G->>S: grow()
        G->>SB: update_score(1)
    else if Snake hits boundary or itself
        G->>S: die()
        G->>G: end_game()
    end
```

## Anything UNCLEAR
The requirement is clear to me.