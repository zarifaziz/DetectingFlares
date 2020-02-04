# Flare Detection

This repository contains the development of an algorithm that can automatically detect if an image
is subject to lens flare or not.

Outputs 1s and 0s for 'faulty' and 'good' images respectively.

## Running the Program

These instructions will get you a copy of the tool up and running on your local machine.

### Prerequisites

The program requires [Python = 3.6](https://www.python.org/downloads/) to be downloaded and installed on the machine.
Last tested on Python 3.6 and Ubuntu 18.04.

### Installing
Clone the repository onto local machine and enter the project
```
git clone https://github.com/zarifaziz/DetectingFlares.git
cd DetectingFlares
```
Set up environment using
```bash
pip install -r requirements.txt
```
Place the images to be classified (e.g. image1.jpg, image2.jpg) in the main directory.
Once everything is set up, run program using the command below.
```bash
python -m detector image1.jpg image2.jpg
```

## Training the Model

A Convolutional Neural Network (CNN) model has been pre-trained for the predictions which is currently
being used by the program through the `load_model()` function.

However, to train a new model, please use the `training.py` file.
