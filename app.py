import cv2
import os
from flask import Flask, render_template, Response
from dotenv import load_dotenv
from twilio.rest import Client
from ultralytics import YOLO

# Load environment variables
load_dotenv()

# Twilio credentials from .env (never hardcode!)
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
ALERT_PHONE = os.getenv("ALERT_PHONE")

# Initialize Twilio client
client = Client(TWILIO_SID, TWILIO_TOKEN)

# Load YOLOv8 fire detection model
model = YOLO("fire_detector.pt")

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # webcam


def generate_frames():
    fire_detected = False
    while True:
        success, frame = camera.read()
        if not success:
            break

        results = model(frame)
        annotated = results[0].plot()

        # Check detections
        for box in results[0].boxes:
            cls = int(box.cls[0])
            if model.names[cls].lower() == "fire":
                if not fire_detected:
                    fire_detected = True
                    send_alert()
            else:
                fire_detected = False

        ret, buffer = cv2.imencode('.jpg', annotated)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def send_alert():
    """Send SMS alert using Twilio"""
    if TWILIO_SID and TWILIO_TOKEN and TWILIO_PHONE and ALERT_PHONE:
        message = client.messages.create(
            body="🔥 Fire detected! Please take action immediately.",
            from_=TWILIO_PHONE,
            to=ALERT_PHONE
        )
        print("SMS sent:", message.sid)
    else:
        print("⚠️ Twilio not configured, SMS not sent.")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
