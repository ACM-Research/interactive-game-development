# Interactive-Game-Development-using-Machine-Learning-Models

## Poster
![Poster](https://user-images.githubusercontent.com/33157393/202885887-bad7d12f-5526-4e0a-a086-3ac6cb55596c.png)

## Introduction
Machine learning techniques are becoming increasingly popular in the field of human-computer interaction. With this in mind, participants will program their own version of the web-based video game "Slither.io" but controlled using hand gestures through a computer webcam, rather than a keyboard like the original game. To achieve this, they will design and train a deep neural network that translates the position of the gamer's hand into game controls.

## Problem Description
The challenge given was to create a "Snake" or "Slither.io"-esque game, where a snake travels around the map and consumes food to grow larger while simultaneously avoiding either itself or other snake entities. The unique ambition of this project was to control the snake with the player's hand through a webcam, as opposed to a mouse or keyboard. This requirement meant that an AI model capable of processing images being fed through the webcam and translating it into game commands at sufficient speed was required, posing many technical challenges.

## Dataset
Training the AI to recognize hand gestures required creation of a dataset consisting of pictures of hands in different poses. These poses were to be matched with the labels "up", "down", "left", or "right", corresponding to the movement that the snake should make on the screen. To do this, our team took many pictures of our own hands under different lighting conditions and different positions on the screen. These images would then be labeled with "up", "down", "left", or "right", with the hand and its corresponding pose being selected by bounding boxes with labeling software like Label Studio and Roboflow.

In total, there were [] images taken, consisting of [] "up", [] "down", [] "left", and [] "right" images.

## Model

We used Tensorflow to train a model. We prioritized speed in our model, since the final product would end up processing live input and translating it to game controls. Games require very low input lag, on the order of milliseconds, so a very accurate but slow model fell out of favor as opposed to a generally accurate but fast model. Originally, we used YOLO-v5, which is exceptionally good at fast object detection. 

### Strategies


### Training
The model was trained on Google Colaboratory, since it provided a Python environment with usable GPUs for training. 

### Results
TBD 


## Game Creation
The game being used was based off of the Snake game 
## Contributors: Aarian Ahsan, Abiola Alalade, Kayla Baker, Naveen Mukkatt, Aaron Jacob
