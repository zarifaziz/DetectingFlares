import cv2
import numpy as np
import sys
from tensorflow.keras.models import model_from_json


def load_model():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")

    return loaded_model


def detect_flare_from_image(img_file, model):
    """Calls model.predict(image) for the new image. Prints output of classification."""
    # pre-processing the image
    new_img = cv2.resize(img_file, (500, 400))
    new_img = np.array(new_img).reshape(-1, 400, 500, 3)

    # prints '1' or '0' on the screen
    print(model.predict(new_img))


def main():
    files = sys.argv[1:]

    model = load_model()

    for file in files:
        img = cv2.imread(file)
        detect_flare_from_image(img, model)


if __name__ == '__main__':
    main()
