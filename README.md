# Hand Gesture Recognition Flask App  

This project is a Flask web application that uses OpenCV, Mediapipe, and cvzone to detect and recognize hand gestures from a webcam feed. It captures hand images, compares them with a dataset of predefined gestures, and saves recognized gestures into a text file (example.txt).  

## 🚀 Features  
- Live webcam hand tracking using OpenCV and cvzone  
- Hand landmark extraction with Mediapipe  
- Gesture recognition by comparing with images in check_image/  
- Real-time video streaming in the browser  
- Saves recognized gestures into static/example.txt  
- REST API to fetch recognition results  

## 🛠️ Tech Stack  
- Python (Flask backend)  
- OpenCV – image processing  
- Mediapipe – hand landmark detection  
- cvzone – hand bounding box & utilities  
- NumPy – numerical operations  

## ⚙️ Installation  
- Clone the repository
 
```bash
git clone https://github.com/sushilkumar-me/SIH_PROJECT-ISL-TO-TEXT-/
cd SIH_PROJECT(ISL TO TEXT)

```
- Install dependencies  
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project  

- Run the application  
```bash
python app.py
```

- Open in browser  
```bash
http://127.0.0.1:5000/
```

---

## 📂 Project Structure  
```
SIH_PROJECT-ISL-TO-TEXT-/
│-- app.py                # Main Flask app
│-- requirements.txt      # Dependencies
│-- static/               # CSS, JS, images
│-- templates/            # HTML templates
│-- model/                # Trained models
│-- utils/                # Helper functions
```

---

## 👨‍💻 Contributors  
- Team SIH 2024 Finalists  
