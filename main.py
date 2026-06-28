import os
import httpx
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 👇 זה החלק הקריטי
http_client = httpx.Client(verify=False)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    http_client=http_client
)

def generate_command(user_input):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": open("prompt3.txt", "r", encoding="utf-8").read()
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response.choices[0].message.content.strip()


# בדיקה
user_input = input("Enter request: ")
result = generate_command(user_input)

print("CLI Command:", result)