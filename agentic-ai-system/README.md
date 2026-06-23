AI Customer Support Agent with RAG, LangGraph and FastAPI
Overview

AI Customer Support Agent is an end-to-end agentic AI system designed to provide intelligent customer support using Retrieval-Augmented Generation (RAG), ReAct reasoning, tool calling, conversation memory, LangGraph workflows, and a production-ready FastAPI backend.

The system uses locally running open-source Large Language Models through Ollama and combines retrieval, reasoning, memory, and API serving to generate context-aware responses.

Features
Retrieval-Augmented Generation (RAG)
Document ingestion pipeline
Text chunking
Embedding generation
ChromaDB vector storage
Semantic similarity search
Knowledge base retrieval
ReAct Agent

Implemented features

Manual ReAct loop
Tool selection
Observation generation
Multi-step reasoning
Final answer synthesis
Conversation Memory

Supports

Session-based memory
Window buffer memory
Multi-turn conversations
Conversation history retention

Memory implementation

deque(maxlen=10)
LangGraph Workflow

Implemented nodes

Agent Node
Tool Node
Critic Node

Capabilities

Stateful execution
Conditional routing
Tool invocation
Response critique
Hallucination reduction
FastAPI Backend

Implemented endpoints

GET /health

POST /api/v1/chat

WebSocket /api/v1/ws/{session_id}

Features

Pydantic request validation
Pydantic response validation
OpenAPI documentation
Swagger UI integration
Token streaming using WebSockets
Health checks
Global exception handling
CORS middleware
Tools Implemented
search_knowledge_base

Performs semantic search over ChromaDB and retrieves relevant documents.

check_order_status

Returns predefined order tracking information.

escalate_to_human

Escalates customer requests requiring human intervention.

Models Used
LLMs
Llama 3.1 8B

Used for

Tool calling
ReAct agent
LangGraph workflow
FastAPI backend
Qwen 2.5 7B

Preferred production model

Reason

Generated more professional and detailed customer-support responses during evaluation.

Phi-3

Used as a lightweight backup model.

Reason

Fast inference speed on available hardware.

Embedding Model
nomic-embed-text

Used for

Embedding generation
Vector similarity search
ChromaDB integration
Technologies Used
Programming Language
Python
Frameworks
LangChain
LangGraph
FastAPI
Vector Database
ChromaDB
Local Model Serving
Ollama
API Development
FastAPI
Pydantic
HTTPX
WebSockets
Memory Management
Conversation Buffer Memory
Session Memory
Development Tools
VS Code
Git
GitHub
Project Architecture
ReAct Workflow
User Query
      │
      ▼
LLM
      │
      ▼
Tool Selection
      │
      ▼
Knowledge Base Search
      │
      ▼
Observation
      │
      ▼
LLM Reasoning
      │
      ▼
Final Answer
LangGraph Workflow
User Query
     │
     ▼
 Agent Node
     │
     ▼
Conditional Routing
     │
 ┌───┴────┐
 ▼        ▼
Tools   Critic
 │        │
 └────┬───┘
      ▼
Final Response
FastAPI Architecture
User
 │
 ▼
POST /api/v1/chat
 │
 ▼
FastAPI
 │
 ▼
Pydantic Validation
 │
 ▼
LangGraph
 │
 ├── Agent Node
 │
 ├── Tool Node
 │
 └── Critic Node
 │
 ▼
LLM
 │
 ▼
ChatResponse
Project Structure
backend/

├── agents/
│   ├── prompts.py
│   ├── tools.py
│   ├── memory.py
│   ├── react_agent.py
│   ├── graph_agent.py
│   ├── critic_graph.py
│
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│
├── api/
│   ├── main.py
│   ├── models.py
│   ├── dependencies.py
│   └── routers/
│       ├── chat.py
│       └── health.py
│
frontend/

docs/

docker/

data/
Current Status
Implemented
Local LLM execution
ChromaDB integration
RAG pipeline
Tool calling
ReAct agent
Session memory
LangGraph workflow
Critic node
FastAPI backend
WebSocket streaming
Health monitoring
Global exception handling
Upcoming
Redis session persistence
React frontend
Docker deployment
Evaluation and benchmarking