"""This file is meants to have the needed functions to load the data for the autoencoder, including the preprocessing and whatnot
"""
from tensorflow.keras.datasets import mnist

def get_data():
    (train_x, train_y), (test_x, test_y) = mnist.load_data()
    return train_x, train_y, test_x, test_y

print(type(get_data()[0]))