# Hand Gesture Mac Control 🖐️💻

This project uses **MediaPipe** and **OpenCV** to control my Mac using hand gestures captured from the webcam in real time. this only works on macOS currently.

## Features
- Tracks hand landmarks in real time
- Controls mouse movement using thump finger
- Gesture-based clicking using finger distance

## Technologies Used
- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## How It Works
The camera detects the hand, MediaPipe extracts landmarks, and gestures are mapped to mouse actions on macOS.

## but why the thump ?
while testing, i found out that if i were to track the index finger, when clicking i have to join my index and my thump together, this makes the cursor move with the clicking movement macking it click on unwanted stuff. that's why i opted to tracking with my thump.

## Demo
(Coming soon)

## Author
Ammar yasir abdulrahman

> This project was built as part of my journey learning computer vision and human–computer interaction.
