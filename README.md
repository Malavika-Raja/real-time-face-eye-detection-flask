# Real-Time Face & Eye Detection Web Application

A real-time computer vision web application built using **Flask** and **OpenCV** that performs face and eye detection from a live webcam stream and renders the processed frames in a browser.

---

## Project Overview

This application captures video from the system webcam, detects faces using Haar Cascade classifiers, and performs nested eye detection within detected face regions. The processed frames are streamed continuously to the frontend using HTTP multipart responses.

This project demonstrates practical implementation of:

- Real-time image processing
- Classical computer vision techniques
- Backend API streaming
- Flask-based web application development

---

## Tech Stack

- **Python**
- **Flask**
- **OpenCV**
- **NumPy**
- **Haar Cascade Classifiers**
- HTML (Jinja templating)

---

## Features

- Live webcam streaming
- Real-time face detection
- Eye detection within face regions (ROI-based optimization)
- Frame encoding using JPEG compression
- Continuous streaming using `multipart/x-mixed-replace`

---

## How It Works

1. The Flask server initializes webcam capture using OpenCV.
2. Each frame is converted to grayscale for improved detection performance.
3. Face detection is performed using Haar Cascade classifiers.
4. Eye detection is restricted to the face region for efficiency.
5. Frames are encoded as JPEG images.
6. A generator function streams frames continuously to the browser.

---


---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/real-time-face-eye-detection-flask.git
cd real-time-face-eye-detection-flask
```
### 2. Create Virtual Environment
```
venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Run the application and open your browser
```
python app.py
```

## Engineering Highlights

- Efficient region-of-interest (ROI) processing for nested detection
- Real-time frame streaming using Flask Response generator
- Clean separation between backend processing and frontend rendering
- Optimized cascade loading to avoid repeated initialization overhead

## Limitations

- Uses classical Haar cascades instead of deep learning-based detectors
- Requires local webcam access
- Not containerized or deployed to cloud (local development setup)


