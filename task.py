from dataclasses import dataclass

@dataclass
class Task:
    """A class to represent a task."""
    description: str
    is_completed: bool = False
