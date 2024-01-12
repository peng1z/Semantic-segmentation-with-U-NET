# Semantic Segmentation with U-Net in PyTorch
This repository contains an implementation of Semantic Segmentation using the U-Net architecture in PyTorch. Semantic Segmentation is a computer vision task where the goal is to classify each pixel in an image into a specific class.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Leveraging the U-Net architecture and its significance in semantic segmentation.

## Installation

You need to install the necessary toolkits and set up the environment to run this project. 

```bash
# Clone the repository
git clone https://github.com/peng1z/Semantic-segmentation-with-U-NET.git
cd Semantic-segmentation-with-U-NET

# Install the toolkits
pip3 install torch torchvision albumentations
```

## Usage

To use this ML model, you should have your datasets which should contain images and images' masks in the folder ```data/``` located in the root folder. I didn't include the datasets as it's too large and storage-consuming. You can pick your own ones.

```bash
python train.py --input_path path/to/input/image.jpg --output_path path/to/save/output/mask.gif
```

Attention: in my code, I used the ```.jpg``` file extension for train images and the ```.gif``` for train images' masks. If yours are different, please modify the code so that there won't be a failure.

## Training

Check out the hyperparameters in the ```train.py``` file. By default, I set: 
- BATCH_SIZE = 16, 
- NUM_EPOCHS = 3,
- NUM_WORKERS = 2,
- IMAGE_HEIGHT = 160,
- IMAGE_WIDTH = 240.

You can try different combinations of hyperparameters to make the model more accurate and efficient.

## Evaluation

Based on my training with 3 epochs, the accuracy for validation datasets reached 99.55% with a dice score of 98.75%. Try it yourself and feel free to comment if you got a better performance.

## Results

The result I got with 3 epochs is:
- Accuracy: 99.55%
- Dice score: 98.75%

## Contributing

If you want to contribute to this project, please contact me.

## License

This project is licensed under the MIT License.