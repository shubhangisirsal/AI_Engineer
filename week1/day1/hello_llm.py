import os
from dotenv import load_dotenv
from groq import Groq   # or from openai import OpenAI if using OpenAI

# Load environment variables from .env
load_dotenv()

# Read the key from environment
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize client
client = Groq(api_key=groq_api_key)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a helpful AI tutor."},
        {"role": "user", "content": "Hello, this is my first Groq LLM call!"}
    ]
)

print(response.choices[0].message.content)
