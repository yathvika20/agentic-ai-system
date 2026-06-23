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


llm = ChatOllama(
    model="llama3.1:8b"
).bind_tools(tools)


critic_llm = ChatOllama(
    model="llama3.1:8b"
)


####################################################
# Agent State
####################################################

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]
    session_id: str


####################################################
# Agent Node
####################################################

def agent_node(state: AgentState):

    messages = [
        SystemMessage(content=AGENT_SYSTEM)
    ] + state["messages"]

    response = llm.invoke(messages)

    return {
        "messages": [response]
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

tool_node = ToolNode(tools)


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
    tool_node
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

# Compile graph
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