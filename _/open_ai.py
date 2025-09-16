from openai import Client
from dotenv import load_dotenv
import os

load_dotenv()

client=Client(
    api_key=os.getenv('GEMINI_API_KEY'),
    base_url='https://generativelanguage.googleapis.com/v1beta'
)

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            'role':'user',
            'content':"Explain how AI works in a few words"
        }
    ]
)

print(response.choices[0].message.content)