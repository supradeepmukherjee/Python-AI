from openai import Client
from dotenv import load_dotenv
import os
import requests

load_dotenv()

client=Client(
    api_key=os.getenv('GEMINI_API_KEY'),
    base_url='https://generativelanguage.googleapis.com/v1beta'
)

def getWeather(city:str):
    url=f'https://wttr.in/{city.lower()}?format=%C+%t'
    res=requests.get(url)
    if res.status_code==200:
        print(f'The weather in {city} is {res.text}')
    else:
        print('Something went wrong')

def main():
    userQuery=input('Ask me:')
    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                'role':'user',
                'content':userQuery
            }
        ]
    )

    print(response.choices[0].message.content)

# main()
getWeather('Kharagpur')