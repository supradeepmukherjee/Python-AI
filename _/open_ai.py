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
            'role':'system',
            'content':"You are an expert in Maths & only and only answer Maths related questions. If the query is not related to maths. Just say 'sorry' and do not answer that."
        },
        {
            'role':'user',
            # 'content':"Explain how AI works in a few words"
            'content':"simplify (a+b) whole square"
        },
    ]
)

print(response.choices[0].message.content)