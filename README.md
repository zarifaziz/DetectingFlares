# Flare Detection

This repository contains the development of an algorithm that can automatically detect if an image
is subject to lens flare or not.

Outputs 1s and 0s for 'faulty' and 'good' images respectively.

![Image with Flare](./training/flare/G0015142.JPG)

## Running the Program

These instructions will get you a copy of the tool up and running on your local machine.

### Prerequisites

The program requires [Python = 3.6](https://www.python.org/downloads/) and `virtualenv` to be downloaded and installed on the machine.
Last tested on Python 3.6 and Ubuntu 18.04.

### Installing
Clone the repository onto local machine and enter the project
```
git clone https://github.com/zarifaziz/DetectingFlares.git
cd DetectingFlares
```
Initiate the environment using the following commands
```bash
python -m venv venv
source venv/bin/activate
```
Set up dependencies using
```
pip install -r requirements.txt
```

Place the images to be classified (e.g. image1.jpg, image2.jpg) in the main directory.
Once everything is set up, run program using the command below.
```bash
python -m detector image1.jpg image2.jpg
```

## Training the Model

A Convolutional Neural Network (CNN) model has been pre-trained for the predictions and is saved 
to this repository (`model.h5` and `model.json`). This is currently
being used by the program through the `load_model()` function.

However, to train a new model, the `training.py` file must be run.
