from typing import TypedDict, Annotated
import operator

from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from langchain_ollama import ChatOllama
from langchain_core.messages import (
    BaseMessage,
    SystemMessage,
    HumanMessage
)

from backend.agents.fallback_chain import get_llm_with_fallback

from backend.agents.tools import (
    search_knowledge_base,
    check_order_status,
    escalate_to_human
)

from backend.agents.prompts import AGENT_SYSTEM


####################################################
# Tools and Models
####################################################

tools = [
    search_knowledge_base,
    check_order_status,
    escalate_to_human
]

# Primary model with automatic fallback
llm = get_llm_with_fallback(tools)

# Critic model (no fallback required)
import os

critic_llm = ChatOllama(
    model="llama3.1:8b",
    base_url=os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )
)


####################################################
# Agent State
####################################################

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]
    session_id: str

    input_tokens: int
    output_tokens: int
    total_tokens: int


####################################################
# Agent Node
####################################################

def agent_node(state: AgentState):

    messages = [
        SystemMessage(content=AGENT_SYSTEM)
    ] + state["messages"]

    # Uses fallback automatically
    response = llm(messages)
    print("\n========== MODEL RESPONSE ==========")
    print(response)

    print("\n========== TOOL CALLS ==========")
    print(response.tool_calls)
    print("====================================\n")
    ####################################################
    # Token Tracking
    ####################################################

    metadata = getattr(response, "response_metadata", {})

    input_tokens = metadata.get("prompt_eval_count", 0)

    output_tokens = metadata.get("eval_count", 0)

    total_tokens = input_tokens + output_tokens

    print("\n==============================")
    print("TOKEN USAGE")
    print("==============================")
    print(f"Input Tokens : {input_tokens}")
    print(f"Output Tokens: {output_tokens}")
    print(f"Total Tokens : {total_tokens}")
    print("==============================\n")

    return {
        "messages": [response],
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens
    }


####################################################
# Critic Node
####################################################

def critic_node(state: AgentState):

    last_response = state["messages"][-1].content

    critique_prompt = f"""
Review this customer support response.

Response:
{last_response}

Check:

1. Is it factually grounded?

2. Is it helpful?

3. Any policy violations?

If response is good output:

APPROVED

If changes are needed output:

REVISE: reason
"""

    critique = critic_llm.invoke(critique_prompt)

    print("\n==============================")
    print("CRITIC REVIEW")
    print("==============================\n")

    print(critique.content)

    return {
        "messages": []
    }


####################################################
# Tool Node
####################################################

from langgraph.prebuilt import ToolNode

tool_node = ToolNode(tools)


def tool_node_wrapper(state: AgentState):
    print("\n========== ENTERED TOOL NODE ==========\n")

    result = tool_node.invoke(state)

    print(result)

    print("\n========== EXIT TOOL NODE ==========\n")

    return result


####################################################
# Conditional Routing
####################################################

def should_continue(state: AgentState):

    last_message = state["messages"][-1]

    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"

    return "critic"


####################################################
# Build Graph
####################################################

builder = StateGraph(AgentState)

builder.add_node(
    "agent",
    agent_node
)

builder.add_node(
    "tools",
    tool_node_wrapper
)

builder.add_node(
    "critic",
    critic_node
)

builder.add_conditional_edges(
    "agent",
    should_continue
)

builder.add_edge(
    "tools",
    "agent"
)

builder.add_edge(
    "critic",
    END
)

builder.set_entry_point(
    "agent"
)

####################################################
# Compile Graph
####################################################

graph = builder.compile()

# Export graph for FastAPI
agent_graph = graph


####################################################
# Test Graph
####################################################

if __name__ == "__main__":

    state = {
        "messages": [
            HumanMessage(
                content="Where is my order 1001?"
            )
        ],
        "session_id": "1"
    }

    result = graph.invoke(state)

    print("\n==============================")
    print("FINAL RESPONSE")
    print("==============================\n")

    print(result["messages"][-1].content)

    print("\n==============================")