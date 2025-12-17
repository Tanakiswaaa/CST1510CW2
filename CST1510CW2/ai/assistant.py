import os
from openai import OpenAI


def ask_ai(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "OpenAI API key is not configured."

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a cybersecurity analyst assistant. "
                    "Provide concise, professional, and actionable insights."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content

