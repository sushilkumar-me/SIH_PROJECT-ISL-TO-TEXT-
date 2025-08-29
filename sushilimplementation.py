from flask import Flask, render_template, Response, jsonify, send_file
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import mediapipe as mp
import math
import time
import os
import re

app = Flask(__name__)

# Configuration
offset = 50
imgSize = 300
folder = "captured_images"
comparison_folder = "check_image"
example_txt_path = "static/example.txt"

# Ensure required folders exist
os.makedirs(folder, exist_ok=True)
os.makedirs(comparison_folder, exist_ok=True)
os.makedirs("static", exist_ok=True)  # for example.txt

# Clear old example.txt at startup
with open(example_txt_path, "w") as f:
    f.write("")

# Webcam setup
cap = cv2.VideoCapture(0)

# Global match data
match_data = {"message": "No match found"}
last_word = None   # track last matched word

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)
detector = HandDetector(maxHands=1, detectionCon=0.8)


# Extract landmarks
def extract_hand_landmarks(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(image_rgb)
    if result.multi_hand_landmarks:
        landmarks = result.multi_hand_landmarks[0]
        return np.array([[lm.x, lm.y, lm.z] for lm in landmarks.landmark]).flatten()
    return None


# Similarity between hand landmark arrays
def calculate_similarity(landmarks1, landmarks2):
    if landmarks1.shape != landmarks2.shape:
        return float('inf')
    return np.linalg.norm(landmarks1 - landmarks2)


# Compare image with dataset
def match_image(input_image):
    input_landmarks = extract_hand_landmarks(input_image)
    if input_landmarks is None:
        return None

    closest_distance = float('inf')
    matched_file = None

    for file_name in os.listdir(comparison_folder):
        file_path = os.path.join(comparison_folder, file_name)
        comparison_landmarks = extract_hand_landmarks(file_path)
        if comparison_landmarks is not None:
            distance = calculate_similarity(input_landmarks, comparison_landmarks)
            if distance < closest_distance:
                closest_distance = distance
                matched_file = file_name

    if matched_file:
        matched_label = os.path.splitext(matched_file)[0]
        cleaned_label = re.sub(r'[ \[\] (){}0-9]', '', matched_label)
        return cleaned_label
    return None


# Capture from webcam and match
def capture_images_and_match(img):
    hands_list, _ = detector.findHands(img, draw=False)
    if not hands_list:
        return None

    hand = hands_list[0]
    x, y, w, h = hand['bbox']
    height, width = img.shape[:2]

    x1, y1 = max(0, x - offset), max(0, y - offset)
    x2, y2 = min(x + w + offset, width), min(y + h + offset, height)
    imgCrop = img[y1:y2, x1:x2]

    if imgCrop.size == 0:
        return None

    imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
    aspectRatio = h / w

    if aspectRatio > 1:
        k = imgSize / h
        wCal = math.ceil(k * w)
        imgResize = cv2.resize(imgCrop, (wCal, imgSize))
        wGap = math.ceil((imgSize - wCal) / 2)
        imgWhite[:, wGap:wGap + wCal] = imgResize
    else:
        k = imgSize / w
        hCal = math.ceil(k * h)
        imgResize = cv2.resize(imgCrop, (imgSize, hCal))
        hGap = math.ceil((imgSize - hCal) / 2)
        imgWhite[hGap:hGap + hCal, :] = imgResize

    timestamp = str(time.time())
    captured_image_path = f"{folder}/Image_{timestamp}.jpg"
    cv2.imwrite(captured_image_path, imgWhite)

    return match_image(captured_image_path)


# Webcam feed
def video_feed():
    global match_data, last_word
    last_called_time = time.time()
    interval = 3

    while True:
        success, img = cap.read()
        if not success:
            break

        current_time = time.time()
        if current_time - last_called_time >= interval:
            matched_label = capture_images_and_match(img)
            if matched_label and matched_label != last_word:
                # Update global state
                match_data = {"matched_label": matched_label}
                last_word = matched_label

                # Save to file
                with open(example_txt_path, "a") as file:
                    file.write(matched_label + " ")

            last_called_time = current_time

        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--img\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# ---------- ROUTES ----------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed1")
def video_feed1():
    return Response(video_feed(), mimetype='multipart/x-mixed-replace; boundary=img')


@app.route("/match-result", methods=["GET"])
def get_match_result():
    return jsonify(match_data)


@app.route("/example.txt")
def serve_example_file():
    if os.path.exists(example_txt_path):
        return send_file(example_txt_path)
    return "File not found", 404


# Run the app
if __name__ == '__main__':
    try:
        app.run(debug=True, use_reloader=False)
    finally:
        cap.release()
        cv2.destroyAllWindows()
