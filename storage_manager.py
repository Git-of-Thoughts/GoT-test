import pickle

class StorageManager:
    def __init__(self, filename):
        self.filename = filename

    def save_tasks(self, tasks):
        with open(self.filename, 'wb') as file:
            pickle.dump(tasks, file)

    def load_tasks(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []
