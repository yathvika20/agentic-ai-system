from typing import TypedDict, Annotated
import operator

from langgraph.graph import StateGraph, END

from langchain_ollama import ChatOllama
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    AIMessage,
)

####################################################
# Models
####################################################

agent_llm = ChatOllama(model="llama3.1:8b")

critic_llm = ChatOllama(
    model="llama3.1:8b",
    base_url="http://ollama:11434"
)


####################################################
# State
####################################################

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]


####################################################
# Agent Node
####################################################

def agent_node(state: AgentState):

    messages = state["messages"]

    response = agent_llm.invoke(messages)

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


    print("\nCritic Review:")
    print(critique.content)


    if "REVISE" in critique.content:

        return {

            "messages": [

                HumanMessage(

                    content=f"""
Revise your response.

Feedback:

{critique.content}

"""
                )

            ]

        }


    return {

        "messages": []

    }


####################################################
# Routing
####################################################

def critic_route(state):

    if len(state["messages"]) == 0:
        return END


    last_message = state["messages"][-1]


    if isinstance(last_message, HumanMessage):

        return "agent"


    return END


####################################################
# Build Graph
####################################################

builder = StateGraph(AgentState)


builder.add_node(
    "agent",
    agent_node
)

builder.add_node(
    "critic",
    critic_node
)


builder.set_entry_point(
    "agent"
)


builder.add_edge(
    "agent",
    "critic"
)


builder.add_conditional_edges(
    "critic",
    critic_route
)


graph = builder.compile()


####################################################
# Test
####################################################

if __name__ == "__main__":

    state = {

        "messages": [

            HumanMessage(

                content="My order has not arrived"

            )

        ]

    }


    result = graph.invoke(state)


    print("\n======================")
    print("FINAL ANSWER")
    print("======================\n")


    print(result["messages"][-1].content)