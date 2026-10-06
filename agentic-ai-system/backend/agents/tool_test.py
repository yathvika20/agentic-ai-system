from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

from backend.agents.tools import (
    check_order_status,
    search_knowledge_base,
    escalate_to_human,
)

llm = ChatOllama(
    model="llama3.1:8b"
).bind_tools([
    check_order_status,
    search_knowledge_base,
    escalate_to_human,
])

response = llm.invoke([
    HumanMessage(content="Where is my order 1001?")
])

print("\n===== RESPONSE =====")
print(response)

print("\n===== TOOL CALLS =====")
print(response.tool_calls)