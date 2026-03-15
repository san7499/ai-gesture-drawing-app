"""
routes.py

Main application routes for the
AI Hand Gesture Drawing App.
"""

from flask import Blueprint, render_template, Response
from camera.camera_stream import generate_frames


# Create Blueprint
main_routes = Blueprint("main_routes", __name__)


@main_routes.route("/")
def index():
    """
    Render the main webpage
    """
    return render_template("index.html")


@main_routes.route("/video_feed")
def video_feed():
    """
    Stream video frames from the webcam
    """

    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@main_routes.route("/health")
def health_check():
    """
    Simple route to check if server is running
    """
    return {"status": "AI Gesture Drawing App running"}