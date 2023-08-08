from sklearn.linear_model import LogisticRegression

class ModelTrainer:
    def __init__(self, data):
        self.data = data
        self.model = None

    def train_model(self):
        X = self.data.drop('target', axis=1)
        y = self.data['target']
        self.model = LogisticRegression()
        self.model.fit(X, y)

    def save_model(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump(self.model, f)
