from autoencoder import Autoencoder
from train import train
from test import test

def main():
    autoencoder = Autoencoder(32)
    autoencoder.build(784)
    train(autoencoder, 50, 256)
    encoded_imgs, decoded_imgs = test(autoencoder)
    print("Encoded Images: ", encoded_imgs)
    print("Decoded Images: ", decoded_imgs)

if __name__ == "__main__":
    main()
