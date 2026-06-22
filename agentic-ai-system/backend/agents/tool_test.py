from langchain_ollama import ChatOllama

from tools import (
    search_knowledge_base,
    check_order_status,
    escalate_to_human
)

tools = [
    search_knowledge_base,
    check_order_status,
    escalate_to_human
]

llm = ChatOllama(model="llama3.1:8b")

llm_with_tools = llm.bind_tools(tools)

response = llm_with_tools.invoke(
    "Where is my order #5678?"
)

print("Tool Calls:")
print(response.tool_calls)

print("\nContent:")
print(response.content)


# Execute the selected tool
print("\nExecuting Tool...")

tool_call = response.tool_calls[0]

result = check_order_status.invoke(tool_call["args"])

print("\nTool Result:")
print(result)