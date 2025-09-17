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
            # 'content':"You are an expert in Maths & only and only answer Maths related questions. If the query is not related to maths. Just say 'sorry' and do not answer that."
            'content':"You should only and only ans the coding related questions. Do not answer anything else. Your name is 'DoLand Trump Gandu'. If user asks something other than coding, just say 'OpenAI will kill Gemini'"
        },
        {
            'role':'user',
            # 'content':"Explain how AI works in a few words"
            'content':"What is the capital of India?"
        },
    ]
)

print(response.choices[0].message.content)
# 1. 0-shot prompting: The model is given a direct question/task without prior example