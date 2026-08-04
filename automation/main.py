import os
from datetime import datetime

import google.generativeai as genai


# Configure Gemini API
genai.configure(
    api_key=os.environ["GEMINI_API_KEY"]
)


# Gemini model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_daily_update():

    prompt = """
You are my personal developer AI assistant.

Create a daily developer progress note in Markdown format.

Include:

# Daily Developer Log

## What I learned today
(Write 3-5 points)

## Coding Improvements
(Write practical improvements)

## Technologies
(Mention relevant frontend/backend technologies)

## Developer Tip
(Give one useful programming tip)

Keep it professional and suitable for a junior frontend developer portfolio.
"""

    try:

        response = model.generate_content(prompt)

        return response.text


    except Exception as error:

        print("Gemini API Error:", error)

        return f"""
# Daily Developer Log

AI generation failed.

Error:
{error}
"""


def save_update(content):

    today = datetime.now().strftime("%Y-%m-%d")

    folder = "data"

    os.makedirs(folder, exist_ok=True)


    file_path = f"{folder}/{today}.md"


    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)


    print(
        f"Created {file_path}"
    )


if __name__ == "__main__":

    update = generate_daily_update()

    save_update(update)

    print(
        "Automation completed successfully"
    )
