import numpy as np

class DataLoader:
    def load_data(self):
        # This function should load and return the amino acid sequences and their corresponding labels.
        # For the purpose of this example, we will generate random data.
        sequences = np.random.randint(0, 20, size=(1000, 100))
        labels = np.random.randint(0, 2, size=(1000,))
        return sequences, labels
