"""
app.py

Main Flask application for the
AI Hand Gesture Drawing Application.
"""

import os
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

    # Register blueprints
    app.register_blueprint(main_routes)
    app.register_blueprint(ai_routes)

    return app


# Create application instance
app = create_app()


if __name__ == "__main__":

    print("\n🚀 Starting AI Gesture Drawing App...")

    # Get port from environment (Render uses PORT)
    port = int(os.environ.get("PORT", 5000))

    print(f"🌐 Server running on port {port}\n")

    # Run Flask server
    app.run(
        host="0.0.0.0",
        port=port,
        debug=app.config["DEBUG"]
    )
