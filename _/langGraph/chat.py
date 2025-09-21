from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,START,END
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class State(TypedDict):
    messages:Annotated[list,add_messages]

def chatbot(state:State):
    response=llm.invoke(state.get('messages'))
    return {'messages':response}

def sampleNode(state:State):
    print('\n\nInside sample node',state)
    return {'messages':['Sample msg appended']}


graphBuilder=StateGraph(State)

graphBuilder.add_node('xyz',chatbot)
graphBuilder.add_node('sample',sampleNode)

graphBuilder.add_edge(START,'xyz')
graphBuilder.add_edge('xyz','sample')
graphBuilder.add_edge('sample',END)

graph=graphBuilder.compile()
updatedState=graph.invoke(State({'messages':['Hi, my name is Supradeep Mukherjee']}))
print('\n\n')
print(updatedState)