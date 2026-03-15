"""
config.py

Configuration settings for the
AI Gesture Drawing Application.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    """Base configuration"""

    # Flask Settings
    SECRET_KEY = os.getenv("SECRET_KEY", "gesture_app_secret_key")

    # Debug Mode
    DEBUG = False

    # Camera Settings
    CAMERA_INDEX = int(os.getenv("CAMERA_INDEX", 0))
    FRAME_WIDTH = int(os.getenv("FRAME_WIDTH", 1280))
    FRAME_HEIGHT = int(os.getenv("FRAME_HEIGHT", 720))

    # Drawing Settings
    DEFAULT_DRAW_COLOR = (255, 0, 255)  # Purple (BGR)
    BRUSH_THICKNESS = int(os.getenv("BRUSH_THICKNESS", 8))
    ERASER_THICKNESS = int(os.getenv("ERASER_THICKNESS", 50))

    # Base Directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # File Storage Paths
    DRAWINGS_FOLDER = os.path.join(BASE_DIR, "static", "canvas", "drawings")
    DATA_FOLDER = os.path.join(BASE_DIR, "data")

    # Ensure directories exist
    os.makedirs(DRAWINGS_FOLDER, exist_ok=True)
    os.makedirs(DATA_FOLDER, exist_ok=True)

    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)

    # AI Model
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""

    DEBUG = False