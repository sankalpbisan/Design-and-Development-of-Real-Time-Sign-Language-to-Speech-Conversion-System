# Design and Development of Real Time Sign Language to Speech Conversion System

<p align="center">  
<img src="Images_and_Visuals/Designed_Glove/Designed_Glove4.jpg" alt="Designed Glove" width="600" height="350">
</p>

*The glove is designed and fused with flex and accelerometer and gyroscope sensors, the STM32 microcontroller development board is the processing unit which is connected to Desktop for consuming power as well as establishing communication.*

A real-time system designed to convert sign language gestures into spoken words, enabling seamless communication for the hearing and speech-impaired community. This project leverages embedded systems, machine learning, and text-to-speech technologies to bridge the communication gap.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Resources Used](#resources-used)
- [Block Diagram](#block-diagram)
- [Visuals](#visuals)
- [Demo](#demo)
- [Conclusion](#conclusion)
- [Contact](#contact)

---

## Introduction

This project aims to create a real-time system that interprets sign language gestures using designed glove and Machine Learning and converts them into speech using text-to-speech (TTS) technology. It is designed to assist individuals with hearing or speech impairments in communicating more effectively with others.

---

## Features

- **Real-Time Gesture Recognition**: Captures and interprets sign language gestures in real-time using sensors fused on the glove.
- **Text-to-Speech Conversion**: Converts recognized gestures into audible speech.
- **Portable**: Handy and comfortable mobile glove.

---

## Resources Used

#### Flex Sensors
<p align="center">  
<img src="Images_and_Visuals/Other_Images/Flex_Sensor.jpg" alt="Flex Sensors" width="350" height="300">
</p>
- The flex sensors are used for capturing the fingers flex movement

#### MPU6050
<p align="center">  
<img src="Images_and_Visuals/Other_Images/mpu6050.png" alt="MPU6050" width="350" height="300">
</p>
- This sensor is used for accounting the hand movements  

#### STM32F103C8T6
<p align="center">  
<img src="Images_and_Visuals/Other_Images/stm32.jpg" alt="STM32F103C8T6" width="350" height="300">
</p>
- This is a processing unit which takes the input from sensors and deliver it to Desktop for further process

---

## Block Diagram

<p align="center">  
<img src="Images_and_Visuals/Other_Images/Block_Diagram.jpg" alt="Block Diagram" width="450" height="380">
</p>

The block diagram is self-explanatory.
- The designed glove is only responsible for collecting data/input.
- All processing and classification task takes place on the Desktop itself

---

## Visuals

!['Welcome' sign all sensors plots](Images_and_Visuals/Other_Images/wel_graphs.png)
- All three sensors data is visualized on the plot, for efficient visuals, average of each data points is taken 


!['Bye' sign all sensors plots](Images_and_Visuals/Other_Images/bye_graphs.png)
- All three sensors data is visualized on the plot, for efficient visuals, average of each data points is taken 

---

## Demo

![While Performing "Bye-Bye" Gesture](Images_and_Visuals/Other_Images/Live_Image.png)

---

## Conclusion

- The designed and developed system performs well for two sign gestures only.
- Collecting more data leads to more complexity but it can be solved by designing more robust design. 
- It can be integrated with other sensors or replaced with high computing resources.
- While collecting data, sampling rate and minor fluctuations must be considered.
- Moreover, the systems overall robustness and functioning can be enhanced with more better devices and sensors.   

---

## Contact

For any questions or inquiries, feel free to reach out:

- **Email**: sankalpbisan07@gmail.com
- **LinkedIn**: [My LinkedIn Profile](https://in.linkedin.com/in/sankalpbisan)

---

Also check out my various projects:
1. **Vehicle Insurance MLOps Project** - [Click Here to visit this repo](https://github.com/sankalpbisan/Vehicle-Insurance-MLOps-Project.git)
2. **Student Performance Indicator** - [Click Here to visit this repo](https://github.com/sankalpbisan/MLOps_practice_project_students_performance_indicator.git)
3. **Patients Hospital Charges Predictor** - [Click Here to visit this repo](https://github.com/sankalpbisan/MLOps_Practice_Project-Patients-Hospital-Charges-Predictor.git)

---
