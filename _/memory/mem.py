from openai import Client
from mem0 import Memory
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import json

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_KEY = os.getenv("QDRANT_KEY")

client = Client(
    api_key=GEMINI_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

# ------------------------------
# HuggingFace Embedder
# ------------------------------
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
EMBED_DIM = 384  # all-MiniLM-L6-v2 output dimension

def embedFn(texts: list[str]) -> list[list[float]]:
    return embedder.encode(texts, convert_to_numpy=True).tolist()

qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_KEY)

COLLECTION_NAME = "mem0"  # default collection name used by mem0

try:
    info = qdrant_client.get_collection(COLLECTION_NAME)
    existing_dim = info.config.params.vectors.size
    if existing_dim != EMBED_DIM:
        print(f"[INFO] Dimension mismatch ({existing_dim} vs {EMBED_DIM}). Recreating collection...")
        qdrant_client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=EMBED_DIM, distance=Distance.COSINE)
        )
except Exception:
    print("[INFO] Creating collection fresh...")
    qdrant_client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=EMBED_DIM, distance=Distance.COSINE)
    )

NEO4J_URI=os.getenv('NEO4J_URI')
NEO4J_USERNAME=os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD=os.getenv('NEO4J_PASSWORD')
print('\n',NEO4J_URI)
print('\n',NEO4J_USERNAME)
print('\n',NEO4J_PASSWORD)

memory = Memory.from_config({
    "version": "v1.1",
    "embedder": {
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/all-MiniLM-L6-v2"
        }
    },
    "llm": {
        "provider": "gemini",
        "config": {
            "api_key": GEMINI_KEY,
            "model": "gemini-2.5-flash"
        }
    },
    'graph_store':{
        'provider':'neo4j',
        'config':{
            'url':NEO4J_URI,
            'username':NEO4J_USERNAME,
            'password':NEO4J_PASSWORD,
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "url": QDRANT_URL,
            "api_key": QDRANT_KEY
        }
    }
})

while True:
    userQuery = input("> ")

    searchMemory=memory.search(user_id="supradeep",query=userQuery)

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "system",
                "content": f'''
                    Here is the context about the user
                    {json.dumps([f'ID: {mem['id']}\nMemory: {mem['memory']}' for mem in searchMemory['results']])}
                    '''
            },
            {
                "role": "user",
                "content": userQuery
            },
        ]
    )

    geminiResponse = response.choices[0].message.content
    print("Gemini response: ", geminiResponse)

    memory.add(
        user_id="supradeep",
        messages=[
            {
                "role": "user",
                "content": userQuery
            },
            {
                "role": "assistant",
                "content": geminiResponse
            }
        ]
    )