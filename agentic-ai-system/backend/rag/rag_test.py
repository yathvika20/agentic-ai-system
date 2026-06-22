from langchain_ollama import ChatOllama
from backend.agents.tools import search_knowledge_base


tools = [search_knowledge_base]

llm = ChatOllama(
    model="llama3.1:8b"
).bind_tools(tools)


question = "What is your return policy?"

response = llm.invoke(question)


if response.tool_calls:

    tool_call = response.tool_calls[0]

    tool_result = search_knowledge_base.invoke(
        tool_call["args"]
    )

    print("\nTool Result:\n")
    print(tool_result[:300])

    final = ChatOllama(
        model="llama3.1:8b"
    ).invoke(

        f"""
Context:

{tool_result}


Question:

{question}


Answer based only on the provided context.
"""
    )

    print("\nFinal Answer:\n")
    print(final.content)

else:
    print("\nDirect Answer:\n")
    print(response.content)