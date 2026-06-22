# AI Customer Support Agent with RAG

## Overview

This project is an AI-powered Customer Support Agent built during an Agentic AI internship.

The system combines Retrieval-Augmented Generation (RAG), tool calling, ReAct reasoning, and conversation memory to answer customer queries accurately using locally running open-source models.

---

## Use Case

Users can ask questions related to:

- Product information
- Shipping details
- Return policies
- Refund procedures
- Order tracking
- Frequently Asked Questions

The agent performs the following steps:

1. Receives the user's query
2. Decides whether external information is needed
3. Uses tools to retrieve relevant information
4. Searches the knowledge base using RAG
5. Reasons over retrieved information
6. Produces a final answer
7. Maintains conversation context across turns

---

## Technology Stack

### Core Technologies

- Python
- LangChain
- Ollama
- ChromaDB

### Models

- Llama 3.1 8B
- Qwen 2.5 7B
- Phi-3
- nomic-embed-text

### Memory

- Conversation Buffer Memory
- Session-based Memory
- deque(maxlen=10)

### Planned Technologies

- LangGraph
- FastAPI
- Docker

---

## Project Structure

```text
backend/
│
├── agents/
│   ├── prompts.py
│   ├── tools.py
│   ├── react_agent.py
│   ├── memory.py
│   ├── agent_test.py
│
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│   ├── rag_test.py
│
frontend/

data/

docker/
```

---

## Features Implemented

### Day 1

- Development environment setup
- Ollama installation
- Git repository initialization
- Project scaffold creation

### Day 2

- Compared Phi-3, Mistral 7B, Qwen 2.5 7B and Llama 3.1 8B
- Selected Qwen 2.5 7B as preferred production model
- Selected nomic-embed-text for embeddings

### Day 3

Implemented agent building blocks

- System prompts
- Structured schemas
- Tool definitions
- Tool testing

### Day 4

Implemented Retrieval-Augmented Generation

- Document ingestion
- Chunking
- Embedding generation
- ChromaDB vector storage
- Retriever implementation
- Knowledge base search tool

### Day 5

Implemented ReAct Agent

Features:

- Manual ReAct loop
- Tool calling
- RAG integration
- Conversation memory
- Session-based memory
- Window buffer memory
- Multi-turn conversations

Tools available:

- search_knowledge_base
- check_order_status
- escalate_to_human

---

## ReAct Workflow

```text
User Query
    ↓
LLM
    ↓
Tool Selection
    ↓
Knowledge Base Search
    ↓
Observation
    ↓
LLM Reasoning
    ↓
Final Answer
```

---

## Memory Workflow

```text
Session ID
    ↓
ConversationMemory
    ↓
deque(maxlen=10)
    ↓
Conversation History
    ↓
ReAct Agent
```

---

## Models Used During Week 1

### Development Model

Llama 3.1 8B

Reason:

Used during implementation because of stable LangChain tool-calling support.

---

### Preferred Production Model

Qwen 2.5 7B

Reason:

Produced more professional and detailed customer-support responses during evaluation.

---

### Embedding Model

nomic-embed-text

Reason:

Runs locally with Ollama and works well for RAG pipelines.

---

### Backup Model

Phi-3

Reason:

Fastest model on available hardware and useful during development.

---

## Current Status

### Completed

- Environment setup
- Local LLM execution with Ollama
- ChromaDB integration
- RAG pipeline
- ReAct agent
- Tool calling
- Conversation memory
- Session memory
- Multi-turn chat support

### Upcoming

- LangGraph stateful memory
- FastAPI backend
- Streamlit frontend
- Docker deployment
- Evaluation and benchmarking