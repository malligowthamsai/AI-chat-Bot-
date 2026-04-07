

import requests

API_KEY = ""

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def ask_ai(prompt):
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(f"{URL}?key={API_KEY}", json=data)
        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"Error: {e}"
