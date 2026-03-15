"""
drawing_utils.py

Handles drawing operations for the
AI Gesture Drawing Application.
"""

import cv2
import numpy as np


class DrawingBoard:

    def __init__(self, width=1280, height=720):

        # Create blank drawing canvas
        self.canvas = np.zeros((height, width, 3), np.uint8)

        # Drawing settings
        self.draw_color = (255, 0, 255)  # Purple (BGR)
        self.brush_thickness = 8
        self.eraser_thickness = 50

        # Previous drawing position
        self.prev_x = None
        self.prev_y = None

    def draw(self, x, y):
        """
        Draw line between previous point and new point
        """

        # Initialize first point
        if self.prev_x is None or self.prev_y is None:
            self.prev_x, self.prev_y = x, y
            return

        # Draw smooth line
        cv2.line(
            self.canvas,
            (self.prev_x, self.prev_y),
            (x, y),
            self.draw_color,
            self.brush_thickness
        )

        # Update previous point
        self.prev_x, self.prev_y = x, y

    def erase(self, x, y):
        """
        Erase drawing using a circular brush
        """

        cv2.circle(
            self.canvas,
            (x, y),
            self.eraser_thickness,
            (0, 0, 0),
            cv2.FILLED
        )

        # Reset previous drawing position
        self.prev_x = None
        self.prev_y = None

    def clear(self):
        """
        Clear the entire drawing canvas
        """

        self.canvas[:] = 0
        self.prev_x = None
        self.prev_y = None

    def change_color(self, color):
        """
        Change drawing color
        """

        self.draw_color = color

    def reset_position(self):
        """
        Reset previous drawing coordinates
        """

        self.prev_x = None
        self.prev_y = None

    def overlay(self, frame):
        """
        Overlay drawing canvas onto webcam frame
        """

        # Ensure canvas size matches frame
        if self.canvas.shape[:2] != frame.shape[:2]:
            self.canvas = cv2.resize(
                self.canvas,
                (frame.shape[1], frame.shape[0])
            )

        # Convert canvas to grayscale
        gray = cv2.cvtColor(self.canvas, cv2.COLOR_BGR2GRAY)

        # Create mask
        _, inv = cv2.threshold(
            gray,
            50,
            255,
            cv2.THRESH_BINARY_INV
        )

        inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)

        # Combine frame and drawing
        frame = cv2.bitwise_and(frame, inv)
        frame = cv2.bitwise_or(frame, self.canvas)

        return frame