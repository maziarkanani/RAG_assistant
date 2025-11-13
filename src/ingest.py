from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_and_split_docs(path="data/"):
    all_docs = []
    for f in os.listdir(path):
        if f.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(path, f))
            pages = loader.load()
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
            chunks = splitter.split_documents(pages)
            all_docs.extend(chunks)
    return all_docs

if __name__ == "__main__":
    docs = load_and_split_docs()
    print(f"Loaded {len(docs)} chunks.")
