from openai import Client
from dotenv import load_dotenv
import os
import json
import requests
from pydantic import BaseModel,Field
from typing import Optional

load_dotenv()

client=Client(
    api_key=os.getenv('GEMINI_API_KEY'),
    base_url='https://generativelanguage.googleapis.com/v1beta'
)

def getWeather(city:str):
    url=f'https://wttr.in/{city.lower()}?format=%C+%t'
    res=requests.get(url)
    if res.status_code==200:
        return(f'The weather in {city} is {res.text}')
    return('Something went wrong')

availableTools={
    'getWeather':getWeather
}

class MyOutputFormat(BaseModel):
    step:str=Field(...,description='The ID of the step. Example: PLAN,OUTPUT,TOOL, etc.')
    content:Optional[str]=Field(None,description='The optional string content for the step')
    tool:Optional[str]=Field(None,description='The ID of the tool to call.')
    input:Optional[str]=Field(None,description='The input params for the tool.')

systemPrompt='''
            You're an expert AI Assistant in resolving user queries using chain of thought.
            You work on START, PLAN & OUTPUT steps.
            You need to first PLAN what needs to be done. The PLAN can be multiple steps.
            Once you think enough PLAN has been done, finally you can give an OUTPUT.
            You can also call a TOOL if required from the list of available tools.
            For every tool, wait for the OBSERVE step which is the output from the called tool.

            Rules:
            - Strictly Follow the given JSON output format
            - Only run one step at a time
            - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user).

            Output JSON Format:
            {{
                'step':'START'|'PLAN'|'OUTPUT'|'TOOL',
                'content':'string',
                'tool','string',
                'input':'string'
            }}

            Available Tools:
            - getWeather(city:str): Takes city name as an input string & returns the weather information about the city

            Example 1:
            START: Can you solve 2+3*5/10
            PLAN:{
                'step':'PLAN', 
                'content':'Seems like user is interested in math problem'
                },
            PLAN:{
                'step':'PLAN',
                'content':'Looking at this problem, we should solve this using the BODMAS method'
                },
            PLAN:{
                'step':'PLAN',
                'content':'Yes, the BODMAS is correct thing to be done here'
                },
            PLAN:{
                'step':'PLAN',
                'content':'First, we must multiply 3*5 which is 15'
                },
            PLAN:{
                'step':'PLAN',
                'content':'Now, the new equation is 2+15/10'
                },
            PLAN:{
                'step':'PLAN',
                'content':'We must perform divide that is 15/10=1.5'
                },
            PLAN:{
                'step':'PLAN',
                'content':'Now, the new equation is 2+1.5'
                },
            PLAN:{
                'step':'PLAN',
                'content':'Now finally lets perform the addition to get 3.5'
                },
            PLAN:{
                'step':'PLAN',
                'content':'Great, we have solved & finally left with 3.5 as answer'
                },
            OUTPUT:{
                'step':'OUTPUT',
                'content':'3.5'
                }

            Example 2:
            START: What is the weather of Kharagpur?
            PLAN:{
                'step':'PLAN', 
                'content':'Seems like user is interested in getting weather of Kharagpur'
                },
            PLAN:{
                'step':'PLAN',
                'content':'Lets see if we have any available tool from the list of available tools'
                },
            PLAN:{
                'step':'PLAN',
                'content':'Great, we have getWeather tool available for this query'
                },
            PLAN:{
                'step':'PLAN',
                'content':'I need to call getWeather tool for delhi as input for city'
                },
            PLAN:{
                'step':'TOOL',
                'tool':'getWeather',
                'input':'Kharagpur'
                },
            PLAN:{
                'step':'OBSERVE',
                'tool':'getWeather',
                'content':'The temperature of Kharagpur is cloudy with 30 C'
                },
            PLAN:{
                'step':'PLAN',
                'content':'Great, I got the weather info about Kharagpur.'
                },
            OUTPUT:{
                'step':'OUTPUT',
                'content':'The current weather in Kharagpur is 30 C with cloudy sky'
                },
            '''

msgHistory=[
    {
        'role':'system',
        'content':systemPrompt
    }
]

while True:
    userQuery=input('\n\nAsk me: ')
    msgHistory.append({
        'role':'user',
        'content':userQuery
    })

    while True:
        response=client.chat.completions.parse(
            model="gemini-2.5-flash",
            response_format=MyOutputFormat,
            messages=msgHistory
        )
        rawResult=response.choices[0].message.content
        msgHistory.append({'role':'assistant','content':rawResult})
        parsedResult=response.choices[0].message.parsed

        if parsedResult.step=='START':
            print('\nStarting LLM Loop:',parsedResult.content)
            continue

        if parsedResult.step=='PLAN':
            print('\nPlanning:',parsedResult.content)
            continue

        if parsedResult.step=='TOOL':
            toolToCall=parsedResult.tool
            toolInput=parsedResult.input
            print(f'Tool: {toolToCall}({toolInput})')
            toolResponse=availableTools[toolToCall](toolInput)
            print(f'Tool Response: ${toolResponse}')
            msgHistory.append({'role':'developer','content':json.dumps({
                'step':'OBSERVE',
                'tool':toolToCall,
                'input':toolInput,
                'output':toolResponse
                })
            })
            continue

        if parsedResult.step=='OUTPUT':
            print('\nDone:',parsedResult.content)
            break

# response=client.chat.completions.create(
#     model="gemini-2.5-flash",
#     response_format={'type':'json_object'},
#     messages=[
#         {
#             'role':'system',
#             'content':systemPrompt
#         },
#         {
#             'role':'user',
#             # 'content':"Explain how AI works in a few words"
#             'content':"Write js program to add two numbers"
#         },
#         # manually keep adding messages to history
#         {
#             'role':'assistant',
#             'content':json.dumps({
#                 "step": "START",
#                 "content": "Write js program to add two numbers"
#             })
#         },
#         {
#             'role':'assistant',
#             'content':json.dumps({
#                 "step": "PLAN",
#                 "content": "The user wants a JavaScript program to add two numbers. I will provide a simple function that takes two arguments and returns their sum, then demonstrate its usage."
#             })
#         },
#         {
#             'role':'assistant',
#             'content':json.dumps({
#                 "step": "PLAN",
#                 "content": "First, I need to define a JavaScript function that accepts two arguments."
#             })
#         },
#         {
#             'role':'assistant',
#             'content':json.dumps({
#                 "step": "PLAN",
#                 "content": "Inside the function, I will use the '+' operator to add the two arguments."
#             })
#         },
#         {
#             'role':'assistant',
#             'content':json.dumps({
#                 "step": "PLAN",
#                 "content": "The function should then return the result of the addition."
#             })
#         },
#         {
#             'role':'assistant',
#             'content':json.dumps({
#                 "step": "PLAN",
#                 "content": "After defining the function, I will show how to call it with example numbers."
#             })
#         },
#     ]
# )

# print(response.choices[0].message.content)