from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
import os

load_dotenv()

pdfPath=Path(__file__).parent/'nodejs.pdf'

# Load this file in python program
loader=PyPDFLoader(file_path=pdfPath)
docs=loader.load()

# Split the docs into smaller chunks
textSplitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks=textSplitter.split_documents(documents=docs)

embeddingModel = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorStore=QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddingModel,
    url=os.getenv('QDRANT_URL'),
    api_key=os.getenv('QDRANT_KEY'),
    collection_name='learningRag',
    force_recreate=True
)