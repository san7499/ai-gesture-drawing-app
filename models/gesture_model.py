"""
gesture_model.py

Detects hand gestures based on MediaPipe hand landmarks.
"""

class GestureModel:

    def __init__(self):
        # Finger tip landmark IDs from MediaPipe
        self.finger_tips = [4, 8, 12, 16, 20]

    def fingers_up(self, landmarks):
        """
        Detect which fingers are up.

        landmarks: list of 21 hand landmarks (x, y)
        returns: list of 5 values (1 = finger up, 0 = finger down)
        """

        fingers = []

        if len(landmarks) < 21:
            return [0, 0, 0, 0, 0]

        # Thumb (x comparison)
        if landmarks[self.finger_tips[0]][0] > landmarks[self.finger_tips[0] - 1][0]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other fingers (y comparison)
        for tip in self.finger_tips[1:]:

            if landmarks[tip][1] < landmarks[tip - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def detect_gesture(self, landmarks):
        """
        Determine gesture based on which fingers are up.
        """

        if not landmarks or len(landmarks) < 21:
            return "NONE"

        fingers = self.fingers_up(landmarks)

        # Gesture conditions

        # Only index finger up → DRAW
        if fingers == [0, 1, 0, 0, 0]:
            return "DRAW"

        # Index + middle finger up → MOVE
        elif fingers == [0, 1, 1, 0, 0]:
            return "MOVE"

        # Three fingers up → CHANGE COLOR
        elif fingers == [0, 1, 1, 1, 0]:
            return "COLOR"

        # Closed fist → ERASE
        elif fingers == [0, 0, 0, 0, 0]:
            return "ERASE"

        # All fingers up → CLEAR SCREEN
        elif fingers == [1, 1, 1, 1, 1]:
            return "CLEAR"

        return "NONE"


# Test the model directly
if __name__ == "__main__":

    # Create fake landmarks for testing
    example_landmarks = [(0, 0) for _ in range(21)]

    model = GestureModel()

    gesture = model.detect_gesture(example_landmarks)

    print("Detected Gesture:", gesture)