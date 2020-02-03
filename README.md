# Flare Detection

This repository contains the development of an algorithm that can automatically detect if an image
is subject to lens flare or not.

Outputs 1s and 0s for flared and good images respectively.

## Getting Started

These instructions will get you a copy of the tool up and running on your local machine.

### Prerequisites

The program requires [Python >= 3.6](https://www.python.org/downloads/) to be downloaded and installed on the machine.
Last tested on Python 3.6.

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
Once environment is set up, run program using the command below. Input integer numbers for `pop_size` and `n_gen`.
```bash
python -m scheduling pop_size n_gen 
```