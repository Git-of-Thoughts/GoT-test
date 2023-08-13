from keras.datasets import mnist
import numpy as np
from autoencoder import Autoencoder

def train(autoencoder, epochs, batch_size):
    (x_train, _), (x_test, _) = mnist.load_data()
    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
    autoencoder.autoencoder.fit(x_train, x_train,
                                epochs=epochs,
                                batch_size=batch_size,
                                shuffle=True,
                                validation_data=(x_test, x_test))
