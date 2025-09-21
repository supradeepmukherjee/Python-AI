from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,START,END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.mongodb import MongoDBSaver
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class State(TypedDict):
    messages:Annotated[list,add_messages]

def chatbot(state:State):
    response=llm.invoke(state.get('messages'))
    return {'messages':response}

graphBuilder=StateGraph(State)

graphBuilder.add_node('xyz',chatbot)

graphBuilder.add_edge(START,'xyz')
graphBuilder.add_edge('xyz',END)

graph=graphBuilder.compile()

def compileGraphWithCheckpointer(checkpointer):
    return graphBuilder.compile(checkpointer)

with MongoDBSaver.from_conn_string(os.getenv('MONGO_URI')) as checkpointer:

    graphWithCheckpointer=compileGraphWithCheckpointer(checkpointer)

    for chunk in graphWithCheckpointer.stream(
        State({'messages':['What is my Name?']}),
        config={'configurable':{'thread_id':'supradeep'}},
        stream_mode='values'
    ):
        chunk['messages'][-1].pretty_print()