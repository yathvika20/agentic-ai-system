# AI Customer Support Agent with RAG

## Overview

This project is an AI Customer Support Agent built as part of an Agentic AI internship.

The system combines Retrieval-Augmented Generation (RAG), tool calling, ReAct reasoning, conversation memory, LangGraph workflows, and a production-ready FastAPI backend to answer customer queries accurately using locally running open-source models.

---

## Use Case

Users ask questions related to:

* Product information
* Shipping details
* Return policies
* Refund procedures
* Order tracking
* Frequently Asked Questions
* Escalation to human agents

The AI agent:

1. Receives the user's question.
2. Decides whether external information is needed.
3. Searches the knowledge base.
4. Retrieves relevant context.
5. Selects and invokes tools if required.
6. Generates a final response.
7. Maintains conversation history across turns.

---

## Technology Stack

### Frameworks

* Python
* LangChain
* LangGraph
* FastAPI

### Vector Database

* ChromaDB

### Local Model Serving

* Ollama

### API Development

* FastAPI
* Pydantic
* HTTPX
* WebSockets

### Development Tools

* Git
* GitHub
* VS Code

---

## Models Used

### Development Model

Llama 3.1 8B

Reason:

Used during implementation because of stable LangChain tool-calling support.

### Preferred Production Model

Qwen 2.5 7B

Reason:

Selected after comparing Phi-3, Mistral 7B, Qwen 2.5 7B and Llama 3.1 8B.

Produced the most detailed and professional customer-support responses.

### Embedding Model

nomic-embed-text

Reason:

Runs locally with Ollama and produces high-quality embeddings for RAG pipelines.

### Backup Model

Phi-3

Reason:

Fastest model on available hardware and useful during development.

---

## Features Implemented

### Retrieval-Augmented Generation (RAG)

* Document ingestion
* Chunking
* Embedding generation
* ChromaDB vector storage
* Semantic similarity search
* Knowledge base retrieval

### ReAct Agent

* Manual ReAct loop
* Tool calling
* Observation generation
* Final answer synthesis
* Multi-turn reasoning

### Conversation Memory

* Conversation Buffer Memory
* Session Memory
* Window Buffer Memory
* Multi-turn conversations
* deque(maxlen=10)

### LangGraph Workflow

Implemented nodes:

* Agent Node
* Tool Node
* Critic Node

Capabilities:

* Stateful execution
* Conditional routing
* Tool invocation
* Response critique
* Hallucination reduction

### FastAPI Backend

Implemented endpoints:

* GET /health
* POST /api/v1/chat
* WebSocket /api/v1/ws/{session_id}

Implemented features:

* Request validation
* Response validation
* Swagger documentation
* WebSocket token streaming
* Health checks
* Global exception handling
* CORS middleware

---

## Tools Implemented

### search_knowledge_base

Performs semantic search over ChromaDB and retrieves relevant documents.

### check_order_status

Returns predefined order tracking information.

### escalate_to_human

Escalates customer requests requiring human intervention.

---

## Project Structure

backend/

├── agents/

│   ├── prompts.py

│   ├── tools.py

│   ├── react_agent.py

│   ├── memory.py

│   ├── graph_agent.py

│   ├── critic_graph.py

├── rag/

│   ├── ingest.py

│   ├── retriever.py

├── api/

│   ├── main.py

│   ├── models.py

│   └── routers/

│       ├── chat.py

│       └── health.py

frontend/

docker/

docs/

data/

test_ws.py

README.md

---

## LangGraph Workflow

```text
START

↓

Agent

↓

Conditional Routing

↓

Tools

↓

Critic

↓

END
```

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

## FastAPI Workflow

```text
User

↓

POST /api/v1/chat

↓

FastAPI

↓

Pydantic Validation

↓

LangGraph

↓

LLM

↓

ChatResponse
```

---

## Current Status

Completed

* Local LLM execution
* ChromaDB integration
* RAG pipeline
* Tool calling
* ReAct agent
* Conversation memory
* Session memory
* LangGraph workflow
* Critic node
* FastAPI backend
* WebSocket streaming
* Health monitoring
* Global exception handling

Upcoming

* Redis session persistence
* React frontend
* Docker deployment
* Evaluation and benchmarking

---

## Commands

Start Ollama

```bash
ollama serve
```

Run FastAPI

```bash
uvicorn backend.api.main:app --reload
```

Swagger UI

```text
http://localhost:8000/docs
```

Run WebSocket client

```bash
python test_ws.py
```
