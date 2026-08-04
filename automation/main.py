import os
from datetime import datetime
from openai import OpenAI


client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)


prompt = """
Generate a short daily programming improvement note.
Save it as a markdown file.
"""


response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)


content = response.choices[0].message.content


date = datetime.now().strftime("%Y-%m-%d")


with open(
    f"data/{date}.md",
    "w",
    encoding="utf-8"
) as file:
    file.write(content)


print("Daily AI update created")
