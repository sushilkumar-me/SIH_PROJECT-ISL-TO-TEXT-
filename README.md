# Hand Gesture Recognition Flask App  

This project is a **Flask web application** that uses **OpenCV, Mediapipe, and cvzone** to detect and recognize hand gestures from a webcam feed. It captures hand images, compares them with a dataset of predefined gestures, and saves recognized gestures into a text file (`example.txt`).  

---

## 🚀 Features  

- Live webcam hand tracking using OpenCV and cvzone  
- Hand landmark extraction with Mediapipe  
- Gesture recognition by comparing with images in `check_image/`  
- Real-time video streaming in the browser  
- Saves recognized gestures into `static/example.txt`  
- REST API to fetch recognition results  

---

## 🛠️ Tech Stack  

- **Python** (Flask backend)  
- **OpenCV** – image processing  
- **Mediapipe** – hand landmark detection  
- **cvzone** – hand bounding box & utilities  
- **NumPy** – numerical operations  

---

## ⚙️ Installation  

### Clone the repository  
```bash
git clone https://github.com/sushilkumar-me/SIH_PROJECT-ISL-TO-TEXT-/
cd SIH_PROJECT(ISL TO TEXT)

### Install dependencies
pip install -r requirements.txt

