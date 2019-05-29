from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D, BatchNormalization
import imageio
import numpy as np

class numRecog():
    def __init__(self):
        # Importing the required Keras modules containing model and layers
        # Creating a Sequential Model and adding the layers
        model = Sequential()
        model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=(28, 28, 1)))
        model.add(BatchNormalization())
        model.add(Conv2D(32, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(Conv2D(32, kernel_size=5, strides=2, padding='same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))

        model.add(Conv2D(64, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(Conv2D(64, kernel_size=3, activation='relu'))
        model.add(BatchNormalization())
        model.add(Conv2D(64, kernel_size=5, strides=2, padding='same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))

        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(BatchNormalization())

        model.add(Dense(10, activation='softmax'))

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        model.load_weights("mnist_cnn.h5")

        self.model = model

    def recog_image(self):
        im = imageio.imread('img.png')
        im2 = np.empty((28, 28, 1), dtype='float32')
        for i in range(28):
            for j in range(28):
                im2[i][j] = [(255 - (int(im[i][j][0]) + int(im[i][j][1]) + int(im[i][j][2])) / 3) / 255]

        pred = self.model.predict(im2.reshape(1, 28, 28, 1))
        return pred.argmax()




