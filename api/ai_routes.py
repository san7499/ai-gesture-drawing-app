from flask import Blueprint, request, jsonify
from utils.ai_processing import correct_text, describe_drawing

# Create blueprint
ai_routes = Blueprint("ai_routes", __name__)


@ai_routes.route("/ai/correct_text", methods=["POST"])
def ai_correct_text():
    """
    Correct handwritten or typed text using OpenAI
    """

    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    corrected = correct_text(text)

    return jsonify({
        "original_text": text,
        "corrected_text": corrected
    })


@ai_routes.route("/ai/describe_drawing", methods=["POST"])
def ai_describe_drawing():
    """
    Describe a drawing using AI
    """

    data = request.json
    description = data.get("description", "")

    if not description:
        return jsonify({"error": "No drawing description provided"}), 400

    result = describe_drawing(description)

    return jsonify({
        "description": result
    })