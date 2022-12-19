# Interactive Game Development Using Machine Learning Models

## Poster
![Poster](https://user-images.githubusercontent.com/33157393/202885887-bad7d12f-5526-4e0a-a086-3ac6cb55596c.png)

## Introduction
Machine learning techniques are becoming increasingly popular in the field of human-computer interaction. With this in mind, participants will program their own version of the web-based video game "Slither.io" but controlled using hand gestures through a computer webcam, rather than a keyboard like the original game. To achieve this, they will design and train a deep neural network that translates the position of the gamer's hand into game controls.

## Problem Description
The challenge given was to create a "Snake" or "Slither.io"-esque game, where a snake travels around the map and consumes food to grow larger while simultaneously avoiding walls. The unique ambition of this project was to control the snake with the player's hand through a webcam, as opposed to a mouse or keyboard. This requirement meant that an AI model capable of processing images being fed through the webcam and translating it into game commands at sufficient speed was required, posing many technical challenges.

## Dataset
Training the AI to recognize hand gestures required creation of a dataset consisting of pictures of hands in different poses. These poses were to be matched with the labels "up", "down", "left", or "right", corresponding to the movement that the snake should make on the screen. To do this, our team took many pictures of our own hands under different lighting conditions and different positions on the screen. These images would then be labeled with "up", "down", "left", or "right", with the hand and its corresponding pose being selected by bounding boxes with labeling software like Label Studio and Roboflow.

In total, there were approximately 1,200 images taken, consisting of approximately 300 images per direction.

## Model
We primarily used the TensorFlow 2 Object Detection API to train models. We prioritized speed in our model instances, since the final product would end up processing live input and translating it to game controls. Games require very low input lag, on the order of milliseconds, so a very accurate but slow model fell out of favor as opposed to a generally accurate but fast model. We used SSDMobileNetv2 and YOLOv7, which are excellent at fast object detection. 

## Training
The model was trained on Google Colaboratory, since it provided a Python environment with usable GPUs for training. 

## Game Creation
We used the OpenCV and Tkinter libraries to create the snake game. For more information, view our [poster](https://viewscreen.githubusercontent.com/view/pdf?browser=safari&color_mode=light&commit=11f50a39b205e58d94ce6f70e60030ca492e76bb&device=unknown_device&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f41434d2d52657365617263682f696e7465726163746976652d67616d652d646576656c6f706d656e742f313166353061333962323035653538643934636536663730653630303330636134393265373662622f706f737465725f686967685f7265735f4947442e706466&logged_in=true&nwo=ACM-Research%2Finteractive-game-development&path=poster_high_res_IGD.pdf&platform=mac&repository_id=527306219&repository_type=Repository&version=15#e006daa4-35a1-4117-9e37-5f604207c0bb).

## Contributors
- Aarian Ahsan
- Abiola Alalade
- Kayla Baker
- Aaron Jacob ([@ProjectSkyapple](http://github.com/ProjectSkyapple))
- Naveen Mukkatt ([@NVC541](http://github.com/NVC541))
- Sisira Aarukapalli (Research Lead)
- Dr. Ranran Feng (Advisor)
