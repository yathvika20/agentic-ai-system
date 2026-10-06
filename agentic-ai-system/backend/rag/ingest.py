import os

from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


def ingest_documents(
    docs_dir="data/documents",
    persist_dir="data/chroma_db",
):
    # Load text documents
    loader = DirectoryLoader(
        docs_dir,
        glob="*.txt",
        loader_cls=TextLoader,
    )

    docs = loader.load()
    print(f"Loaded {len(docs)} documents")

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )

    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    # Create embeddings
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text",
        base_url=os.getenv(
            "OLLAMA_BASE_URL",
            "http://ollama:11434",
        ),
    )

    print("Generating embeddings...")

    # Store in ChromaDB
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir,
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB")
    print(f"Database location: {persist_dir}")

    return vectorstore


if __name__ == "__main__":
    ingest_documents()