"""
camera_stream.py

Handles webcam capture, hand detection,
gesture recognition, and frame streaming
to the Flask application.
"""

import cv2

from utils.hand_tracking import HandTracker
from utils.gesture_detection import GestureDetector
from utils.drawing_utils import DrawingBoard


# Initialize modules
hand_tracker = HandTracker()
gesture_detector = GestureDetector()
drawing_board = DrawingBoard()


def generate_frames():
    """
    Capture webcam frames, detect gestures,
    and stream frames to Flask.
    """

    cap = cv2.VideoCapture(0)

    # Set camera resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("❌ Error: Could not open webcam.")
        return

    while True:

        success, frame = cap.read()

        if not success:
            print("⚠️ Frame capture failed")
            break

        # Flip frame for mirror effect
        frame = cv2.flip(frame, 1)

        # Detect hand
        frame = hand_tracker.detect_hands(frame)

        # Get hand landmarks
        landmarks = hand_tracker.get_landmarks(frame)

        if landmarks and len(landmarks) >= 21:

            # Detect gesture
            gesture = gesture_detector.detect_gesture(landmarks)

            # Debug print (helps verify gestures)
            print("Gesture:", gesture)

            # Index finger tip
            x, y = landmarks[8]

            # Gesture actions
            if gesture == "DRAW":
                drawing_board.draw(x, y)

            elif gesture == "ERASE":
                drawing_board.erase(x, y)
                drawing_board.prev_x = 0
                drawing_board.prev_y = 0

            elif gesture == "CLEAR":
                drawing_board.clear()
                drawing_board.prev_x = 0
                drawing_board.prev_y = 0

            else:
                # Reset if gesture is not drawing
                drawing_board.prev_x = 0
                drawing_board.prev_y = 0

        else:
            # No hand detected
            drawing_board.prev_x = 0
            drawing_board.prev_y = 0

        # Overlay drawing canvas on webcam frame
        frame = drawing_board.overlay(frame)

        # Encode frame as JPEG
        ret, buffer = cv2.imencode(".jpg", frame)

        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        # Stream frame
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" +
            frame_bytes +
            b"\r\n"
        )

    cap.release()