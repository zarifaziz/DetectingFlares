import cv2
import numpy as np
import sys
import os
from tensorflow.keras.models import model_from_json


def load_model():
    """Loads and returns pre-trained model"""
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")

    return loaded_model


def detect_flare_from_image(img_file, model):
    """Calls model.predict(image) for the new image. Prints '1' or '0' for 'faulty' and 'good' images respectively."""
    # pre-processing the image
    new_img = cv2.resize(img_file, (500, 400))
    new_img = np.array(new_img).reshape(-1, 400, 500, 3)

    # inverting output because model was trained to classify the other way.
    if model.predict(new_img) == 0:
        print(1)
    else:
        print(0)


def test_flare_images():
    """Test function to run on flared images"""
    model = load_model()

    DATADIR = "./test/"
    CATEGORY = 'flare'
    path = os.path.join(DATADIR, CATEGORY)
    for img in os.listdir(path):
        try:
            img_array = cv2.imread(os.path.join(path, img))
        except Exception as e:
            print("something's wrong")
        detect_flare_from_image(img_array, model)


def test_good_images():
    """Test function to run on good images"""
    model = load_model()

    DATADIR = "./test/"
    CATEGORY = 'good'
    path = os.path.join(DATADIR, CATEGORY)
    for img in os.listdir(path):
        try:
            img_array = cv2.imread(os.path.join(path, img))
        except Exception as e:
            print("something's wrong")
        detect_flare_from_image(img_array, model)


def main():
    files = sys.argv[1:]

    model = load_model()

    for file in files:
        img = cv2.imread(str(file))
        detect_flare_from_image(img, model)

    # file = sys.argv[1]
    #
    # model = load_model()
    # print(f"File: {file}")
    #
    # img = cv2.imread(str(file))
    #
    # detect_flare_from_image(img, model)


if __name__ == '__main__':
    main()