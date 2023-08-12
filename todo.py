from dataclasses import dataclass

@dataclass
class Todo:
    id: int
    task: str
    completed: bool = False
