from openai import Client
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
import os

client=Client(
    api_key=os.getenv('GEMINI_API_KEY'),
    base_url='https://generativelanguage.googleapis.com/v1beta'
)

embeddingModel = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorDb=QdrantVectorStore.from_existing_collection(
    api_key=os.getenv('QDRANT_KEY'),
    collection_name='learningRag',
    embedding=embeddingModel,
    url=os.getenv('QDRANT_URL'),
)

def processQuery(query:str):
    print('Searching chunks for: ',query)
    searchResults=vectorDb.similarity_search(query)
    response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            'role':'system',
            'content':f'''
                You are a helpful AI assistant who answers user query based on the available context retrieved from a PDF file along with page contents & page number.

                You should only answer a user based on the following context and navigate the user to open the right page number to know more.

                Context:{'\n\n\n'.join([f'Page Content: {res.page_content}\nPage number: {res.metadata['page_label']}\nFile location:{res.metadata['source']}' for res in searchResults])}
                '''
        },
        {
            'role':'user',
            'content':query
        },
        ]
    )

    return response.choices[0].message.content