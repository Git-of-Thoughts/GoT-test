class Task:
    """
    Represents a task in the To-Do list.
    """
    def __init__(self, description):
        self.description = description
        self.is_completed = False

    def __str__(self):
        return self.description
