import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import os
from dotenv import load_dotenv

load_dotenv()


def get_chroma_collection():
    openai_api_key = os.getenv("OPENAI_API_KEY")

    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_key=openai_api_key,
        model_name="text-embedding-3-small"
    )

    # ✅ THIS is the correct persistent client
    client = chromadb.PersistentClient(path="chroma_db")

    collection = client.get_or_create_collection(
        name="regintel_docs",
        embedding_function=embedding_function
    )

    return collection


def add_chunks_to_collection(collection, chunks):
    ids = []
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        source = chunk["metadata"]["source"]
        page = chunk["metadata"]["page"]
        ids.append(f"{source}_page_{page}_chunk_{i}")
        documents.append(chunk["text"])
        metadatas.append(chunk["metadata"])

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )


def query_collection(collection, query_text, top_k=5):
    results = collection.query(
        query_texts=[query_text],
        n_results=top_k
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    return documents, metadatas