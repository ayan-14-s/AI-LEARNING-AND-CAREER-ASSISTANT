import os
import requests

API_KEY = os.environ.get("GEMINI_API_KEY")

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent"


def get_ai_response(question):

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": API_KEY
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": (
                            "Answer the user's request clearly and professionally.\n"
                            "Use clean headings and numbered points when appropriate.\n"
                            "Use simple bullet points with '-' instead of '*'.\n"
                            "Do not use Markdown symbols such as *, **, #, or ```.\n"
                            "Keep the response well organized and easy to read.\n\n"
                            "USER REQUEST:\n"
                            + question
                        )
                    }
                ]
            }
        ]
    }

    try:

        response = requests.post(
            URL,
            headers=headers,
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            return result["candidates"][0]["content"]["parts"][0]["text"]

        else:

            return "Unable to get a response from AI. Please try again."

    except requests.exceptions.RequestException:

        return "Unable to connect to the AI service. Please check your internet connection."