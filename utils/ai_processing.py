from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please add it to your .env file.")

# Create OpenAI client
client = OpenAI(api_key=api_key)


def correct_text(text):
    """
    Correct spelling mistakes using OpenAI
    """
    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You correct spelling mistakes."
                },
                {
                    "role": "user",
                    "content": f"Correct this text: {text}"
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


def describe_drawing(description):
    """
    Describe a drawing using OpenAI
    """
    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You describe drawings."
                },
                {
                    "role": "user",
                    "content": description
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"