import os
import random
from datetime import datetime

import google.generativeai as genai


# Gemini configuration
genai.configure(
    api_key=os.environ["GEMINI_API_KEY"]
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)



def generate_daily_note(commit_number, total_commits):

    prompt = f"""
You are a developer AI assistant.

Create developer progress note #{commit_number} out of {total_commits}.

Generate a unique Markdown note.

Include:

# Developer Progress Update

## Learning
Write something a frontend developer can learn.

## Coding Practice
Mention a practical coding improvement.

## Technology Insight
Mention React, Next.js, TypeScript, JavaScript,
Git, AI, or web development.

## Developer Tip
Give one useful professional tip.

Keep it short and realistic.
Do not repeat previous notes.
"""


    try:

        response = model.generate_content(
            prompt
        )

        return response.text


    except Exception as error:

        return f"""
# Developer Progress Update

Automation completed.

Fallback note generated.

Error:
{error}
"""



def create_commits():

    # Random commits between 1 and 10
    total_commits = random.randint(
        1,
        10
    )


    print(
        f"Today's commit count: {total_commits}"
    )


    date = datetime.now().strftime(
        "%Y-%m-%d"
    )


    os.makedirs(
        "data",
        exist_ok=True
    )


    for number in range(
        1,
        total_commits + 1
    ):


        content = generate_daily_note(
            number,
            total_commits
        )


        filename = (
            f"data/{date}-update-{number}.md"
        )


        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)



        print(
            f"Created {filename}"
        )



if __name__ == "__main__":

    create_commits()
