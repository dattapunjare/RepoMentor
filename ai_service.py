
import requests


def explain_code(code):
    """
    Send source code to Qwen and get an explanation.
    """

    url = "http://localhost:11434/api/generate"

    prompt = f"""
    You are a friendly Python programming teacher.

    Explain the following source code in simple language.

    Include:
    1. Purpose of the code
    2. Important functions and classes
    3. How the code works step by step
    4. Important programming concepts used

    Source code:

    {code}
    """

    payload = {
        "model": "qwen3:1.7b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=180
        )

        response.raise_for_status()

        return response.json()["response"]

    except requests.RequestException as error:
        return f"Error connecting to Ollama: {error}"
