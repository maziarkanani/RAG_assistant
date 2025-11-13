from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from ingest import load_and_split_docs
import os

def build_vector_db():
    docs = load_and_split_docs()
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma.from_documents(docs, embeddings, persist_directory="chroma_store")
    db.persist()
    print("Vector database built and stored locally.")

if __name__ == "__main__":
    build_vector_db()
