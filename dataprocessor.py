import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.filepath)

    def preprocess_data(self):
        scaler = StandardScaler()
        self.data = scaler.fit_transform(self.data)
