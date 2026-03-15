"""
app.py

Main Flask application for the
AI Hand Gesture Drawing Application.
"""

from flask import Flask
from config import DevelopmentConfig

# Import blueprints
from api.routes import main_routes
from api.ai_routes import ai_routes


def create_app():
    """
    Create and configure the Flask application
    """

    # Initialize Flask app
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(DevelopmentConfig)

    # Register Blueprints
    app.register_blueprint(main_routes)
    app.register_blueprint(ai_routes)

    return app


# Create application instance
app = create_app()


if __name__ == "__main__":

    print("\n🚀 Starting AI Gesture Drawing App...")
    print("🌐 Open your browser at: http://127.0.0.1:5000\n")

    # Run Flask server
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=app.config["DEBUG"]
    )