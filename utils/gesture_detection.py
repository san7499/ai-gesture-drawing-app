"""
gesture_detection.py

Detects hand gestures based on MediaPipe landmarks.
Used for controlling drawing actions.
"""

class GestureDetector:

    def __init__(self):
        # Finger tip landmark IDs
        self.finger_tips = [4, 8, 12, 16, 20]

    def fingers_up(self, landmarks):
        """
        Determine which fingers are raised.

        landmarks: list of (x, y) coordinates from MediaPipe
        returns: list of 5 values (1 = finger up, 0 = finger down)
        """

        fingers = []

        # Safety check
        if not landmarks or len(landmarks) < 21:
            return [0, 0, 0, 0, 0]

        # Thumb (x-axis comparison)
        if landmarks[self.finger_tips[0]][0] > landmarks[self.finger_tips[0] - 1][0]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other four fingers (y-axis comparison)
        for tip in self.finger_tips[1:]:

            if landmarks[tip][1] < landmarks[tip - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def detect_gesture(self, landmarks):
        """
        Detect gesture based on which fingers are up.
        """

        if not landmarks or len(landmarks) < 21:
            return "NONE"

        fingers = self.fingers_up(landmarks)

        # Gesture rules

        # Only index finger → DRAW
        if fingers == [0, 1, 0, 0, 0]:
            return "DRAW"

        # Index + middle → MOVE
        elif fingers == [0, 1, 1, 0, 0]:
            return "MOVE"

        # Three fingers → COLOR CHANGE
        elif fingers == [0, 1, 1, 1, 0]:
            return "COLOR"

        # Closed fist → ERASE
        elif fingers == [0, 0, 0, 0, 0]:
            return "ERASE"

        # All fingers → CLEAR SCREEN
        elif fingers == [1, 1, 1, 1, 1]:
            return "CLEAR"

        return "NONE"