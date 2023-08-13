# a) Install dependencies
pip install -r requirements.txt

# b) Run all necessary parts of the codebase
# Train the autoencoder
python train.py

# Perform K-means clustering on the latent space
python cluster.py
