from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder
from keras.layers import Embedding
import numpy as np

from data_loader import DataLoader

# Load data
data_loader = DataLoader()
sequences, labels = data_loader.load_data()

# One-hot encode sequences
encoder = OneHotEncoder()
sequences_encoded = encoder.fit_transform(sequences)

# Embed sequences
embedding = Embedding(input_dim=sequences_encoded.shape[1], output_dim=50)
sequences_embedded = embedding(sequences_encoded)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(sequences_embedded, labels, test_size=0.2, random_state=42)

# Train MLP classifier
mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=1000)
mlp.fit(X_train, y_train)

# Make predictions
y_pred = mlp.predict(X_test)

# Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
