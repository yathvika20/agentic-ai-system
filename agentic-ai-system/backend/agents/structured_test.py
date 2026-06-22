from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from schemas import AgentResponse


llm = OllamaLLM(model="llama3.1:8b")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
IMPORTANT:
Return ONLY valid JSON.

Do not explain anything.
Do not use markdown.

Schema:
{schema}
"""
    ),
    (
        "human",
        "{query}"
    )
])

chain = prompt | llm

result = chain.invoke({
    "schema": AgentResponse.model_json_schema(),
    "query": "Where is my order #1234?"
})

print(result)