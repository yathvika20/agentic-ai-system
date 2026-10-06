# AI Customer Support Agent

## Project Overview

The AI Customer Support Agent is an intelligent customer-support system designed to automatically understand and respond to customer queries. The system uses a Large Language Model (LLM), Retrieval-Augmented Generation (RAG), and LangGraph-based agent orchestration to provide accurate and context-aware responses.

The agent can handle common customer-support tasks such as:

- Product-related queries
- Shipping and delivery information
- Return and refund policies
- Frequently Asked Questions (FAQs)
- Order status and tracking
- Human-agent escalation for unresolved issues

The system retrieves relevant information from a knowledge base before generating responses, reducing the chances of incorrect or unsupported answers.

## Key Features

### 1. Retrieval-Augmented Generation (RAG)

The system uses RAG to retrieve relevant information from the customer-support knowledge base before generating an answer.

The retrieved documents are stored and searched using a vector database, allowing the agent to provide responses based on the available company information.

### 2. Intelligent Agent Workflow

LangGraph is used to create the agent workflow. The system determines which action or tool is appropriate for the user's query.

For example:

- Shipping questions → Knowledge Base
- Return/refund questions → Knowledge Base
- Product questions → Knowledge Base
- Order tracking → Order Status Tool
- Unresolved issues → Human Escalation Tool

### 3. Knowledge Base Search

The `search_knowledge_base` tool retrieves information related to:

- Products
- Shipping
- Returns
- Refunds
- FAQs
- Warranty information

### 4. Order Status Checking

The `check_order_status` tool handles queries where the customer provides an order ID and asks about delivery or order status.

Example:

> Where is my order 1001?

The agent identifies the order-related request and invokes the appropriate tool.

### 5. Human Escalation

If the agent cannot appropriately resolve a customer issue, the `escalate_to_human` tool can be used to transfer the issue to a human support representative.

### 6. Critic / Validation Node

A critic component is included in the LangGraph workflow to review the generated response before it is returned to the customer.

The response is evaluated and can be approved before being sent to the frontend.

### 7. Web-Based Chat Interface

The project includes a frontend chat interface through which users can interact with the customer-support agent in real time.

The frontend communicates with the FastAPI backend using WebSocket communication.

---

## System Architecture

```text
                    User
                     │
                     ▼
              React Frontend
                     │
                WebSocket
                     │
                     ▼
              FastAPI Backend
                     │
                     ▼
             LangGraph Agent
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
      Knowledge   Order      Human
       Base Tool  Status    Escalation
          │         Tool        Tool
          ▼
       ChromaDB
          │
          ▼
    Retrieved Context
          │
          ▼
        LLM
          │
          ▼
     Critic Node
          │
          ▼
    Final Response
          │
          ▼
      Frontend

## Project Output

![AI Customer Support Agent](screenshot/project-output.png)