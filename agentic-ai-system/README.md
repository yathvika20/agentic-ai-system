# AI Customer Support Agent with RAG

## Overview

This project is an AI Customer Support Agent built as part of an Agentic AI internship.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from documents and generate accurate answers to user queries.

## Use Case

Users ask questions about products, services, FAQs, or company policies.

The AI agent:

1. Receives the user's question.
2. Searches relevant documents.
3. Retrieves useful context.
4. Generates an accurate response using a language model.

## Technology Stack

* Python
* LangChain
* LangGraph
* ChromaDB
* Sentence Transformers
* Ollama
* Phi-3
* FastAPI
* Docker

## Project Structure

backend/ → Agent logic, APIs, and RAG components

frontend/ → User interface

data/documents/ → Knowledge base documents

docker/ → Deployment configuration

## Current Status

* Agentic AI concepts studied
* Use case selected
* Development environment configured
* Ollama installed
* Phi-3 running locally
* Project scaffold created
* GitHub repository initialized

## Model Decisions

### Primary LLM
Qwen 2.5 7B

Reason:
Selected after comparing Phi-3, Mistral 7B, Qwen 2.5 7B, and Llama 3.1 8B. Qwen produced the most detailed and professional customer-support responses.

### Embedding Model
nomic-embed-text

Reason:
Free, runs locally with Ollama, produces 768-dimensional embeddings, and is suitable for RAG pipelines.

### Fine-Tuning Plan
Use RAG for factual knowledge and prompt engineering for behavior. Consider QLoRA fine-tuning later for customer-support style adaptation.

### Backup Model
Phi-3

Reason:
Fastest model on available hardware and useful for development/testing.