# ALERT-EYE: REAL-TIME FIRE DETECTION AND ALERT SYSTEM USING YOLOV8
Fire hazards present a major risk to human life, property, and the environment, demanding rapid and reliable detection systems. This research introduces AlertEye: Real-Time Fire Detection and Alert System using YOLOv8, a deep learning-based solution designed for high-accuracy fire recognition and real
time alerts. Built on the YOLOv8 architecture, the system is supported by a Flask backend, web-based UI, and Twilio API for instant SMS notifications, ensuring 
prompt responses during fire incidents. Trained on a custom-labeled dataset of 5,000 images (fire and non-fire), the model achieves a precision of 93.2%, recall of 
92.8%, and Fl-score of 93.0%, showcasing its effectiveness in distinguishing lire-related visuals. Training was performed on Google Colab Pro with preprocessing steps such as image normalization, resizing (640x640), and bounding box annotation to enhance detection reliability. Real-time performance is enabled by WebSocket 
integration for efficient live video streaming and continuous detection feedback. A key feature of AlertEye is its automated alert system that leverages Twilio to send 
SMS notifications upon fire detection, minimizing response time and potential damage. The modular design supports scalability, making it suitable for deployment on 
loT-enabled smart surveillance systems. However, the system encounters challenges like false positives from reflective surfaces, difficulties in identifYing small fires, 
and dependency on network latency. Future enhancements include thermal imaging integration, optimization for edge devices (e.g., NVIDIA Jetson Nano, Raspberry 
Pi), and federated learning for continuous model improvement.

