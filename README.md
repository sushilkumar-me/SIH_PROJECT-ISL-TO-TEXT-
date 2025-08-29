Hand Gesture Recognition Flask App

This project is a Flask web application that uses OpenCV, Mediapipe, and cvzone to detect and recognize hand gestures from a webcam feed. It captures hand images, compares them with a dataset of predefined gestures, and saves recognized gestures into a text file (example.txt).

🚀 Features

-Live webcam hand tracking using OpenCV and cvzone

-Hand landmark extraction with Mediapipe

-Gesture recognition by comparing with images in check_image/

-Real-time video streaming in the browser

-Saves recognized gestures into static/example.txt

-REST API to fetch recognition results

🛠️ Tech Stack

Python (Flask backend)

OpenCV – image processing

Mediapipe – hand landmark detection

cvzone – hand bounding box & utilities

NumPy – numerical operations

⚙️ Installation

Clone the repository

git clone https://github.com/sushilkumar-me/SIH_PROJECT-ISL-TO-TEXT-/
cd SIH_PROJECT(ISL TO TEXT)


(Optional) Create a virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


requirements.txt should contain:

flask
opencv-python
cvzone
mediapipe
numpy

▶️ Running the App

Start the Flask server:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/

📡 API Endpoints

/ → Home page with video feed

/video_feed1 → Live webcam stream (MJPEG)

/match-result → JSON response with last recognized gesture

/example.txt → Returns saved recognized gestures

📘 How to Use

1.Place reference gesture images inside the check_image/ folder.

Example: Hello.jpg, Thanks.jpg, etc.

2.Run the Flask app.

3.Show your hand gesture to the webcam.

4.If matched, the recognized gesture will:

Be shown in the app

Be saved inside static/example.txt

📸 Workflow

1.User shows a hand gesture

2.App captures the hand region

3.Extracts landmarks using Mediapipe

4.Compares with dataset images in check_image/

5.Saves recognized gesture into example.txt

🙌 Contribution

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to improve.
