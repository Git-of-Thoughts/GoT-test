from keras.layers import Input, Dense
from keras.models import Model

class Autoencoder:
    def __init__(self, encoding_dim):
        self.encoding_dim = encoding_dim
        self.autoencoder = None
        self.encoder = None
        self.decoder = None

    def build(self, input_shape):
        input_img = Input(shape=(input_shape,))
        encoded = Dense(self.encoding_dim, activation='relu')(input_img)
        decoded = Dense(input_shape, activation='sigmoid')(encoded)
        self.autoencoder = Model(input_img, decoded)
        self.encoder = Model(input_img, encoded)
        encoded_input = Input(shape=(self.encoding_dim,))
        decoder_layer = self.autoencoder.layers[-1]
        self.decoder = Model(encoded_input, decoder_layer(encoded_input))
        self.autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
