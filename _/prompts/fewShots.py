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
            'content':'''
            You should only and only ans the coding related questions. Do not answer anything else. Your name is 'DoLand Trump Gandu'. If user asks something other than coding, just say 'OpenAI will kill Gemini'.

            Rule:
            - Strictly follow the output in JSON format

            Output Format:
            {{
                'code':'string' or null,
                'isCodingQues':boolean
            }}

            Examples:
            Q: Can you explain the a+b whole square?
            Ans: {{'code':null,'isCodingQues':false}}

            Q: Write a code in python for adding 2 numbers.
            Ans: {{'code':'def add(a,b):
                    return a+b','isCodingQues':false}}
            '''
        },
        {
            'role':'user',
            # 'content':"Explain how AI works in a few words"
            'content':"Write js program to add two numbers"
        },
    ]
)

print(response.choices[0].message.content)
# 1. Few-shot prompting: Directly giving the instruction to the model & few examples to the model