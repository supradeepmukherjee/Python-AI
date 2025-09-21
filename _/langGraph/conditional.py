from typing_extensions import TypedDict
from typing import Annotated,Optional,Literal
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,START,END
from langchain_google_genai import ChatGoogleGenerativeAI
from openai import Client
import os
from dotenv import load_dotenv

load_dotenv()

client=Client(
    api_key=os.getenv('GEMINI_API_KEY'),
    base_url='https://generativelanguage.googleapis.com/v1beta'
)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class State(TypedDict):
    userQuery:str
    llmOutput:Optional[str]
    isGood:Optional[bool]

def chatbot(state:State):
    print('\n\nChatbot: ',state)
    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                'role':'user',
                'content':state.get('userQuery')
            }
        ]
    )

    state['llmOutput']=response.choices[0].message.content
    return state

def evaluateResponse(state:State)->Literal['chatbot_otherModel','endNode']:
    print('\n\nEvaluate: ',state)
    # if True:
    if False:
        return 'endNode'
    return 'chatbot_otherModel'

def chatbotOtherModel(state:State):
    print('\n\nChatbot other model: ',state)
    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                'role':'user',
                'content':state.get('userQuery')
            }
        ]
    )
    state['llmOutput']=response.choices[0].message.content
    return state

def endNode(state:State):
    return state

graphBuilder=StateGraph(State)

graphBuilder.add_node('chatbot',chatbot)
graphBuilder.add_node('chatbot_otherModel',chatbotOtherModel)
graphBuilder.add_node('endNode',endNode)

graphBuilder.add_edge(START,'chatbot')
graphBuilder.add_conditional_edges('chatbot',evaluateResponse)

graphBuilder.add_edge('chatbot_otherModel','endNode')
graphBuilder.add_edge('endNode',END)

graph=graphBuilder.compile()
updatedState=graph.invoke(State({'userQuery':'What is 2+3*5'}))
print('\n\n')
print(updatedState)