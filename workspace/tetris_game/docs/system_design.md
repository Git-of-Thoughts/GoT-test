## Implementation approach
We will use the Pygame library, which is an open-source module for Python designed for video game creation. It includes computer graphics and sound libraries. The difficult points of the requirements are the game mechanics of Tetris and the implementation of a feature to track high scores. We will need to design the game in such a way that it efficiently handles the falling blocks and the completed lines. For the high score feature, we will need to implement a way to store and retrieve the highest scores.

## Python package name
```python
"tetris_game"
```

## File list
```python
[
    "main.py",
    "game.py",
    "block.py",
    "scoreboard.py"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Game{
        +pygame.Surface game_surface
        +Block current_block
        +ScoreBoard score_board
        +bool game_over
        +bool paused
        +__init__(self)
        +run(self)
        +pause(self)
        +resume(self)
        +check_game_over(self)
        +draw(self)
    }
    class Block{
        +pygame.Rect block
        +int x
        +int y
        +__init__(self, x, y)
        +move(self, x, y)
        +rotate(self)
        +draw(self, surface)
    }
    class ScoreBoard{
        +int score
        +int high_score
        +__init__(self)
        +update_score(self, score)
        +get_high_score(self)
        +reset_score(self)
        +draw(self, surface)
    }
    Game "1" -- "1" Block: has
    Game "1" -- "1" ScoreBoard: has
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant B as Block
    participant S as ScoreBoard
    M->>G: game = Game()
    loop Game Loop
        G->>G: game.run()
        G->>B: block = Block(x, y)
        G->>B: block.move(x, y)
        G->>B: block.rotate()
        G->>B: block.draw(game_surface)
        G->>S: score_board.update_score(score)
        G->>S: score_board.draw(game_surface)
        G->>G: game.check_game_over()
        alt Game Over
            G->>M: break
        else Game Paused
            G->>G: game.pause()
            G->>G: game.resume()
        end
    end
```

## Anything UNCLEAR
The requirement is clear to me.