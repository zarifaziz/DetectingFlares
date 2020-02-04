import cv2
import os
import random
import numpy as np
from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense


def label_data():
    """Formats training data with labels. 0 for 'faulty', 1 for 'good'"""
    DATADIR = "./training/"
    CATEGORIES = ['flare', 'good']

    training_data = []
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img))
                new_array = cv2.resize(img_array, (500, 400))
                training_data.append([new_array, class_num])
            except Exception as e:
                print(f"Exception: {e}")

    # shuffling the training data
    random.shuffle(training_data)

    return training_data


def create_training_data():
    """Creates training data for Keras. Returns of X and y."""
    training_data = label_data()

    # pack it into the variables we're going to use
    X = []
    y = []

    for features, label in training_data:
        X.append(features)
        y.append(label)

    # converting to numpy arrays
    X = np.array(X).reshape(-1, 400, 500, 3)
    y = np.array(y)

    # We should scale the data / normalise it
    X = X / 255.0

    return X, y


def create_model(X):
    """Creates a CNN model to classify flares in images"""

    # Building a simple stack of 2 convolution layers with a ReLU activation
    model = Sequential()

    model.add(Conv2D(32, (3, 3), input_shape=X.shape[1:]))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # On top adding two fully-connected layers. We end the model with a single
    # unit and a sigmoid function, which is good for binary classification
    model.add(Flatten())  # this converts our 3D feature  maps to 1D feature vectors
    model.add(Dense(64))
    model.add(Activation('relu'))

    model.add(Dropout(0.5)) # using dropout to decrease over-fitting
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    adam = optimizers.Adam(learning_rate=0.0005)

    model.compile(loss='binary_crossentropy',
                  optimizer=adam,
                  metrics=['accuracy'])

    return model


def main(epochs=20, batch_size=32, validation_split=0.2):
    """Running main function. Saves the final model to disk."""
    X, y = create_training_data()

    model = create_model(X)

    model.fit(X, y, batch_size=batch_size, epochs=epochs, validation_split=validation_split)

    # serialize model to JSON
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model.h5")
    print("Saved model to disk")


if __name__ == '__main__':
    """Running this file will setup and train the flare prediction model. Output is a pickle file called 'model'."""
    main()
