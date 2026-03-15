"""
hand_tracking.py

Handles hand detection and landmark extraction
using MediaPipe.
"""

import cv2
import mediapipe as mp


class HandTracker:

    def __init__(
        self,
        mode=False,
        max_hands=1,
        detection_conf=0.7,
        track_conf=0.7
    ):

        self.mode = mode
        self.max_hands = max_hands
        self.detection_conf = detection_conf
        self.track_conf = track_conf

        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_conf,
            min_tracking_confidence=self.track_conf
        )

        self.results = None

    def detect_hands(self, image, draw=True):
        """
        Detect hands in the frame and optionally draw landmarks.
        """

        # Convert BGR → RGB
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Improve performance by marking image as not writeable
        img_rgb.flags.writeable = False

        # Process image
        self.results = self.hands.process(img_rgb)

        # Allow writing again
        img_rgb.flags.writeable = True

        # Draw landmarks if detected
        if self.results and self.results.multi_hand_landmarks:

            for hand_landmarks in self.results.multi_hand_landmarks:

                if draw:
                    self.mp_draw.draw_landmarks(
                        image,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )

        return image

    def get_landmarks(self, image):
        """
        Extract landmark coordinates from detected hand.
        """

        landmark_list = []

        if self.results and self.results.multi_hand_landmarks:

            hand = self.results.multi_hand_landmarks[0]

            h, w, _ = image.shape

            for idx, lm in enumerate(hand.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                landmark_list.append((cx, cy))

        return landmark_list