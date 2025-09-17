from openai import Client
from dotenv import load_dotenv
import os
import json

load_dotenv()

client=Client(
    api_key=os.getenv('GEMINI_API_KEY'),
    base_url='https://generativelanguage.googleapis.com/v1beta'
)

systemPrompt='''
    You are an AI persona assistant named Supradeep.
    You are acting on behalf of Supradeep who is 21 years old Tech Enthusiast & principle engineer, Your main tech stack is Javascript & Python and You are learning GenAI those days.
'''


msgHistory=[
    {
        'role':'system',
        'content':systemPrompt
    }
]

userQuery=input('\n\nAsk me: ')
msgHistory.append({
    'role':'user',
    'content':userQuery
})

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    # response_format={'type':'json_object'},
    messages=msgHistory
)

print(response.choices[0].message.content)