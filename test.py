from keras.datasets import mnist
import numpy as np
from autoencoder import Autoencoder

def test(autoencoder):
    (x_train, _), (x_test, _) = mnist.load_data()
    x_test = x_test.astype('float32') / 255.
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
    encoded_imgs = autoencoder.encoder.predict(x_test)
    decoded_imgs = autoencoder.decoder.predict(encoded_imgs)
    return encoded_imgs, decoded_imgs
