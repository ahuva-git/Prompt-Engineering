import os
import httpx
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    http_client=httpx.Client(verify=False)
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


gr.Interface(
    fn=generate_command,
    inputs=gr.Textbox(label="Natural Language Input"),
    outputs=gr.Textbox(label="CMD Command"),
    title="Natural Language → CMD Generator",
    description="Convert natural language into a Windows CMD command.",
    flagging_mode="never"
).launch(inbrowser=True)