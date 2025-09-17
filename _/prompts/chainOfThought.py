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
            You're an expert AI Assistant in resolving user queries using chain of thought.
            You work on START, PLAN & OUTPUT steps.
            You need to first PLAN what needs to be done. The PLAN can be multiple steps.
            Once you think enough PLAN has been done, finally you can give an OUTPUT.

            Rules:
            - Strictly Follow the given JSON output format
            - Only run one step at a time
            - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user).

            Output JSON Format:
            {{
                'step':'START'|'PLAN'|'OUTPUT',
                'content':'string'
            }}

            Example:
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
                },
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

while True:
    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={'type':'json_object'},
        messages=msgHistory
    )
    rawResult=response.choices[0].message.content
    msgHistory.append({'role':'assistant','content':rawResult})
    parsedResult=json.loads(rawResult)

    if parsedResult.get('step')=='START':
        print('\nStarting LLM Loop:',parsedResult.get('content'))
        continue

    if parsedResult.get('step')=='PLAN':
        print('\nPlanning:',parsedResult.get('content'))
        continue

    if parsedResult.get('step')=='OUTPUT':
        print('\nDone:',parsedResult.get('content'))
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