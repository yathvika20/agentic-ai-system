import logging

from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage

import os


def get_llm_with_fallback(tools=None):

    

    OLLAMA_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )

    primary = ChatOllama(
        model="llama3.1:8b",
        base_url=OLLAMA_URL,
        num_ctx=512,
    )

    fallback = ChatOllama(
        model="llama3.1:8b",
        base_url=OLLAMA_URL,
        num_ctx=512,
    )

    if tools:
        primary = primary.bind_tools(tools)
        fallback = fallback.bind_tools(tools)

    def invoke_with_fallback(messages: list[BaseMessage]):

        try:
            return primary.invoke(messages)

        except Exception as e:

            logging.warning(
                f"Primary model failed: {e}. Trying fallback..."
            )

            return fallback.invoke(messages)

    return invoke_with_fallback